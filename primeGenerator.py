
max=int(input("What is your max:"))
primes = [2, 3, 5]
for num in range(7, max):
    for prime in primes:
        if num % prime == 0:
            break
    else: # no break
        primes.append(num)
print(len(primes))

f = open("primes.txt", "w")
for p in primes:
    f.write(str(p)+'\n')
f.close()

        # if 0 not in [num % prime for prime in primes]:
        #     print(num, "is prime")
        #     primes.append(num)
