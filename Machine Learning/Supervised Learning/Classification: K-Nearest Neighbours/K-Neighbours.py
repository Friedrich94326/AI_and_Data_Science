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

