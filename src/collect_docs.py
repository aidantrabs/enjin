import os
import requests
import justext
import re

from bs4 import BeautifulSoup
from datetime import datetime as dt
from utils import hash_url

from nltk.corpus import stopwords

nltk.download('stopwords')

def collect_docs(sources: str):
     """
     Description:
          Collect documents from the given sources file.

     Parameters:
          sources (str): The path to the sources file.
          
     Returns:
          None
     """
     with open(sources, "r") as f:
          for line in f.readlines():
               if line.startswith("#"):
                    continue
          
               topic, url = re.split(r',\s*(?![^()]*\))', line.strip())
               topic_dir = f"data/{topic}"

               if not os.path.exists(topic_dir):
                    os.mkdir(topic_dir)

               url_hash = hash_url(url)

               if not os.path.exists(f"{topic_dir}/{url_hash}.txt"):
                    try:
                         response = requests.get(url)
                         paragraphs = justext.justext(response.content, justext.get_stoplist("English"))

                         with open(f"{topic_dir}/{url_hash}.txt", "w") as f:
                              for paragraph in paragraphs:
                                   if not paragraph.is_boilerplate:
                                        stop_words = set(stopwords.words('english'))
                                        word_tokens = paragraph.text.split()
                                        filtered_sentence = [w for w in word_tokens if not w in stop_words]
                                        paragraph.text = " ".join(filtered_sentence)

                                        f.write(paragraph.text)
                                        f.write("\n")

                         write_to_crawl_log(topic, url, url_hash)
                         crawl_links(topic, url, response.content)

                    except Exception:
                         continue
     return

def write_to_crawl_log(topic, url, url_hash):
     """
     Description:
          Write the given URL to the crawl log.

     Parameters:
          topic (str): The topic of the URL.
          url (str): The URL to write to the crawl log.
          url_hash (str): The hash of the URL.

     Returns:
          None
     """
     with open("data/output/crawl.log", "a") as f:
          f.write(f"{topic},{url},{url_hash},{dt.now()}")
          f.write("\n")

     return

def crawl_links(topic, initial_url, content):
     """
     Description:
          Crawl the links on the given page.

     Parameters:
          topic (str): The topic of the URL.
          initial_url (str): The URL to crawl.
          content (str): The content of the URL.

     Returns:
          None
     """
     soup = BeautifulSoup(content, 'html.parser')
     for link in soup.find_all('a'):
          href = link.get('href')
          if href is not None and initial_url in href:
               link_hash = hash_url(href)
               if not os.path.exists(f"data/{topic}/{link_hash}.txt"):
                    try:
                         response = requests.get(href)
                         paragraphs = justext.justext(response.content, justext.get_stoplist("English"))

                         with open(f"data/{topic}/{link_hash}.txt", "w") as f:
                              for paragraph in paragraphs:
                                   stop_words = set(stopwords.words('english'))
                                   word_tokens = paragraph.text.split()
                                   filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]
                                   filtered_text = " ".join(filtered_sentence)

                                   f.write(filtered_text)
                                   f.write("\n")

                         write_to_crawl_log(topic, href, link_hash)

                    except Exception:
                         continue

     return
