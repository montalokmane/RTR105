def add (a,b):
    return a+b

fh=open("output.txt",'w')

print(add(5,6),file=fh)

fh.close()

fh=open("output.txt",'r')

print(fh.read())
