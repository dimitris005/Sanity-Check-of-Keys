import re

# Define the regular expression pattern
pattern = r'"x":"([^"]+)","y":"([^"]+)"'

# Create a set to store unique pairs of (x, y)
unique_pairs = set()

# Open the input file and read its contents
with open('input.txt', 'r') as f:
    input_text = f.read()

# Find all matches of the pattern in the input text
matches = re.findall(pattern, input_text)

# Open the output file for writing
with open('output.txt', 'w') as f:
    # Loop over the matches and write each pair of (x, y) to the output file
    for match in matches:
        x, y = match
        pair = (x, y)
        # Only write the pair to the output file if it's not already in the set of unique pairs
        if pair not in unique_pairs:
            f.write(f'{x},{y}\n')
            unique_pairs.add(pair)

# Print the total number of keys encountered and the number of unique keys
total_keys = len(matches)
unique_keys = len(unique_pairs)
print(f'Total keys encountered: {total_keys}')
print(f'Unique keys: {unique_keys}')