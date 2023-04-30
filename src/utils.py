import nltk
import nltk.corpus
import nltk.stem
import nltk.tokenize
import hashlib

from urllib.parse import urlparse, urljoin

from InquirerPy.utils import color_print, patched_print

def hash_url(url: str):
    """
    Description:
        Returns the SHA256 hash of the given URL.

    Parameters:
        url (str): The URL to hash.

    Returns:
        str: The SHA256 hash of the given URL.
    """
    return hashlib.sha256(url.encode()).hexdigest()    

def is_valid_url(url, base_url):
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme) and base_url in url

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
    """
    Description:
        Print an error message.
        
    Parameters:
        message: The message to print.
        
    Returns:
        None
    """
    color_print([("Red bold", "Error: "), ("Red", message)])
    return

def success(message: str):
    """
    Description:
        Print a success message.

    Parameters:
        message: The message to print.

    Returns:
        None
    """
    color_print([("Green bold", "Success: "), ("Green", message)])
    return

def is_valid_url(link: str):
    """
    Description:
        Check if the given link is a valid URL.

    Parameters:
        link: The link to check.

    Returns:
        True if the link is valid, False otherwise.
    """
    return link.startswith("http://") or link.startswith("https://") or link.startswith("www.")
