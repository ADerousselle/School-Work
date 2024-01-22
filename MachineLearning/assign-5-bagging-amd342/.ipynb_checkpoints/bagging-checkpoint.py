from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.tree import DecisionTreeClassifier
from sklearn.utils.validation import check_X_y, check_array, check_is_fitted
from sklearn.utils.multiclass import unique_labels
from sklearn.base import clone
import numpy as np
import random



class CustomBaggingClassifier(BaseEstimator, ClassifierMixin):

    def __init__(self, base_estimator=None, n_estimators=10, random_state=None):
        """
        Parameters
        ----------
        base_estimator : object or None, optional (default=None)    The base estimator to fit on random subsets of the dataset. 
                                                                    If None, then the base estimator is a decision tree.
        n_estimators : int, optional (default=10)                   The number of base estimators in the ensemble.
        random_state : int or None, optional (default=None)         Controls the randomness of the estimator. 
        """

        if base_estimator is None:
            self.base_estimator = DecisionTreeClassifier()
        else:
            self.base_estimator = base_estimator
        self.n_estimators = n_estimators
        self.random_state = random_state



    def fit(self, X, y):
        """
        Build a Bagging classifier from the training set (X, y).
        
        Parameters
        ----------
        X : ndarray of shape (n_samples, n_features)                 The input samples.
        y : ndarray of shape (n_samples,)                            The target values.
        
        Returns
        -------
        self : object
            Returns self.
        """

        # Check that X and y have correct shape
        X, y = check_X_y(X, y)

        # Store the classes seen during fit
        self.classes_ = unique_labels(y)
        self.n_classes = len(self.classes_)

        self.estimators = []
        n_samples = X.shape[0]
        for i in range(self.n_estimators):
            indices = np.random.choice(n_samples, size=n_samples, replace=True)
            X_subset, y_subset = X[indices], y[indices]
            estimator = clone(self.base_estimator)
            estimator.fit(X_subset, y_subset)
            self.estimators.append(estimator)

        # Return the classifier
        return self
    

    def predict(self, X):
        """
        Predict class for X.
        
        Parameters
        ----------
        X : ndarray of shape (n_samples, n_features)                 The input samples.
        
        Returns
        -------
        pred : ndarray of shape (n_samples,)                         The predicted classes.
        """

        # Check is fit had been called
        check_is_fitted(self)

        # Input validation
        X = check_array(X)

        n_samples = X.shape[0]
        predictions = np.empty((self.n_estimators, n_samples), dtype=int)
        for i, estimator in enumerate(self.estimators):
            predictions[i,:] = estimator.predict(X)
        pred, count = mode(predictions, axis=0)

        return pred


    def predict_proba(self, X):
        """
        Predict class probabilities for X.

        Parameters
        ----------
        X : ndarray of shape (n_samples, n_features)                 The input samples.

        Returns
        -------
        probas : ndarray of shape (n_samples, n_classes)             The class probabilities of the input samples. The order of 
                                                                     the classes corresponds to that in the attribute classes_.
        """

        # Check is fit had been called
        check_is_fitted(self)

        # Input validation
        X = check_array(X)

        predictions = np.empty((self.n_estimators, self.n_samples, self.n_classes), dtype=float)
        for i, estimator in enumerate(self.estimators):
            predictions[i,:,:] = estimator.predict_proba(X)
            
        probas = np.mean(predictions, axis=0)

        return probas


    def _get_bootstrap_sample(self, X, y):
        """
        Returns a bootstrap sample of the same size as the original input X, 
        and the out-of-bag (oob) sample. According to the theoretical analysis, about 63.2% 
        of the original indexes will be included in the bootsrap sample. Some indexes will
        appear multiple times.
        
        Parameters
        ----------
        X : ndarray of shape (n_samples, n_features)                  The input samples.
        y : ndarray of shape (n_samples,)                             The target values.

        Returns
        -------
        bootstrap_sample_X : ndarray of shape (n_samples, n_features) The bootstrap sample of the input samples.
        bootstrap_sample_y : ndarray of shape (n_samples,)            The bootstrap sample of the target values.
        oob_sample_X : ndarray of shape (n_samples, n_features)       The out-of-bag sample of the input samples.
        oob_sample_y : ndarray of shape (n_samples,)                  The out-of-bag sample of the target values.
        """

        # Check that X and y have correct shape
        X, y = check_X_y(X, y)
        
        b_indices = np.random.choice(self.n_samples, size=self.n_samples, replace=True)
        o_indices = np.setdiff1d(np.arange(self.n_samples), b_indices)
        
        bootstrap_sample_X = X[b_indices]
        bootstrap_sample_y = y[b_indices]
        oob_sample_X = X[o_indices]
        oob_sample_y = y[o_indices]

        return bootstrap_sample_X, bootstrap_sample_y, oob_sample_X, oob_sample_y

