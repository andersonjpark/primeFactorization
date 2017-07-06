def isPrime(number):
    '''checks whether the number is prime number of not, returns True or False'''

    for divisor in range(2,number):
        if number % divisor == 0:
            #Found a divisor
            return False

    return True

def primeListing(number):
    '''Lists N prime numbers'''
 
    if int(number) > 5000: #Raising ValueError for numbers bigger than 5000
        raise ValueError("Number {} is too big, please use a smaller number"/fomat(number))

    primeList = [2]
    candidate = 3

    while len(primeList) < int(number):
        if isPrime(candidate) == True:
            primeList.append(candidate)

        candidate +=1
    return primeList

if __name__=='__main__':
    while True:
        N = input('Number of primes to print(if none, input 0): ')

        if N == 0: #To get out of the loop
            break

        try: #For raising error
            print primeListing(N)
        except ValueError: #The error I defined for values too big.
            print "Value is too large, please use something smaller than 5000"
