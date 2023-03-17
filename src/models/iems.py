
# This is the model as an operational package ready to use.
# ===================================================

### Importing libraries.
import numpy as np
import pandas as pd
import tensorflow as tf
import random as python_random
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier

def aims(dataset_path, feature_columns, dv_column):

### ### Fixing the seeds to 123.
    np.random.seed(123)
    python_random.seed(123)
    tf.random.set_seed(123)

### Importing dataset.
    dataset = pd.read_csv(str(dataset_path))
    X = dataset.iloc[:, feature_columns].values
    y = dataset.iloc[:, dv_column].values

### Spliting Dataset. 
    X_train, X_test, y_train= train_test_split(X, y, test_size = 0.15, random_state = 11)

### independent variables scaling. 
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)

### Model training on training datastet.
    classifier = DecisionTreeClassifier(criterion = 'entropy', splitter = 'best', max_features = 2 )
    classifier.fit(X_train, y_train)

### Testing the model on the test dataset. 
    y_pred = classifier.predict(X_test)

    return y_pred
# End.
# ===================================================
