# largest prime factor

'''
def check_prime(n):

    for i in range(2,n//2 + 1):
        if n % i == 0:
            return False
        
    else:
        return True
    

n = 600851475143
 
for i in range(n,1,-1):
    if n%i == 0 and check_prime(i):
        print('largest prime factor: ', i)
        break
'''

# overflow of stack in above so it doesnt work ^

# recursion depth exceeds in below so doesnt work:

'''
def largest_prime(num, divisor, largest):

    if num <= 1:
        return largest
    
    elif num % divisor == 0:
        return largest_prime(num / divisor, divisor, divisor)
    
    else:
        return largest_prime(num, divisor + 1, largest)
    
n = 600851475143

print(largest_prime(n, 2, 1))'''

 