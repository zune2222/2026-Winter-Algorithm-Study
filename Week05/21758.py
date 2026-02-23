import sys 
input=sys.stdin.readline

N=int(input())

ary=list(map(int,input().split()))

st=[0]*N
ed=[0]*N
rs=0
ary_sum=sum(ary)
st[0]=ary_sum-ary[0]
for i in range(1,N):
    st[i]=st[i-1]-ary[i]

for i in range(j,0,-1):
    ed[i]=st[i]-ary[i]
    rs=max(rs,(max(st)+max(ed)))
print(rs)