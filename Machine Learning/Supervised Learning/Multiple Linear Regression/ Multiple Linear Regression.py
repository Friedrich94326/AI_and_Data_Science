import codecademylib3_seaborn
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from mpl_toolkits.mplot3d import Axes3D

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

streeteasy = pd.read_csv("https://raw.githubusercontent.com/sonnynomnom/Codecademy-Machine-Learning-Fundamentals/master/StreetEasy/manhattan.csv")

df = pd.DataFrame(streeteasy)

x = df[['size_sqft','building_age_yrs']]
y = df[['rent']]

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size = 0.8, test_size = 0.2, random_state=6)

ols = LinearRegression()

ols.fit(x_train, y_train)

# Plot the figure

fig = plt.figure(1, figsize=(6, 4))
plt.clf()

elev = 43.5
azim = -110

ax = Axes3D(fig, elev=elev, azim=azim)

ax.scatter(x_train[['size_sqft']], x_train[['building_age_yrs']], y_train, c='k', marker='+')

ax.plot_surface(np.array([[0, 0], [4500, 4500]]), np.array([[0, 140], [0, 140]]), ols.predict(np.array([[0, 0, 4500, 4500], [0, 140, 0, 140]]).T).reshape((2, 2)), alpha=.7)

ax.set_xlabel('Size (ft$^2$)')
ax.set_ylabel('Building Age (Years)')
ax.set_zlabel('Rent ($)')

ax.w_xaxis.set_ticklabels([])
ax.w_yaxis.set_ticklabels([])
ax.w_zaxis.set_ticklabels([])

# Add the code below:
plt.show()



# import train_test_split
from sklearn.model_selection import train_test_split

streeteasy = pd.read_csv("https://raw.githubusercontent.com/sonnynomnom/Codecademy-Machine-Learning-Fundamentals/master/StreetEasy/manhattan.csv")

df = pd.DataFrame(streeteasy)

x = df[['bedrooms', 'bathrooms', 'size_sqft', 'min_to_subway', 'floor', 'building_age_yrs', 'no_fee',
'has_roofdeck', 'has_washer_dryer', 'has_doorman', 'has_elevator', 'has_dishwasher', 'has_patio', 'has_gym']]
y= df[['rent']]

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size = 0.8, test_size = 0.2, random_state = 6)


print(x_train.shape) # dimensions of the array
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)



# Sonn'y Apartment
import codecademylib3_seaborn
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


streeteasy = pd.read_csv("https://raw.githubusercontent.com/sonnynomnom/Codecademy-Machine-Learning-Fundamentals/master/StreetEasy/manhattan.csv")

df = pd.DataFrame(streeteasy)

x = df[['bedrooms', 'bathrooms', 'size_sqft', 'min_to_subway', 'floor', 'building_age_yrs', 'no_fee', 'has_roofdeck', 'has_washer_dryer', 'has_doorman', 'has_elevator', 'has_dishwasher', 'has_patio', 'has_gym']]

y = df[['rent']]

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size = 0.8, test_size = 0.2, random_state=6)

# Add the code here:

mlr = LinearRegression().fit(x_train, y_train)

y_predict = mlr.predict(x_test)



# Now let's predict Sonny's apartment

#print(x_train['has_washer_dryer'])

x_sonny_apartment = [[1, 1, 620, 16, 1, 98, 1, 0, 1, 0, 0, 1, 1, 0]]

y_sonny_apartment = mlr.predict(x_sonny_apartment)

print("predicted rent of Sonny's apartment: %.2f USD" %y_sonny_apartment) # actual rent is under 2000 USD


# Create a scatter plot of y_test and y_predict
plt.scatter(y_test, y_predict, alpha = 0.4)
plt.xlabel("y_test")
plt.ylabel("y_predict")
plt.show()

# LinearRegression has attributes coef_ & intercept_
print(mlr.coef_)

# Correlations

# Checking of Correlations
fig = plt.figure(1, figsize = (8, 6))
fig.suptitle("Apartment Rentals in Manhattan", fontsize = 14)
fig.subplots_adjust(hspace = .4, wspace = .4)


ax1 = plt.subplot(2, 2, 1)
ax1.scatter(df[['size_sqft']], df[['rent']], c = 'green', alpha = .4)
# alpha for transparency 0~1
ax1.set_xlabel("size ($ft^2$)")
ax1.set_ylabel("rent (USD)")
ax1.set_title("rent v.s. size")

ax2 = plt.subplot(2, 2, 2)
ax2.scatter(df[['min_to_subway']], df[['rent']], c = 'red', alpha = .4)
ax2.set_xlabel("mins")
ax2.set_ylabel("rent (USD)")
ax2.set_title("rent v.s. minute to subway")

ax3 = plt.subplot(2, 2, 3)
ax3.scatter(df[['building_age_yrs']], df[['rent']], c = 'blue', alpha = .4)
ax3.set_xlabel("year")
ax3.set_ylabel("rent (USD)")
ax3.set_title("rent v.s. building age")

ax4 = plt.subplot(2, 2, 4)
ax4.scatter(df[['floor']], df[['rent']], c = 'orange', alpha = .4)
ax4.set_xlabel("floor number")
ax4.set_ylabel("rent (USD)")
ax4.set_title("rent v.s. floor number")

plt.show()


# Evaluating the Model's Accuracy by Residual Analysis

# find the mean squared error regression loss for the training set
print("Train score: %.2f" %mlr.score(x_train, y_train)) # Train score: 0.772546055982

# find the mean squared error regression loss for the testing set
print("Test score: %.2f" %mlr.score(x_test, y_test)) # Test score: 0.805037197536



# Rebuild the Model

# Remove some of the features that don’t have strong correlations and see if your scores improved!
x = df[['bedrooms', 'bathrooms', 'size_sqft', 'floor', 'building_age_yrs',  'has_roofdeck', 'has_washer_dryer', 'has_doorman', 'has_elevator', 'has_dishwasher', 'has_patio', 'has_gym']]
# 'min_to_subway' & 'no_fee' have been removed
y = df[['rent']]

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size = 0.8, test_size = 0.2, random_state=6)

lm = LinearRegression()

model = lm.fit(x_train, y_train)

y_predict= lm.predict(x_test)

print("Train score:")
print(lm.score(x_train, y_train))

print("Test score:")
print(lm.score(x_test, y_test))

plt.scatter(y_test, y_predict)
plt.plot(range(20000), range(20000), color = 'red')

plt.xlabel("Prices: $Y_i$")
plt.ylabel("Predicted prices: $\hat{Y}_i$")
plt.title("Actual Rent vs Predicted Rent")

plt.show()

