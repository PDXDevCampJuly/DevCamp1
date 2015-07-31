# find prime factors of a number

numFactor = int(input("Please enter an integer of your choosing. >> "))
#print(numFactor)
#ie 60.. it prints 60
def primefactors(numFactor):
    factorlist = []
    loop = 2
    while loop <= numFactor:
        if numFactor % loop == 0:
            numFactor /= loop
            factorlist.append(loop)
        else:
            loop += 1

    return factorlist

    unique = []
    for factor in factorlist:
        if factor not in unique:
            unique.append(factor)

    return unique

#  i = [i**(x+1) for x in range(factorlist[i])]


print(numFactor)
print(primefactors(numFactor))

#ie.. it prints  2, 2, 3, 5
##print prettier  ie: 60 = 2 ^ 2 * 3 * 5
