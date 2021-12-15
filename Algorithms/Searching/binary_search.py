# Binary search

# Algo
''' Step 1: Sort the array
    Step 2: Find the middle elemnt
    Step 3: If middle is less then traverse through the elements on the right side vice versa on left if the elemnt is greater
'''

def binary_search(array,target):
  array.sort()
  n = len(array)
  # middle element
  
  if array[n/2] == target:
    return n/2
  
  # on right side 
  if array[n/2] < target:
    for i in range(0,n/2):
      if array[i] == target:
        return i
  
  # Left side
  if array[n/2] > target:
    for i in range(n/2,len(array):
      if array[i] == target:
        return i
