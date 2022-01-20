import nltk
from nltk import tokenize
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
import string
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
import io
import os



class Preprocess:
    nltk.download('stopwords')
    nltk.download('punkt')
    nltk.download('wordnet')
    nltk.download('omw-1.4')
    
    
    def __init__(self, csv_path):
        self.df = pd.read_csv(csv_path, encoding="utf-8-sig", delimiter=',', thousands=r',', dtype=None, chunksize=None)
        # self.all_reviews = [self.all_reviews.append(r) for r in self.df.review]
        self.all_reviews = ''.join(self.df.review)
        
    def print_sample_data(self, row=5):
        print(self.df.head(row))


    def stopwords_list(self):
        # Create Stop words list
        sw_list = list(stopwords.words('english'))
        sw_list += list(string.punctuation)
        sw_list += ["''", '""', '...', '``', '’', '“', '’', '”', '‘', '‘',"'", '©',
        'said',"'s", "also",'one',"n't",'com', 'satirewire', '-', '–', 
        '—', '_','satirewire.com',"/"]
        return sw_list
        # print(sw_list)

    # create a function to tokenize text data 
    # using the stop words list to remove stop words and lowercase every token
    def tokenize(self, review):
        tokens = nltk.word_tokenize(review)
        return tokens
    
    
    def remove_stopwords_and_punctuation(self, tokens):
        stopwords_removed = [token.lower() for token in tokens if token.lower() not in self.stopwords_list()]
        return stopwords_removed
    
    
    def stemming(self, tokenized_review):
        ps = PorterStemmer()
        stemmed=[]
        for token in tokenized_review:
            stemmed.append(ps.stem(token))
        return stemmed
        
        
    def lemmatization(self, tokenized_review):
        lemmatizer = WordNetLemmatizer()
        lemma_list=[]
        for token in tokenized_review:
            lemma_word=lemmatizer.lemmatize(token, pos='v') 
            lemma_list.append(lemma_word)
        return lemma_list   
        
    def merge_column_to_df(self, list):
        pass
    def save_to_csv(self, path, df):
        df.to_csv(path, columns=None, index=False, header=True, encoding='utf-8-sig', sep=',', decimal='.') 
        
        
if __name__ == '__main__': 
    csv_path  = r'./canned_coffee_5star.csv'
    p = Preprocess(csv_path)    
        # tokenization, 
    tokenized_reviews = list(map(p.tokenize, p.df.review))
        # stop words removal, punctuation marks removel
    processed_review_list = list(map(p.remove_stopwords_and_punctuation, tokenized_reviews))
        # stemming
    processed_review_list = list(map(p.stemming, processed_review_list))
        # lemmatization
    processed_review_list = list(map(p.lemmatization, processed_review_list))
    print(processed_review_list[:5])    
    
    
    processed_review_array = np.array(processed_review_list)
    processed_reviews_df = pd.DataFrame(processed_review_array, columns=['processed_review'])
    df_processed = pd.concat([p.df, processed_reviews_df], axis=1) # a list of df will do
    
    # p.merge_column_to_df(processed_review_list)
    csv_processed = r'./canned_coffee_5star_processed.csv'
    p.save_to_csv(csv_processed, df_processed)
    
    
    