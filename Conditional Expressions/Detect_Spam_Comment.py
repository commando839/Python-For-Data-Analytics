a = ["make a lot of money", "buy now", "subscribe this", "click this"]
b = input("Enter the text here to check: ")

if ("make a lot of money" in b):
    print ("This is spam.")
elif("buy now" in b):
    print("This is a spam.")
elif("subscribe this" in b):
    print("This is a spam.")
elif("click this" in b):
    print("This is a spam.")    
else:
    print ("This is not a spam.")