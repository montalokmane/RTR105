x= 5
if x < 10:
    print('Smaller')
if x > 20:
    print('g')
x = 5
if x == 5 :
    print('Equals 5')
if x > 4 :
    print('Grater than 4')
if x >= 5 :
    print('Greater than or Equals 5')
if x < 6 : print('Less than 6')
if x <= 5 :
    print('Less than or Equals 5')
if x != 6:
    print ('Not equal 6')

astr = 'hello bob'
try:
    istr = int(astr)
except:
    istr = -1
print ('First',istr)
