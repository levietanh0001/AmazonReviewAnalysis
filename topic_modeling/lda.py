from pandas.io.parsers import read_csv
import sklearn
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation as LDA
import sys
import numpy
numpy.set_printoptions(threshold=sys.maxsize)
# import preprocess
# import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt
from gensim import corpora, models, similarities, downloader


## Evaluation
# C_v measure is based on a sliding window, one-set segmentation of the top words and an indirect confirmation measure that uses normalized pointwise mutual information (NPMI) and the cosine similarity
# C_p is based on a sliding window, one-preceding segmentation of the top words and the confirmation measure of Fitelson’s coherence
# C_uci measure is based on a sliding window and the pointwise mutual information (PMI) of all word pairs of the given top words
# C_umass is based on document cooccurrence counts, a one-preceding segmentation and a logarithmic conditional probability as confirmation measure
# C_npmi is an enhanced version of the C_uci coherence using the normalized pointwise mutual information (NPMI)
# C_a is baseed on a context window, a pairwise comparison of the top words and an indirect confirmation measure that uses normalized pointwise mutual information (NPMI) and the cosine similarity
class MyLDA:
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
    def set_number_of_topics(self, number_of_topics=5):
        self.number_of_topics = number_of_topics
    def engine(self, ngram):
        if ngram == '' or ngram == None:
            print("\nPlease specify n-gram!")
        self.ngram = ngram
        self.vectorizer = CountVectorizer(ngram_range=(self.ngram, self.ngram))
        self.bow_matrix = self.vectorizer.fit_transform(self.corpus)
        lda = LDA(n_components=self.number_of_topics)
        lda.fit(self.bow_matrix)
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
        
        
# Function for bigram
def get_top_n_bigram(corpus, n=None):
    vec = CountVectorizer(ngram_range=(2, 2),
stop_words='english').fit(corpus)
    bag_of_words = vec.transform(corpus)
    sum_words = bag_of_words.sum(axis=0) 
    words_freq = [(word, sum_words[0, idx]) for word, idx in vec.vocabulary_.items()]
    words_freq =sorted(words_freq, key = lambda x: x[1], reverse=True)
    return words_freq[:n]


# create a function for bigram plots
def n_gram_plot(data,title,color):
    x=[x[0] for x in data]
    y=[x[1] for x in data]
    sns.barplot(y,x,color='{}'.format(color))
    plt.title('{} Reviews Bigrams'.format(title),fontsize=15)
    plt.yticks(rotation=0,fontsize=15)
    
    
    
if __name__ == '__main__':
    l = MyLDA()
    csv_path = r"./databases/canned_coffee_5star_processed.csv"
    df = pd.read_csv(csv_path, encoding="utf-8-sig", delimiter=',', thousands=r',', dtype=None, chunksize=None)
    l.set_dataframe_source(csv_path)
    l.produce_corpus_from_df_col('processed_review_tokens_list')
    dictionary = gensim.corpora.Dictionary(l.corpus)
    # l.set_number_of_topics()
    # l.engine(ngram=2)
    # l.set_number_of_keywords(n=20)
    # l.compute_words_frequency()
    # x = l.get_word_frequency_list()
    # y = l.get_word_list()
    # l.plot_word_frequency_bar_chart(x, y, title=f'Top {l.n} 5-star bigram LDA')