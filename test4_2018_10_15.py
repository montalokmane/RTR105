n=5
while n > 0 :
    print(n)
    n= n-1
print('Blastoff!')
print(n)

n=0
while n > 0 :
    print('Lather')
    print('Rinse')
print('Dry off!')

while True:
    line = input('>')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
    print('Done!')
    
for i in [5,4,3,2,1] :
    print(i)
print('Blastoff!')
