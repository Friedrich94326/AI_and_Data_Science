def large_power(base, exponent):
  isLargePower = False
  if ( base**exponent > 5000 ):
    isLargePower = True
  return isLargePower


def over_budget(budget, food_bill, electricity_bill, internet_bill, rent):
  total = food_bill + electricity_bill + internet_bill + rent
  isOverBudget = False
  if (total > budget):
    isOverBudget = True
  return isOverBudget
  
def twice_as_large(num1, num2):
  ans = False
  if ( num1 > 2*num2 ):
    ans = True
  return ans
  
def divisible_by_ten(num):
  isDivisible = True
  if ( num % 10 ):
    isDivisible = False
  return isDivisible

def not_sum_to_ten(num1, num2):
  isSumToTen = False
  if ( num1 + num2 != 10):
    isSumToTen = True
  return isSumToTen
  
def in_range(num, lower, upper):
  isInRange = False
  if (num >= lower) and (num <= upper):
    isInRange = True
  return isInRange
  
 def same_name(your_name, my_name):
  isSame = False
  if ( your_name == my_name ):
    isSame = True
  return isSame
  
def always_false(num):
  threshold = 10
  TrueOrFalse = True
  if ( num > threshold ) or not (num > threshold):
    TrueOrFalse = False
  return TrueOrFalse
  
def movie_review(rating):
  level = ""
  if (rating <= 5):
    level += "Avoid at all costs!"
  elif (rating < 9):
    level += "This one was fun."
  else:
    level += "Outstanding!"
  return level
  

  
