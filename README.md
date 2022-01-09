# AmazonReviewAnalysis (Natural Language Processing Web App)


Oveview
---
Analyze reviews of best-selling products, extract most frequent keywords with 5-star rating and visualize them.


Objectives
---
Recommend keywords or features for a product to achieve a 5-star rating


Tech Stack
---
- Django (backend)
- React.js (frontend)
- Chart.js (data visualization)
- nltk/spacy (NLP)
- sklearn (machine leanring)


Approach
---
Use TF-IDF Vectorizer to assess how much a keyword affects the overall rating.
Use CountVectorizer to count how many times a keyword appears in the 5-star set of reviews.


Steps
---
1. Preprocessing
2. Applying TF-IDF Vectorizer
3. Visualize the keywords
4. Evaluate
Predict how much a review (containing a set of keywords) will be rated using SVM.
 
 
TFIDF vs CountVectorizer
---
- Different in preprocessing approach
  - CountVectorizer: frequency of a word in all of the reviews, each being an array of tokens
  - TFIDF: importance of a word in a corpus containing reviews, with each review being a string of tokens


Members
---



References
---
https://medium.com/swlh/natural-language-processing-nlp-analysis-with-amazon-review-data-part-i-data-engineering-6573b782e4dc
https://melaniesoek0120.medium.com/natural-language-processing-nlp-amazon-review-data-part-ii-eda-data-preprocessing-and-model-3866dcbdbb77
https://medium.com/analytics-vidhya/sentiment-analysis-on-amazon-reviews-using-tf-idf-approach-c5ab4c36e7a1

