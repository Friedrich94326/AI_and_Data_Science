def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn
from cars import training_points, training_labels, testing_points, testing_labels
import warnings
from sklearn.ensemble import RandomForestClassifier


classifier = RandomForestClassifier(n_estimators = 2000, random_state = 0)

classifier.fit(training_points, training_labels)

# test the random forest and examine the accuracy
print("accuracy of random forest: %.4f" %classifier.score(testing_points, testing_labels)) # 0.9827

