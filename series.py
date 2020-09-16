n=int(input())
out=[]
l=[int(x) for x in input().split()]
print(l)
t=0
for i in range(0,n-1):
    if(l[i+1]-l[i]==1 and t==0):
        continue
    elif((l[i+1]-l[i]==1) and (t==1)):
        out.append(l[i+1])
        t=0
    elif((l[i+1]>l[i])or (l[i+1]<l[i])):
        out.append(l[i+1])
        t=1
for i in range(len(out)-1):
    if(out[i+1]-out[i]>6):
        print(out[i],end="")
        break
    else:
        print(out[i],end="")
