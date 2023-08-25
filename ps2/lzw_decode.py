def lzw_decode(encoded_data):
    # Initialize the dictionary with all possible single-character patterns
    dictionary = {i: chr(i) for i in range(256)}
    
    # Initialize variables
    current_code = encoded_data[0]
    output = dictionary[current_code]
    previous_string = output
    
    # Loop through the input codes
    for code in encoded_data[1:]:
        if code in dictionary:
            current_string = dictionary[code]
        elif code == len(dictionary):
            current_string = previous_string + previous_string[0]
        else:
            raise ValueError("Bad compressed code")
        
        # Output the current string and add it to the dictionary
        output += current_string
        dictionary[len(dictionary)] = previous_string + current_string[0]
        previous_string = current_string
    
    return output