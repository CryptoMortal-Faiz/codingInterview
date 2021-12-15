# Find two numbers in array equal to the target
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
