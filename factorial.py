num=int(input('enter number:'))
fact=1
for i in range(1,num+1):
    fact=fact*i
print("Factorial of {:2d} is {:3d}".format(num,fact))
