
# decimel to binary using recursion
def dectobin(num):
    assert int(num)==num,'integers only'
    if num==0 :
        return 0
    return num%2 + 10*dectobin(int(num/2))
print(dectobin(30))
