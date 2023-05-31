import re

input_file_path = "input.txt"
output_file_path = "output.txt"

#pattern match the expressions
pattern = r'\"ecdsa_public_key\"\:\{\"b\"\:\"([A-Za-z0-9\+\/\=]+)\"\,\"curve\"\:\"([A-Za-z0-9\-\_]+)\"\,\"gx\"\:\"([A-Za-z0-9\+\/\=]+)\"\,\"gy\"\:\"([A-Za-z0-9\+\/\=]+)\"\,\"length\"\:([0-9]+)\,\"n\"\:\"([A-Za-z0-9\+\/\=]+)\"\,\"p\"\:\"([A-Za-z0-9\+\/\=]+)\"'

unique_curves = set()
all_keys = []
with open(input_file_path, 'r') as input_file:
    #read input
    for line in input_file:
        matches = re.findall(pattern, line)
        for match in matches:
            #create tuple
            b, curve, gx, gy, length, n, p = match
            key = (b, curve, gx, gy, length, n, p)
            all_keys.append(key)
            unique_curves.add(key)

#output the parameters for each curve & number of times it appears
with open(output_file_path, 'w') as output_file:
    for key in unique_curves:
        count = all_keys.count(key)
        output_file.write(f"{key}\n{count}\n\n")
        total_count = len(all_keys)
    unique_count = len(unique_curves)
    output_file.write(f"Total keys: {total_count}\nUnique Curves: {unique_count}\n")