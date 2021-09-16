
#is palindrome using recursion
def ispal(name):
    if len(name)==0:
        return True
    if name[0]!=name[-1]:
        return False
    return ispal(name[1:-1])

print(ispal('awesome')) # false
print(ispal('tacocat')) # true
