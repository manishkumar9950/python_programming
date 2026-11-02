#Q1
'''while True :
    n=int(input("Enter a number :"))
    if n>0 and n<101:
        break
    else:
        print("Enter number between 1 to")
        pass
l=[]
for i in range(1,n+1):
    if i%3==0 and i%5==0:
        l.append("FizzBuzz")
    elif i%3==0:
        l.append("Fizz")
    elif i%5==0:
        l.append("Buzz")
    else:
        l.append(i)
print(l)'''

#Q2 Palindrome Number
'''while True:
    try:
        n=int(input("Enter Number to check Palindrome:"))
        if n>=-1000000 and n<=1000000:
            break
    except ValueError:
        pass
#Method 1
if str(n)==str(n)[::-1]:
    print(f"{n} is Palindrom Number")
else :
    print(f"{n} not an Palindrom Number")


#Method 2

while True:
    while True:
        try:
            n=int(input("Enter Number to check Palindrome:"))
            if n>=-1000000 and n<=1000000:
                break
        except ValueError:
            pass
    l=len(str(n))
    S,m=0,n
    for i in range(l,0,-1):
        p=m%10
        if i>1:
            S=S+p*int("1"+'0'*(i-1))
        else:
            S=S+p*1
        m//=10
        
    if S==n:
        print("True")
    else:
        print("False")
    while True:
        ch=input("enter your choice continue(check more number) or not(y/n):")
        if ch in ("y","n"):
            break
        else:
            pass
    if ch=="y":
        pass
    else:
        break'''

#Q3  Contains Duplicate
while True:
    while True:
        ch=input("You want create own list or continue with random " \
                "(Y for own and N for Random):")
        if ch.lower() in ("y","n"):
            break
        else:
            pass
    while True:
        if ch.lower()=="y":
            try:
                n=int(input('How many element you want to add in list:'))
                if n<=1 and n<=100:
                    pass
                else:
                    l=[]
                    m=[]
                    for i in range(n):
                        try:
                            element=int(input("enter element you want to add:"))
                            if element<=1000 and element>=-1000:
                                m.append(element)
                            else:
                                pass
                        except ValueError:
                            pass
                    l.append(m)    
                    break
            except ValueError:
                pass
        else:
            l=[[5, 6, 7], [4, 4], [9, 8, 7, 6, 5, 9], [1], [10, 20, 30, 40, 50, 10]]    
            break
    for l in l:
        while True:
            for i in l:
                c=l.count(i)
                t=c
                while t>1:
                    l.remove(i)
                    t-=1
                if c>1:
                    repeate=True
                    break
                else:
                    repeate=False
                    pass
            if repeate==True:
                print("True")
            else:
                print("False")
            break
    c=input("you to continue (y/n):")
    if c.lower() in ("y","n"):
        if c.lower()=="y":
            continue
        else:
            break
    else:
        pass
    
        
    
    
    
