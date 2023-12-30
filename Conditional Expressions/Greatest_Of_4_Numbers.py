a = input ("Enter the first number: ")
a = int (a)
b = input ("Enter the second number: ")
b = int (b)
c = input ("Enter the third number: ") 
c = int (c)
d = input ("Enter the fourth number: ")
d = int (d)

if(a>d):
    f1 = a
else:
    f1 = d

if (b>c):
     f2 = b
else:
    f2 = c 

if (f1>f2):
    print (f1," is the greatest.")
else:
    print (f2, " is the greatest.")
