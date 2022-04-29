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


#Approach 2
def max_sub_array_of_size_k(k, arr):
  n = len(arr)
  
  window_sum, max_sum =0,0
  window_start = 0
  ele = []

  for window_end in range(n):
    window_sum += arr[window_end]
    ele.append(arr[window_end])
    if window_end >= k-1:
      # print(window_sum)
      # print(window_end , " k-1 " , k-1)
      max_sum = max(max_sum, window_sum)
      window_sum -= arr[window_start]  # subtract the element going out
      window_start += 1  # slide the window ahead
    print(ele)
  return max_sum
