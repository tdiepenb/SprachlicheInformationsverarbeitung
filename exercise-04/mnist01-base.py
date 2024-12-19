import csv
from sklearn.naive_bayes import CategoricalNB
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
import numpy as np


def read_dataset(filename):
    x = []
    y = []
    with open(filename, newline="") as csvfile:
        next(csvfile)
        reader = csv.reader(csvfile, delimiter=",")
        for row in reader:
            y.append(int(row[0]))
            x.append([int(pixel) for pixel in row[1:]])
    return (np.array(x), np.array(y))


x_train, y_train = read_dataset("./mnist01/train.csv")

x_test, y_test = read_dataset("./mnist01/test.csv")

print(f"Training items: {len(x_train)}")
print(f"Test items: {len(x_test)}")

print("train image", x_train[0])
print("train_true", y_train[0])
print("train image shape", len(x_train[0]))

print("test image", x_test[0])
print("test_true", y_test[0])
print("test image shape", len(x_test[0]))

print(f"x_train shape: {x_train.shape}")
print(f"x_test shape: {x_test.shape}")


bayesModel = CategoricalNB()
bayesModel.fit(x_train, y_train)

bayesPredict = bayesModel.predict(x_test)


print("Accuracy = {} %".format(accuracy_score(y_test, bayesPredict) * 100))
print(
    "Classification Report \n {}".format(
        classification_report(y_test, bayesPredict, labels=range(0, 10))
    )
)
