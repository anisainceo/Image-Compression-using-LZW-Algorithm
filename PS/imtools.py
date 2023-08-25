from PIL import *
from PIL import Image
import numpy as np
import os

def compress(data):
    dictionary = {chr(i): i for i in range(256)} # Initialize dictionary with 256 ASCII values
    w = ""
    result = []
    for c in data:
        wc = w + c
        if wc in dictionary:
            w = wc
        else:
            result.append(dictionary[w])
            dictionary[wc] = len(dictionary)
            w = c
    if w:
        result.append(dictionary[w])
    return result, dictionary

def main():
    # get the current directory where this program is placed
    current_directory = os.path.dirname(os.path.realpath(__file__))
    image_file_path = current_directory + '/thumbs_up.bmp'
    img = readPILimg(image_file_path)
    img.show()
    img_gray = color2gray(img)
    img_gray.show()
    image_file_path = current_directory + '/thumbs_up_grayscale.bmp'
    savePILimg(img_gray, image_file_path)
    arr = PIL2np(img)
    new_img = np2PIL(arr)
    new_img.show()

def readPILimg(img_file_path):
    img = Image.open(img_file_path)
    return img

def savePILimg(img, img_file_path):
    img.save(img_file_path, 'bmp')

def color2gray(img):
    img_gray = img.convert('L')
    return img_gray

def PIL2np(img):
    nrows = img.size[1]
    ncols = img.size[0]
    print("nrows, ncols : ", nrows, ncols)
    imgarray = np.array(img)
    return imgarray

def np2PIL(im):
    print("size of array: ", im.shape)
    img = Image.fromarray(np.uint8(im))
    return img

if __name__=='__main__':
    main()
