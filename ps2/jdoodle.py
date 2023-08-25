import cv2

# Read in the input image
image = cv2.imread('input.png', cv2.IMREAD_GRAYSCALE)

# Compress the image
encoded_data = lzw_encode_gray(image)

# Save the compressed data to a file
with open('compressed.dat', 'wb') as f:
    for code in encoded_data:
        f.write(code.to_bytes(2, byteorder='big'))

# Read in the compressed data from the file
with open('compressed.dat', 'rb') as f:
    encoded_data = []
    while True:
        code = f.read(2)
        if not code:
            break
        encoded_data.append(int.from_bytes(code, byteorder='big'))

# Decompress the image
width = image.shape[1]
height = image.shape[0]
decoded_image = lzw_decode_gray(encoded_data, width, height)

# Save the decompressed image to a file
cv2.imwrite('output.png', decoded_image)
