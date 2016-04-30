import csv
import os
import sklearn
from sklearn.svm import SVC


class Classifier(object):

    def __init__(self):
        self.data = []
        self.test_data = []
        self.path = "C:\\Users\\JAN\\PycharmProjects\\BSK-SPAM-filter"
        [self.load_data(self.path + "\\" + path, self.data) for path in os.listdir(self.path) if "training.csv" in path]
        [self.load_data(self.path + "\\" + path, self.test_data) for path in os.listdir(self.path) if "testing.csv" in path]

    def load_data(self, path, data):
        print path
        with open(path, "rU") as infile:
            r = csv.reader(infile)
            for row in r:
                if len(row) > 1:
                    if "non_" in path:
                        row.append('0')
                        data.append(row)
                    else:
                        row.append('1')
                        data.append(row)

    def train(self):
        x_train = []
        y_train = []
        x_test = []
        y_test = []
        for row in self.data:
            x_train.append(row[0:len(row) - 2])
            y_train.append(row[len(row)-1])
        for row in self.test_data:
            x_test.append(row[0:len(row) - 2])
            y_test.append(row[len(row) - 1])
        clf = SVC()
        clf.fit(x_train, y_train)
        print "score: ", clf.score(x_test, y_test)


def main():
    c = Classifier()
    c.train()


main()
