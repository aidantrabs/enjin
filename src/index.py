from typing import List
import re
from collections import defaultdict
from collections import defaultdict as dd
import glob
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords as sw

def tokenize_text(text: str) -> List[str]:
    """
    Tokenize the given text.
    """
    word_list = word_tokenize(text)
    filtered_words = []
    for word in word_list:
        if word.isalnum():
            filtered_words.append(word.lower())
    stop_words = set(sw.words('english'))
    filtered_words_list = []
    for word in word_list:
        if word not in stop_words:
            filtered_words_list.append(word)
    return filtered_words_list

def get_soundex_code(word):
    """
    Get the soundex code for the given word.
    """
    word = re.sub(r'[^A-Za-z]+', '', word.upper())
    
    if not word:
        return word
    
    remove_code = str.maketrans('', '', 'AEIOUYHW')
    word_code = word[1:].translate(remove_code)

    soundex_code = word[0]
    digit_map = str.maketrans('BFPVCGJKQSXZDTLMNR', '111122222222334556')
    soundex_code += word[1:].translate(digit_map)
    
    soundex_code = re.sub(r'(\d)\1+', r'\1', soundex_code)
    soundex_code = re.sub(r'0', '', soundex_code)
    
    soundex_code = soundex_code + '000'
    return soundex_code[:4]

def create_inverted_index():
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
            with open(file_path, "r", encoding="utf-8", errors='replace') as file:
                content = file.read()
                tokens = tokenize_text(content)
                term_freq = dd(int)
                for token in tokens:
                    term_freq[token] += 1

                for term, freq in term_freq.items():
                    inverted_index[term].append((doc_id, freq))

            mapping[file_hash] = doc_id
            doc_id += 1
            
    with open("data/output/invertedindex.txt", "w", encoding="utf-8") as file:
        header = "| {0:<15} | {1:<8} | {2:<50} |\n".format("Term", "Soundex", "Appearances (DocHash, Frequency)")
        file.write(header)
        file.write("|-" + "-"*15 + "-|-" + "-"*8 + "-|-" + "-"*50 + "-|\n")
        for term, appearances in inverted_index.items():
            soundex = get_soundex_code(term)
            appearances_str = ', '.join([f'(H{doc_id}, H{freq})' for doc_id, freq in appearances])
            file.write("|-" + "-"*15 + "-|-" + "-"*8 + "-|-" + "-"*50 + "-|\n")

            # Update output_str line with fixed-width formatting
            output_str = "| {0:<15} | {1:<8} | {2:<50} |\n".format(term, soundex, appearances_str)            
            file.write(output_str)
    with open("data/output/mapping.txt", "w") as file:
        for file_hash, doc_id in mapping.items():
            file.write(f"{file_hash} {doc_id}\n")    
            print()
    print("Inverted index created and saved to file.")