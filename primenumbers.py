num=int(input("enter number:"))
prime=[]
for i in range(2,num+1):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            prime.append(i)
print('prime numbers bewtween 1 and {} is {}'.format(num,prime))
