def square (l):
    area = l*l
    return area

def rectangle(l,w):
    area=l*w
    return area

print("Please enter shape form")
print("Square = 1")
print("Rectangle = 2")
print("========")

user_input = 0
while user_input not in (1,2) :
    user_input = int(input("Enter your choices:"))

if (user_input == 1):
    print("Area of square")
    length= int(input("Enter length of square: "))
    area = square(length)
    print("Area of square is :", area)

if (user_input == 2):
    print("Area of rectangle")
    length= int(input("Enter length of rectagle: "))
    width= int(input("Enter width: "))
    area = rectangle(length,width)
    print("Area of square is :", area)
                
    
