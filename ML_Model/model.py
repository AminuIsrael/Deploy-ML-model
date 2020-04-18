#importing library
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')
warnings.filterwarnings('ignore', category=DeprecationWarning)

#Data Source: https://data.world/abelvikas/diabetes-type-dataset
df = pd.read_csv('Diabetestype.csv')

#Dropping the class feature
df.drop("Class",1,inplace=True)

#import the libraries
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble.gradient_boosting import GradientBoostingClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression, LogisticRegressionCV

X = df.drop('Type',1)
y = df.iloc[:,-1]

def compute_score(clf, X, y, scoring='accuracy'):
    xval = cross_val_score(clf, X, y, cv = 5, scoring=scoring)
    return np.mean(xval) #Cross validation to check for biasness and variance   


#Testing different base models
logreg = LogisticRegression()
logreg_cv = LogisticRegressionCV()
rf = RandomForestClassifier(n_estimators=50, max_features='sqrt')
gboost = GradientBoostingClassifier()
models = [logreg, logreg_cv, rf, gboost]


for model in models:
    print('Cross-validation of : {0}'.format(model.__class__))
    score = compute_score(clf=model, X=X, y=y, scoring='accuracy')
    print('CV score = {0}'.format(score))
    print('****')


#Lets try train test split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=0)


#Using the random forest algorithm
model = rf.fit(X_train,y_train)

#Saving the model with pickle
import pickle
# save the model to disk
model_name  = 'model.pkl'
pickle.dump(model, open(model_name, 'wb'))
print("[INFO]: Finished saving model...")


#