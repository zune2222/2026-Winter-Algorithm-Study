import sys
from collections import deque

input = sys.stdin.readline

def solve():
    M, N = map(int, input().split())
    
    graph = []
    queue = deque()
    
    for i in range(N):
        row = list(map(int, input().split()))
        for j in range(M):
            if row[j] == 1:
                queue.append((i, j))
        graph.append(row)
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    
    max_days = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                print(-1)
                return
            max_days = max(max_days, graph[i][j])
    
    print(max_days - 1)

solve()