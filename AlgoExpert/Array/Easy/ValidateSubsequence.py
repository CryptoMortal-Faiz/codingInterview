def isValidSubsequence(array, sequence):
# Declare empty array to store all indices in the main array
	idxs = []
# Loop through all elements in sequence array and find respective indices in the main array
	for i in sequence:
		if i not in array: # If any element from sequence is not present in the main array return False as there is no sequence
			return False
		idx = array.index(i) # Gets the index of sequence element from main array
		idxs.append(idx) # Append the index of element from main array into idxs array
	idxss = [] # Declare empty array to remove all duplicate indesxes
	for i in idxs:
		if i not in idxss:
			idxss.append(i)
	if sorted(idxss) == idxss: # Compare if the indices are in sequence if not return False
		n = len(idxss)
		if n == 1:
			return True
		elif n != len(sequence):
			return False
		else:
			if (idxss[0] <= idxss[1] and idxss[n - 2] <= idxss[n - 1]) :
				return True
			else:
				return False
	else:
				return False
