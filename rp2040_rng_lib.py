# rp2040_rng_lib.py
import machine
import utime
import struct
import hashlib
from time import sleep_us

class TIMESTAMP:
    """
    Class to get the Unix timestamp from the RP2040's RTC (Real Time Clock).
    """
    def __init__(self):
        self.rtc = machine.RTC()

    def get_unix_timestamp(self):
        """
        Get the current Unix timestamp.
        Returns the timestamp as an integer representing the number of seconds
        since January 1, 1970.
        """
        year, month, day, _, hour, minute, second, _ = self.rtc.datetime()
        return int(utime.mktime((year, month, day, hour, minute, second, 0, 0)))


class RandomGenerator:
    """
    Class that generates random numbers based on entropy collected from an ADC (Analog-to-Digital Converter).
    It uses an entropy pool that is mixed with ADC readings, and the entropy is whitened using SHA-256.
    """
    def __init__(self):
        self.adc = machine.ADC(28)  # GPIO Pin 28 for ADC
        self.clock = machine.Pin(0, machine.Pin.OUT)  # Pin to add entropy through toggling
        self.timestamp = TIMESTAMP()  # To get the current time
        self.entropy_pool = bytearray(64)  # Entropy pool to be updated
        self.last_entropy = 0  # Last generated random value
        self.counter = 0  # Counter to introduce variability

    def _read_adc_values(self):
        """
        Reads 8 values from the ADC and returns them as a list.
        These values are masked to keep only the 12 least significant bits.
        """
        return [self.adc.read_u16() & 0xFFF for _ in range(8)]

    def _mix_entropy(self, adc_values):
        """
        Mixes the entropy values using a simple XOR and multiplication method.
        This function generates a mixed entropy value from the ADC readings.
        """
        mixed_value = 0
        for val in adc_values:
            mixed_value ^= val
            mixed_value = (mixed_value * 1103515245 + 12345) & 0xFFFFFFFF  # Apply a linear congruential generator
        return mixed_value

    def _update_entropy_pool(self, mixed_value, adc_values):
        """
        Updates the entropy pool by packing the mixed entropy value and ADC readings
        into the pool. The pool is packed in big-endian format.
        """
        for i in range(0, 64, 8):
            value = (mixed_value << 28) | (adc_values[i // 8] << 16) | (adc_values[(i // 8 + 1) % 8] << 4) | (self.counter & 0xF)
            struct.pack_into('>Q', self.entropy_pool, i, value)
        self.counter = (self.counter + 1) & 0xFFFFFFFF

    def _whiten_entropy(self):
        """
        Whiten the entropy by applying a SHA-256 hash function to the entropy pool.
        The result is reduced to a 64-bit random value.
        """
        sha256 = hashlib.sha256()
        sha256.update(self.entropy_pool)
        sha256.update(struct.pack('>Q', self.timestamp.get_unix_timestamp()))
        sha256.update(struct.pack('>Q', self.last_entropy))
        whitened = sha256.digest()
        return struct.unpack('>Q', whitened[:8])[0]

    def generate(self):
        """
        Generates an infinite stream of random numbers by continuously collecting entropy
        from the ADC, mixing it, whitening it, and checking for changes in the last random value.
        The generator yields the next random number.
        """
        while True:
            current_time = self.timestamp.get_unix_timestamp()
            sleep_time = (current_time % 100) + 50

            # Toggle the clock pin to add some jitter to the entropy collection
            self.clock.toggle()
            sleep_us(sleep_time)
            self.clock.toggle()
            sleep_us(sleep_time)

            # Read and process ADC values to generate new entropy
            adc_values = self._read_adc_values()
            mixed_value = self._mix_entropy(adc_values)
            self._update_entropy_pool(mixed_value, adc_values)
            random_value = self._whiten_entropy()

            # Only yield a new value if it is different from the last one
            if random_value != self.last_entropy:
                self.last_entropy = random_value
                return random_value
