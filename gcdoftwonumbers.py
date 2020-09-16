#Using Euclidean Algorithm
def main():
    t=input().split()
    a=int(t[0])
    b=int(t[1])
    while(b):
        a,b=b,a%b
    print(a,end="")

 # Write code here 

main()
