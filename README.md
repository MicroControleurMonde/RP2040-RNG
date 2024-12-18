# RP2040  Random Number Generator (RNG)

![Image locale](https://github.com/MicroControleurMonde/RP2040-RNG/blob/main/Reports/RP2040-resizeimage3.png)

### Breakdown of Sections

1. **Project Description**: Generation of random numbers using the RP2040 and various entropy sources.
2. **Features**: Lists the main features of the project, such as the use of ADC for entropy, SHA-256 whitening, and the use of RTC for additional randomness.
3. **Requirements**: Specifies what hardware and software are needed.
4. **Installation**: Provides steps for cloning the repository and uploading the files to the RP2040.
5. **Usage**: Details how to use the library and run the example script (generate_random.py).
6. **How it Works**: Explains the steps involved in generating random numbers and how entropy is collected, mixed, and whitened.
7. **Performance and output**: calculation of the TRNG yield.
8. **Testing Randomness**: Mentions statistical tests that can be used to evaluate the quality of randomness.
9. **Diehard Test for Validation**:  Test reliably and validation.
10. **Precautions of use** 
11. **Acknowledgements**: Credits any technologies or libraries used in the project.
12. **Disclaimer**

## Project Description

This project implements a **True Random Number Generator (TRNG)** using the **RP2040** microcontroller. The generator collects entropy from an **ADC** (Analog-to-Digital Converter) and mixes it with a **SHA-256** hashing function to produce high-quality random numbers. The randomness is further enhanced by using the **RP2040's RTC (Real-Time Clock)** for time-based entropy.

## Features

- **ADC-based entropy**: Collects noise-based entropy using the RP2040's ADC (GPIO 28).
- **Entropy mixing**: Uses XOR and Linear Congruential Generator (LCG) techniques for mixing the entropy.
- **SHA-256 whitening**: Applies the **SHA-256** hash function to whiten the entropy and reduce correlations.
- **Real-Time Clock (RTC)**: Uses the RP2040's RTC to add time-based entropy for further randomness.
- **Counter-based variability**: Introduces additional variability using an internal counter.

## Requirements

- **RP2040-based microcontroller**.
- **MicroPython** firmware installed on the board.
- **`machine`**, **`utime`**, and **`hashlib`** libraries (built-in with MicroPython).

## Installation

### 1. Clone the repository

- git clone https://github.com/MicroControleurMonde/RP2040-RNG/rp2040-trng.git
- cd rp2040-trng

### 2. Upload the files to your RP2040 board
Upload the following Python files to your RP2040 board:

- rp2040_rng_lib.py
- generate_random.py

### 3. Run the script
Once the files are uploaded, you can run the 'generate_random.py' script to start generating random numbers.

## Usage
#### 1. rp2040_rng_lib.py – Library for generating random numbers
This Python library provides a class ***RandomGenerator*** that generates random numbers based on the RP2040's ADC and a SHA-256 whitening process.

#### 2. generate_random.py – Example script
This script imports the RandomGenerator class from ***rp2040_rng_lib.py*** and generates one random number at a time.

#### Output Example:

Generated random number: 4779610172586853948

## How it Works

### 1. Entropy Collection
The generator uses the analog signal captured by the ADC (analog-to-digital converter) to obtain entropy from sources such as electronic noise, temperature fluctuations, or other random physical phenomena.

### 2. Entropy Mixing
The collected entropy is mixed using XOR operations and a Linear Congruential Generator (LCG) to enhance randomness.

### 3. Whitening

The whitening process with the SHA-256 makes possible to transform the collected entropy, often biased or correlated, into a truly random output by eliminating patterns and predictability.

### 4. Time-based Entropy
The current Unix timestamp from the RP2040's RTC is used to further whiten the entropy.

### 5. Output
The final output is a 64-bit random number that is periodically generated and can be used in applications requiring randomness.

## Performance and output

Generating 100,000 random numbers (64 bits) and saving them.

Elapsed time to generate 100000 random numbers: 424.00 seconds.

**Random number generation rate: 1886.79 bytes per second.**

Number of random numbers generated per second:
(100'000/424) ≈ **235**

## Testing Randomness

To ensure the quality of the random numbers, you can use statistical randomness tests such as:

- **Diehard Tests**
[Dieharder: A Random Number Test Suite Version 3.31.1] (https://webhome.phy.duke.edu/~rgb/General/dieharder.php)

This test will help evaluate the strength of the randomness generated by this code. 

The Dieharder tests Test Suite is used to evaluate whether the output of the random number generator is sufficiently unpredictable and complies with the statistical criteria of pure random numbers.

## Diehard Test for Validation

To perform a Diehard test reliably and validate the random number generator for RP2040, it is recommended to generate a sample of at least several million bits.

For example, for a sample of 10 million bits, you will need to generate approximately **156,250** 64-bit numbers.

- Diehard test results (over 200,000 values) can be found in the file **'diehard_sample_report.txt '**.

[Diehard sample report.txt](https://github.com/MicroControleurMonde/RP2040-RNG/blob/main/Reports/diehard_sample_report.txt)
  
- General results comments  in the file **'diehard_sample_report.md '**.

[Diehard Test for Validation](https://github.com/MicroControleurMonde/RP2040-RNG/blob/main/Reports/diehard_sample_report.md)

### Number of bits needed
To generate 1 million bits, you will need to generate about:

$$
\frac{10^{6} \, \text{bits}}{64 \, \text{bits by number}} \approx 15625 \, \text{64-bit numbers}
$$

## Precautions of use

Please consult the CAcert tests and analyses report before considering the use of this generator.

[CAcert tests and analyses](https://github.com/MicroControleurMonde/RP2040-RNG/blob/main/Reports/CAcert_Analysys.md)

## Ent Tests
Ent sources (www.fourmilab.ch/random/)

[Ent Report - Raw](https://github.com/MicroControleurMonde/RP2040-RNG/blob/main/Reports/Ent_Report_RP2040.tx)

## Acknowledgements

The project is based on the **RP2040 microcontroller**, and its **MicroPython firmware**.  
The entropy whitening is done using the **SHA-256 algorithm** from the **hashlib** library.

Tested on an original Raspberry Pi Pico, a XIAO seed studio RP2040 and a Waveshare RP2040-Plus. 
The code works perfectly on all three platforms, regardless of the ADC channel used. 

* Raspberry Pi Pico: MicroPython v1.23.0 on 2024-06-02; 
* XIAO seed studio: MicroPython v1.22.1 on 2024-01-05;
* Waveshare RP2040-Plus:  MicroPython ef518cbf2-dirty on 2023-03-24; 

## Disclaimer

The code contained in this repository is provided “as is”, without any warranty of performance, accuracy or result. The author shall not be liable for any direct or indirect damages that may result from the use of this code, including, but not limited to, loss of data or interruption of service.

Use of this code is entirely at your own risk. Please ensure that you fully understand the code before using it in a production environment or integrating it into your projects.
