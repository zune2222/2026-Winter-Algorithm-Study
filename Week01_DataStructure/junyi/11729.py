n=int(input())
ary=[]
cnt=0
def hanoi(n,start,mid,to):
    global cnt
    if n==1:
        ary.append((start,to))
        cnt+=1
        return
    hanoi(n-1,start,to,mid)
    ary.append((start,to))
    cnt+=1
    hanoi(n-1,mid,start,to)
hanoi(n,1,2,3)
print(cnt)
for x in ary:
    x1,x2=x
    print(x1,x2)
