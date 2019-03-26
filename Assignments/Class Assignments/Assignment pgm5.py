#Assignment Program 5

scr=input("Enter your score:")
score=float(scr)

if(score >= 0.0) and (score <=1.0):
    if score >= .9:
        print("Grade: A")
    elif score >= .8:
        print("Grade: B")
    elif score >= .7:
        print("Grade: C")
    elif score >= .6:
        print("Grade: D")
    else:
        print("Grade: F")
else:
    print("Enter a score between 0.0 to 1.0")