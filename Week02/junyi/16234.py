import sys
from collections import deque

input = sys.stdin.readline

def solve():
    N, L, R = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    def bfs(x, y, visited):
        queue = deque([(x, y)])
        visited[x][y] = True
        
        union = [(x, y)]
        total_population = graph[x][y]
        
        while queue:
            cx, cy = queue.popleft()
            
            for i in range(4):
                nx, ny = cx + dx[i], cy + dy[i]
                
                if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                    diff = abs(graph[cx][cy] - graph[nx][ny])
                    
                    if L <= diff <= R:
                        visited[nx][ny] = True
                        queue.append((nx, ny))
                        union.append((nx, ny))
                        total_population += graph[nx][ny]
        
        return union, total_population

    days = 0
    
    while True:
        visited = [[False] * N for _ in range(N)]
        is_moved = False 
        
        for i in range(N):
            for j in range(N):
                if not visited[i][j]:
                    union, total_pop = bfs(i, j, visited)
                    
                    if len(union) > 1:
                        is_moved = True
                        new_pop = total_pop // len(union)
                        
                        for ux, uy in union:
                            graph[ux][uy] = new_pop
        
        if not is_moved:
            break
            
        days += 1
        
    print(days)

solve()