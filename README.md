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
# 1. Existing methods for the task
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

# 2. Current mainstream methods: TFIDF, RAKE and chunking

# 3. Methods
- We model the task by firstly trying out every possible topic modelling techniques and information extraction methods listed above. We skip several methods like LSA for its nature of reducing the size of exisitng dataset, and for this task is focused on information mining rather than modeling the topics.
- We found a potential solution for the task which requires a supervisor with certain knowledge on the field of targeting products to firstly look at the initial output words produced by CountVectorizer, TFIDF, RAKE, and select a custom set of words and phrases that might be useful (+), as well as those that are irrelevant (-). We then apply the chunking technique using these two sets (+) and (-) to infer the grammatical structure of important words and phrases, along with possible repeating features.

# 4. Evaluation
- Dataset description: reviews directly scraped from the product page on Amazon. Since we are focusing on mining information, we currently don't split our dataset to training and testing, but rather, improving the results gradually. The results would then be made into a custom model that takes a list of 5-star reviews, their ratings and helpfulness votes and output potential words and phrases. This model would then be evaluated based on how many top words and phrases it produces that statisfy our supervisor/client requirements.

- Evaluation measures:

## CountVectorizer
![image](https://user-images.githubusercontent.com/47298653/148825489-45e1935b-31d5-4382-a466-f0f4208dc634.png)

## TFIDF
![image](https://user-images.githubusercontent.com/47298653/148825435-5a590bee-013d-4b09-9bc5-bb601310774d.png)

## LDA
The following snapshots evaluate the coherence scores that determines which model with how many topics is the most efficient in producing topics with words closely related to each other:

### Model based on c_v coherence score
![c_v_topics_vs_coherence_score](https://user-images.githubusercontent.com/47298653/150640022-fbbd2be8-b7a4-4c36-8c98-3aa437242555.png)

### Model based on u_mass coherence score
![umass_topics_vs_coherence_score](https://user-images.githubusercontent.com/47298653/150640046-4ed73e90-cdba-4b19-bfc5-4e1a1095b96c.png)

- Results: After trying the above methods, we move on to the chunking technique and obtain some promising results:

## Chunking
### NOUN VERB NOUN 
['stores carry item', 'husband love starbucks', 'I find 🙁', 'I love drink', 'that hit stop', 'I have time', 'I get order', 'I love Frappuccino', 'frappe use item', 'I have cases', 'I want frappuccino', 'I love coffee', 'it take time', 'I open box', 'store sell size', 'I pay attention', 'I enjoy Mocha', 'I find version', 'I resist coffee', 'I order box', 'I have problem', 'one have problem', 'I love flavor', 'I enjoy drink', 'I love flavor', 'I order product', 'we buy pack', 'we reorder bottles', 'I like flavor', 'seller do gouge', 'It have flavor', 'they arrive quantity', 'I enjoy flavor', 'Amazon allow return', 'flavor love drinks', 'I love product', 'I have addiction', 'I have time', 'I order cases', 'health bring frapps', 'I love Starbucks', 'I love fact', 'store carry flavor', 'I order bottle', 'I love stuff', 'I pay dollars', 'I love flavor', 'Starbucks jerk customers', 'we get Frapps', 'They pack bottles', 'We love flavor', 'I do hope', 'This add pizzazz', 'you get bottles', 'love love drinks', 'we have frappuccinos', 'we have frappuccinos worries', 'I drink bottles', 'I give review', 'I read amount', 'You beat Starbucks', 'we have Starbucks', 'they charge bottle', 'that carry flavor', 'I have time', 'you do math', 'I order cases', 'I love taste', 'I like flavor', 'coffee effect stomach', 'I love frappuccino', 'I have time', 'I make shake', 'I doubt complaints', 'I order coffee', 'I order coffee times']


### ADJECTIVE NOUN 
['best cold coffee', 'Starbucks stores', 'auto delivery', 'morning starbucks', 'coffee flavor', 'iced coffees', 'soda pop', 'other size', 'same product', 'more calories', 'Fantastic coffee drink', 'Book size', 'hard time', 'favorite coffee', 'secure box', 'broken bottles', 'great value', 'own frappe', 'love love', 'front door', 'individual ones', 'coffee frappuccino', 'local grocery stores', 'long time', 'Prime customer', 'grocery frequent store', 'smaller size', 'S&S choices', 'Hubbys addiction', 'local storrs', 'good price', 'close attention', 'Lite version', 'Starbucks version', 'favorite flavor', 'local food stores', 'heavy bottles', 'Great flavor', 'great price Price', 'delivery issues', 'mocha flavor', 'only complaint', 'favorite coffee', 'Best flavor', 'reasonable price', 'price gouge', 'cold coffee', 'seller ships', 'Good quantity', 'bottle label', 'coffee flavor', 'broken bottle', 'local shortages', 'same price', 'mocha ones', 'Starbucks flavor', 'large bottles', 'local store', 'favorite flavor', 'serious addiction', 'hard time', 'preferred size', 'mental health', 'mocha frapps', 'grocery store', 'coffee flavor', 'smaller bottle', 'retail stores', 'great good value', 'pricy- Folks', 'weight watch', 'coffee flavor', 'flat coffee', 'milk flavors', 'good time', 'many years', 'sturdy box', 'coffee flavor', 'grocery store', 'caffeine kick', 'bad price', 'long time', 'f riends', 'small size', 'impromptu brew drink', 'same old drink', 'busy day', 'old mother', 'Good stuff', 'great price Purchase', 'VA Resdential center', 'Love love', 'local stores', 'favorite drink', 'world trouble', 'local grocery store', 'preferred mocha flavor', 'many levels', 'good review', 'red bull', 'Glass bottles', 'coffee drinks', 'grocery stores', 'best Love', 'tall size', 'sturdy reliable packaging', 'local grocery stores', 'local grocery store', 'best breakfast', '👍 🍶 stores', 'glass bottles', 'good taste', 'hard time', 'several cases', 'single bottle', 'coffee flavor', 'mocha flavor', 'black coffee', 'oz bottles', 'Starbucks frappuccino', 'own ice shake', 'users complaints', 'liquid coffee', 'other bottled drinks', 'broken bottle', 'chilled coffee']

### WITH PREPS 
['Hands down coffee', 'Hands in bottle', 'convenience of delivery', 'wake up', 'favorite of coffees', 'size of product', 'calories at time', 'flavor in brand', 'box with bottles', 'convenience of', 'addiction to crap', 'version of flavor', 'none of', 'version in opinion', 'bottle in box', 'Buying by case', 'flavor at Price', 'seals on', 'pop up', 'pop on lid', 'flavor of drink', 'flavor between Mocha', 'lot of caffeine', 'side of bottle', 'piece of label', 'bottom of cap', 'issue with bottle', 'source of taste', 'price as', 'flavor in bottles', 'price for size', 'addiction to Frapps', 'size for delivery', 'stead of coffee', 'Folks on watch', 'fan of mocha', 'Thanks for', 'bottles for bucks', 'value for', 'drink in trouble', 'habit of', 'worries about', 'amount of caffeine', 'fan of', 'Package for shipment', 'date on bottle', 'product of time', 'breakfast in morning stores', 'flavor of Frappuccino', 'taste of coffee', 'ease of', 'milk than coffee', 'deal for', 'complaints of boxes']


- Analysis:
## Solved
Sucessfully extracting potential words and phrases that might be helpful
## Unsolved
Keywords and phrases are not yet properly ranked.
A function to predict the grammatical and semantic patterns.

# 5. Demo: this whole project is initially conceived to be a Django-React web app. However due to our lack of experience in intergrating models with the web app, currently the demo only have the front page with a placeholder chart. To deploy this web app, we go to the root directory and run:
```bat
python manage.py runserver 
```

# 6. Conclusions
## Key findings
We believe in order to obtain useful, or at least noteworthy information by obtaining the intial set of keywords and phrases using TFIDF and RAKE, and then customizing and refining our chunking patterns gramatically, regex-wise, combining with unwanted keywords removal. Our finalizing result would be a keywords-and-phrases engine capable of improving overtime and tuned to output the most notable information relating to a product based on its reviews.
