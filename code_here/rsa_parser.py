import re
import base64

#initiate pattern
pattern = re.compile(r'"modulus":"(.*?)"')
unique_moduli = set()

with open('input.txt', 'r') as infile, open('output.txt', 'w') as outfile:
    for line in infile:
        #find pattern in file 
        for modulus in pattern.findall(line):
            #put modulus in correct encoding 
            modulus_bytes = base64.urlsafe_b64decode(modulus + '==')
            modulus_hex = int.from_bytes(modulus_bytes, byteorder='big')
            hex_modulus = hex(modulus_hex)
            #check for uniqueness
            if hex_modulus not in unique_moduli:
                unique_moduli.add(hex_modulus)
                outfile.write(hex_modulus + '\n')
