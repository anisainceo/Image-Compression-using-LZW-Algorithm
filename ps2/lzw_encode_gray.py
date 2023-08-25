
import numpy as np

def lzw_encode_gray(image):
    # Initialize the dictionary with all possible pixel intensities
    dictionary = {i: i for i in range(256)}
    
    # Convert the input image to a 1D array
    input_data = np.array(image).ravel()
    
    # Initialize variables
    current_pixel = input_data[0]
    output = []
    code = 256
    
    # Loop through the input data
    for pixel in input_data[1:]:
        # If the current pixel plus the next pixel is in the dictionary, update the current pixel
        if current_pixel * 256 + pixel in dictionary:
            current_pixel = current_pixel * 256 + pixel
        else:
            # Output the code for the current pixel and add the new pattern to the dictionary
            output.append(dictionary[current_pixel])
            dictionary[current_pixel * 256 + pixel] = code
            code += 1
            current_pixel = pixel
    
    # Output the code for the final pixel
    output.append(dictionary[current_pixel])
    
    return output