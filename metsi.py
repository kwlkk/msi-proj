import matplotlib.pyplot as plt
from sklearn.externals import joblib

from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from sklearn.ensemble import VotingClassifier
from sklearn.model_selection import cross_val_score

from numpy import genfromtxt, array, append

# Load train data set 
data = genfromtxt('train.csv', delimiter=',', skip_header=1)

# Split features and labels
X = data[:, 1:]
y = data[:, 0]

"""
# Wyświetlenie przykładowego zdjęcia
img1 = X[8, :]
img1.shape = ((28, 28))
print(img1.shape)
imgplot = plt.imshow(img1)
plt.show()
"""

clf1 = KNeighborsClassifier()
clf2 = GaussianNB()
clf3 = DecisionTreeClassifier()
clf4 = SVC()

eclf = VotingClassifier(
    estimators=[('KNN', clf1), ('GNB', clf2), ('DT', clf3)], voting='hard')
eclf = eclf.fit(X, y)

print("Fit score: ", eclf.score(X, y))

# Cross Validation 5x2
arr = array([])

for i in range(5):
    eclf_sc = cross_val_score(eclf, X, y, cv=2)
    arr = append(arr, eclf_sc)

print("Standard deviation", arr.std(), ", Mean: ", arr.mean())

# Create model
joblib.dump(eclf, 'model.joblib')
