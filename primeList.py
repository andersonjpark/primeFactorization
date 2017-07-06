def primeListing(number):
	#list the prime number 

	primeList = [2]
	candidate = 3

	while len(primeList) < int(number):
		found = False
		for divisor in range(2,candidate):
			if candidate % divisor == 0:
				found = True # Found a divisor
				break

		if found == False:
			primeList.append(candidate)

		candidate = candidate + 1
if __name__ == "__main__":
	N = raw_input('Number of primes to print?')


