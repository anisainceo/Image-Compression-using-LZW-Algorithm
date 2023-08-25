from LZW import LZWCoding
import sys

path = "tobe.txt"

l = LZWCoding(path, 12)
output_path= l.write_compressed_file()
print("output path: ",output_path)
decom_path = l.decompress_file(output_path)
print("Decompressed file path: " + decom_path)