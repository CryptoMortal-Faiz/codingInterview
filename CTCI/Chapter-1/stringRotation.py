def is_substring(string, sub):
    print(string)
    print(sub)
    print(string.find(sub))
    return string.find(sub) != -1


def string_rotation(s1, s2):
    if len(s1) == len(s2) != 0:
        return is_substring(s1 + s1, s2)
    return False

print(string_rotation('cba', 'bac'))
