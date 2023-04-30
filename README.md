# CP-423-Project

<div align="center">



# Final Project Report



#### Friday 28th April 2023



</div>



## Group Members

*  **Aidan Traboulay** 200115590 - trab5590@mylaurier.ca

*  **Mobina Tooranisama** 200296720 - toor6720@mylaurier.ca

*  **Nausher Rao** 190906250 - raox6250@mylaurier.ca



## Contributions
 #### **Aidan Traboulay** 200115590
 - Implemented `1-Collect New Documents`, `3-Search for a query`
 - Implemented `def hash_url(url: str)`, `def is_valid_url(url, base_url)`, `def load_inverted_index(file_path)`, `def load_mapping(file_path)`, in the `utils.py` file
 - Refactored the codebase, added documentation

####  **Mobina Tooranisama** 200296720
-  Created the implementation of option `2-Inverted index`

####  **Nausher Rao** 190906250
- 


## Explanations
All three programs used quite different modules, but were all written using `Python 3.10`.

### Collecting New Documents (`collect_docs.py`)
This file parsed a given source file which contained 80+ links to crawl from and through. It had a depth which can be updated, depending on the effectiveness of the search. The `justText` and `bs4` libraries were utilized to parse and extract the content from all the links. Based on the selected topics, a subfolder is created where the contents of each URL is then written to a hashed text file. A log file indicating when each file was crawled is also created with relevant information.


### Creating Inverted Index (`index.py`)
#### Introduction:
A program that creates an inverted index of documents from a given set of topics such as Technology, Psychology, and Entertainment. The program utilizes Natural Language Toolkit (NLTK) and creates an index of words appearing in the documents along with their respective term frequency and document frequency. The inverted index is stored in a file named `invertedindex.txt`, and the mapping of documents to their respective document IDs is stored in `mapping.txt` file.

#### Technical Details:
The program is written in Python and requires the following libraries to execute:

    re
    collections
    glob
    nltk

The program defines several functions to tokenize, create soundex code, and build the inverted index:

    Tokenize: This function takes a text string as input and returns a list of words after tokenizing them using NLTK. The function removes any non-alphanumeric characters and converts all words to lowercase for consistency.

    Get_soundex: This function takes a word as input and returns its soundex code. Soundex is a phonetic algorithm that encodes words based on their pronunciation, so similar-sounding words have the same code. The function removes any non-alphabetic characters from the word and calculates its soundex code based on a set of predefined rules. The soundex code is a four-character code that represents the word's pronunciation.

    Inverted_index: This function creates the inverted index by iterating through all the documents in the specified topics. The program first retrieves a list of files in each topic using the glob library. It then reads each file and tokenizes its content using the tokenize function. It then calculates the term frequency of each word in the document and updates the inverted index with the document ID and its respective frequency. The program also creates a mapping of document IDs to file paths for future reference. Finally, the inverted index is saved to the 'invertedindex.txt' file and the mapping is saved to 'mapping.txt' file.

#### Discussion:
The program utilizes several useful libraries to perform its task efficiently. `NLTK` provides a range of functions to tokenize and normalize text, which are useful for text processing tasks. The program's use of soundex encoding ensures that similar-sounding words are grouped together, which is a useful feature for information retrieval tasks. The program's use of the `defaultdict` class from the collections library simplifies the process of updating the inverted index by allowing the use of the append method to update the list of appearances for each term. Finally, the program's use of the `glob` library makes it easy to retrieve a list of files in a directory based on a pattern.

### Search Query (`search_query.py`)
This file parses the inverted index data and vectorizes the data via a custom-built tokenizer to allow for better efficency when performing the search. Simalarites are found within the data and cosine similarity is used to perform this. The closest match is then found using the distance of the soundex codes. A classifier is then trained to create a greater accuracry when determining the top three values and the model is stored in local storage.


### Train ML Classifier (`train.py`)


#### Usage
```sh
python searchengine.py
```

#### Notes:
- The user scrolls through the options using the arrow keys in the terminal.
- Initial usage might take a while to propogate due to the amount of data being pulled.
- Preprocessed files were not included.
