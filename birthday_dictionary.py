birthdays = {}
birthdays["Albert Einstein"] = "03/14/1879"
birthdays["Michael Kocht"] = "02/09/1980"
birthdays["Jessica Pless"] = "15/06/1989"
birthdays["Peter Parker"] = "20/09/1970"
birthdays["Eddie Brock"] = "12/10/1988"

liSt = birthdays.keys()

print("Welcome to the birthday dictionary. We know the birthdays of: ")
    
print(birthdays.keys())
        
name = input("Who's birthday do you want to look up?")

if(name in liSt):
    print(name +  "'s birthday is"+ birthdays[name])
else:
    print("Sorry, but we don't have the name in our dictionary.")