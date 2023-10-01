# summation of primes
# sum of all primes below 2 million
# can use the eratosthenes sieve

# have to make it more efficient for it to work for 2 million

# current complexity of erathosthenes seive: O(n^2)
# required: O(nlog(log(n)))

end = 200000
output = range(2,end)

j = 2
while j < end:
    if j in output:
        start = output.index(j) + 1
        output = list(output[0:start]) + list(filter(lambda x: x % j != 0, output[start:]))
    j += 1

print(sum(output))