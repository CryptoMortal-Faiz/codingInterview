'''
Given a string s, sort it in decreasing order based on the frequency of the characters. 
The frequency of a character is the number of times it appears in the string.
Return the sorted string. If there are multiple answers, return any of them. 
'''

def frequencySort(self, s: str) -> str:
    freq = {}
    for i in s:
      if i not in freq:
        freq[i] = 1
      else:
        freq[i] += 1
    print(freq)
    sorted_dict = dict(sorted(freq.items(),
                              key=lambda item: item[1],
                              reverse=True))
    res = ''
    for k,v in sorted_dict.items():
      res = res + k * v
    return res
  
# Approach two 

import collections
from collections import Counter
def frequencySort(s) :

    # Count up the occurances.
    counts = collections.Counter(s)
    
    # Build up the string builder.
    string_builder = []
    for letter, freq in counts.most_common():
        # letter * freq makes freq copies of letter.
        # e.g. "a" * 4 -> "aaaa"
        string_builder.append(letter * freq)
    print(string_builder)
    return "".join(string_builder)
    
print(frequencySort("tree"))
