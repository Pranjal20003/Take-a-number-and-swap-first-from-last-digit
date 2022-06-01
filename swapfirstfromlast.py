a=int(input("Enter a number:"))
b=a%10
b=str(b)
c=a//1000
c=str(c)
a=a//10
d=a%100
d=str(d)
print(b+d+c)
