def OneAway(str1, str2):
    n1 = len(str1)
    n2 = len(str2)
    if n1 == n2:
        return "Zero Edits"
    elif n1 > n2:
        findDiff(n1,n2)
    else:
        findDiff(n2,n1)
        
def findDiff(num1,num2):
    diff = num1-num2
    if diff > 1:
        return "More than One Edits"
    return "One Edit"
print(OneAway("Malay", "Chaley"))
