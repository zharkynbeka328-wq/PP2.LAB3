#Реверс слов

def reverse_sentence(s):
    return " ".join(s.split()[::-1])

print(reverse_sentence("We are ready"))  


# ready are We
