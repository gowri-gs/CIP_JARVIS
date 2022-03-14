
import csv
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score,confusion_matrix
import numpy as np

from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import AdaBoostClassifier
X = "C:\\Users\\ADMIN\\Desktop\\ipclssf(train).csv"
y = "C:\\Users\\ADMIN\\Desktop\\opclssf(train).csv"
X_train = []
y_train = []
with open(X) as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)  # change contents to float
    for row in reader: #each row is a list
        X_train.append(row)
with open(y) as csvfile1:
    reader1 = csv.reader(csvfile1, quoting=csv.QUOTE_NONNUMERIC)  # change contents to float

    for row in reader1:  # each row is a list
        y_train.append(row)

q = "C:\\Users\\ADMIN\\Desktop\\ipclssf(test).csv"
p = "C:\\Users\\ADMIN\\Desktop\\opclssf(test).csv"
q_train = []
p_train = []
with open(q) as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)  # change contents to floats
    for row in reader:  # each row is a list
        q_train.append(row)

with open(p) as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)  # change contents to floats
    for row in reader:  # each row is a list
        p_train.append(row)

# validation part
X_test = np.array(q_train)
y_test = np.array(p_train)

X_t = np.array(X_train)
y_t = np.array(y_train)

classifier1 = DecisionTreeClassifier()
classifier1.fit(X_t,y_t.ravel())
y_pred = classifier1.predict(X_test)
confusion_mat = confusion_matrix(y_test,y_pred)
accuracy = accuracy_score(y_test,y_pred)*100
print('\nAccuracy of the Decision Tree Classifier CART model: '+str(round(accuracy,2))+'%')
print('Precision: %.3f' % precision_score(y_test, y_pred))
print('Recall: %.3f' % recall_score(y_test, y_pred))
print('F1 Score: %.3f' % f1_score(y_test, y_pred))

#kf = StratifiedKFold(n_splits=5)
rf = RandomForestClassifier(n_estimators=100,random_state=95)
rf.fit(X_t,y_t.ravel())
y_pred = rf.predict(X_test)
confusion_mat = confusion_matrix(y_true=y_test,y_pred=y_pred)
accuracy = accuracy_score(y_test,y_pred)*100
#allacc = cross_val_score(estimator=rf, X=X_test, y=y_test, cv=kf)
#print('Accuracy mean for Random forest:',allacc.mean())
print('Accuracy of the RandomForest model: '+str(round(accuracy,2))+'%')
print('Precision: %.3f' % precision_score(y_test, y_pred))
print('Recall: %.3f' % recall_score(y_test, y_pred))
print('F1 Score: %.3f' % f1_score(y_test, y_pred))
file_name = "C:\\Users\\ADMIN\\Desktop\\groomrf.sav"
pickle.dump(rf,open(file_name,'wb'))

from sklearn.naive_bayes import GaussianNB

gnb = GaussianNB()
#kf1 = StratifiedKFold(n_splits=5)
gnb.fit(X_t,y_t.ravel())
y_pred = gnb.predict(X_test)
confusion_mat = confusion_matrix(y_test,y_pred)
accuracy = accuracy_score(y_test,y_pred)*100
#allacc1 = cross_val_score(estimator=gnb, X=X_test, y=y_test, cv=kf1)
#print('Accuracy mean for Naive bayes:',allacc1.mean())
print('\nAccuracy of the Naive bayes model: '+str(round(accuracy,2))+'%')
print('Precision: %.3f' % precision_score(y_test, y_pred))
print('Recall: %.3f' % recall_score(y_test, y_pred))
print('F1 Score: %.3f' % f1_score(y_test, y_pred))
file_name = "C:\\Users\\ADMIN\\Desktop\\groomgnb.sav"
pickle.dump(gnb,open(file_name,'wb'))


classifier = KNeighborsClassifier(n_neighbors = 8,p=2)
classifier.fit(X_t,y_t.ravel())
y_pred = classifier.predict(X_test)
confusion_mat = confusion_matrix(y_test,y_pred)
accuracy = accuracy_score(y_test,y_pred)*100
print('\nAccuracy of the KNN model: '+str(round(accuracy,2))+'%')
print('Precision: %.3f' % precision_score(y_test, y_pred))
print('Recall: %.3f' % recall_score(y_test, y_pred))
print('F1 Score: %.3f' % f1_score(y_test, y_pred))


AdaModel = AdaBoostClassifier(learning_rate=1.5)

model = AdaBoostClassifier()
clf = AdaModel.fit(X_t, y_t.ravel())
y_pred = clf.predict(X_test)
confusion_mat = confusion_matrix(y_test,y_pred)
accuracy = accuracy_score(y_test,y_pred)*100
print('\nAccuracy of the AdaBoost model: '+str(round(accuracy,2))+'%')
print('Precision: %.3f' % precision_score(y_test, y_pred))
print('Recall: %.3f' % recall_score(y_test, y_pred))
print('F1 Score: %.3f' % f1_score(y_test, y_pred))



'''
classifier = LogisticRegression()
classifier.fit(X_t,y_t.ravel())
y_pred = classifier.predict(X_test)
confusion_mat = confusion_matrix(y_test,y_pred)
accuracy = accuracy_score(y_test,y_pred)*100
print('Accuracy of the LR model: '+str(round(accuracy,2))+'%')
print('Precision: %.3f' % precision_score(y_test, y_pred))
print('Recall: %.3f' % recall_score(y_test, y_pred))
print('F1 Score: %.3f' % f1_score(y_test, y_pred))

classifier = LinearDiscriminantAnalysis()
classifier.fit(X_t,y_t.ravel())
y_pred = classifier.predict(X_test)
confusion_mat = confusion_matrix(y_test,y_pred)
accuracy = accuracy_score(y_test,y_pred)*100
print('Accuracy of the LR model: '+str(round(accuracy,2))+'%')
print('Precision: %.3f' % precision_score(y_test, y_pred))
print('Recall: %.3f' % recall_score(y_test, y_pred))
print('F1 Score: %.3f' % f1_score(y_test, y_pred))
'''

# Compare Algorithms
import pandas
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
# load dataset
url = "C:\\Users\\ADMIN\\Desktop\\data.csv"
names = ['s1', 's2', 's3', 's4', 's5', 's6', 'class']
dataframe = pandas.read_csv(url, names=names)
array = dataframe.values
X = array[:,0:6]
Y = array[:,6]
# prepare configuration for cross validation test harness
seed = 7
# prepare models
models = []
models.append(('Logistic Regression', LogisticRegression()))
models.append(('Linear Discriminant Analysis', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('Decision Tree Classifier', DecisionTreeClassifier()))
models.append(('Naive Bayes', GaussianNB()))
#models.append(('SVM', SVC()))
# evaluate each model in turn
results = []
names = []
scoring = 'accuracy'
for name, model in models:
	kfold = model_selection.KFold(n_splits=10,shuffle=True)
	cv_results = model_selection.cross_val_score(model, X, Y, cv=kfold, scoring=scoring)
	results.append(cv_results)
	names.append(name)
	msg = "%s: %f " % (name, cv_results.mean())
	print(msg)
# boxplot algorithm comparison
fig = plt.figure()
fig.suptitle('Algorithm Comparison')
ax = fig.add_subplot(111)
plt.boxplot(results)
ax.set_xticklabels(names)
plt.show()

