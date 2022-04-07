# Liner Search


'''
The time complexity of linear search is O(n)
meaning that the time taken to execute increases
with the number of items in our input list
'''

# Find indexes of target element 
# Eg: Target - 9 , return first two indexes of the 9
# [8,9,9,9,0] 
# Output - [1,2]
def linear_search(array,target):
    result = []
    for i in range(len(array)):
        if array[i] == target:
            result.append(i)
            if len(result) >= 2:
                return result
    return [-1,-1]
            
    
print(linear_search([9,9,9,0,0,0],9))
print(linear_search([9,0,0,0,0],9))
print(linear_search([0,0,0],9))
