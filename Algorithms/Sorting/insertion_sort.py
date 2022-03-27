


def insertionSort(array):
	print("Orig array ", array)
	for i in range(1,len(array)):
		j = i
		print(j)
		while j > 0 and array[j] < array [j-1]:
			print(j)
			array[j],array[j-1] = array[j-1],array[j]
			print(array)
			j -= 1
	return array
