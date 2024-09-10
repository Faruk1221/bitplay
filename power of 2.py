number= int (input("input a number"))
if number==0:
    print("number is 0 hence not a power of 2")
if (number & (~(number-1)))==number:
    print("number is power of 2")
else:
    print("number is not a power of 2")