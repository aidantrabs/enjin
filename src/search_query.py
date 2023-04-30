import os
import pickle
import string
import numpy as np

from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

from index import get_soundex_code, tokenize_text
from utils import load_inverted_index, load_mapping

INVERTED_INDEX_FILE = "data/output/invertedindex.txt"
MAPPING_FILE = "data/output/mapping.txt"

mapping = load_mapping(MAPPING_FILE)
inverted_index = load_inverted_index(INVERTED_INDEX_FILE)

def custom_tokenizer(text, stop_words=stopwords.words('english')):
     """
     Description:
          Custom tokenizer for the TF-IDF vectorizer.

     Parameters:
          text (str): The text to tokenize.

     Returns:
          tokens (list): The list of tokens.
     """
     tokens = text.split()
     tokens = [token.lower() for token in tokens if token not in stop_words and token not in string.punctuation]
     
     return tokens

def search_query(query):
     """
     Description:
          Search for documents containing the given query.

     Parameters:
          query (str): The query to search for.

     Returns:
          None
     """
     query_terms = tokenize_text(query)
     for i, term in enumerate(query_terms):
          if term not in inverted_index:
               closest_match = find_closest_match(term, inverted_index.keys())
               query_terms[i] = closest_match

     relevant_docs = set()
     for term in query_terms:
          appearances = inverted_index[term]
          for doc_id, _ in appearances:
               relevant_docs.add(doc_id)

     doc_texts = []
     for doc_id in relevant_docs:
          file_hash = [k for k, v in mapping.items() if v == doc_id][0]
          topic = None
          for t in ["Technology", "Psychology", "Entertainment"]:
               if os.path.exists(f"data/{t}/{file_hash}.txt"):
                    topic = t
                    break
          with open(f"data/{topic}/{file_hash}.txt", "r") as file:
               content = file.read()
               doc_texts.append(content)

     vectorizer = TfidfVectorizer(tokenizer=custom_tokenizer)
     doc_vectors = vectorizer.fit_transform(doc_texts)
     query_vector = vectorizer.transform([" ".join(query_terms)])

     similarities = cosine_similarity(query_vector, doc_vectors)

     top_3_indices = np.argsort(-similarities[0])[:3]
     for i in top_3_indices:
          file_hash = [k for k, v in mapping.items() if v == i + 1][0]
          print(f"Document {mapping[file_hash]}: data/{topic}/{file_hash}.txt")

def find_closest_match(term, index_terms):
     """
     Description:
          Find the closest match to the given term using Soundex.

     Parameters:
          term (str): The term to find the closest match to.
          index_terms (list): The list of index terms to search through.

     Returns:
          str: The closest match to the given term.     
     """
     term_soundex = get_soundex_code(term)
     closest_match = None
     min_distance = float('inf')

     for index_term in index_terms:
          index_term_soundex = get_soundex_code(index_term)
          soundex_distance = sum(c1 != c2 for c1, c2 in zip(term_soundex, index_term_soundex))

          if soundex_distance < min_distance:
               min_distance = soundex_distance
               closest_match = index_term

     return closest_match

def train_classifier():
     """
     Description:
          Train a classifier to classify documents into one of three topics.

     Parameters:
          None

     Returns:
          None
     """
     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

     classifiers = [
          tree.DecisionTreeClassifier(),
          KNeighborsClassifier(),
          SVC(),
          GaussianNB(),
          RandomForestClassifier()
     ]

     best_classifier = None
     best_accuracy = 0
     for classifier in classifiers:
          classifier.fit(X_train, y_train)
          y_pred = classifier.predict(X_test)

          accuracy = accuracy_score(y_test, y_pred)
          if accuracy > best_accuracy:
               best_accuracy = accuracy
               best_classifier = classifier

          print(f"{classifier.__class__.__name__} accuracy: {accuracy}")
          print("Confusion matrix:")
          print(confusion_matrix(y_test, y_pred))
          print("Classification report:")
          print(classification_report(y_test, y_pred))

     with open("classifier.model", "wb") as f:
          pickle.dump(best_classifier, f)

     print("Classifier saved.")