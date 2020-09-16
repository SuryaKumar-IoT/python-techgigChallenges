''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
    n=int(input())
    temp=n
    g=n
    order=0
    count=0
    while n!=0:
        n=int(n/10)
        if n==0:
            order=order+1
            break
        else:
            order=order+1
    while temp!=0:
        t=temp%10
        temp=int(temp/10)
        count=count+pow(t,order)
    print(count==g,end="")

 # Write code here 

main()

