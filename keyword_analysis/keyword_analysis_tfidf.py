from pandas.io.parsers import read_csv
import sklearn
import pandas as pd
import numpy as np
import sys
import numpy
numpy.set_printoptions(threshold=sys.maxsize)
import seaborn as sns
import json
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer



class TFIDFKeywordAnalyzer:
    def set_dataframe_source(self, src):
        self.src = src
    def get_dataframe_source(self):
        return self.src
    def set_corpus(self, data_col):
        self.data_col = data_col
        self.df = pd.read_csv(self.src, encoding="utf-8-sig")
        self.corpus = self.df[f'{self.data_col}']
    def get_corpus(self):
        return self.corpus
    def tfidf_engine(self, ngram):
        self.ngram = ngram
        self.vectorizer = TfidfVectorizer(ngram_range=(self.ngram, self.ngram))
        self.bow_matrix = self.vectorizer.fit_transform(self.corpus)
    def get_bag_of_words(self):
        return self.bow_matrix
    def set_number_of_keywords(self, n):
        self.n = n
    def compute_words_frequency(self):
        self.sum_words = self.bow_matrix.sum(axis=0)
        self.words_freq = [(word, self.sum_words[0, idx]) for word, idx in self.vectorizer.vocabulary_.items()]
        self.words_freq = sorted(self.words_freq, key = lambda x: x[1], reverse=True)
    def get_word_frequency_list(self):
        self.x = [w[0] for w in self.words_freq[:self.n]]
        return self.x
    def get_word_list(self):
        self.y = [w[1] for w in self.words_freq[:self.n]]
        return self.y



if __name__ == '__main__':
    df = pd.read_csv(r"canned_coffee_5star_processed.csv", encoding="utf-8-sig", delimiter=',', thousands=r',', dtype=None, chunksize=None)
    
    # with open(r'./processed_review_list.json') as f:
    #     processed_review_list = json.load(f)
    # print(processed_review_list[:20])
    
    corpus = df.processed_review_tfidf
    vectorizer = TfidfVectorizer()
    
    
    print('\n--- MONOGRAM - TFIDF ---')
    bow_matrix = vectorizer.fit_transform(corpus)
    # print(bow_matrix)
    # print(vectorizer.get_feature_names_out())
    # print(bow_matrix.shape)
    sum_words = bow_matrix.sum(axis=0)
    words_freq = [(word, sum_words[0, idx]) for word, idx in vectorizer.vocabulary_.items()]
    words_freq = sorted(words_freq, key = lambda x: x[1], reverse=True)
    x = [x[0] for x in words_freq[:20]]
    y = [x[1] for x in words_freq[:20]]
    
    
 
    sns.barplot(y, x, color='{}'.format('Green'))
    plt.title('5-star monogram TFIDF', fontsize=15)
    plt.show()
    
    
    
    
    print('\n--- BIGRAM - TFIDF ---')
    # bow_matrix = vectorizer.fit_transform(corpus)
    vec = TfidfVectorizer(ngram_range=(2, 2)).fit(corpus)
    bow_matrix = vec.transform(corpus)
    # print(bow_matrix)
    # print(vectorizer.get_feature_names_out())
    # print(bow_matrix.shape)
    sum_words = bow_matrix.sum(axis=0)
    words_freq = [(word, sum_words[0, idx]) for word, idx in vec.vocabulary_.items()]
    words_freq = sorted(words_freq, key = lambda x: x[1], reverse=True)
    x2 = [x[0] for x in words_freq[:20]]
    y2 = [x[1] for x in words_freq[:20]]
    
    
    sns.barplot(y2, x2, color='{}'.format('Green'))
    plt.title('5-star bigram TFIDF', fontsize=15)
    plt.show()