
# This script is used to predict y_pred using new datasets of features X (X_test).
#================================================================================
#
#
#
#
#

y_pred = classifier.predict(X_test)
print(np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)),1))

#
#
#
#
#
#