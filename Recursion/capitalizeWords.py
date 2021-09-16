# capitalizeWords Solution
def capitalizeWords(arr):
    result = []
    if len(arr) == 0:
        return result
    result.append(arr[0].upper())
    return result + capitalizeWords(arr[1:])
words = ['i', 'am', 'learning', 'recursion']
print(capitalizeWords(words)) # ['I', 'AM', 'LEARNING', 'RECURSION']

# 2nd way
def cap(words):
    result = []
    if len(words) == 0:
        return result
    result.append(words[0].upper())
    result.extend(cap(words[1:]))
    return result
words = ['i', 'am', 'learning', 'recursion']
print(cap(words)) # ['I', 'AM', 'LEARNING', 'RECURSION']