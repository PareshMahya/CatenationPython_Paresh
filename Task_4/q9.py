
# 9. Write a function called showNumbers that takes a parameter called limit. 
# It should print all the numbers between 0 and limit with a label to identify the even and odd numbers. 
# Sample input: show Numbers(3) (where limit=3) 
# Expected output:
# 0 EVEN 
# 1 ODD 
# 2 EVEN 
# 3 ODD

def showNumbers(x):
    for i in range(x+1):
        if i%2==0:
            print(i, "EVEN")
        elif i%2!=0:
            print(i, "ODD")
q9 = int(input("Enter your limit for even-odd number :"))
showNumbers(q9)
