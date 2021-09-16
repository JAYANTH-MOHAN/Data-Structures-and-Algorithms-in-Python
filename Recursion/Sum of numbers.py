
# sum of numbers using recursion
def sumofnum(n):
    if n%10==0 :
        return 0
    elif  n<0:
        raise Exception('negative numbers are not allowed')
    else :
     return n%10 + sumofnum(int(n/10))
print(sumofnum(122))
