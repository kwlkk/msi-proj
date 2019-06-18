from recognize.convert import convertPicture
from recognize.digit_recognizer import DGRecognizer

model_path = "model.joblib"
img_path = "imgs/6.png"

file_path = convertPicture(img_path)

dgr = DGRecognizer()

# model_path, file_path
dgr.single(model_path, file_path)