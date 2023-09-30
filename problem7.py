
import math

def chkprime(n):

    end = math.floor(math.sqrt(n)) + 1
    for i in range(2, end):
        if n % i == 0:
            return False
    else:
        return True
    
largest = 0
len = 0
i = 2
final = 10001

while len < final:
    if i > largest and chkprime(i):
        largest = i 
        len += 1

    i += 1

print(largest)

