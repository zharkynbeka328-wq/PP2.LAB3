#Уникальные элементы списка

def unique_list(lst):
    result = []
    for x in lst:
        if x not in result:
            result.append(x)
    return result

print(unique_list([1,2,2,3,4,4,5])) 


# [1,2,3,4,5]
