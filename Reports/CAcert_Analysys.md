# Additional tests and analyses

For greater security concerning the random number generator on RP2040, a sample of almost 700,000 values has been submitted for analysis on the CAcert site:

https://www.cacert.at/random/

The results are shown below.

![CAcert results](https://github.com/MicroControleurMonde/RP2040-RNG/blob/main/Reports/Result%20700'000%20cacert.at.png)

## Entropy (→8): 3.437706

- In this case, 3.437706 bits of entropy per byte (→8) suggests moderate, but not perfect, random quality.
- A high-quality TRNG should have an entropy score closer to 8.

## Birthday Spacing: 0.000000

- This parameter measures the complexity of the matrices used to assess the quality of the randomness generated.

## 6x8 Matrix Ranks: 0.000

- 6x8 Matrix Ranks: 0.000.
- This field is a more specific version of the previous analysis, but with a 6x8 matrix format. 

## Conclusion 

- Metrics such as entropy (3.437706) are relatively modest for a hardware generator, meaning that it is not completely free of bias or **does not achieve ideal levels of randomness**.

- Its use in Cryptography, Authentication, Session Key generation is subject to caution.

### The following uses, on the other hand, should not pose any problems
* Statistical simulations and modelling
* Software testing and validation
* Games and lotteries
* Securing hardware devices
