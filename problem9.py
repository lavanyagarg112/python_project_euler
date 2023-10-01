# pythagorean triplet
# exactly one pythagorean triplet where a + b + c = 1000
# find a,b,c

# can find all combination of a,b,c which add up to give 1000
# check if any of them are pythagorean triplets


# a + b + c = 1000
# natural numbers
# least value of a,b,c = 1 implies most is 998 (since none can be 0)
# iterate from 1 to 998 and 1 to 998 for a,b
# c = 1000 - (a + b)
# if c is also between 1 and 998, then one possible combination of a,b,c is found
# can try storing in sets to avoid repitition 
# then check each for pythagorean triplet

import time

def check_pyth (a,b,c):

    if a**2 + b**2 == c**2:
        return True
    else:
        return False
    
s = set()

start = time.time()

for a in range(1, 999, 2): # make this odd

    for b in range(2, 999, 2): # make this even

        c = 1000 - (a + b)
        if c in range(1, 999, 2): # make this odd
            if a % 3 == 0 or b % 3 == 0:
                if b % 4 == 0: # a is odd so cannot be divisible by 4 anyway
                    if a % 5 == 0 or b % 5 == 0 or c % 5 == 0:
                        s.add((a,b,c))

print(s)

for i in s:

    if check_pyth(i[0],i[1],i[2]):
        print('a:', i[0])
        print('b:', i[1])
        print('c:', i[2])
        print('product:', i[0]*i[1]*i[2])
        break

end = time.time()

print('time taken: ', end-start)
