def reverse (init, n):
    if n == 0:
        return init
    else:
        return reverse(10*init + n%10, n//10)
    

def check_pal(n):

    return n == reverse(0,n)

largest_palindrome = 0

for i in range(999, 100, -1):
    for j in range(i, 100, -1):

        if i*j <= largest_palindrome:
            continue

        else:

            if check_pal(i*j):
                largest_palindrome = i*j

print(largest_palindrome)
        


