import time


def collatz(x):
    results = []
    while x != 1:
        results.append(x)
        if x % 2 == 0:
            x /= 2
        else:
            x *= 3
            x += 1
    return results


longest = (0, 0)
start_time = time.time()
for i in range(1, 1000000):
    result = collatz(i)
    if len(result) > longest[1]:
        longest = (i, len(result))
print(longest)
print('Total Time: ' + str(time.time() - start_time))
