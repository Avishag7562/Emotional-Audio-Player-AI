from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
import pandas as  pd


data = pd.read_csv(r"C:\Users\Avishag\OneDrive\songs_data.csv")
X = data.loc[:, 'tempo':]
y = data['class']
featureName = list(X)
for name in featureName:
    X[name] = (X[name]-X[name].min())/(X[name].max()-X[name].min())
    print("X[name].min",X[name].max)




