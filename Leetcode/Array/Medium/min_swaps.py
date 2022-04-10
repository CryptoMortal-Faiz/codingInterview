# Minimum swaps required to sort the array


def minSwaps(arr, N):
     
    ans = 0
    temp = arr.copy()
    temp.sort()
   
    for i in range(N):
       
        # This is checking whether
        # the current element is
        # at the right place or not
        if (arr[i] != temp[i]):
            ans += 1
 
            # Swap the current element
            # with the right index
            # so that arr[0] to arr[i]
            # is sorted
            swap(arr, i, arr.index(temp[i]))
   
    return ans
   
def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
   
array = [3,2,4,5,1,7]
print(minSwaps(array,6))
