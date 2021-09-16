
# Product of array using recursion
def prod(arr):
    if len(arr) == 0:
        return 1
    return arr[0] * prod(arr[1:])

print(prod([1,2,3]))

