#Q1
# while True :
#     n=int(input("Enter a number :"))
#     if n>0 and n<101:
#         break
#     else:
#         print("Enter number between 1 to")
#         pass
# l=[]
# for i in range(1,n+1):
#     if i%3==0 and i%5==0:
#         l.append("FizzBuzz")
#     elif i%3==0:
#         l.append("Fizz")
#     elif i%5==0:
#         l.append("Buzz")
#     else:
#         l.append(i)
# print(l)

#Q2 Palindrome Number
while True:
    try:
        n=int(input("Enter Number to check Palindrome:"))
        if n>=-1000000 and n<=1000000:
            break
    except ValueError:
        pass
#Method 1
# if str(n)==str(n)[::-1]:
#     print(f"{n} is Palindrom Number")
# else :
#     print(f"{n} not an Palindrom Number")
#Method 2
l=len(str(n))
print(l)
while l>1:
    print(n,l)
    if n//(10*(l-1))==n%10:
        palindrome=True
    else:
        palindrome=False
    n%=(10*(l-1))
    print(n)
    n//=10
    print(n)
    l-=1       
if palindrome==True:
    print(n,"is a palindrome Number")
else:
    print(n,"is not a palindrome Number")
