
# power of numbers using recursion
def power(base,exp):
    if exp==0:
        return 1
    elif exp<0:
        raise ValueError("exp cant be negative")
    else:
        return base*power(base,exp-1)
print(power(-2.2,2))

