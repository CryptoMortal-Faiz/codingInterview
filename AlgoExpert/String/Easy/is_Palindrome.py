# Two pointer approach
# Check if string is a palindrome
# Time - O(n) , space - O(1)

def isPalindrome(string):
    
	l = 0
	r = len(string) - 1
	
	while l < r:
		if string[l] != string[r]:
			return False
		l += 1
		r -= 1
	return True
