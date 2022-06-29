#Given a string and a pattern, find out if the string contains any permutation of the pattern.

result = []
def find_permutation(str1, pattern):
  n = len(pattern)
  a = list(pattern)
  permute(a, 0, n)
  for i in result:
     if i in str1:
        return True
  return False

def permute(data, i, length):
	if i == length:
		result.append(''.join(data) )
	else:
		for j in range(i, length):
			# swap
			data[i], data[j] = data[j], data[i]
			permute(data, i + 1, length)
			data[i], data[j] = data[j], data[i]
