from collections import deque

def solution(land):
    n = len(land)
    m = len(land[0])
    
    visited = [[False] * m for _ in range(n)]
    result = [0] * m
    
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and not visited[i][j]:
                q = deque()
                q.append((i, j))
                visited[i][j] = True
                
                count = 1
                cols_touched = {j}
                
                while q:
                    y, x = q.popleft()
                    
                    for k in range(4):
                        ny = y + dy[k]
                        nx = x + dx[k]
                        
                        if 0 <= ny < n and 0 <= nx < m:
                            if land[ny][nx] == 1 and not visited[ny][nx]:
                                visited[ny][nx] = True
                                q.append((ny, nx))
                                count += 1
                                cols_touched.add(nx)
                
                for col in cols_touched:
                    result[col] += count
                    
    return max(result)