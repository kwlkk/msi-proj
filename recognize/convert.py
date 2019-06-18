import glob
from PIL import Image
import numpy as np
import sys
import os
import csv
import os.path

def convertPicture(img_path):

    img_file = Image.open(img_path)
    
    img_grey = img_file.convert('L')

    value = np.asarray(img_grey.getdata(), dtype=np.int).reshape((img_grey.size[1], img_grey.size[0]))
    value = value.flatten()

    x = lambda z: (-z + 255)
    new_value = np.array([x(a) for a in value])
    
    if os.path.isfile(img_path + ".csv"):
        os.remove(img_path + ".csv")
        print("File found")

    with open(img_path + ".csv", 'a') as f:
        writer = csv.writer(f)
        writer.writerow(new_value)

    print(img_path + " converting done.")
    return img_path + ".csv"
