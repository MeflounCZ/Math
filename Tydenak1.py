import itertools

woutreps = ["".join(item) for item in itertools.permutations("0234678", 4)]
result1 = []
for i in woutreps:
    if i[0] != '0':
        if int(i)%3 == 0:
            result1.append(i)


wreps = ["".join(item) for item in itertools.product("0234678", repeat=4)]
result2 = []
for i in wreps:
    if i[0] != '0':
        if int(i)%3 == 0:
            result2.append(i)
            
            
print (result1)
print ('\n')
print (len(result1))
print ('\n')
print ('\n')
print (result2)
print ('\n')
print (len(result2))
