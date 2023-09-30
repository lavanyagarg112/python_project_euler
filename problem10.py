# summation of primes
# sum of all primes below 2 million
# can use the eratosthenes sieve

# have to make it more efficient for it to work for 2 million

end = 30
output = range(2,end)

for i in range(2, end):
    output = list(filter(lambda x: x == i or x % i != 0, output))


print(sum(output))