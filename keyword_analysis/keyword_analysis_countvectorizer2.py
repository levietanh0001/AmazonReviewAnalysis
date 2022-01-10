from pandas.io.parsers import read_csv
import sklearn
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
import sys
import numpy
numpy.set_printoptions(threshold=sys.maxsize)
# import preprocess
# import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt


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
    df = pd.read_csv(r"canned_coffee_5star_processed.csv", encoding="utf-8-sig", delimiter=',', thousands=r',', dtype=None, chunksize=None)
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
    
    
    corpus = df.processed_review_tfidf
    
    
    vectorizer = CountVectorizer()
    bag_of_words = vectorizer.fit_transform(corpus)
    sum_words = bag_of_words.sum(axis=0)
    words_freq = [(word, sum_words[0, idx]) for word, idx in vectorizer.vocabulary_.items()]
    words_freq = sorted(words_freq, key = lambda x: x[1], reverse=True)
    
    
    x = [x[0] for x in words_freq[:20]]
    y = [x[1] for x in words_freq[:20]]
    
    
    sns.barplot(y, x, color='{}'.format('Green'))
    plt.title('{} Reviews Monograms'.format('5-star review keywords monogram'),fontsize=15)
    plt.show()
    
    
    # x = []
    # y = []
    
    # for word, occurrence in vectorizer.vocabulary_.items():
    #     x.append(word)
    #     y.append(occurrence)
    # print(x)
    # print('-------------------')
    # print(y)
    
    
    
    
    
    
    
    vec = CountVectorizer(ngram_range=(2, 2)).fit(corpus)
    bag_of_words = vec.transform(corpus)
    sum_words = bag_of_words.sum(axis=0) 
    words_freq = [(word, sum_words[0, idx]) for word, idx in vec.vocabulary_.items()]
    words_freq = sorted(words_freq, key = lambda x: x[1], reverse=True)
    
    # vectorizer2 = CountVectorizer(analyzer='word', ngram_range=(2, 2))
    # bag_of_words = vectorizer2.fit_transform(corpus)
    # sum_words = bag_of_words.sum(axis=0)
    # words_freq2 = [(word, sum_words[0, idx]) for word, idx in vectorizer2.vocabulary_.items()]
    # words_freq2 = sorted(words_freq, key = lambda x: x[1], reverse=True)
    
    
    x2 = [x[0] for x in words_freq[:20]]
    y2 = [x[1] for x in words_freq[:20]]
    
    # print(x2)
    sns.barplot(y2, x2, color='{}'.format('Green'))
    plt.title('{} Reviews Bigrams'.format('5-star review keywords bigram'),fontsize=15)
    plt.show()
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
    

    
    
    