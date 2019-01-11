from random import random
# seed random number generator
seed(1)
# generate some random numbers
print(random(), random(), random())
# reset the seed
seed(1)
# generate some random numbers
print(random(), random(), random())




--------------------------------------------------------------

from random import seed
from random import randint
# seed random number generator
seed(1)
# generate some integers
for _ in range(10):
	value = randint(0, 10)
	print(value)
