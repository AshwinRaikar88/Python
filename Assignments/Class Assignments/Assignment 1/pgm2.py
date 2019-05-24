#Assignment Program 2

count=0
total=0
while(True):
    num=input("Enter a number:")
    if(num=="done"):
        print(total, count, (total/count))
        break
    try:
        number=int(num)
        count += 1
        total += number   
    except:
        print("\nInvalid input")
