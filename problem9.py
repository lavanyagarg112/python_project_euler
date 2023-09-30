import time

def factorial(n):
    if n == 1:
        return 1 
    else:
        return n * factorial(n-1)
    

start = time.time()
    
print(factorial(20))

end = time.time()

print(end - start)