#Assignment Program 6
try:
    hours=input("Enter Hours: ")
    hrs=float(hours)    
    rate=input("Enter Rate: ")
    rte=float(rate)

    grosspay=hrs*rte
    print("\nGrosspay:",grosspay)
    
except:
    print("Error, please enter numeric input")
