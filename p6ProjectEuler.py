count = 1
count2 = 1
squareSum = 0
sumSquared = 0
number2 = 0
result = 0
for count in range(1,101):
     number2 = count*count
     squareSum += number2
     count +=1

for count in range(1,101):
     sumSquared += count

sumSquared = sumSquared*sumSquared
if sumSquared > squareSum:
     result = sumSquared - squareSum
else:
     result = squareSum - sumSquared
print (result)
