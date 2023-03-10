# This the script to visualize training or testing outputs.

from matplotlib.colors import ListedColormap
from sklearn.preprocessing import StandardScaler
import numpy as np
from sklearn.svm import SVC
import matplotlib.pyplot as plt

def eims_visulize(X, y):

    sc = StandardScaler()
    X_data = X # Specify your training or testing matrix of features here.
    y_data = y # Specify your training or testing matrix of dependent variable here.
    classifier = SVC( kernel = 'linear', C = 2.3, tol = 1.18 , probability= False, )
    classifier.fit(X, y)


    X_set, y_set = sc.inverse_transform(X_data), y_data
    X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() - 10, stop = X_set[:, 0].max() + 10, step = 0.25),
                     np.arange(start = X_set[:, 1].min() -10, stop = X_set[:, 1].max() + 10, step = 0.25))
    plt.contourf(X1, X2, classifier.predict(sc.transform(np.array([X1.ravel(), X2.ravel()]).T)).reshape(X1.shape),
             alpha = 0.75, cmap = ListedColormap(('red', 'green')))
    plt.xlim(X1.min(), X1.max())
    plt.ylim(X2.min(), X2.max())
    for i, j in enumerate(np.unique(y_set)):
        plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1], c = ListedColormap(('red', 'green'))(i), label = j)


    plt.title('title')
    plt.xlabel('x lable')
    plt.ylabel('y label')
    plt.legend()
    plt.show()

    return(plt.show)