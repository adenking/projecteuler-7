import math

prime_numbers = []
prime = True
for i in range(2, 1000000):
    if(len(prime_numbers)) == 10001:
        break
    else:
        print(len(prime_numbers))
    prime = True
    for j in range(2, max(int(math.sqrt(i)), min(i, 5))):
        if i % j == 0:
            prime = False
    if prime is True:
        prime_numbers.append(i)

print(prime_numbers[10000])
