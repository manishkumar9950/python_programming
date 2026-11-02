#Q1
while True :
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
print(l)

#Q2 Palindrome Number
while True:
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
        break

#Q3  Contains Duplicate
while True:
    while True:
        ch=input("You want create own list or continue with random " \
                "(Y for own and N for Random):")
        if ch.lower() in ("y","n"):
            break
        else:
            pass
    if ch.lower()=="y":
        while True :   
            try:
                n=int(input('How many element you want to add in list:'))
                if n>=1 and n<=100:
                    len="Yes"
                    break
                else:
                    pass                    
            except ValueError:
                pass
    else:
        l=[[5, 6, 7], [4, 4], [9, 8, 7, 6, 5, 9], [1], [10, 20, 30, 40, 50, 10]]   
    while len=="Yes":
        l,count=[],1
        m=[]
        while n>0:
            try:
                element=int(input(f"enter element {count} :"))
                if element<=1000 and element>=-1000:
                    m.append(element)
                    n-=1
                    count+=1                            
                else:                                
                    pass
            except ValueError:
                pass
        l.append(m)
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

#Q4 Two Sum
while True:
    try:
        target=int(input("Enter a target Number:"))
    except ValueError:
        pass
    while True:
        ch=input("You wnat to create Own list or Continue with rondom list" \
        "(y for Own & n for random):")
        if ch.lower() in ("y","n"):
            break
        else:
            pass
    while True:
        if ch.lower()=="y":
            print("let Create Own List ")
            try:
                n=int(input("how many element want to add:"))
                if 2<=n and n<=100:
                    max="Yes"
                    break
                else:
                    pass
            except ValueError:
                pass                
        else:
            print("hy")
            l=[2,7,11,15]
            break             
    while max=="Yes":
        l,count=[],1
        while n>0:
            try:
                element=int(input(f"enter element {count} :"))
                if element<=1000 and element>=-1000:
                    n-=1
                    count+=1                            
                else:                                
                    pass
            except ValueError:
                pass
            l.append(element)
        break
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if l[i]+l[j]==target:
                print(i,j)
                break
            else:
                pass
    c=input("You want to continue(y/n):")
    if c.lower() in ("y","n"):
        if c.lower()=="y":
            pass
        else:
            break
    else:
        pass

#Q5 Best Time to Buy and Sell Stock
prices = [7, 1, 5, 3, 6, 4]
buy=prices[0]
for i in range(len(prices)):
    if buy>prices[i]:
        buy=prices[i]
    l=prices.index(buy)
    d=0
    for j in range(l+1,len(prices)):
        s=prices[j]-buy
        if s>0:
            if s>d:
                d=s
        else:
            pass
print(d)

#Q6 Roman to Integer
d={'I':1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
s='LVIII'
c=0
for i in range(len(s)):
    v=d[s[i]]
    if i+1<len(s) and v<d[s[i+1]]:
        c-=v
    else:
        c+=v
print(c)



    