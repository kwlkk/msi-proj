from sklearn.externals import joblib
from numpy import genfromtxt
from sklearn.metrics import accuracy_score

class DGRecognizer:
    def many(self, model_path, file_path):
        model = joblib.load(model_path)

        X_test = genfromtxt(file_path, delimiter=',', skip_header=1)
        y_test = X_test[:, 0]
        X_test = X_test[:, 1:]

        y_pred = model.predict(X_test)
        score = accuracy_score(y_test, y_pred)

        print("Accuracy = %.3f" % score)

    def single(self, model_path, file_path):
        model = joblib.load(model_path)
        X_test = genfromtxt(file_path, delimiter=',')
        X_test = X_test.reshape(1, -1)
        y_pred = model.predict(X_test)
        print(y_pred)
