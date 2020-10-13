from movies import movie_dataset, movie_ratings
from sklearn.neighbors import KNeighborsRegressor

regressor = KNeighborsRegressor(n_neighbors = 5, weights = "distance")
regressor.fit(movie_dataset, movie_ratings)


# These three lists are the features for Incredibles 2, The Big Sick, and The Greatest Showman.
unknowns = [
  [0.016, 0.300, 1.022],
  [0.0004092981, 0.283, 1.0112],
  [0.00687649, 0.235, 1.0112]
]
predicts = regressor.predict(unknowns)
print(predicts)   # [6.84913968 5.47572913 6.91067999]

