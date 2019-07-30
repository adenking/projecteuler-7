prime_numbers = []
prime = True
for i in range(2, 1000000):
    if(len(prime_numbers)) == 10001:
        break
    else:
        print(len(prime_numbers))
    prime = True
    for j in range(2, i):
        if( i % j == 0):
            prime = False
    if(prime is True):
        prime_numbers.append(i)

print(prime_numbers[10000])