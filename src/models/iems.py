
# This is the as an operational package ready to use.
# ===================================================

### Importing libraries.
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import pandas as pd
from dotenv import load_dotenv

def aims(dataset_path, feature_columns, dv_column):

### Importing dataset.
    load_dotenv()
    dataset = pd.read_csv(str(dataset_path))
    X = dataset.iloc[:, feature_columns].values
    y = dataset.iloc[:, dv_column].values

### Spliting Dataset. 
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.15, random_state = 39)

### independent variables scaling. 
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)

### Model training on training datastet.
    from sklearn.svm import SVC
    classifier = SVC( kernel = 'linear', C = 2.3, tol = 1.18 , probability= False, )
    classifier.fit(X_train, y_train)

### Testing the model on the test dataset. 
    y_pred = classifier.predict(X_test)

    return y_pred
# End.
# ===================================================
