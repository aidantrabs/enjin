import pandas
import joblib
import seaborn as sns
import matplotlib.pyplot as plt

import sklearn
import sklearn.metrics
import sklearn.naive_bayes
import sklearn.neighbors
import sklearn.svm
import sklearn.tree

from sklearn.feature_extraction.text import CountVectorizer
from utils import process_text

CONFUSION_MATRIX_FILE_NAME = "confusion_matrix.png"
VECTORIZER_OUTPUT_FILE_NAME = "vectorizer.joblib"
CLASSIFIER_OUTPUT_FILE_NAME = "classifier.joblib"

def init_classifier(dataset_file_name: str):
     """
     Description:
          Initialize the classifier and vectorizer.

     Parameters:
          dataset_file_name: The name of the dataset file.

     Returns:
          vectorizer: The count vectorizer.
          classifier: The classifier fitted with the X and Y vector.
          X: The X vector.
          Y: The Y vector.
     """
     file_name = f"data/training_sentiment/{dataset_file_name}"
     data = pandas.read_csv(file_name, sep='\t', header=None)
     text = process_text(data[0])

     vectorizer = CountVectorizer()
     X = vectorizer.fit_transform(text)
     Y = data[1]

     classifier = sklearn.svm.SVC()
     classifier.fit(X, Y)
     return vectorizer, classifier, X, Y

def calculate_performance_metrics(Y, y_pred):
     """
     Description:
          Calculate the performance metrics using the given vectors.

     Parameters:
          Y: The Y vector.
          y_pred: The predicted Y vector.

     Returns:
          accuracy: The accuracy of the classifier.
          precision: The precision of the classifier.
          recall: The recall of the classifier.
          f1: The f1 score of the classifier.
     """
     accuracy = sklearn.metrics.accuracy_score(Y, y_pred)
     precision = sklearn.metrics.precision_score(Y, y_pred, average="macro")
     recall = sklearn.metrics.recall_score(Y, y_pred, average="macro")
     f1 = sklearn.metrics.f1_score(Y, y_pred, average="macro")

     return accuracy, precision, recall, f1

def print_metrics(dataset: str, accuracy: float, precision: float, recall: float, f1: float):
     """
     Description:
          Print the performance metrics.

     Parameters:
          title: The title of the print.
          dataset: The dataset used.
          classifierType: The classifier type used.
          accuracy: The accuracy of the classifier.
          precision: The precision of the classifier.
          recall: The recall of the classifier.
          f1: The f1 score of the classifier.
     """
     print()
     print(f"Option 3 | {dataset} using SVM:")
     print("==============================================")
     print(f"Accuracy: {accuracy:.5f}")
     print(f"Precision: {precision:.5f}")
     print(f"Recall: {recall:.5f}")
     print(f"F1: {f1:.5f}")
     print("==============================================")
     print()

     return

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

def serialise_model(classifier, vectorizer):
     """
     Description:
          Save and dump the vectorizer and classifier to the disk.

     Parameters:
          classifier: The classifier.
     """
     with open(CLASSIFIER_OUTPUT_FILE_NAME, "wb") as file:
          joblib.dump(classifier, file)

     with open(VECTORIZER_OUTPUT_FILE_NAME, "wb") as file:
          joblib.dump(vectorizer, file)

     return