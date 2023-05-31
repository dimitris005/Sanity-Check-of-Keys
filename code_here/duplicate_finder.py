with open("input.txt", "r") as input_file, open("output.txt", "w") as output_file:
    unique_moduli = set()
    for line in input_file:
        # Remove any leading or trailing whitespace characters
        modulus = line.strip()

        # Add the modulus to the set if not already present
        if modulus not in unique_moduli:
            unique_moduli.add(modulus)
            output_file.write(modulus + "\n")