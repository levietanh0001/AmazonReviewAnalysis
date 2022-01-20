from pandas.io.parsers import read_csv
import sklearn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
import io
from sklearn.feature_extraction.text import CountVectorizer
# import sys
# import numpy
# numpy.set_printoptions(threshold=sys.maxsize)


df = pd.read_csv(r"canned_coffee_5star_processed.csv", encoding="utf-8-sig", delimiter=',', thousands=r',', dtype=None, chunksize=None)
arraylist_review_5star = df.processed_review

# Function for bigram
def get_top_n_bigram(corpus, n=None):
    vec = CountVectorizer(ngram_range=(2, 2),
stop_words='english').fit(corpus)
    bag_of_words = vec.transform(corpus)
    sum_words = bag_of_words.sum(axis=0) 
    words_freq = [(word, sum_words[0, idx]) for word, idx in vec.vocabulary_.items()]
    words_freq =sorted(words_freq, key = lambda x: x[1], reverse=True)
    return words_freq[:n]

# common_words_good = get_top_n_bigram(arraylist_review_5star, 30)

# print(common_words_good)
if __name__ == '__main__':
    corpus = arraylist_review_5star
    vec = CountVectorizer(ngram_range=(2, 2), stop_words='english').fit(corpus)
    bag_of_words = vec.transform(corpus)
    sum_words = bag_of_words.sum(axis=0) 
    # words_freq = [(word, sum_words[0, idx]) for word, idx in vec.vocabulary_.items()]
    # words_freq =sorted(words_freq, key = lambda x: x[1], reverse=True)
    # print(words_freq[:10])
    print(bag_of_words.toarray())
    print(bag_of_words)
    
    
    