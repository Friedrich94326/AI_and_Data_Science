# movie_title = [runtime, release year]
star_wars = [125, 1977]
raiders = [115, 1981]
mean_girls = [97, 2004]

def distance(movie1, movie2):
  distance = 0
  if len(movie1) == len(movie2):
    for i in range(len(movie1)):
      distance += ( movie1[i] - movie2[i] ) ** 2
  else:
    pass
  return distance ** (1/2)
  
 
# distance in 3D
def distance(movie1, movie2):
  if len(movie1) == len(movie2):
    length_difference = (movie1[0] - movie2[0]) ** 2
    year_difference = (movie1[1] - movie2[1]) ** 2
    budge_difference = (movie1[2] - movie2[2]) ** 2
    distance = (length_difference + year_difference + budge_difference) ** 0.5
  else:
    pass
  return distance


print(distance(star_wars, raiders))
print(distance(star_wars, mean_girls))


# Stage 1- Data with Different Scales: Normalisation

release_dates = [1897, 1998, 2000, 1948, 1962, 1950, 1975, 1960, 2017, 1937, 1968, 1996, 1944, 1891, 1995, 1948, 2011, 1965, 1891, 1978]

def min_max_normalize(lst):
  minimum = min(lst)
  maximum = max(lst)
  normalized = []

  for i in range(len(lst)):
    normalized.append( ( lst[i] - minimum) / (maximum - minimum) )
  
  return normalized

print(min_max_normalize(release_dates))


# Stage 2- Finding the Nearest Neighbors
from movies import movie_dataset, movie_labels

#print(movie_dataset['Bruce Almighty'])
#print(movie_labels['Bruce Almighty'])

def distance(movie1, movie2):
  squared_difference = 0
  for i in range(len(movie1)):
    squared_difference += (movie1[i] - movie2[i]) ** 2
  final_distance = squared_difference ** 0.5
  return final_distance

def classify(unknown, dataset, k):
  distances = []
  
  for title in dataset:
    distance_to_point = distance(dataset[title], unknown)
    distances.append([distance_to_point, title])

  distances.sort()
  neighbors = distances[:k]
  return neighbors


# the 5 nearest neighbors associated with their distnaces
print(classify([.4, .2, .9], movie_dataset, 5))


# Stage 3- Count Neighbors
from movies import movie_dataset, movie_labels

def distance(movie1, movie2):
  squared_difference = 0
  for i in range(len(movie1)):
    squared_difference += (movie1[i] - movie2[i]) ** 2
  final_distance = squared_difference ** 0.5
  return final_distance

def classify(unknown, dataset, labels, k):
  distances = []
  num_good = 0
  num_bad = 0
  new_label = 0

  #Looping through all points in the dataset
  for title in dataset:
    movie = dataset[title]
    distance_to_point = distance(movie, unknown)
    #Adding the distance and point associated with that distance
    distances.append([distance_to_point, title])
  distances.sort()
  #Taking only the k closest points
  neighbors = distances[0:k]

  # count of 2 classes
  for movie in neighbors:
    title = movie[1]
    if labels[title] == 0:
      num_bad += 1
    else:
      num_good += 1
  
  # comparison of occurrence frequencies
  if num_good > num_bad:
      new_label = 1
  else:
      new_label = 0

  return new_label



predicted_label = classify([.4, .2, .9], movie_dataset, movie_labels, k =5)
print(predicted_label)
# the trained model predicts this movie to be good 

# Classify Your Favorite Movie

from movies import movie_dataset, movie_labels, normalize_point

def distance(movie1, movie2):
  squared_difference = 0
  for i in range(len(movie1)):
    squared_difference += (movie1[i] - movie2[i]) ** 2
  final_distance = squared_difference ** 0.5
  return final_distance

def classify(unknown, dataset, labels, k):
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
  num_good = 0
  num_bad = 0
  for neighbor in neighbors:
    title = neighbor[1]
    if labels[title] == 0:
      num_bad += 1
    elif labels[title] == 1:
      num_good += 1
  if num_good > num_bad:
    return 1
  else:
    return 0

# make sure the movie that we want to classify is not in our database
print("Call Me By Your Name" in movie_dataset)

# [budge, runtime, release year]
my_movie = [350000, 132, 2017]
normalized_my_movie = normalize_point(my_movie)
print(normalized_my_movie)
# normalized = [2.8634276635608227e-05, 0.3242320819112628, 1.0112359550561798]

print(classify(normalized_my_movie, movie_dataset, movie_labels, k = 5))
# result = 1 aka a good one


# Training and Validation Sets

from movies import training_set, training_labels, validation_set, validation_labels

bee_movie_data = validation_set["Bee Movie"]
# "Bee Movie" is a key name
print(bee_movie_data)
#print(classify())
print(type(validation_set)) # which is a dictionary

guess = classify(bee_movie_data, training_set, training_labels, k = 5)
print(guess)
if (guess == validation_labels["Bee Movie"]):
  print("Correct!")
else:
  print("Wrong!")
 


# Choosing K

def find_validation_accuracy(training_set, training_labels, validation_set, validation_labels, k):
  num_correct = 0
  for title in validation_set:
    guess = classify(validation_set[title], training_set, training_labels, k)
    if (guess == validation_labels[title]):
      num_correct += 1
    else:
      continue
  return num_correct / len(validation_set)


print(find_validation_accuracy(training_set, training_labels, validation_set, validation_labels, k = 3))




