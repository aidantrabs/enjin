import nltk
import nltk.corpus
import nltk.stem
import nltk.tokenize
from InquirerPy.utils import color_print, patched_print

def process_text(text: str):
    """
    Description:
        Process the text fetched from a given dataset by removing stopwords and tokenizing the text.

    Parameters:
        text: The text to process.

    Returns:
        text: The processed text.
    """

    stop_words = set(nltk.corpus.stopwords.words('english'))
    tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+')
    return text.apply(lambda x: ' '.join([word for word in tokenizer.tokenize(x.lower()) if word not in stop_words]))


def err(message: str):
    color_print([("Red bold", "Error: "), ("Red", message)])
    return


def success(message: str):
    color_print([("Green bold", "Success: "), ("Green", message)])
    return


def is_valid_url(link: str):
    return link.startswith("http://") or link.startswith("https://") or link.startswith("www.")
