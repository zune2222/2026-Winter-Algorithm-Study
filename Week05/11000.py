import sys
import heapq

input=sys.stdin.readline

lectures=[]

N=int(input())

for _ in range(N):
    S,T=map(int,input().split())
    lectures.append((S,T))


lectures.sort()
pq=[]

heapq.heappush(pq,lectures[0][1])

for i in range(1,N):
    start,end=lectures[i]
    if start >=pq[0]:
        heapq.heappop(pq)
    heapq.heappush(pq,end)


print(len(pq))