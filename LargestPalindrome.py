product = 0
numOne = 0
numTwo = 0
for numOne in range(999, 100, -1):
    for numTwo in range(numOne, 100, -1):
        x = numOne * numTwo
        if x > product:
            xS = str(numOne * numTwo)
            if xS == xS[::-1]:
                 product = numOne*numTwo
print (product)