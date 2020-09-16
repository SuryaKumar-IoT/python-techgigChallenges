def main():
    series = int(input())
    a=0
    b=1
    for i in range(series):
        print(a, end= " ")
        a,b=b,a+b
main()
