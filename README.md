# RP2040-RNG
Temporary repo

### Diehard Test for Validation
To perform a Diehard test reliably and validate the random number generator for RP2040, it is recommended to generate a sample of at least several million bits. For example, for a sample of 10 million bits, it is necessary to generate approximately 156,250 64-bit numbers.

Number of bits needed :
For example, if you need 1 million bits, you will need to generate about :



$$
\frac{10^{6} \, \text{bits}}{64 \, \text{bits by number}} \approx 15625 \, \text{64-bit numbers}
$$
