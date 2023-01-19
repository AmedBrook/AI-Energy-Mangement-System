# This script is used to train the model on a X_train and y_train datasets
# ========================================================================
#
#
#
#
#


from sklearn.svm import SVC

classifier = SVC( kernel = 'linear', C = 2.3, tol = 1.18 , probability= False, )
classifier.fit(X_train, y_train)
print(classifier.predict(sc.transform([[101,9]])))


#
#
#
#
#
#
#
#