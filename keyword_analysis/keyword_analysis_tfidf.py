from pandas.io.parsers import read_csv
import sklearn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
import sys
import numpy
numpy.set_printoptions(threshold=sys.maxsize)
import seaborn as sns
import json


if __name__ == '__main__':
    df = pd.read_csv(r"canned_coffee_5star_processed.csv", encoding="utf-8-sig", delimiter=',', thousands=r',', dtype=None, chunksize=None)
    
    with open(r'./processed_review_list.json') as f:
        processed_review_list = json.load(f)
    # print(processed_review_list[:20])
    
    corpus = df.processed_review_tfidf
    vectorizer = TfidfVectorizer()
    bow_matrix = vectorizer.fit_transform(corpus)
    # print(bow_matrix)
    print(vectorizer.get_feature_names_out())
    # print(bow_matrix.shape)
    
    