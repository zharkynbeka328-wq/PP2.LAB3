#Перестановки строки

import itertools

def string_permutations(s):
    return list(itertools.permutations(s))

print(string_permutations("abc"))
