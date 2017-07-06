def allPrimesLessThan(N):
    '''Input: Integer N
       Output: A list of all primes less than N

       e.g. allPrimesLessThan(12) returns [2,3,5,7,11]

       Input values bigger than 5000 raise an error.'''

    if int(N) > 50000: # Raising ValueError for numbers bigger than 5000
        raise ValueError("Number {} is too big, please use something under 50000".format(N))

    primeList = []
    candidate = 2
    while (candidate < N):
    
        #counts the number of divisors of candidate

        foundDivisor = False
        for divisor in range(2,candidate):
            if candidate % divisor == 0:
                foundDivisor = True #divisor found, not a prime number
                break # don't check anymore, one divisor is enough
            
        if not foundDivisor: # aka if foundDivisor is False
            primeList.append(candidate)
        candidate +=1 

    return primeList

def divideByPrimeUnder(N):
    '''
    Input: Integer N
    
    Output: A list of all primes that can divide N

    e.g. divideByPrimeUnder(12) returns [2,2,3].'''

    divisionList = []

    primeList = allPrimesLessThan(N)

    for divisor in primeList:

        if N % divisor ==0:
            
            while N % divisor == 0:
                # start of the loop to check how many same divisors are in N
                divisionList.append(divisor) 
                N = N / divisor # then we make a new N to see if it can be divided by the same
                                #number that was just appended

    return divisionList

def myCount(N):
    
    '''
    Input: Integer N

    Output: A data table of p and exponenet.
    (p is the prime divisor and exponent shows how many times p can divide N)

    e.g. print myCount(12)
    p    exponent
    -------------
        2       2
        3       1

    Use print myCount() to cleanly get the result'''

    dL = divideByPrimeUnder(N)

    s = '' 
    if dL == []: #when N is a primeNumber
        s = s + '{:4s} {:8s}\n'.format('p','exponent')
        s = s + '-'*13 + '\n' #\n makes sure that the new line is made
        s = s + '{:4d} {:8d}'.format(N,1)
        return s

    s = '{:4s} {:8s}\n'.format('p','exponent')
    s = s + '-'*13 + '\n'
    for d in set(dL): #getting the divisor from the divisionList
        s = s + '{:4d} {:8d}\n'.format(d,dL.count(d))
        #from divisionList, counts how many same 'd' is in the list and displays the result
    return s

if __name__ == "__main__": 

    listOfFns = [allPrimesLessThan,divideByPrimeUnder,myCount] 

    descriptions = ["""\t Gives a list of all primes that are less than or equal to its input""",
                    """\t Gives a list of all primes that divide the input""",
                    """\t Returns a nicely formatted table of the prime factorization of the input"""]
    while True:
        my_number = input("What integer do you want me to factorize? (If none, input 0): ")

        if int(my_number) == 0: 
            break 

        for index,fn in enumerate(listOfFns):
            
            print "Option {}: Apply {}".format(index,fn.__name__)
            print "           {}".format(descriptions[index])
            print ""

        print "Option 3: Quit"

        option = input("Please enter your option: ")
        if option == 3: 
                break

        try:
            print listOfFns[option](my_number)
        except ValueError: 
            print "Number {} is too big, please use something under 50000".format(my_number)
