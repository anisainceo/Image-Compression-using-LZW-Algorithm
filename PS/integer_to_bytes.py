int_array = [84, 79, 66, 69, 79, 82, 78, 79, 84, 256, 258, 260, 265, 259, 261, 263]
array1 = [84,79,66]
codelength = 12
def int_array_to_binary_string(int_array, codelength = 12):
    import math
    bitstr = ""
    total_bits = 0
    for num in int_array:
        for n in range(codelength):
            if num & (1 << (codelength - 1 - n)):
                bitstr += "1"
            else:
                bitstr += "0"
            total_bits += 1
    #print("total number of bits: ", total_bits)
    return (bitstr)

#print(int_array_to_binary_string(array1, codelength))
print("integer codes: ", array1)
bitstr = int_array_to_binary_string(array1, codelength)
print("bit string: ",bitstr)
print("total number of bits: ", len(bitstr))
print("integer from first 12 bits: ",int(bitstr[0:12],2))

int_codes = []
for bits in range(0,len(bitstr),12):
    #print(bits)
    bits_12 = bitstr[bits:bits+12]
    print("12 bit slice: ",bits_12, ", integer code: ", int(bits_12,2))
    int_codes.append(int(bitstr[bits:bits+codelength],2))
print(int_codes)







