# Pay computation

def computepay(hours,rate):
    if hours >= 40:
        pay=(hours*rate)+(rate*2.5)
    else:
        pay=hours*rate
    return pay

hours=input("Enter Hours: ")
rate=input("Enter Rate: ")

hrs=float(hours)
rte=float(rate)

print("\nPay: ",computepay(hrs,rte))