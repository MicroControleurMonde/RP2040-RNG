# rp2040_generate_random.py

import rp2040_rng_lib  # Importing the rp2040_rng_lib library

def main():
    # Creating an instance of the random number generator
    random_generator = rp2040_rng_lib.RandomGenerator()

    # Generating a unique random number
    random_value = random_generator.generate()

    # Displaying the generated random number
    print(f"Generated random number: {random_value}")

# Running the main function
if __name__ == "__main__":
    main()
