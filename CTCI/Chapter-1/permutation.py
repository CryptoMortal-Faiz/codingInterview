# Using sorted

def permutation(s1, s2):
    return sorted(s1) == sorted(s2)

## Loops
def permutation(s1, s2):
    ele = {}
    for i in s1:
        if i in ele:
            ele[i] += 1
        else:
            ele[i] = 1

    for i in s2:
        if i in ele:
            ele[i] -= 1
            if ele[i] == 0:
                del(ele[i])

    return len(ele) == 0
