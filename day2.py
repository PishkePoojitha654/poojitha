a=int(input("enter a number"))
if a<=1:
    print("not prime")
else:
    for i in range(2,a):
        a % i==0
        print("not prime")
        break
    else:
        print("prime")