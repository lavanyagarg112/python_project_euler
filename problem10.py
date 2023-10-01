# summation of primes
# sum of all primes below 2 million
# can use the eratosthenes sieve

# have to make it more efficient for it to work for 2 million

# current complexity of erathosthenes seive: O(n^2)
# required: O(nlog(log(n)))

'''end = 2000000
output = range(2,end)

j = 2
while j < end:
    if j in output:
        start = output.index(j) + 1
        output = list(output[0:start]) + list(filter(lambda x: x % j != 0, output[start:]))
    j += 1

print(sum(output))'''

# recursion depth exceeded:
# we are doing - 
# recursion O(n), membership O(n), index finding O(n), filter O(n)
# complexity: O(n^2)
'''sums = 0
end = 2000
output = range(2,end)

def seive(i, end, lst):

    if i == end:
        return 0
    else:
        if i in lst:
            start = lst.index(i) + 1
            return sum(list(lst[0:start])) + seive(i + 1, end, list(filter(lambda x: x % i != 0, lst[start:])))
        else:
            return seive(i+1, end, lst)
        

print(seive(2, end, output))'''
            
