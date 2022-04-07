# Binary Search


'''
The time complexity of linear search is O(n)
meaning that the time taken to execute increases
with the number of items in our input list
'''

# ITERATIVE
def binary_search(array,target):
    l = 0
    r = len(array)-1
    index = -1
    
    while l<=r and index == -1:
        mid = (l+r)//2
        if target == array[mid]:
            index = mid
        else:
            if target <= array[mid]:
                r = mid-1
            else:
                l = mid+1
    return index

# RECURSIVE


    
    
    
# print(binary_search([9,9,9,0,0,0],9))
print(binary_search([1,2,3,9],3))
