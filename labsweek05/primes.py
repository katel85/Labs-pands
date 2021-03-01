# getting prime numbers from a range
# Catherine Leddy
primes =[]
upto = 100000

for candidate in range(2, upto):
    #print (candidate)
    isprime=True
    #for divisor in range (2, candidate) :
    for divisor in primes: # if divisable by an int then it is not a prime number
        if (candidate % divisor ==0):
            isprime=False # so there is no reason to keep checking 
            break

    if isprime:
        primes.append(candidate)
print (primes)






