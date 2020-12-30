# Classify Your Favorite Movie

from movies import movie_dataset, movie_labels, normalize_point

# Euclidean metric is used
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


print(find_validation_accuracy(training_set, training_labels, validation_set, validation_labels, k = 3)) #  0.66
