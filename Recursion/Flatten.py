
# Flattening list  using recursion
def flatten(_list):
    result=[]
    for x in _list:
        if type(x) == list:
            result.extend(flatten(x))
        else:result.append(x)
    return result
print(flatten([1, 2, 3, [4, 5]])) # [1, 2, 3, 4, 5]
