import numpy as np
import matplotlib.pyplot as plt
import codecademylib3_seaborn

teacher_one_grades = [83.42, 88.04, 82.12, 85.02, 82.52, 87.47, 84.69, 85.18, 86.29, 85.53, 81.29, 82.54, 83.47, 83.91, 86.83, 88.5, 84.95, 83.79, 84.74, 84.03, 87.62, 81.15, 83.45, 80.24, 82.76, 83.98, 84.95, 83.37, 84.89, 87.29]
teacher_two_grades = [85.15, 95.64, 84.73, 71.46, 95.99, 81.61, 86.55, 79.81, 77.06, 92.86, 83.67, 73.63, 90.12, 80.64, 78.46, 76.86, 104.4, 88.53, 74.62, 91.27, 76.53, 94.37, 84.74, 81.84, 97.69, 70.77, 84.44, 88.06, 91.62, 65.82]

print("Teacher One mean: " + str(np.mean(teacher_one_grades)))
print("Teacher Two mean: " + str(np.mean(teacher_two_grades)))

plt.subplot(211)
plt.title("Teacher One Grades")
plt.xlabel("Grades")
plt.hist(teacher_one_grades)
plt.xlim(65, 105)


plt.subplot(212)
plt.title("Teacher Two Grades")
plt.xlabel("Grades")
plt.hist(teacher_two_grades, bins = 20)
plt.xlim(65, 105)

plt.tight_layout()
plt.show()




# Distance from the mean
grades = [88, 82, 85, 84, 90]
mean = np.mean(grades)




difference_one = grades[0] - np.average(grades)
difference_two = grades[1] - np.average(grades)
difference_three = grades[2] - np.average(grades)
difference_four = grades[3] - np.average(grades)
difference_five = grades[4] - np.average(grades)


# IGNORE CODE BELOW HERE
print("The mean of the data set is " + str(mean) + "\n")
print("The first student is " +str(round(difference_one, 2)) + " percentage points away from the mean.")
print("The second student is " +str(round(difference_two, 2)) + " percentage points away from the mean.")
print("The third student is " +str(round(difference_three, 2)) + " percentage points away from the mean.")
print("The fourth student is " +str(round(difference_four, 2)) + " percentage points away from the mean.")
print("The fifth student is " +str(round(difference_five, 2)) + " percentage points away from the mean.")

# Average Distances

#Part 1: Sum the differences
difference_sum = 0
for i in range(len(grades)):
  difference_sum += grades[i] - mean

#Part 2: Average the differences
average_difference = difference_sum / len(grades)

#IGNORE CODE BELOW HERE
print("The sum of the differences is " + str(format(difference_sum, "f")))
print("The average difference is " + str(format(average_difference, "f")))


# Square the Differences

#When calculating these variables, square the difference.
difference_one = (88 - mean) ** 2
difference_two = (82 - mean) ** 2
difference_three = (85 - mean) ** 2
difference_four = (84 - mean) ** 2
difference_five = (90 - mean) ** 2

difference_sum = difference_one + difference_two + difference_three + difference_four + difference_five

variance = difference_sum / 5

print("The sum of the squared differences is " + str(difference_sum))
print("The variance is " + str(variance))


# Variance In NumPy

teacher_one_grades = [80.24, 81.15, 81.29, 82.12, 82.52, 82.54, 82.76, 83.37, 83.42, 83.45, 83.47, 83.79, 83.91, 83.98, 84.03, 84.69, 84.74, 84.89, 84.95, 84.95, 85.02, 85.18, 85.53, 86.29, 86.83, 87.29, 87.47, 87.62, 88.04, 88.5]
teacher_two_grades = [65.82, 70.77, 71.46, 73.63, 74.62, 76.53, 76.86, 77.06, 78.46, 79.81, 80.64, 81.61, 81.84, 83.67, 84.44, 84.73, 84.74, 85.15, 86.55, 88.06, 88.53, 90.12, 91.27, 91.62, 92.86, 94.37, 95.64, 95.99, 97.69, 104.4]

#Set these two variables equal to the variance of each dataset using NumPy
teacher_one_variance = np.var(teacher_one_grades)
teacher_two_variance = np.var(teacher_two_grades)


#IGNORE THE CODE BELOW HERE
plt.hist(teacher_one_grades, alpha = 0.75, label = "Teacher 1 Scores", bins = 7)
plt.hist(teacher_two_grades, alpha = 0.5, label = "Teacher 2 Scores", bins = 30)
plt.title("Student test grades in two different classes")
plt.xlabel("Grades")
plt.legend()
plt.show()

print("The mean of the test scores in teacher one's class is " + str(np.mean(teacher_one_grades)))
print("The mean of the test scores in teacher two's class is " + str(np.mean(teacher_two_grades)))

print("The variance of the test scores in teacher one's class is " +str(teacher_one_variance))
print("The variance of the test scores in teacher two's class is " +str(teacher_two_variance))

from data import dataset_one, dataset_two

plt.hist(dataset_one, alpha =0.75, label = "dataset_one", bins = 80)
plt.hist(dataset_two, alpha = 0.5, label = "dataset_two", bins = 80)
plt.legend()

print("The mean of the first dataset is " + str(np.mean(dataset_one)))
print("The mean of the second dataset is " + str(np.mean(dataset_two)) + "\n")

print("The variance of the first dataset is " + str(np.var(dataset_one)))
print("The variance of the second dataset is " + str(np.var(dataset_two)))

plt.show()
