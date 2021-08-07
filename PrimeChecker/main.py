def prime_checker(number):
    divs = []
    counter = 0
    for x in range(2, number + 1):
        for i in range(1, x + 1):
            if x % i == 0:
                divs.append(i)
        if len(divs) >= 3:
            #print(f"{x} is not prime.")
            divs = []
        else:
            print(f"{x} is a prime.")
            counter += 1
            divs = []
    print(f"There are {counter} number of primes between 2 and {number}")
    
n = int(input("Check up to this number: "))

prime_checker(number=n)