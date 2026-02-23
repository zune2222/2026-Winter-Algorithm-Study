import sys
import heapq
sys.stdin.readline

N,M=map(int,input().split())

INF=float('inf')
graph=[[] for _ in range(N+1)]


for _ in range(M):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))


S,E=map(int,input().split())

def dijkstra(start):
    dist = [-INF] * (N + 1)
    q = []
    heapq.heappush(q, (-INF, start))
    dist[start] = 0

    while q:
        weight, current_node = heapq.heappop(q)
        weight*=-1

        if dist[current_node] > weight:
            continue

        for next_node, w in graph[current_node]:
            next_weight = min(weight,w)
            if next_weight > dist[next_node]:
                dist[next_node] = next_weight
                heapq.heappush(q, (-next_weight, next_node))
                
    return dist
rs=dijkstra(S)
print(rs[E])