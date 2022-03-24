def twoNumberSum(array, t):
	nums = dict()
	for n in array:
		print(n)
		match = t - n
		print(nums)
		if match in nums:
			return [match, n]
		else:
			nums[n] = True
	return []


# Approach 2

def twoNumberSum(array, targetSum):
	if array ==  None or len(array) == 0:
		return []
    for i in array:
      tofind = targetSum - i
		if tofind in array and tofind != i:
			return [tofind,i]
		elif tofind not in array:
			return []
		
		
