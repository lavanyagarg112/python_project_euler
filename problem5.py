prods = 1
n = 20

'''
def simplify(m,n):
        
    hcf = gcd(m,n)
    return (m/hcf, n/hcf)
'''

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)



for i in range(1, n+1):

    if prods % i != 0:
        #sim = simplify(prods, i)
        '''if gcd(prods, i) == 1:
            prods *= i
        else:
            prods *= i/gcd(prods, i)'''
        
        prods *= i/gcd(prods, i) # i/gcd is lcm
            


    

print(prods)
