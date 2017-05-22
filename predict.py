import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
import pandas as pd
import discretize_label
from sklearn.model_selection import train_test_split

names = ["Neural Net"]
classifier = MLPClassifier(alpha=1)

# load wordvector (features) here
X = np.load("docvec60000")
X = np.matrix(X)
X = StandardScaler().fit_transform(X)

# load volatility (labels) here
y_all = pd.read_csv("../nlp-forex-predict/fxdata/dataset60000aa.csv")
print "available pairs: ", list(y_all)
y_pair_name = list(y_all)[18]  # specify USD/JPY
print "Selected pair:", y_pair_name

# make the volatility descrite, combine them and make dataset
y_continuouse = np.asarray(y_all[y_pair_name].tolist())
y = discretize_label.discretise_label(y_continuouse)

fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
ax1.plot(y_continuouse)
ax2 = fig1.add_subplot(111, sharex=ax1, frameon=False)
ax2.yaxis.tick_right()
ax2.yaxis.set_label_position("right")
ax2.plot(y,'r')

dataset = (X, y) 

# preprocess dataset, split into training and test part
X, y = dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.1, random_state=42)
classifier.fit(X_train, y_train)
score = classifier.score(X_test, y_test)
print score # only accuracy is available.
plt.show()
