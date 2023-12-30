Dict = { 
    "haal" : "deed",
    "acha" : "good",
    "bura" : "bad",
    "sahih" : "ok",
    "par" : "wings",
}

a = input("Enter the word you want to search: ")

meaningOfA = Dict.get(a)

print (meaningOfA)