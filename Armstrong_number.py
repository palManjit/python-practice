num=int(input("enter a numebr"))
b=len(str(num))
sum =0
temp=num
while num!=0:
  r=num%10
  sum=sum+r**b
  num//=10
if sum==temp:
    print("armstrong")
else:
    print("not armstrong")
