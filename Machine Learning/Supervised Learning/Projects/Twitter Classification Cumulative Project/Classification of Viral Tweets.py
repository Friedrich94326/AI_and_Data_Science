"""
In the first part, you will make a system that predicts whether or not a tweet will go viral by using a K-Nearest Neighbor classifier.
What features of a tweet do you think are the most important in determining its virality? 
"""

import pandas as pd

all_tweets = pd.read_json("random_tweets.json", lines=True)

print(len(all_tweets))

# get all column names
print(all_tweets.columns)
print(all_tweets.loc[0]['text'])


#Print the user here and the user's location here.
print(all_tweets.head())
print(all_tweets["user"].head()) # "user" is a dictionary

for i in range(len(all_tweets)):
    print(all_tweets.loc[i]["user"]["location"]) # dictionary "user" with keys "location"

    
    
# Defining Viral Tweets
import numpy as np

print(np.median(all_tweets["retweet_count"])) # 13

# create a column to show which tweets are viral and which are not
all_tweets["is_viral"] = np.where(all_tweets["retweet_count"] > np.median(all_tweets["retweet_count"]), 1, 0 )
print(all_tweets["is_viral"].value_counts())
print("num of viral tweets: %d" %all_tweets["is_viral"].value_counts().loc[1]) # 5537
print("num of non-viral tweets: %d" %all_tweets["is_viral"].value_counts().loc[0]) # 5562


# Making Features

# Setting axis = 1 creates a new column rather than a new row.

all_tweets['tweet_length'] = all_tweets.apply(lambda tweet: len(tweet['text']), axis=1)
all_tweets["followers_count"] = all_tweets.apply(lambda tweet: tweet["user"]["followers_count"], axis = 1)
all_tweets["friends_count"] = all_tweets.apply(lambda tweet: tweet["user"]["friends_count"], axis = 1)
all_tweets["listed_count"] = all_tweets.apply(lambda tweet: tweet["user"]["listed_count"], axis = 1)

# create another column to analyze the location as US or others
all_tweets["location"] = all_tweets.apply(lambda tweet: tweet["user"]["location"], axis = 1)
print(all_tweets["location"])
print(all_tweets["location"].value_counts())

# access multiple key names from dictionary "user"
print("user keys below:")
print(all_tweets.loc[0]["user"].keys())


# Normalising The Data

from sklearn.preprocessing import scale

labels = all_tweets["is_viral"]
data = all_tweets[ ["tweet_length", "followers_count", "friends_count"] ]
data_2 = all_tweets[ ["tweet_length", "followers_count", "friends_count", "listed_count"] ] # features should be continuous like numbers


scaled_data = scale(data, axis = 0) # This scales the columns as opposed to the rows.
scaled_data_2 = scale(data_2, axis = 0)
#print("unscaled data:")
#print(data)
#print("normalised data:")
#print(scaled_data)
#print("normalised data 2:")
#print(scaled_data_2)


# Creating the Training Set and Test Set

from sklearn.model_selection import train_test_split

train_data, test_data, train_labels, test_labels = train_test_split(scaled_data, labels, test_size = .2, random_state = 1)
train_data_2, test_data_2, train_labels_2, test_labels_2 = train_test_split(scaled_data_2, labels, test_size = .2, random_state = 1)


# Using the Classifier

from sklearn.neighbors import KNeighborsClassifier

classifier = KNeighborsClassifier(n_neighbors = 5)
classifier.fit(train_data, train_labels)

classifier_2 = KNeighborsClassifier(n_neighbors = 5)
classifier_2.fit(train_data_2, train_labels)

# test the models
print(classifier.score(test_data, test_labels)) # 0.5883
print(classifier_2.score(test_data_2, test_labels)) #0.6009


# Choosing K

import matplotlib.pyplot as plt

scores = []
scores_2 = []

for K in range(1, 201):
    classifier = KNeighborsClassifier(n_neighbors = K)
    classifier.fit(train_data, train_labels)
    scores.append(classifier.score(test_data, test_labels))
    print("K = %d: accuracy score = %.4f"%(K, classifier.score(test_data, test_labels)))

for K in range(1, 201):    
    classifier_2 = KNeighborsClassifier(n_neighbors = K)
    classifier_2.fit(train_data_2, train_labels)
    scores_2.append(classifier_2.score(test_data_2, test_labels))
    print("K = %d: accuracy score = %.4f"%(K, classifier_2.score(test_data_2, test_labels)))
    
    
K_Max = [ K + 1 for K in range(0, 200) if scores[K] == max(scores) ]
K_Max_2 = [ K + 1 for K in range(0, 200) if scores_2[K] == max(scores_2) ]


# Visualisation of Data

fig, axis = plt.subplots(figsize = (10, 6)) 

axis.plot(range(1, 201), scores, color = "blue", label = "features: tweet length, followers count, friends count")
#axis.plot([0, K_Max[0], K_Max[0]], [max(scores), max(scores), 0.55], "r--", lw = 2, label = "K for max accuracy")
axis.set_title("Classifying Tweets as Viral or Not with KNN")
axis.set_xlabel("K (num of neighbours)")
axis.set_ylabel("accuracy")
axis.plot(range(1, 201), scores_2, color = "green", label = "features: tweet length, followers count, friends count, listed count")
#axis.plot([0, K_Max_2[0], K_Max_2[0]], [max(scores_2), max(scores_2), 0.55], "k--", lw = 2, label = "K for max accuracy")
plt.legend(loc = "best")

axis.annotate('$K_{max}$ for classifier 1', 
            xy = (K_Max[0], max(scores) - 0.007), 
            xytext = (K_Max[0], max(scores) - 0.03), 
            arrowprops = dict(facecolor = 'black', shrink = 0.01, width = 1.5, headwidth = 6, headlength = 8))

axis.annotate('$K_{max}$ for classifier 2', 
            xy = (K_Max_2[0], max(scores_2) - 0.001), 
            xytext = (K_Max_2[0], max(scores_2) - 0.02), 
            arrowprops = dict(facecolor='black', shrink = 0.005, width = 1.5, headwidth = 6, headlength = 8))



plt.show()
plt.close('all')
