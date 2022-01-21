import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import wordnet as wn
import string
import pandas as pd
import numpy as np
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from collections import Counter
# from MyJSON import *


class PreprocessForCountVectorizer:
    nltk.download('stopwords')
    nltk.download('punkt')
    nltk.download('wordnet')
    nltk.download('omw-1.4')
    def __init__(self, csv_path):
        self.nlp = spacy.load("en_core_web_lg")
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
    def tokenize(self, review):
        tokens = nltk.word_tokenize(review)
        return tokens
    def remove_punctuation(self, tokens):
        no_punc = [token.lower() for token in tokens if token.lower() not in list(string.punctuation)]
        return no_punc
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
        wnl = WordNetLemmatizer()
        porter = PorterStemmer()
        lemma_list=[]
        for token in tokenized_review:
            lemma_word= wnl.lemmatize(token) if wnl.lemmatize(token).endswith('e') else porter.stem(token)
            lemma_list.append(lemma_word)
        return lemma_list   
    def lemmatization2(self, tokenized_review):
        doc = self.nlp(tokenized_review)
        lemma_list=[]
        for token in doc: 
            lemma_list.append(token.lemma_)    
        # wnl = WordNetLemmatizer()
        # porter = PorterStemmer()
        # lemma_list=[]
        # for token in tokenized_review:
        #     lemma_word= wnl.lemmatize(token) if wnl.lemmatize(token).endswith('e') else porter.stem(token)
        #     lemma_list.append(lemma_word)
        return lemma_list
    def save_to_csv(self, path, df):
        df = df.replace('^\s*$', np.nan, regex=True).fillna("-")
        # df.fillna(0, inplace=True)
        df.to_csv(path, columns=None, index=False, header=True, encoding='utf-8-sig', sep=',', decimal='.') 
        
        
        
        
                
if __name__ == '__main__': 
    print('\n--- INITIALIZE PREPROCESS OBJECT ---')
    csv_path  = r'../databases/canned_coffee_5star.csv'
    p = PreprocessForCountVectorizer(csv_path)    
    
    
    
    # print('\n--- PREPROCESSING FOR COUNTVECTORIZER ---')
    # print('\n--- TOKENIZE ---')
    # tokenized_reviews = list(map(p.tokenize, p.df.review))
    #     # stop words removal, punctuation marks removel
    # processed_review_token_list = list(map(p.remove_stopwords_and_punctuation, tokenized_reviews))
    #     # stemming
    # # processed_review_token_list = list(map(p.stemming, processed_review_token_list))
    # print('\n--- LEMMATIZE ---')
    # processed_review_token_list = list(map(p.lemmatization, processed_review_token_list))
    # # print(processed_review_token_list[:5])
    
    
    
    print('\n--- PREPROCESSING FOR TFIDF ---')
    print('\n--- TOKENIZE ---')
    docs = []
    for line in p.df.review:
        docs.append(p.nlp(line))
    tokenized_review_list = []
    for doc in docs:
        tokens = []
        for token in doc:
            tokens.append(token.text)
        # tokens = 
        nostop_tokens = []
        for word in tokens:
            lexeme = p.nlp.vocab[word]
            if lexeme.is_stop == False and lexeme.is_punct == False:
                nostop_tokens.append(word) 
        tokenized_review_list.append(' '.join(map(str, nostop_tokens)))
    # print(tokenized_review_list)
    
    
    print('\n--- LEMMATIZE ---')
    docs = []
    for review in tokenized_review_list:
        docs.append(p.nlp(review))
    lemmatized_review_list = []
    lemmatized_tokens_list = []
    for doc in docs:
        tokens = []
        for token in doc:
            tokens.append(token.lemma_)
        lemmatized_review_list.append(' '.join(map(str, tokens)))
        lemmatized_tokens_list.append(tokens)
    print(lemmatized_review_list)
    print(lemmatized_tokens_list)

     
    
    
    
    print('\n--- NOUN EXTRACTION ---')
    docs = []
    for review in lemmatized_review_list:
        docs.append(p.nlp(review))
    noun_only_review_list = []
    adj_only_review_list = []
    for doc in docs:
        tokens = []
        for token in doc.noun_chunks:
            # if token.pos_ not in ('ADJ', 'VERB'):
            tokens.append(token)
        # for token in doc:
        #     if token.pos_ in ('NOUN', 'PROPN'):
        #         # and token.pos_ not in ('ADJ', 'VERB'))
        #         tokens.append(token)
        noun_only_review_list.append(' '.join(map(str, tokens)))
        tokens = []
        for token in doc:
            if token.pos_ in ('ADJ'):
                tokens.append(token)
        adj_only_review_list.append(' '.join(map(str, tokens)))
    # print(noun_only_review_list)
    
        
    
    print('\n--- WORD FREQUENCY ---')
    lemmatized_reviews = ''.join(map(str, lemmatized_review_list))
    doc = p.nlp(lemmatized_reviews)
    for token in doc:
        words = [token.text for token in doc]
        word_freq = Counter(words)
    print(word_freq.most_common(10))
    
    
    print('\n--- REVIEW TOKENS LIST TO DATAFRAME ---')
    processed_review_token_array = np.array(lemmatized_tokens_list)
    processed_reviews_df = pd.DataFrame(processed_review_token_array, columns=['processed_review_tokens_list'])
    df_processed = pd.concat([p.df, processed_reviews_df], axis=1)
    
    
    print('\n--- REVIEW LIST TO DATAFRAME ---')
    processed_review_token_array_tfidf = np.array(lemmatized_review_list)
    processed_reviews_df_tfidf = pd.DataFrame(processed_review_token_array_tfidf, columns=['processed_review'])
    df_processed = pd.concat([df_processed, processed_reviews_df_tfidf], axis=1)
    
    
    print('\n--- NOUN-ONLY REVIEW LIST TO DATAFRAME ---')
    processed_review_token_array_tfidf = np.array(noun_only_review_list)
    processed_reviews_df_tfidf = pd.DataFrame(processed_review_token_array_tfidf, columns=['processed_review_noun_only'])
    df_processed = pd.concat([df_processed, processed_reviews_df_tfidf], axis=1)
    
    
    print('\n--- ADJ-ONLY REVIEW LIST TO DATAFRAME ---')
    processed_review_token_array_tfidf = np.array(adj_only_review_list)
    processed_reviews_df_tfidf = pd.DataFrame(processed_review_token_array_tfidf, columns=['processed_review_adj_only'])
    df_processed = pd.concat([df_processed, processed_reviews_df_tfidf], axis=1)
    
    
    
    print('\n--- WRITE TO CSV ---')
    csv_processed_path = r'../databases/canned_coffee_5star_processed.csv'
    p.save_to_csv(csv_processed_path, df_processed)
    
    
    
    # print('\n--- JSON PROCESSING ---')  
    # myson = MyJSON(processed_review_list)
    # myson.save_as_json(r'./keyword_analysis/processed_review_list.json')
    # myson.print_json()