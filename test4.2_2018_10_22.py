
    
for i in [5,4,3,2,1] :
    print(i)
print('Blastoff!')


print('Before')
for thing in [9,41,12,3,74,15]:
    print(thing)
print('After')


largest_so_far= -1
print('Before', largest_so_far)
for the_num in [9,41,12,3,74,15] :
    if the_num > largest_so_far :
        largest_so_far= the_num
    print(largest_so_far,the_num)
print('After',largest_so_far)


zork = 0
print('Before', zork)
for thing in[9,41,12,3,74,15]:
    zork = zork +1
    print(zork, thing)
print('After', zork)


zork = 0
print('Before', zork)
for thing in [9,41,12,3,74,15]:
    zork= zork + thing
    print(zork,thing)
print('After', zork)


print('before')
for value in [9, 41, 12, 3, 74, 15]:
    if value > 20:
        print('large number', value)
        print('after')


found = False
print('Before', found)
for value in[9, 41, 12, 3 ,74, 15]:
    if value == 3 :
        found = True
    print(found, value)
    print('After', found)


largest_so_far = -1
print('Before', largest_so_far)
for the_num in [9, 41, 12, 3, 74, 15]:
    if the_num > largest_so_far:
        largset_so_far= the_num
    print(largest_so_far, the_num)

print('After', largest_so_far)


smallest_so_far= -1
print('Before', smallest_so_far)
for the_num in [9, 41, 12, 3, 74, 15]:
    if the_num < smallest_so_far :
        smallest_so_far= the_num
print('After',smallest_so_far)

smallest_so_far= -1
print('Before', smallest_so_far)
for the_num in [9, 41, 12, 3, 74, 15]:
    if the_num < smallest_so_far :
        smallest_so_far= the_num
print('After',smallest_so_far)

smallest= None
print('Before')
for value in [9, 41, 12, 3, 74, 15]:
    if smallest is None:
        smallest = value
    elif value < smallest :
        smallest = value
    print(smallest, value)
print('After',smallest)


smallest= None
print('Before')
for value in [3, 41, 12, 9, 74, 15]:
    if smallest is None:
        smallest = value
    elif value < smallest :
        smallest = value
    print(smallest, value)
print('After',smallest)
