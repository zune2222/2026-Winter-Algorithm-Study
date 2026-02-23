import sys
input=sys.stdin.readline

N,S=map(int,input().split())
ary=list(map(int,input().split()))


dp=[(0,0) for _ in range(N)]
start_point=0
dp[0]=(ary[0],1)

rs=float('inf')
if ary[0]>=S:
    rs=min(rs,dp[0][1])
for i in range(1,N):
    value,count=dp[i-1]
    dp[i]=(value+ary[i],count+1)
    while dp[i][0]>S and start_point<=i and dp[i][0]-ary[start_point]>=S:
        dp[i]=(dp[i][0]-ary[start_point],dp[i][1]-1)
        start_point+=1
    if dp[i][0]>=S:
        rs=min(rs,dp[i][1])

if rs==float('inf'):
    print(0)
else:
    print(rs)
