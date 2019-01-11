import math #math library
 

def mean(values):

    return sum(values)/len(values)
   
def stanDev(values):

    length = len(values)

    m = mean(values)

    total_sum = 0

    for i in range(length): 

        total_sum += (values[i]-m)**2

    return math.sqrt(total_sum/length)

x = [7,9,8,11,4]

stan_dev = stanDev(x)

print(stan_dev)
