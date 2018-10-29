print('Hello')
big = max('Hello world')
print(big)
tiny = min('Hello world')
print(tiny)
big= max('Hello world')
print(big)

print(float(99)/100)
i=42
type(i)
f = float(i)
print(f)
type(f)
print(1+2*float(3)/4-5) 

def print_lyrics():
    print('I sleep all night and I work all day.')

x= 5
print('Hello')

def print_lyrics():
    print('I sleep all night and I work all day.')

print('yo')
x= x+2
print(x)

x= 5
print('Hello')
def print_lyrics():
    print('I sleep all night and I work all day.')
print('yo')
print_lyrics()
x=x+2
print(x)

def greet(lang):
    if lang == 'es':
        print('Hola')
    elif lang == 'fr':
        print('Bonjour')
    else:
        print('Hello')
greet('en')
greet('es')
greet('fr')

def greet():
    return " Hello"
print(greet(),'Glenn')
print(greet(),'Sally')

def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'
print(greet('en'),'Glenn')
print(greet('es'), 'Sally')
print(greet('fr'),'Michael')

def addtwo(a,b):
    added = a + b
    return added
x= addtwo(3,5)
print(x)
