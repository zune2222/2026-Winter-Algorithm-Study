import sys
import heapq
input=sys.stdin.readline

V,E=map(int,input().split())

K=int(input())

ary=[[] for _ in range(V+1)]

INF=float('inf')
dist=[INF for _ in range(V+1)]

for i in range(E):
    u,v,w=map(int,input().split())
    ary[u].append((v,w))



def dk(start):
    q=[]
    heapq.heappush(q,(0,start))
    dist[start]=0
    while q:
        w,v=heapq.heappop(q)

        if dist[v]<w:
            continue

        for next,weight in ary[v]:
            if weight+w < dist[next]:
                dist[next]=weight+w
                heapq.heappush(q,(weight+w,next))
dk(K)

for i in range(1,V+1):
    if dist[i]==INF:
        print("INF")
    else:
        print(dist[i])



