import sys
import heapq

input=sys.stdin.readline

N=int(input())
arr=[]
for _ in range(N):
    p,d=map(int,input().split())
    arr.append((d,p))
arr.sort()
rs=0
day=1

q=[]
for x in arr:
    d,v=x
    heapq.heappush(q,v)
    if len(q) > d:
        heapq.heappop(q)

print(sum(q))