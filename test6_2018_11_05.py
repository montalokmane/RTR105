str1 = "Hello"
str2 = 'there'
bob = str1 + str2
print(bob)

fruit = 'banana'
letter = fruit[1]
print letter

x= 3
w= fruit[x-1]
print(w)

fruit = 'banana'
print(len(fruit))

fruit = 'banana'
index = 0
while index < len(fruit):
    letter=fruit[index]
    print(index,letter)
    index = index+1

fruit = 'banana'
for letter in fruit:
    print(letter)

index=0
while index<len(fruit):
    letter= fruit[index]
    print(letter)
    index=index+1

word= 'banana'
count= 0
for letter in word:
    if letter == 'a':
        count= count+1
print(count)

s= 'Montly Python'
print(s[0:4])
print(s[6:7])
print(s[6:20])

s= 'Monty Python'
print(s[:2])
print(s[8:])
print(s[:])

a= 'Hello'
b= a + 'There'
print(b)
c= a + ''+ 'There'
print(c)

fruit= 'banana'
'n' in fruit
'm'in fruit
'nan'in fruit
if 'a'in fruit:
    print('Found it!')


if word == 'banana':
    print('All right, bananas.')

if word < 'banana':
    print('Your word,' + word + ', comes before banana.')
elif word > 'banana':
    print('Your word,' + word + ', comes after banana.')
else:
    print('All right, bananas.')

greet = 'Hello Bob'
zap = greet.lower()
print(zap)
print(greet)
print('Hi There'.lower())

fruit= 'banana'
pos= fruit.find('na')
print(pos)
aa= fruit.find('z')
print(aa)

greet = 'Hello Bob'
nnn= greet.upper()
print(nnn)
www= greet.lower()
print(www)

greet= 'Hello Bob'
nstr= greet.replace('Bob','Jane')
print(nstr)
nstr= greet.replace('o', 'X')
print(nstr)


