sumOfMultiples = 23
count = 10
while count < 1000:
    if count%3 == 0 or count%5 == 0:
        sumOfMultiples = sumOfMultiples + count
        count = count + 1
    else:
        count = count + 1
print (sumOfMultiples)
