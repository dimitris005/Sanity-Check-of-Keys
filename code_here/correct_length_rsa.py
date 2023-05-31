import re
import base64

pattern = re.compile(r'"modulus":"(.*?)"')
unique_moduli = set()

with open('input.txt', 'r') as infile, open('output.txt', 'w') as outfile:
    for line in infile:
        for modulus in pattern.findall(line):
            modulus_bytes = base64.urlsafe_b64decode(modulus + '==')
            modulus_hex = int.from_bytes(modulus_bytes, byteorder='big')
            hex_modulus = hex(modulus_hex)[2:] # remove the leading "0x" from the hexadecimal string
            if len(hex_modulus) < 256:
                hex_modulus = '0' * (256 - len(hex_modulus)) + hex_modulus # pad with zeros
            if hex_modulus not in unique_moduli:
                unique_moduli.add(hex_modulus)
                outfile.write(hex_modulus + '\n')