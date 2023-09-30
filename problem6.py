n = 100

def sum_of_square(n):
    if n == 0:
        return 0
    else:
        return n*n + sum_of_square(n-1)
    
def sums(n):
    if n == 0:
        return 0
    else:
        return n + sums(n-1)
    
def square_of_sum(n):
    sum2 = sums(n)
    return sum2 ** 2
    
diff = square_of_sum(n) - sum_of_square(n)

print(diff)


# can just directly do formula instead