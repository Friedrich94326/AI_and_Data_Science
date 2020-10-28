# Formatting the Data for scikit-learn
from reviews import neg_list, pos_list
from sklearn.feature_extraction.text import CountVectorizer

review = "This crib was amazing"

# a CountVectorizer object is needed
counter = CountVectorizer()

# counter will learn the vocabulary of strings which are fed in it
# our training set: neg_list + pos_list
counter.fit(neg_list + pos_list)
print(counter.vocabulary_)


review_counts = counter.transform([review])
print(review_counts)

training_counts = counter.transform(neg_list + pos_list)
print(training_counts)


# Train the model using scikit-learn

from reviews import counter, training_counts
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

review = "This crib was amazing"
review_counts = counter.transform([review])


classifier = MultinomialNB()

training_labels = [0] * len(neg_list) + [1] * len(pos_list)

# Train the model
classifier.fit(training_counts, training_labels)

# test the model that we trained
print(classifier.predict(review_counts))
print(classifier.predict_proba(review_counts))

test_review = "This crib was great amazing and wonderful"
test_review_counts = counter.transform([test_review])
prediction = classifier.predict(test_review_counts)
print("The prediction result: %d" %prediction)
prediction_proba = classifier.predict_proba(test_review_counts)
print(prediction_proba)



# Review
from reviews import baby_counter, baby_training, instant_video_counter, instant_video_training, video_game_counter, video_game_training
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

review = "this game was violent but awesome"

baby_review_counts = baby_counter.transform([review])
instant_video_review_counts = instant_video_counter.transform([review])
video_game_review_counts = video_game_counter.transform([review])

baby_classifier = MultinomialNB()
instant_video_classifier = MultinomialNB()
video_game_classifier = MultinomialNB()

baby_labels = [0] * 1000 + [1] * 1000
instant_video_labels = [0] * 1000 + [1] * 1000
video_game_labels = [0] * 1000 + [1] * 1000


baby_classifier.fit(baby_training, baby_labels)
instant_video_classifier.fit(instant_video_training, instant_video_labels)
video_game_classifier.fit(video_game_training, video_game_labels)

print("Baby training set: " +str(baby_classifier.predict_proba(baby_review_counts)))
print("Amazon Instant Video training set: " + str(instant_video_classifier.predict_proba(instant_video_review_counts)))
print("Video Games training set: " + str(video_game_classifier.predict_proba(video_game_review_counts)))




