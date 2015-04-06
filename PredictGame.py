from sklearn import naive_bayes
from sklearn.naive_bayes import GaussianNB
from sklearn import datasets
from sklearn import metrics
import numpy as np
from sklearn.naive_bayes import MultinomialNB

#mnb = naive_bayes.MultinomialNB();
#mnb.fit(xtrain,ytrain);
#print "classification accuracy of MNB = ",mnb.score(xtest,ytest)
dataset = datasets.load_iris()
model = GaussianNB()
model.fit(dataset.data, dataset.target)
#fit(x,y) - Fit Naive Bayes classifier according to X, y
#x=training, y=target values
print(model)
#X = np.random.randint(5, size=(6, 100))
#y = np.array([1, 2, 3, 4, 5, 6])
#clf = naive_bayes.MultinomialNB()
#clf.fit(X, y)
expected = dataset.target
predicted = model.predict(dataset.data)
#predict(X) - Perform classification on an array of test vectors X.
#returns predicted targeted values for X
print(metrics.classification_report(expected, predicted))
print(metrics.confusion_matrix(expected, predicted))

#MultinomialNB(alpha=1.0, class_prior=None, fit_prior=True)
#class_prior = prior probs for the classes
#default value for alpha is 1.0. It is the smoothing parameter
#print(clf.predict(X[2]))
#predict(X) - Perform classification on an array of test vectors X.
#returns predicted targeted values for X