# Serch each element one by one until the target element is found 

def liner_search(array, target):
  for i in range(len(array)):
    if array[i] == target:
      return i
  
