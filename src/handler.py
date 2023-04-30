from InquirerPy.utils import patched_print
from train import init_classifier, calculate_performance_metrics, print_metrics, save_confusion_matrix, serialise_model
from collect_docs import collect_docs
from utils import err

SOURCES = "data/input/sources.txt"

def collect():
    try:
        collect_docs(SOURCES)
    except Exception:
        err("Something went wrong while collecting documents!")

    return

def inverted_index():
    try:
        patched_print("inverted_index")

    except FileNotFoundError:
        err("You need to collect documents first!")

    return

def search(query: str):
    try:
        patched_print("search")

    except FileNotFoundError:
        err("You need to collect documents first!")

    return

def train():
    try:
        vectorizer, classifier, X, Y = init_classifier("SOMETHING")
        y_pred = classifier.predict(X)

        performance = calculate_performance_metrics(Y, y_pred)
        print_metrics("SOMETHING", *performance)
        save_confusion_matrix(Y, y_pred)
        serialise_model(classifier, vectorizer)

    except FileNotFoundError:
        err("No data found!")

    return

def predict_link(link: str):
    try:
        patched_print("predicted_link")

    except Exception:
        err("Something went wrong while predicting the link!")

    return
