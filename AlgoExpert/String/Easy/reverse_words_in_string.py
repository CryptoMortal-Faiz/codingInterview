def reverseWordsInString(string):
    array = string.split(" ")
    rev_array = []
    for i in reversed(range(len(array))):
        rev_array.append(array[i])
    return " ".join(rev_array)

print(reverseWordsInString("4   ss"))

# Time - O(n) , Space - O(n)
