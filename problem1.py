sums = 0

n = 10

for i in range(1, n):

    if i%3==0 or i%5 == 0:
        sums += i

print(sums)