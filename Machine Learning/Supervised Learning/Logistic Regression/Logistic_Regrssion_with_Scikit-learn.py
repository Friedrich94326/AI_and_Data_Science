import numpy as np
from sklearn.linear_model import LogisticRegression
from exam import hours_studied_scaled, passed_exam, exam_features_scaled_train, exam_features_scaled_test, passed_exam_2_train, passed_exam_2_test, guessed_hours_scaled

# Create and fit logistic regression model here
model = LogisticRegression()
model.fit(hours_studied_scaled, passed_exam)

# Save the model coefficients and intercept here
calculated_coefficients = model.coef_
intercept = model.intercept_
print("coefficients:")
print(calculated_coefficients)
print("intercept:")
print(intercept)

# Predict the probabilities of passing for next semester's students here
# model.predict_proba()
passed_predictions = model.predict_proba(guessed_hours_scaled)
print("predicted passage:")
print(passed_predictions)


# Create a new model on the training data with two features here
model_2 = LogisticRegression()
model_2.fit(exam_features_scaled_train, passed_exam_2_train)


# Predict whether the students will pass here
# model.predict() Predict class labels
passed_predictions_2 = model_2.predict(exam_features_scaled_test)
print("new predicted passage:")
print(passed_predictions_2 )


# Feature Importance

import codecademylib3_seaborn
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from exam import exam_features_scaled, passed_exam_2

# Train a sklearn logistic regression model on the normalized exam data
model_2 = LogisticRegression()
model_2.fit(exam_features_scaled,passed_exam_2)

# Assign and update coefficients
coefficients = model_2.coef_

# convert the array into a list and grab the values we want to visualize
coefficients = coefficients.tolist()[0]

# Plot bar graph
plt.bar([1, 2], coefficients)
plt.xticks([1, 2], ['hours studied', 'math courses taken'])
plt.xlabel('feature')
plt.ylabel('coefficient')
plt.title('Comparsion of Feature Importance')

plt.show()
