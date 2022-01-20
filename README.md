# AmazonReviewAnalysis - A Natural Language Processing Web App

Overview
---


Objectives
---


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
- Visualize the data in a web app

TFIDF vs CountVectorizer
---
- Different in preprocessing approach
  - CountVectorizer: frequency of a word in all of the reviews, each being an array of tokens
  - TFIDF: importance of a word in a corpus containing reviews, with each review being a string of tokens


Demo
---
1. Data Visualization

![image](https://user-images.githubusercontent.com/47298653/148825435-5a590bee-013d-4b09-9bc5-bb601310774d.png)

![image](https://user-images.githubusercontent.com/47298653/148825489-45e1935b-31d5-4382-a466-f0f4208dc634.png)



References
---
1. https://medium.com/swlh/natural-language-processing-nlp-analysis-with-amazon-review-data-part-i-data-engineering-6573b782e4dc
2. https://melaniesoek0120.medium.com/natural-language-processing-nlp-amazon-review-data-part-ii-eda-data-preprocessing-and-model-3866dcbdbb77
3. https://medium.com/analytics-vidhya/sentiment-analysis-on-amazon-reviews-using-tf-idf-approach-c5ab4c36e7a1

