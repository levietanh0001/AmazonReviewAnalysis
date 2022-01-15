from tkinter.messagebox import NO
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
    def produce_corpus_from_df_col(self, data_col):
        if data_col == '' or data_col == None:
            print("\nPlease specify dataframe column!")
        self.data_col = data_col
        self.df = pd.read_csv(self.src, encoding="utf-8-sig")
        self.corpus = self.df[f'{self.data_col}']
        return self.corpus
    def tfidf_engine(self, ngram):
        if ngram == '' or ngram == None:
            print("\nPlease specify n-gram!")
        self.ngram = ngram
        self.vectorizer = TfidfVectorizer(ngram_range=(self.ngram, self.ngram))
        self.bow_matrix = self.vectorizer.fit_transform(self.corpus)
    def get_bag_of_words_matrix(self):
        return self.bow_matrix
    def set_number_of_keywords(self, n=20):
        self.n = n
    def compute_words_frequency(self):
        self.sum_words = self.bow_matrix.sum(axis=0)
        self.words_freq = [(word, self.sum_words[0, idx]) for word, idx in self.vectorizer.vocabulary_.items()]
        self.words_freq = sorted(self.words_freq, key = lambda x: x[1], reverse=True)
        return self.words_freq
    def get_word_frequency_list(self):
        self.x = [w[0] for w in self.words_freq[:self.n]]
        return self.x
    def get_word_list(self):
        self.y = [w[1] for w in self.words_freq[:self.n]]
        return self.y
    def plot_word_frequency_bar_chart(self, x, y, title):
        if x == '' or x == None:
            print("\nPlease enter x-axis data!")
        if y == '' or y == None:
            print("\nPlease specify y-axis data!")
        if title == '' or title == None:
            print("\nPlease specify the chart title!")
        self.title = title
        sns.barplot(y, x, color='{}'.format('Green'))
        plt.title(title, fontsize=15)
        plt.show()



if __name__ == '__main__':
    t = TFIDFKeywordAnalyzer()
    t.set_dataframe_source(r"canned_coffee_5star_processed.csv")
    t.produce_corpus_from_df_col('processed_review_tfidf')
    t.tfidf_engine(ngram=2)
    t.set_number_of_keywords(n=20)
    t.compute_words_frequency()
    x = t.get_word_frequency_list()
    y = t.get_word_list()
    t.plot_word_frequency_bar_chart(x, y, title=f'Top {t.n} 5-star bigram TFIDF')
    