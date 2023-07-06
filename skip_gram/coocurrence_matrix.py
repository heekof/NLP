from collections import defaultdict
from functools import reduce 
import random
import numpy as np
from typing import Dict, List 
from pprint import pprint
import functions as F

# PATH_DATA = r"data\prospectus.txt"
PATH_DATA = r"data\black_holes.txt"


TOPK = 5

def set_default_value():
    return 0

def compute_coocurrence_matrix():

    coocurrence_matrix : Dict = defaultdict(set_default_value)


    with open(PATH_DATA,'r', encoding="utf-8") as file:
        corpus_txt_lines : List[str] = file.readlines()



    corpus_txt = " ".join(corpus_txt_lines)

    corpus_txt_preprocessed = F.preprocessing(corpus_txt)

    coocurrence_matrix["Hello"] = defaultdict(set_default_value)

    coocurrence_matrix["Hello"]["Word"] = 1

    print()
    print("START PROGRAM")
    # print(f"Corpus text : {corpus_txt_preprocessed[0:500]}")
    # print(f"sentences = {F.get_sentences(corpus_txt_preprocessed[0:TOPK00])}")

    for sentence in F.get_sentences(corpus_txt_preprocessed):
        coocurrence_matrix.update(F.construct_coocurrence(sentence, coocurrence_matrix))

    print(f"Hello word, coocurrence matrix : ")

    for key, _ in coocurrence_matrix.items():
        top_elements = sorted(coocurrence_matrix[key].items(), key= lambda x:x[1], reverse=True)[0:TOPK]

        current_sum = sum([number for _, number in top_elements])
        if current_sum>240:
            print(f"key = {key}")
            pprint( top_elements )
            print(f"current sum = {current_sum}")

    return coocurrence_matrix

def get_most_probable_next_word(word:str, coocurrence_matrix) -> str:

    # print(f"word = {word}, next word = {coocurrence_matrix[word]}")
    if coocurrence_matrix[word] == 0 or word == '0':
        return '0'

    top_elements = sorted(coocurrence_matrix[word].items(), key= lambda x:x[1], reverse=True)[0:TOPK]
    current_sum = sum([number for _, number in top_elements])

    return   np.random.choice([k for k,v in sorted(coocurrence_matrix[word].items(), key= lambda x:x[1], reverse=True)[0:TOPK]],TOPK, p = [v/current_sum for k,v in sorted(coocurrence_matrix[word].items(), key= lambda x:x[1], reverse=True)[0:TOPK]])[0]
