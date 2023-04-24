import argparse
import enum
import joblib
import matplotlib.pyplot as plt
import nltk
import nltk.corpus
import nltk.stem
import nltk.tokenize
import numpy
import pandas
import seaborn as sns
import sklearn
import sklearn.metrics
import sklearn.naive_bayes
import sklearn.neighbors
import sklearn.svm
import sklearn.tree

from InquirerPy.utils import color_print, patched_print
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import KFold, cross_val_score
from typing import Union

CONFUSION_MATRIX_FILE_NAME = "confusion_matrix.png"
VECTORIZER_OUTPUT_FILE_NAME = "vectorizer.joblib"
CLASSIFIER_OUTPUT_FILE_NAME = "classifier.joblib"

def collect():
    patched_print("collect")

def inverted_index():
    patched_print("inverted_index")

def search(query: str):
    patched_print("search")

def train():
    def save_confusion_matrix(Y, y_pred):
        """
        Description:
            Save the confusion matrix to the disk.

        Parameters:
            Y: The Y vector.
            y_pred: The predicted Y vector.
        """
        matrix = sklearn.metrics.confusion_matrix(Y, y_pred)

        sns.heatmap(matrix, fmt="d", annot=True)
        plt.title("Confusion Matrix")
        plt.xlabel("Predicted Label")
        plt.ylabel("Actual Label")
        plt.savefig(CONFUSION_MATRIX_FILE_NAME)
        return

    def serialise_classifier(classifier):
        """
        Description:
            Save and dump the vectorizer and classifier to the disk.

        Parameters:
            classifier: The classifier.
        """
        with open(CLASSIFIER_OUTPUT_FILE_NAME, "wb") as file:
            joblib.dump(classifier, file)

        return

def predict_link(link: str):
    patched_print("predicted_link")
