# String Compression

def str_comp(input):
    print(input)
    count = dict()
    for i in input:
        if i in count:
            count[i] += 1
        elif i not in count:
            count[i] = 1
    res = ''
    final = ''
    for k in count.keys():
        res = str(k)+str(count[k])
        final += res
    if len(final) >= len(input):
        return input
    return final

print(str_comp('aaabbcccc'))
print(str_comp('abc'))
