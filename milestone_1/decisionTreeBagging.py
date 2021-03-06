import pandas as pd
import numpy as np
import sys
from sklearn import tree
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.ensemble import BaggingClassifier
from sklearn.model_selection import cross_val_score

def validate_cmdline_args(nargs, msg):
    if len(sys.argv) < nargs:
        print(msg)
        sys.exit(1)
validate_cmdline_args(3,'Usage: python decisionTree_bagging.py <DATASET_PATH_RED> <DATASET_PATH_WHITE>')
DATASET_PATH_RED = sys.argv[1]
DATASET_PATH_WHITE = sys.argv[2]

data_features = ["fa","va","ca","rs","ch","fsd","tsd","dens","pH","sulp","alcohol","eval"]
data_red = pd.read_csv(DATASET_PATH_RED,names=data_features)
data_white = pd.read_csv(DATASET_PATH_RED,names=data_features)
clf = BaggingClassifier(tree.DecisionTreeClassifier(), max_samples=0.5, max_features=0.5)

                                    ## Red Wine ##
print('-------------Red Wine Evaluation-------------')

train_x, test_x, train_y, test_y = train_test_split(data_red[data_features[:10]],data_red[data_features[11]], train_size=0.7)

clf_mult_fit = clf.fit(train_x,train_y)

print('Decision Tree with Bagging Multinomial Classification Train Accuracy :: {}'.format(metrics.accuracy_score(train_y, clf_mult_fit.predict(train_x))))
print('Decision Tree with Bagging Multinomial Classification Test Accuracy :: {}'.format(metrics.accuracy_score(test_y, clf_mult_fit.predict(test_x))))
print('Multinomial CV-prediction error rate :: {}'.format(cross_val_score(clf, data_red[data_features[:10]], data_red[data_features[11]], cv=10)))


train_y[train_y<5] = 0
train_y[train_y>=5] = 1
test_y[test_y<5] = 0
test_y[test_y>=5] = 1
cv_x = data_red[data_features[:10]]
cv_y = data_red[data_features[11]]
cv_y[cv_y<5] = 0
cv_y[cv_y>=5] = 1


clf_bin_fit = clf.fit(train_x, train_y)

print('Decision Tree with Bagging Binary Classification Train Accuracy :: {}'.format(metrics.accuracy_score(train_y, clf_bin_fit.predict(train_x))))
print('Decision Tree with Bagging Binary Classification Test Accuracy :: {}'.format(metrics.accuracy_score(test_y, clf_bin_fit.predict(test_x))))
print('Binary CV-prediction error rate :: {}'.format(cross_val_score(clf, cv_x, cv_y, cv=10)))

                                    ## White Wine ##
print('-------------White Wine Evaluation-------------')

train_x_w, test_x_w, train_y_w, test_y_w = train_test_split(data_white[data_features[:10]],data_white[data_features[11]], train_size=0.7)

clf_mult_fit_w = clf.fit(train_x_w,train_y_w)

print('Decision Tree with Bagging Multinomial Classification Train Accuracy :: {}'.format(metrics.accuracy_score(train_y_w, clf_mult_fit_w.predict(train_x_w))))
print('Decision Tree with Bagging Multinomial Classification Test Accuracy :: {}'.format(metrics.accuracy_score(test_y_w, clf_mult_fit_w.predict(test_x_w))))
print('Multinomial CV-prediction error rate :: {}'.format(cross_val_score(clf, data_white[data_features[:10]], data_white[data_features[11]], cv=10)))

train_y_w[train_y_w<5] = 0
train_y_w[train_y_w>=5] = 1
test_y_w[test_y_w<5] = 0
test_y_w[test_y_w>=5] = 1
cv_x_w = data_white[data_features[:10]]
cv_y_w = data_white[data_features[11]]
cv_y_w[cv_y_w<5] = 0
cv_y_w[cv_y_w>=5] = 1

clf_bin_fit_w = clf.fit(train_x_w, train_y_w)

print('Decision Tree with Bagging Classification Train Accuracy :: {}'.format(metrics.accuracy_score(train_y_w, clf_bin_fit_w.predict(train_x_w))))
print('Decision Tree with Bagging Classification Test Accuracy :: {}'.format(metrics.accuracy_score(test_y_w, clf_bin_fit_w.predict(test_x_w))))
print('Binary CV-prediction error rate :: {}'.format(cross_val_score(clf,cv_x, cv_y, cv=10)))
