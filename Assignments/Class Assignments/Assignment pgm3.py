#Assignment Program 3

number=list()

while(True):
    num=input("Enter a number:")

    if(num=="done"):
        print("Maximum value:",max(number),"Minimum value:",min(number))
        break
    try:
            number.append(int(num))
            
    except:
        print("\nInvalid input")

