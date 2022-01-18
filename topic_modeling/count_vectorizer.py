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



class MyCountVectorizer:
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
    def countvectorizer_engine(self, ngram):
        if ngram == '' or ngram == None:
            print("\nPlease specify n-gram!")
        self.ngram = ngram
        self.vectorizer = CountVectorizer(ngram_range=(self.ngram, self.ngram))
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
    c = MyCountVectorizer()
    csv_path = r"./databases/canned_coffee_5star_processed.csv"
    df = pd.read_csv(csv_path, encoding="utf-8-sig", delimiter=',', thousands=r',', dtype=None, chunksize=None)
    c.set_dataframe_source(csv_path)
    c.produce_corpus_from_df_col('processed_review_tfidf')
    c.countvectorizer_engine(ngram=2)
    c.set_number_of_keywords(n=20)
    c.compute_words_frequency()
    x = c.get_word_frequency_list()
    y = c.get_word_list()
    c.plot_word_frequency_bar_chart(x, y, title=f'Top {c.n} 5-star bigram CountVectorizer')
    
    
    # arraylist_review_5star = df.processed_review_token_list_cv
    
    
    
    # corpus = arraylist_review_5star
    # vec = CountVectorizer(ngram_range=(1, 2), stop_words='english').fit(corpus)
    # bag_of_words = vec.transform(corpus)
    # sum_words = bag_of_words.sum(axis=0) 
    # words_freq = [(word, sum_words[0, idx]) for word, idx in vec.vocabulary_.items()]
    # words_freq = sorted(words_freq, key = lambda x: x[1], reverse=True)
    # # print(words_freq[:20])
    # top_keywords_5star = words_freq[:30]
    
    
    #     # bigram plot using function above
    # plt.figure(figsize=(30,8))
    # # good reviews bigrams
    # plt.subplot(1,3,1)
    # n_gram_plot(top_keywords_5star,'Good','blue')
    # plt.show()
    
    # # previous version
    # corpus = df.processed_review_tfidf
    
    
    # vectorizer = CountVectorizer()
    
    
    # print('\n--- MONOGRAM - COUNT VECTORIZER ---')
    # bag_of_words = vectorizer.fit_transform(corpus)
    # topic_count = 5
    # lda = LDA(n_components=topic_count)
    # lda.fit(bag_of_words)
    
    
    # sum_words = bag_of_words.sum(axis=0)
    # words_freq = [(word, sum_words[0, idx]) for word, idx in vectorizer.vocabulary_.items()]
    # words_freq = sorted(words_freq, key = lambda x: x[1], reverse=True)
    # x = [x[0] for x in words_freq[:20]]
    # y = [x[1] for x in words_freq[:20]]
    
    
    # print('\n--- PLOT MONOGRAM - COUNT VECTORIZER ---')
    # sns.barplot(y, x, color='{}'.format('Green'))
    # plt.title('{} Reviews Monograms'.format('5-star review keywords monogram'),fontsize=15)
    # plt.show()
    
    
    # print('\n--- BIGRAM - COUNT VECTORIZER ---')
    # vec = CountVectorizer(ngram_range=(2, 2)).fit(corpus)
    # bag_of_words = vec.transform(corpus)
    # sum_words = bag_of_words.sum(axis=0) 
    # words_freq = [(word, sum_words[0, idx]) for word, idx in vec.vocabulary_.items()]
    # words_freq = sorted(words_freq, key = lambda x: x[1], reverse=True)
    # x2 = [x[0] for x in words_freq[:20]]
    # y2 = [x[1] for x in words_freq[:20]]
    
    
    # print('\n--- PLOT BIGRAM - COUNT VECTORIZER ---')
    # sns.barplot(y2, x2, color='{}'.format('Green'))
    # plt.title('{} Reviews Bigrams'.format('5-star review keywords bigram'),fontsize=15)
    # plt.show()
    # # end previous version
    
    
    
    # x = []
    # y = []
    
    # for word, occurrence in vectorizer.vocabulary_.items():
    #     x.append(word)
    #     y.append(occurrence)
    # print(x)
    # print('-------------------')
    # print(y)


    
    # vectorizer2 = CountVectorizer(analyzer='word', ngram_range=(2, 2))
    # bag_of_words = vectorizer2.fit_transform(corpus)
    # sum_words = bag_of_words.sum(axis=0)
    # words_freq2 = [(word, sum_words[0, idx]) for word, idx in vectorizer2.vocabulary_.items()]
    # words_freq2 = sorted(words_freq, key = lambda x: x[1], reverse=True)
    
    # x2 = []
    # y2 = []
    # for word, occurrence in vectorizer2.vocabulary_.items():
    #     x2.append(word)
    #     y2.append(occurrence)
    # print(x2)
    # print('-------------------')
    # print(y2)

    # sns.barplot(y2[:10], x2[:10],color='{}'.format('Green'))
    # plt.title('{} Reviews Bigrams'.format('5-star review keywords bigram'),fontsize=15)
    
    
    # plt.show()
    

    
    
    