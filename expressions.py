x=2

y=x-8
print(y)

s= x*12
print(s)


a=x/5
print(a)

k=x**5
print(k)

t=x%5
print(t)


count = 0
for itervar in [3, 41, 12, 9, 74, 15]:
    count = count + 1
print('Count: ', count)

largest = None
print('Before:', largest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if largest is None or itervar > largest :
        largest = itervar
    print('Loop:', itervar, largest)
print('Largest:', largest)
