import sys
input=sys.stdin.readline

n=int(input())
m=int(input())

INF=float('inf')

dist=[[INF for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    a,b,c=map(int,input().split())
    dist[a][b]=min(c,dist[a][b])

for k in range(1,n+1):
    for j in range(1,n+1):
        for i in range(1,n+1):
            if i==j:
                continue
            dist[j][i]=min(dist[j][i],dist[j][k]+dist[k][i])

for i in range(1,n+1):
    for j in range(1,n+1):
        if dist[i][j]==INF:
            print(0,end=" ")
        else:
            print(dist[i][j],end=" ")
    print()