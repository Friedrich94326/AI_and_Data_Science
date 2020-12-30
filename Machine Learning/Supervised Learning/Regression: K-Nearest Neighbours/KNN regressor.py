"""
In this lesson, we will use the movie dataset that was used in the K-Nearest Neighbors classifier lesson.
However, instead of classifying a new movie as either good or bad, we are now going to predict its IMDb rating as a real number.
"""

# Regression
from movies import movie_dataset, movie_ratings

def distance(movie1, movie2):
  squared_difference = 0
  for i in range(len(movie1)):
    squared_difference += (movie1[i] - movie2[i]) ** 2
  final_distance = squared_difference ** 0.5
  return final_distance

def predict(unknown, dataset, movie_ratings, k):
  distances = []
  #Looping through all points in the dataset
  for title in dataset:
    movie = dataset[title]
    distance_to_point = distance(movie, unknown)
    #Adding the distance and point associated with that distance
    distances.append([distance_to_point, title])
  distances.sort()
  #Taking only the k closest points
  neighbors = distances[0:k]

  total_ratings = 0
  for neighbor in neighbors:
    title = neighbor[1]
    total_ratings += movie_ratings[title]
  return total_ratings / len(neighbors)


print("normalised budget, runtime and release year of movie 'Life of Pi':")
print(movie_dataset["Life of Pi"])
print("IMDb rating of 'Life of Pi' is %.1f " %movie_ratings["Life of Pi"])

# [0.016, 0.300, 1.022] is the normalized budget, runtime, and year of the movie Incredibles 2!
print("predicted IMDb rating of 'Incredible 2' is %f" %predict([.016, .300, 1.022], movie_dataset, movie_ratings, k = 5))



# Weighted Regression
def predict_weighted(unknown, dataset, movie_ratings, k):
  distances = []

  #Looping through all points in the dataset
  for title in dataset:
    movie = dataset[title]
    distance_to_point = distance(movie, unknown)
    #Adding the distance and point associated with that distance
    distances.append([distance_to_point, title])
  distances.sort()
  #Taking only the k closest points
  neighbors = distances[0:k]

  numerator = 0
  denominator = 0
  for neighbor in neighbors:
    title = neighbor[1]
    numerator += movie_ratings[title] / neighbor[0]
    denominator += 1 / neighbor[0]

  return numerator / denominator

# Predict 'Incredibles 2' by weighted KNN regressor
predicted_rating = predict_weighted([.016, .300, 1.022], movie_dataset, movie_ratings, k = 5 )
print("Predicted IMDb rating of 'Incredibles 2' is %.4f" %predicted_rating)





