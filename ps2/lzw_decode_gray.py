def lzw_decode_gray(encoded_data, width, height):
    # Initialize the dictionary with all possible pixel intensities
    dictionary = {i: i for i in range(256)}
    
    # Initialize variables
    current_code = encoded_data[0]
    output = [current_code]
    previous_pixel = current_code
    
    # Loop through the input codes
    for code in encoded_data[1:]:
        if code in dictionary:
            current_pixel = dictionary[code]
        elif code == len(dictionary):
            current_pixel = previous_pixel + (previous_pixel & 0xFF)
        else:
            raise ValueError("Bad compressed code")
        
        # Output the current pixel and add it to the dictionary
        output.append(current_pixel)
        dictionary[len(dictionary)] = previous_pixel * 256 + (current_pixel & 0xFF)
        previous_pixel = current_pixel
    
    # Convert the output to a 2D array with the specified width and height
    output = np.array(output).reshape((height, width))
    
    return output.astype(np.uint8)