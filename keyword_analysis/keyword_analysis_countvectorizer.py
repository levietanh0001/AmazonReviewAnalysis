from pandas.io.parsers import read_csv
import sklearn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
import sys
import numpy
numpy.set_printoptions(threshold=sys.maxsize)
import seaborn as sns
# import preprocess



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
    arraylist_review_5star = df.processed_review_token_list_cv
    
    
    
    corpus = arraylist_review_5star
    vec = CountVectorizer(ngram_range=(1, 2), stop_words='english').fit(corpus)
    bag_of_words = vec.transform(corpus)
    sum_words = bag_of_words.sum(axis=0) 
    words_freq = [(word, sum_words[0, idx]) for word, idx in vec.vocabulary_.items()]
    words_freq = sorted(words_freq, key = lambda x: x[1], reverse=True)
    # print(words_freq[:20])
    top_keywords_5star = words_freq[:30]
    
    
        # bigram plot using function above
    plt.figure(figsize=(30,8))
    # good reviews bigrams
    plt.subplot(1,3,1)
    n_gram_plot(top_keywords_5star,'Good','blue')
    plt.show()
    
    # for word, occurrence in vec.vocabulary_.items():
    #     if word == 'flavor':
    #         print(word, occurrence)
    
    
    # print(vec.vocabulary_)
    # words = []
    # for word, inx in vec.vocabulary_.items():
    #     words.append(word)
    # print(words.count('cheaper'))
    
    # print(bag_of_words.toarray())
    # print(bag_of_words)
    # print(sum_words[0,3])
    # print(vec.vocabulary_.items())
    
    
    