"""
In the second part of this project, you’ll test the power of Naive Bayes classifiers
by creating a system that predicts whether a tweet was sent from New York City, London, or Paris.
You will investigate how language is used differently in these three cities.
"""

import pandas as pd

new_york_tweets = pd.read_json("new_york.json", lines = True)
print(len(new_york_tweets))
print(new_york_tweets.columns)
print(new_york_tweets.loc[12]["text"])


# load json files to create data frames

london_tweets = pd.read_json("london.json", lines = True)
paris_tweets = pd.read_json("paris.json", lines = True)

print("num of tweets from London: %d" %len(london_tweets)) # 5341
print("num of tweets from Paris: %d" %len(paris_tweets)) # 2510


# Classifying using language: Naive Bayes Classifier

new_york_text = new_york_tweets["text"].tolist()
london_text = london_tweets["text"].tolist()
paris_text = paris_tweets["text"].tolist()

all_tweets = new_york_text + london_text + paris_text
# Defining labels for different cities: 0 represents a New York tweet, 1 represents a London tweet, and 2 represents a Paris tweet.
labels = [0] * len(new_york_text) + [1] * len(london_text) + [2] * len(paris_text)


# Making a Training and Test Set
from sklearn.model_selection import train_test_split

train_data, test_data, train_labels, test_labels = train_test_split(all_tweets, labels, test_size = 0.2, random_state = 1)

print("length of training data: %d" %len(train_data))
print("length of testing data: %d" %len(test_data))

# Making the Count Vectors
# To use a Naive Bayes Classifier, we need to transform our lists of words into count vectors.
from sklearn.feature_extraction.text import CountVectorizer

counter = CountVectorizer()
counter.fit(train_data, train_labels)

# Transform documents to a document-term matrix
train_counts = counter.transform(train_data)
test_counts = counter.transform(test_data)

print(train_data[3])
print(train_counts[3])


# Train and Test the Naive Bayes Classifier

from sklearn.naive_bayes import MultinomialNB

classifier = MultinomialNB()
classifier.fit(train_counts, train_labels) # calculates all of the probabilities used in Bayes Theorem


# Evaluating the Model
from sklearn.metrics import accuracy_score

Accu = accuracy_score(test_labels, predictions)
print("accuracy score for the Naive Bayes Classifier: %.4f" %Accu) # 0.6779
predictions = classifier.predict(test_counts)

from sklearn.metrics import confusion_matrix

Confusion_Matrix = confusion_matrix(test_labels, predictions)
print(Confusion_Matrix)


# Test My Own Tweet
#tweet = "Bonjour, I am Friedrich from Paris."
tweet = "c'est la vie"
tweet_counts = counter.transform([tweet])
print(classifier.predict(tweet_counts))

def PredictClass(tweet):
    tweet_counts = counter.transform([tweet])
    predict_class = classifier.predict(tweet_counts)
    if predict_class[0] == 0:
        return "New York"
    elif predict_class[0] == 1:
        return "London"
    else:
        return "Paris"
      
tweet = "Hi there! This is Friedrich. I'm currently learning skills of data science on Codecademy."
print("this tweet is predicted to be from %s." %PredictClass(tweet))
