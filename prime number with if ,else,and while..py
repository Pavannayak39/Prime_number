n=int(input('enter only positive value'))
x=2

a=True

if n>0:
    while x<n:
        if n%x==0:
            a=False
            break
        else:
            a=True
            break
        x=x+1      



    if a==False:
        print("Not prime")
    else:
        print("prime")

else:
    print("Please enter valid number")



