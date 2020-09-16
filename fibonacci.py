num=int(input('enter number:'))
a,b=0,0
fibo=[]
while b<num:
    fibo.append(b)
    a,b=b,a+b
print("fibonacci of {} is {}".format(num,fibo))
