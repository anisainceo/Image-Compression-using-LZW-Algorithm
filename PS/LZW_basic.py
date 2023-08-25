import struct 
import math
import os

def compress(uncompressed):
    """Compress a string to a list of output symbols."""

    # Build the dictionary.
    dict_size = 256
    dictionary = {chr(i): i for i in range(dict_size)}

    w = ""
    result = []
    for c in uncompressed:
        wc = w + c
        if wc in dictionary:
            w = wc
        else:
            result.append(dictionary[w])
            # Add wc to the dictionary.
            dictionary[wc] = dict_size
            dict_size += 1
            w = c

    # Output the code for w.
    if w:
        result.append(dictionary[w])
    return result

def calculate_entropy(data):
    """Calculate the entropy of the input data."""
    
    # Count the frequency of each symbol.
    symbol_counts = {}
    for symbol in data:
        symbol_counts[symbol] = symbol_counts.get(symbol, 0) + 1
    
    # Calculate the entropy.
    entropy = 0
    total_symbols = len(data)
    for count in symbol_counts.values():
        probability = count / total_symbols
        entropy -= probability * math.log2(probability)

    return entropy

def calculate_average_code_length(data, compressed_data):
    """Calculate the average code length of the LZW-compressed data."""
    
    # Count the frequency of each symbol in the original data.
    symbol_counts = {}
    for symbol in data:
        symbol_counts[symbol] = symbol_counts.get(symbol, 0) + 1
    
    # Calculate the length of the compressed data in bytes.
    compressed_size = len(compressed_data)
    
    # Calculate the average code length in bits.
    total_symbols = sum(symbol_counts.values())
    average_code_length = (compressed_size * 8) / total_symbols

    return average_code_length

def calculate_compression_ratio(original_size, compressed_size):
    """Calculate the compression ratio of the LZW algorithm."""
    return original_size / compressed_size

def decompress(compressed):
    """Decompress a list of output ks to a string."""
    from io import StringIO

    # Build the dictionary.
    dict_size = 256
    dictionary = {i: chr(i) for i in range(dict_size)}

    # use StringIO, otherwise this becomes O(N^2)
    # due to string concatenation in a loop
    result = StringIO()
    w = chr(compressed.pop(0))
    result.write(w)
    for k in compressed:
        if k in dictionary:
            entry = dictionary[k]
        elif k == dict_size:
            entry = w + w[0]
        else:
            raise ValueError('Bad compressed k: %s' % k)
        result.write(entry)

        # Add w+entry[0] to the dictionary.
        dictionary[dict_size] = w + entry[0]
        dict_size += 1

        w = entry
    return result.getvalue()

# Open the file in read modef
with open('filename.txt', 'r') as f:
    # Read the entire contents of the file
    data = f.read()

print("input/original data:", data)

# Compress the data
compressed = compress(data)

# Print the compressed data
print("Compressed data:", compressed)

# Decompress the data
decompressed = decompress(compressed)

# Print the original data
print("Decompressed data:", decompressed)


# How to use:
data = "TOBEORNOTTOBEORTOBEORNOT"
print("input data:",data)
compressed = compress(data)
print("compressed_data: ", compressed)
decompressed = decompress(compressed)
print("decompressed_data : ",decompressed)

# Example usage:
data = "TOBEORNOTTOBEORTOBEORNOT"
compressed = compress(data)
print('Compressed data:', compressed)

# Calculate the entropy of the original data.
entropy = calculate_entropy(data)
print('Entropy of original data:', entropy)
