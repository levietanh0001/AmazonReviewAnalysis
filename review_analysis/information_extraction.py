from rake_nltk import Rake
import pandas as pd
import sys
import numpy
numpy.set_printoptions(threshold=sys.maxsize)
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
import string
import re
import spacy




class InformationExtraction:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_lg")
    def set_dataframe_source(self, src):
        self.src = src
    def produce_text_from_df_col(self, data_col):
        if data_col == '' or data_col == None:
            print("\nPlease specify dataframe column!")
        self.data_col = data_col
        self.df = pd.read_csv(self.src, encoding="utf-8-sig")
        # self.corpus = self.df[f'{self.data_col}']
        # self.lines = []
        self.text = ''
        for row in self.df[f'{self.data_col}']:
            # print(row)
            self.text = self.text + ' ' + str(row)
        #     self.lines.append(''.join(str(row)))
        # print(self.text)
        return self.text
    def noun_verb_noun(self, text):
        doc = self.nlp(text)
        nvns = []
        for token in doc:
            if (token.pos_ == 'VERB'):
                nvn = ''
                for left_token in token.lefts:
                    if (left_token.dep_ in ['nsubj','nsubjpass']) and (left_token.pos_ in ['NOUN','PROPN','PRON']):
                        nvn += left_token.text
                        nvn += ' ' + token.lemma_ 
                        for right_token in token.rights:
                            if (right_token.dep_ in ['dobj']) and (right_token.pos_ in ['NOUN','PROPN']):
                                nvn += ' ' + right_token.text
                                nvns.append(nvn)
        return nvns
    def adjective_noun(self, text):
        doc = self.nlp(text)
        ans = []
        for token in doc:
            an = ''
            if (token.pos_ == 'NOUN')\
                and (token.dep_ in ['dobj','pobj','nsubj','nsubjpass']):
                for subtoken in token.children:
                    if (subtoken.pos_ == 'ADJ') or (subtoken.dep_ == 'compound'):
                        an += subtoken.text + ' '     
                if len(an)!=0:
                    an += token.text
            if len(an) != 0:
                ans.append(an)
        return ans
    def with_prepositions(self, text):  
        doc = self.nlp(text)
        with_preps = []
        for token in doc:
            if token.pos_=='ADP':
                phrase = ''
                if token.head.pos_=='NOUN':
                    phrase += token.head.text
                    phrase += ' '+token.text
                    for right_tok in token.rights:
                        if (right_tok.pos_ in ['NOUN','PROPN']):
                            phrase += ' '+right_tok.text
                    if len(phrase)>2:
                        with_preps.append(phrase)
        return with_preps
    
    
    
    
if __name__ == '__main__':
    ix = InformationExtraction()
    csv_path = r"./databases/canned_coffee_5star_processed.csv"
    
    
    ix.set_dataframe_source(csv_path)
    text = ix.produce_text_from_df_col('review')
    nvns = ix.noun_verb_noun(text=text)
    ans = ix.adjective_noun(text=text)
    with_preps = ix.with_prepositions(text=text)
    print(nvns)
    pass