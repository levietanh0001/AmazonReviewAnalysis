# AmazonReviewAnalysis - A Natural Language Processing Web App
** CURRENT WORKING BRANCH: ver6 **


Tech Stack
---
- Django: backend
- React.js: frontend
- Charts.js: data visualization
- selenium: data scraper
- nltk/spacy: natural language processing
- sklearn: machine learning


Members
---


Approach
---
- Use TFIDF to assess how relevant a keyword is with respect to the 5-star review set.
- Use Count Vectorizer to see how many times a keyword appears in a 5-star review set.
- Use LDA to find the common topics
- Visualize the data in a web app

Task description:
---
- Task description: we are provided with a product on Amazon (in this project we have Starbucks Frappuccino), and we have to analyse the product's reviews and extract information that might be useful for our client to implement to their product of the same category.
- Motivation: this project hopes to assist retailers in understanding better about what makes a bestseller and about their competitors' products, providing them with a tool to better make decisions about different approaches to maximize their chances of being among the top-selling.


Survey
---
1. Existing methods for the task: 
- CountVectorizer: this simple technique only provides us with a word-document matrix, i.e. the final output would be a list of words and the number of times they appear in the entire review set. Therefore, it is useful for preprocessing, but not so much useful information could be obtained from CountVectorizer.
- TFIDF: a very popular method to list out significant words in the review set. TF-IDF not only takes into account how many times a word appear in the document (a review in this case), but also putting a restraint on those words that are frequently used. This method goes by the following formula:

```
tf-idf(t, d) = tf(t, d) * idf(t)

where:
tf(t,d) = count of term t in document d / number of words in d
idf(t) = log_e(N/ df(t))
N = Number of documents
df(t) = Document frequency of a term t
```
- LDA: a method to infer topics, i.e. groups of words that are related to each other. In this project, we have found that this technique is not only slow in apllication, but also produces disappointing results, where we can only obtain incoherent n-gram words, i.e. a set of fixed-length words with little meaning.
- RAKE: also know as rapid automatic keyword extraction, this simple method is simplistic yet helpful in extracting not only fixed-length set of words but rather complete phrases. It works by removing the stop-words (words that don't contribute much to the context) and acquire the phrases from what's left. RAKE then ranks the phrases by their relevancy score, going by the formula:
```
score = word degree/ word frequency
where:
word frequency of word w - the number of times word w appears in the input dataset
word degree of word w - total number of words in all phrases containing w in the input dataset
```
- Chunking: potentially the most suitable technique for the task in our opinion, where we would try to group different words into useful phrases based on their grammatical strucutre (noun-verb-noun, adjective-noun, etc.), regular expressions and a list of unwanted words.

2. Current mainstream methods: TFIDF, RAKE and chunking.
3. Methods:
- We model the task by firstly trying out every possible topic modelling techniques and information extraction methods listed above. We skip several methods like LSA for its nature of reducing the size of exisitng dataset, and for this task is focused on information mining rather than modeling the topics.
- We found a potential solution for the task which requires a supervisor with certain knowledge on the field of targeting products to firstly look at the initial output words produced by CountVectorizer, TFIDF, RAKE, and select a custom set of words and phrases that might be useful (+), as well as those that are irrelevant (-). We then apply the chunking technique using these two sets (+) and (-) to infer the grammatical structure of important words and phrases, along with possible repeating features.

4. Evaluation:
- Dataset description: reviews directly scraped from the product page on Amazon. Since we are focusing on mining information, we currently don't split our dataset to training and testing, but rather, improving the results gradually. The results would then be made into a custom model that takes a list of 5-star reviews, their ratings and helpfulness votes and output potential words and phrases. This model would then be evaluated based on how many top words and phrases it produces that statisfy our supervisor/client requirements.
Demo
---
1. Data Visualization

![image](https://user-images.githubusercontent.com/47298653/148825435-5a590bee-013d-4b09-9bc5-bb601310774d.png)

![image](https://user-images.githubusercontent.com/47298653/148825489-45e1935b-31d5-4382-a466-f0f4208dc634.png)



