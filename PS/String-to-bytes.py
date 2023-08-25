from LZW import LZWCoding
from integer_to_bytes import int_array_to_binary_string
import sys
array1 = [84,79,66,256]
path = "tobe.txt"
path= "numbers.txt"
codelength = 9
l = LZWCoding(path, codelength)
#print("integer codes: ", array1)
bitstr = int_array_to_binary_string(array1, codelength)
print("bit string: ",bitstr)
print("total number of bits: ", len(bitstr))
#print("integer from first", codelength, " bits: ",int(bitstr[0:12],2))
padded = l.pad_encoded_text(bitstr)
print("length of padded string",len(padded), ",padded string: ", padded)
my_byte_array = l.get_byte_array(padded)
#print(my_byte_array)

bit_string = ""
for byte in my_byte_array:
        #byte = ord(byte)
        bits = bin(byte)[2:].rjust(8, '0')
        bit_string += bits
print("padded_bit_string:", bit_string)
encoded_text = l.remove_padding(bit_string)
decompressed_text = l.decompress(encoded_text)
print("decompressed data:",decompressed_text )











