import seaborn as sns
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix

data=sns.load_dataset('iris')
print(data.head())

X=data.drop('species',axis=1)
y=data['species']   
model=DecisionTreeClassifier(max_depth=15, random_state=0,min_samples_leaf=5,min_impurity_decrease=0.2)
model.fit(X,y)
y_pred=model.predict(X)
print(classification_report(y,y_pred))
print(confusion_matrix(y,y_pred))   