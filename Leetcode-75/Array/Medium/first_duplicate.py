# Find the first duplicate in the array
# Eg: [1,2,3,4,2,3] Output = 2 ( Since 2 is repating first )

# Use Set
def first_duplicate(array):
    if len(array) == len(set(array)):
        return None
    seen = set()
    for i in array:
        if i in seen:
            return i
        else:
            seen.add(i)
     
# Test
print(first_duplicate([1,3,2]))
