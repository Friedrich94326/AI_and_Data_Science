import codecademylib3_seaborn
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

df = pd.read_csv("https://content.codecademy.com/programs/data-science-path/linear_regression/honeyproduction.csv")

print(df.head())
prod_per_year = df.groupby('year').totalprod.mean().reset_index()

x = prod_per_year['year']
#print("before using reshape: type of x is ")
#print(type(x))
x= x.values.reshape(-1, 1)
#print("after using reshape: type of x is ")
#print(type(x))

y = prod_per_year['totalprod']

plt.scatter(x, y)
plt.title('Honey Production over years')
plt.xlabel('year')
plt.ylabel('total production')
plt.show()
plt.close('all')

# Create a linear regression model from scikit-learn
regr = linear_model.LinearRegression().fit(x, y)

# slope and intercept of the regression line
m_best = regr.coef_
b_best = regr.intercept_
print("best-fit slope = %.2f " %m_best)
print("best-fit intercept = %.2f " %b_best)

y_predict = [m_best * x_i + b_best for x_i in x]

plt.plot(x, y_predict, color = 'orange')
plt.scatter(x, y)
plt.title('Honey Production over years')
plt.xlabel('year')
plt.ylabel('total production')
legend_labels = ['regression line']
plt.legend(legend_labels)
plt.show()
plt.close('all')

# Predict the Honey Decline

X_future = np.array(range(2013, 2050))
# reshape it for scikit-learn
X_future = X_future.reshape(-1, 1)
# X_future is now a big column of numbers — there’s one number in each row

future_predict = regr.predict(X_future)

plt.plot(X_future, future_predict, color = 'red', label = 'future prediction')
plt.legend()
plt.show()

