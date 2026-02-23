import sys
input=sys.stdin.readline

n=int(input())

v1=[False]*n
v2=[False]*(2*n)
v3=[False]*(2*n)

ans=0

def dfs(row):
    global ans
    if row==n:
        ans+=1
 
    for col in range(n):
        if not v1[col] and not v2[col+row] and not v3[col-row+n]:
            v1[col]=True
            v2[col+row]=True
            v3[col-row+n]=True

            dfs(row+1)

            v1[col]=False
            v2[col+row]=False
            v3[col-row+n]=False



dfs(0)
print(ans)