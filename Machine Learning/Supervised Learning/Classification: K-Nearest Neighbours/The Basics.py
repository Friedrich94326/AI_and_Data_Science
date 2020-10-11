# Distance Formulae: Euclidean Distance/ Manhattan Distance/ Hamming Distance

# Euclidean Distance

def euclidean_distance(pt1, pt2):
  distance = 0
  if len(pt1) == len(pt2):
    for i in range(len(pt1)):
       distance += (pt1[i] - pt2[i]) ** 2
    distance = (distance)**(1/2)
  else:
    pass
  return distance

p1_2D = [1, 2]
p2_2D = [4, 0]
print(euclidean_distance(p1_2D, p2_2D))


p1_3D = [5, 4, 3]
p2_3D = [1, 7, 9]
print(euclidean_distance(p1_3D, p2_3D))

# what if the dimensions of points do not match?
print(euclidean_distance(p1_2D, p2_3D))


# Manhattan Distance (L1 norm)

def manhattan_distance(pt1, pt2):
  distance = 0
  if len(pt1) == len(pt2): 
    for i in range(len(pt1)):
      distance += abs(pt1[i] - pt2[i])
  else:
    pass
  return distance
  
# Manhattan Distance v.s. Euclidean Distance
print(euclidean_distance([1, 2], [4, 0]))
print(euclidean_distance([5, 4, 3], [1, 7, 9]))

print(manhattan_distance([1, 2], [4, 0]))
print(manhattan_distance([5, 4, 3], [1, 7, 9]))


# Hamming Distance

# Hamming distance is used in spell checking algorithms.

def hamming_distance(pt1, pt2):
  distance = 0
  if len(pt1) == len(pt2):
    for i in range(len(pt1)):
      if pt1[i] != pt2[i]:
        distance += 1
  else:
    pass    
  return distance

print(hamming_distance([1, 2], [1, 100])) # 1
print(hamming_distance([5, 4, 9], [1, 7, 9])) # 2



# SciPy library
print(distance.euclidean([1, 2], [4, 0]))
print(distance.cityblock([1, 2], [4, 0]))
print(distance.hamming([5, 4, 9], [1, 7, 9])) # answer = 0.6666 cuz scipy divides by the number of dimensions



# Normalisation- The goal of normalization is to make every datapoint have the same scale so each feature is equally important. 

# Min-max normalization: Guarantees all features will have the exact same scale but does not handle outliers well.
# Z-score normalization: Handles outliers, but does not produce normalized data with the exact same scale.
