import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib
from sklearn.metrics import confusion_matrix
import seaborn as sns

df = pd.read_csv(r"C:\Users\Avishag\OneDrive\songs_data.csv")
df.head()

x = df.drop(['id', 'class', 'label', 'song_name', 'Unnamed: 0'], axis=1)
y = df['class']

from sklearn.preprocessing import StandardScaler

ss = StandardScaler()
ss.fit(x)
joblib.dump(ss, 'fitted_scaler.save')
cols = x.columns
x = pd.DataFrame(ss.transform(x))
x.columns = cols
x.head()

# Decision Tree Classifier #

from sklearn import tree
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split

# used to ensure that the class proportions in the target variable (usually denoted as y) are maintained in both the training and testing sets.
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, stratify=y)

model = tree.DecisionTreeClassifier()
param_grid = {'criterion': ['gini', 'entropy']}
dt = model.fit(X_train, y_train)
dtree_cv = GridSearchCV(model, param_grid, cv=8)
dtree_cv.fit(X_train, y_train)
dtree_ypred = dtree_cv.predict(x)

pd.crosstab(y, dtree_ypred, rownames=['True'], colnames=['Predicted'], margins=True)

cm = confusion_matrix(y, dtree_ypred)
sns.heatmap(cm, annot=True)
plt.xlabel('predicted')
plt.ylabel('truth')

print('Testing Accuracy is:', dtree_cv.score(x, y) * 100, '%')


# K Nearest Neighbors #
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

X = x.loc[:, :]
featureName = list(X)
for name in featureName:
    X[name] = (X[name] - X[name].min()) / (X[name].max() - X[name].min())

# Create the KNeighborsClassifier and define the hyperparameter grid
knn = KNeighborsClassifier()
param_grid = {'n_neighbors': np.arange(1, 25)}
knn_cv = GridSearchCV(knn, param_grid, cv=10)
knn_cv.fit(X, y)

print(knn_cv.best_params_)

knn = KNeighborsClassifier(22)
knn_cv = knn.fit(X, y)

knn_Y_pred = knn_cv.predict(X)
pd.crosstab(y, knn_Y_pred, rownames=['True'], colnames=['Predicted'], margins=True)

print("Accuracy Score is: ", accuracy_score(y, knn_Y_pred) * 100, '%')

# Random Forest Classifier #

from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics

model1 = RandomForestClassifier(n_estimators=16)
param = {'n_estimators': np.arange(1, 20)}
rmodel_cv = GridSearchCV(model1, param, cv=10)
rmodel_cv.fit(x, y)

print("best params RandomForestClassifier: ", rmodel_cv.best_params_)
print(rmodel_cv.best_score_)

model1 = RandomForestClassifier(n_estimators=16)
rmodel = model1.fit(x, y)
rmodel_y_pred = rmodel.predict(x)

cm = confusion_matrix(y, rmodel_y_pred)
sns.heatmap(cm, annot=True)
plt.xlabel('predicted')
plt.ylabel('truth')

rY_pred = rmodel_cv.predict(x)
pd.crosstab(y, rY_pred, rownames=['True'], colnames=['Predicted'], margins=True)

print("Accuracy Score is: ", metrics.accuracy_score(y, rY_pred) * 100, '%')

joblib.dump(rmodel, './rmodel.joblib')

# Gaussian Naive Bayes Classifier #

from sklearn.naive_bayes import GaussianNB

gnb = GaussianNB()
gnb = gnb.fit(x, y)
gnby_pred = gnb.predict(x)

pd.crosstab(y, gnby_pred, rownames=['True'], colnames=['Predicted'], margins=True)

print("Accuracy Score is:", metrics.accuracy_score(y, gnby_pred) * 100)
