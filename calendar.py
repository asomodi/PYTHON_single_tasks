print("List of months: January, February, March, April, May, June, July, August, September, October, November, December")

monthName = input("Input the name of Month: ")

if(monthName == "February"):
    print("No. of days: 28/29 days")
elif(monthName in ("April", "June", "September", "November")):
    print("No. of days: 30 days")
elif(monthName in ("January", "March", "May", "July", "August", "October", "December")):
    print("No. of days: 31 days")
else:
    print("Wrong name")