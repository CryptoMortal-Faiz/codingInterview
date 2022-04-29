# Maximum subarray sum of sike K



def max_sub_array_of_size_k(k, arr):
  n = len(arr)
  print(n)
  max_sum = 0

  for i in range(n-k+1):
    window_sum = 0
    for j in range(i,i+k):
      window_sum += arr[j]
    print(window_sum)
    max_sum = max(window_sum,max_sum)
  
  return max_sum
