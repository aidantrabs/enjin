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
 - 

####  **Mobina Tooranisama** 200296720
-  Created the implementation of option `2-Inverted index`

####  **Nausher Rao** 190906250
- 


## Explanations
All three programs used quite different modules, but were all written using `Python 3.10`.

### Collecting New Documents (`collect_docs.py`)



### Creating Inverted Index (`index.py`)
#### Introduction:
A program that creates an inverted index of documents from a given set of topics such as Technology, Psychology, and Entertainment. The program utilizes Natural Language Toolkit (NLTK) and creates an index of words appearing in the documents along with their respective term frequency and document frequency. The inverted index is stored in a file named 'invertedindex.txt', and the mapping of documents to their respective document IDs is stored in 'mapping.txt' file.

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
The program utilizes several useful libraries to perform its task efficiently. NLTK provides a range of functions to tokenize and normalize text, which are useful for text processing tasks. The program's use of soundex encoding ensures that similar-sounding words are grouped together, which is a useful feature for information retrieval tasks. The program's use of the defaultdict class from the collections library simplifies the process of updating the inverted index by allowing the use of the append method to update the list of appearances for each term. Finally, the program's use of the glob library makes it easy to retrieve a list of files in a directory based on a pattern.

#### Elias Delta Coding
The `encode_elias_delta` function takes a number as input and returns the result. The function first calculates the log_2 of the given number and adds 1. This number is then converted to binary and the first bit is removed. The remaining bits are then concatenated with the original number in unary. The simplified version of this formula can be seen below:
$$ n = 1 + \lfloor log_{2}(x) \rfloor \newline result = n_{binary} + x_{unary}$$


#### Elias Gamma Coding
The `encode_elias_gamma` function takes a number as input and returns the result. The function first calculates the log_2 of the given number and adds 1. After this, variables `n` and `b` are calculated using the following simplified formula:
$$ n = 1 + log_{2}(x) \newline b = (x - 2)^{log_{2}(x)} \newline result = n_{unary} + b_{binary}$$


#### Elias Delta Decoding
The `decode_elias_delta` function takes a string as input and returns the result as an integer. The code does the reverse of the encoding function, and then verifies the calculated kdd, kdr, and kdd_binary values against the values calculated from the input string. If the values do not match, the function returns an error message.


#### Elias Gamma Decoding
The `decode_elias_gamma` function takes a string as input and returns the result as an integer. The code does the reverse of the encoding function, and then verifies the calculated value against the basic rules for Elias Coding.


### Page Rank (`page_rank.py`)
The purpose of the program was to utilize the page rank algorithm which took the arguments of `max iteration`, `lambda`, `threshold` and a list of `nodes`. The basic idea was to parse through a large data set (`web-Stanford.txt`) which provided **2,312,502** node connections, the page rank algorithm is then applied to find specified nodes and determine the page rank of those nodes, in order of highest priority. When developing this program, the biggest issue I faced was that of the large data set. My first few iterations of the program worked extremely quickly on a smaller data set which I extracted. Finally, I was able to implement an efficent program, while it is not instanenous it is significantly faster. It avoids recomputing the reciprocal of the number of outbound edges for each node at each iteration by precomputing it once before the iterations begin. It also calculates the number of outbound edges for each node in a more efficient way by iterating over the edges only once, which reduces the number of iterations required to converge. A selection sort is then applied to then display the results to the user. 

#### Program Breakdown

The function `load_data()` loads the data set and splits the lines, seperating the **from_nodes** and **in_nodes** and applies them to a simple graph, which is just a Python dictionary. It returns the graph of the nodes and the number of outbound links given in each node.

The function `page_rank()` aplies the page rank algorithm to each node in the graph. It uses an iterative approach and returns the current pagerank values.

The function `page_rank_handler()` applies the user's arguments to the page rank algorithm (`page_rank()`) and prints the page ID and the rank of that page.

The function `arg_handler()` handles all the user arguments and returns them.

The function `main()` runs the program, by applying the arguments to the `page_rank_handler()`.

#### Usage
```sh
python3 page_rank.py --maxiteration 20 --lambda .25 --thr .01 --nodes 5 87524 632
```

- Note: The user passes in the node list as individual values, space seperated.

### Noisy Channel (`noisy_channel.py`)
The `noisy_channel.py` module defines the functions required for implementing the Noisy Channel Model, including the `noisy_channel_model`, `generate_candidates`, and `channel_model` functions. 

The `nltk` module is used for tokenization and stopword removal. The `Counter` class from the `collections` module is used to count the occurrences of each word in the dataset. The `math` module is used for exponentiation.

The script also includes a workaround for SSL certificate verification, in case SSL verification fails.

The `noisy_channel_model` function generates a set of candidate words for the misspelled word and returns a dictionary of candidate words with their respective probabilities. 

The `generate_candidates` function generates a set of candidate words by performing operations such as deleting, transposing, replacing, and inserting characters. 

The `channel_model` function calculates the probability of a word being a candidate by calculating the cost of transforming one word into another using edit distance.

The `main` function  uses argparse to parse command-line arguments. The `--correct` option takes a list of misspelled words and returns the most probable correction for each misspelled word. The `--proba` option takes a list of words and returns their respective probabilities in the dataset.

The script is callable form the command line as below:


#### Usage
```sh

```



#### Why was __ chosen?
        classifier = sklearn.naive_bayes.MultinomialNB()
        classifier = sklearn.svm.SVC()
        classifier = sklearn.tree.DecisionTreeClassifier()
        classifier = sklearn.neighbors.KNeighborsClassifier(n)
