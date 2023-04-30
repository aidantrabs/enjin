from typing import List
import re
from collections import defaultdict
from collections import defaultdict
import glob
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

def tokenize(text: str) -> List[str]:
    """
    Tokenize the given text.
    """
    words = word_tokenize(text)
    words = [word.lower() for word in words if word.isalnum()]
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]
    return words

def get_soundex(word):
    """
    Get the soundex code for the given word.
    """
    
    # remove all non-alphabetic characters and convert to uppercase
    word = re.sub(r'[^A-Za-z]+', '', word.upper())
    
    # handle empty string or strings with only one character
    if not word:
        return word
    
    # remove select characters
    removeCode = str.maketrans('', '', 'AEIOUYHW')
    wordCode = word[1:].translate(removeCode)

    # map the first character to itself and the rest to their corresponding digits
    soundex_code = word[0]
    digit_map = str.maketrans('BFPVCGJKQSXZDTLMNR', '111122222222334556')
    soundex_code += word[1:].translate(digit_map)
    
    # remove consecutive duplicates and all zeros except the first one
    soundex_code = re.sub(r'(\d)\1+', r'\1', soundex_code)
    soundex_code = re.sub(r'0', '', soundex_code)
    
    # pad the code with zeros or truncate it to length 4
    soundex_code = soundex_code + '000'
    return soundex_code[:4]

def inverted_index():
    """
    Create inverted index and save it to file.
    """
    inverted_index = defaultdict(list)
    doc_id = 1
    mapping = {}

    for topic in ["Technology", "Psychology", "Entertainment"]:
        files = glob.glob(f"data/{topic}/*.txt")
        for file_path in files:
            file_hash = file_path.split("/")[-1].split(".")[0]
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
                tokens = tokenize(content)
                term_freq = defaultdict(int)
                for token in tokens:
                    term_freq[token] += 1

                for term, freq in term_freq.items():
                    inverted_index[term].append((doc_id, freq))

            mapping[file_hash] = doc_id
            doc_id += 1
    with open("invertedindex.txt", "w", encoding="utf-8") as f:
        for term, appearances in inverted_index.items():
            soundex = get_soundex(term)
            appearances_str = ', '.join([f'({doc_id}, {freq})' for doc_id, freq in appearances])
            output_str = f"| {term} | {soundex} | {appearances_str} |\n"
            f.write(output_str)
    with open("mapping.txt", "w") as f:
        print("Saving mapping...")
        for file_hash, doc_id in mapping.items():
            f.write(f"{file_hash} {doc_id}\n")    
            print()
    print("Inverted index created and saved to file.")