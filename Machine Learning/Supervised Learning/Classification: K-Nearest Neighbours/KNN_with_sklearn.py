from movies import movie_dataset, labels
from sklearn.neighbors import KNeighborsClassifier


# Create a classifier with k=5
classifier = KNeighborsClassifier( n_neighbors = 5)

# Train our classifier using training set and labels
classifier.fit(movie_dataset, labels)


# Predicting unknown movies
unknown_movies = [
  [.45, .2, .5],
  [.25, .8, .9],
  [.1, .1, .9]
]
guesses = classifier.predict([[.45, .2, .5], [.25, .8, .9],[.1, .1, .9]])
print(guesses)

