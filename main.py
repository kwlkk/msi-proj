import sys
import os.path
from recognize.convert import convertPicture
from recognize.digit_recognizer import DGRecognizer

if len(sys.argv) > 1:

    if sys.argv[1]=="single":
        model_path = sys.argv[2]
        img_path = sys.argv[3]

        if os.path.exists(model_path) & os.path.exists(img_path):
            file_path = convertPicture(img_path)
            dgr = DGRecognizer()
            dgr.single(model_path, file_path)
        else: 
            print("No such file or directory")

    if sys.argv[1]=="many":
        model_path = sys.argv[2]
        file_path = sys.argv[3]

        if os.path.exists(model_path) & os.path.exists(file_path):
            dgr = DGRecognizer()
            dgr.many(model_path, file_path)
        else: 
            print("No such file or directory")
            