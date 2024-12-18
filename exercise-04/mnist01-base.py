import csv
from sklearn.naive_bayes import CategoricalNB
from sklearn.metrics import classification_report

def read_dataset(filename):
  x = []
  y = []
  with open(filename, newline='') as csvfile:
    next(csvfile)
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
      y.append(int(row[0]))
      x.append([int(pixel) for pixel in row[1:]])
  return (x,y)

x_train, y_train = read_dataset("mnist01/train.csv")
x_test, y_test = read_dataset("mnist01/test.csv")

print(f"Training items: {len(x_train)}")
print(f"Test items: {len(x_test)}")

