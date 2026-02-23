import sys
import heapq

INF = float('inf')
input = sys.stdin.readline

N, E = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

def dijkstra(start):
    dist = [INF] * (N + 1)
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0

    while q:
        weight, current_node = heapq.heappop(q)
        
        if dist[current_node] < weight:
            continue

        for next_node, w in graph[current_node]:
            next_weight = weight + w
            
            if next_weight < dist[next_node]:
                dist[next_node] = next_weight
                heapq.heappush(q, (next_weight, next_node))
                
    return dist

dist_from_1 = dijkstra(1)
dist_from_v1 = dijkstra(v1)
dist_from_v2 = dijkstra(v2)

path_a = dist_from_1[v1] + dist_from_v1[v2] + dist_from_v2[N]

path_b = dist_from_1[v2] + dist_from_v2[v1] + dist_from_v1[N]

answer = min(path_a, path_b)
if answer >= INF:
    print(-1)
else:
    print(answer)