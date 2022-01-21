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




class MyRake:
    def __init__(self, min_length=1, max_length=10):
        self.rake = Rake(min_length=min_length, max_length=max_length)
    def set_dataframe_source(self, src):
        self.src = src
    def get_dataframe_source(self):
        return self.src
    def produce_corpus_from_df_col(self, data_col):
        # r.extract_keywords_from_text(text)
        texts = []
        self.rake_corpus = []
        if data_col == '' or data_col == None:
            print("\nPlease specify dataframe column!")
        self.data_col = data_col
        self.df = pd.read_csv(self.src, encoding="utf-8-sig")
        self.corpus = self.df[f'{self.data_col}']
        print(self.corpus)
        for x in self.corpus:
            texts.append(str(x))
        words_only = []
        special_characters = ['~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/']
        # for text in texts:
        #     for token in text:
        #         if token not in special_characters and token not in list(string.punctuation):
        #             words_only.append(token)      
        words_only = [text.lower() for text in texts if text.lower() not in special_characters]
        # words_only = [re.sub('[^a-zA-Z0-9]+', '', _) for _ in texts]
        text = ' '.join(str(w) for w in words_only)
        self.rake.extract_keywords_from_text(text)
        # print(x)
        self.rake_corpus = self.rake.get_ranked_phrases()
        print(self.rake_corpus)
        return self.rake_corpus
    def phrases_with_scores(self):
        return self.rake.get_ranked_phrases_with_scores()
    def set_number_of_phrases(self, n=20):
        self.n = n
    def plot_phrase_score_horbar_chart(self, x, y, title, limit=20):
        if x == '' or x == None:
            print("\nPlease enter x-axis data!")
        if y == '' or y == None:
            print("\nPlease specify y-axis data!")
        if title == '' or title == None:
            print("\nPlease specify the chart title!")
        self.title = title
        sns.barplot(y[:limit], x[:limit], color='{}'.format('Green'))
        plt.title(title, fontsize=15)
        plt.show()
        
        
if __name__ == '__main__':
    r = MyRake()
    csv_path = r"./databases/canned_coffee_5star_processed.csv"
    
    
    r.set_dataframe_source(csv_path)
    r.produce_corpus_from_df_col('review')
    r.set_number_of_phrases(n=20)
    phrase_score_list = r.phrases_with_scores()
    x = []
    y = []
    for ps in phrase_score_list:
        x.append(ps[1])
        y.append(ps[0])
    title = 'Top 5-star phrases Rake'
    r.plot_phrase_score_horbar_chart(x=x[:r.n], y=y, title=title, limit=r.n)
    # r.df
    