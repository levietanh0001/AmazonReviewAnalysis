from rake_nltk import Rake
import pandas as pd
import sys
import numpy
numpy.set_printoptions(threshold=sys.maxsize)
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer



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
        text = ' '.join(str(t) for t in texts)
        self.rake.extract_keywords_from_text(text)
        # print(x)
        self.rake_corpus = self.rake.get_ranked_phrases()
        print(self.rake_corpus)
        return self.rake_corpus
    def phrases_with_scores(self):
        return self.rake.get_ranked_phrases_with_scores()
    # def engine(self, ngram_range):
    #     if ngram_range == '' or ngram_range == None:
    #         print("\nPlease specify n-gram!")
    #     self.ngram_range = ngram_range
    #     self.vectorizer = TfidfVectorizer(ngram_range=self.ngram_range)
    #     self.bow_matrix = self.vectorizer.fit_transform(self.corpus)
    # def get_bag_of_words_matrix(self):
    #     return self.bow_matrix
    def set_number_of_phrases(self, n=20):
        self.n = n
    # def compute_words_frequency(self):
    #     self.sum_words = self.bow_matrix.sum(axis=0)
    #     self.words_freq = [(word, self.sum_words[0, idx]) for word, idx in self.vectorizer.vocabulary_.items()]
    #     self.words_freq = sorted(self.words_freq, key = lambda x: x[1], reverse=True)
    #     return self.words_freq
    # def get_word_frequency_list(self):
    #     self.x = [w[0] for w in self.words_freq[:self.n]]
    #     return self.x
    # def get_word_list(self):
    #     self.y = [w[1] for w in self.words_freq[:self.n]]
    #     return self.y
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
    