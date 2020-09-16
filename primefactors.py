num=int(input("enter number:"))
t=num
d=2
prime=[]
while num>1:
    if num%d==0:
        prime.append(d)
        num=num/d
        continue
    d=d+1
print("prime foactors for {} is {}".format(t,prime))
