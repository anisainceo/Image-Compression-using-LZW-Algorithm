def lzw_encode(text):
    # Initialize the dictionary with all possible single-character patterns
    dictionary = {chr(i): i for i in range(256)}
    
    # Initialize variables
    current_pattern = text[0]
    output = []
    code = 256
    
    # Loop through the input text
    for symbol in text[1:]:
        # If the current pattern plus the next symbol is in the dictionary, update the current pattern
        if current_pattern + symbol in dictionary:
            current_pattern += symbol
        else:
            # Output the code for the current pattern and add the new pattern to the dictionary
            output.append(dictionary[current_pattern])
            dictionary[current_pattern + symbol] = code
            code += 1
            current_pattern = symbol
    
    # Output the code for the final pattern
    output.append(dictionary[current_pattern])
    
    return output
