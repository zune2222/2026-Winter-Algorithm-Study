import sys
import heapq
input=sys.stdin.readline

N,K=map(int,input().split())

gems=[]

for _ in range(N):
    M,V=map(int,input().split())
    gems.append((M,V))

bags=[]

for _ in range(K):
    bags.append(int(input()))

gems.sort()
bags.sort()

result=0
temp_gems=[]

gem_idx=0

for bag_capacity in bags:
    while gem_idx < N and gems[gem_idx][0] <= bag_capacity:
        heapq.heappush(temp_gems,-gems[gem_idx][1])
        gem_idx+=1
    if temp_gems:
        result+=-heapq.heappop(temp_gems)

print(result)
