#This program will only greet the person whose name starts with an "S".

name = str(input("Enter the name: ")) 

if name.startswith ("S"):
    print ("Greetings, " + name + "!")
else:
    print ("Try again!!")