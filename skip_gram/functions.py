import re
from typing import List, Dict
import itertools
from collections import defaultdict

import nltk
# nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer


WINDOW_SIZE = 10

def all_pairs(L):
    answer = []
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            if (L[i],L[j]) not in answer:
                yield (L[i],L[j])

stop_words_english =set(stopwords.words('english'))

stemmer = PorterStemmer()

def normalize_whitespace(s):
    return re.sub(r'\s+', ' ', s)





def placeholder_return_line(text):
    text2 =  text.replace('\n', '.')
    text2 =  text2.replace(',', ' ').replace("&nbsp;", "").replace("}","").replace("(", "").replace(")", "").replace("\\", "").replace("]", "").replace("[", "").replace("'", "").replace('"', "").replace(';', "")

    text3 = re.sub(r'(?<=\w)-\s(?=\w)', '-', text2)

    return text3

def remove_stop_words(sentence):

    for word in stop_words_english:
        sentence = sentence.replace(" "+word+" ",' ')

    return sentence



def stemming(string) -> str:
    return " ".join([stemmer.stem(word) for word in string.split()])

def preprocessing(string : str) -> str:

    # To convert to chain of responsability pattern
    return (normalize_whitespace(remove_stop_words(placeholder_return_line((string.lower())))))

def context_window(sentence):
    """ 
    
    I love Machine Learning => 

    I love machine

    love machine learning

    machine learning

    """


    for i in range(0,len(sentence.split())-1 ):
        yield " ".join(sentence.split()[i:WINDOW_SIZE+i]) 

def get_sentences(string:str) -> List[str]:

    for sentence in string.split("."):
        for c_w in context_window(sentence.strip()):
            yield c_w.strip()





def construct_coocurrence(sentence, my_dict : Dict):

    words = sentence.split()

    for word1, word2 in all_pairs(words):

        if word1 not in my_dict:
            my_dict[word1] = defaultdict()

        if word2 not in my_dict[word1]:

            my_dict[word1][word2] = 1

        elif word1 == word2:

            my_dict[word1][word2] = 0


        else:

            my_dict[word1][word2] = my_dict[word1][word2] + 1


    return my_dict