## Check if all elements of the string are unique

# Using multiple DS
def isUnique(string):
  ele = []
  for i in string:
    ele.append(i)
  if len(ele) == len(set(ele)):
    return True
  return False

# Using one DS - Hash Map
def isUnique(string):
    ele = {}
    for i in string:
        if i in ele.keys():
            ele[i] += 1
        else:
            ele[i] = 1
    if ele[i] > 1:
        return False
    return True

# Using one DS - Array
def unique(string):
    ele = []
    for i in string:
        if i in ele:
            return False
        ele.append(i)
    return True
  
## Without Using any DS  
def isUnique(s):
    s = sorted(s.lower())
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            return False
    return True 

