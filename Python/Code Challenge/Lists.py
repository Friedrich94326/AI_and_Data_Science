def every_three_nums(start):
  listOfNums = []
  current = start
  while current <= 100:
    print(current)
    listOfNums.append(current)
    current += 3
  return listOfNums
 
def remove_middle(lst, start, end):
  return lst[:start] + lst[end+1:]
  
def more_frequent_item(lst, item1, item2):
  often = 0
  if ( lst.count(item1) > lst.count(item2) ):
    often = item1
  elif (lst.count(item1) < lst.count(item2) ):
    often = item2
  else:
    often = item1
  return often
  
def double_index(lst, index):
  ResultList = lst
  if ( index >= 0 ) and ( index < len(lst) ):
    ResultList[index] *= 2
  return ResultList 
 
def middle_element(lst):
  middle = 0
  if ( len(lst) % 2 == 0 ):
    middle =  ( lst[int(len(lst) /2 ) - 1] + lst[int( len(lst) / 2 ) ] ) / 2
  else:
    middle = lst[int((len(lst) + 1) / 2) - 1]
  return middle
  
