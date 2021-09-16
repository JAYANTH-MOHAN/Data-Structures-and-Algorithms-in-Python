# capitalizeFirst Solution iteratively
# def capital(word):
#     result=[]
#     for x in range(len(word)):
#         result.append(word[x].capitalize())
#     return result


# capitalizeFirst Solution recursively
def cap(words):
    result=[]
    if len(words)==0:
        return result
    result.append(words[0][0].upper() + words[0][1:])
    result += cap(words[1:])
    return result
print(cap(['car', 'taco', 'banana']))