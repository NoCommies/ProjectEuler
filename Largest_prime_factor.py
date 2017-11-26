
def is_prime(a):
    return all(a % i for i in range(2, a))
Number = 600851475143
counter = 1
pf = 1
lpf = 1
Remainder = False
while counter < Number:
    if is_prime(counter):
        pf = counter
        if Number%pf == 0:
            if pf > lpf:
                lpf = pf
    counter += 1
    print ("Current lpf: ", lpf)
print (lpf)
