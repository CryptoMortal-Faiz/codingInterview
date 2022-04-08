# Find index of first non repeating element

def firstNonRepeatingCharacter(string):
    
	non_repeat = {}
	for i in range(len(string)):
		if string[i] not in non_repeat:
			non_repeat[string[i]] = 1
		else:
			non_repeat[string[i]] += 1
			
	for k,v in non_repeat.items():
		if v == 1:
			return string.index(k)
	return -1


