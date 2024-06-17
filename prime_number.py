num=int(input("enter a number"))
flag=0
if num > 1:
  for i in range(2, int(num**0.5) + 1):
    if num%i==0:
      flag=1
      break
  if flag==0:
      print("prime")
  else:
      print("not prime")
else:
     print("not prime")
