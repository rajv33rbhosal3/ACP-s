def P8(n):
    if n == 0:
        return False
    else:
        while n%8 == 0:
            n = n/8
    return n==1
n = int(input("Enter a number : "))
if P8(n):
    print("Number is power of 8")
else:
    print("Numebr is not the power of ")
