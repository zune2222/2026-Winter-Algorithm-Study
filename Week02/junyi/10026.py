import sys
from collections import deque

input = sys.stdin.readline

def bfs(x, y):
    q.append((x, y))
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == graph[x][y] and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    q.append((nx, ny))

n = int(input())
graph = [list(input().rstrip()) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
q = deque()

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

cnt1 = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            cnt1 += 1

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'

visited = [[0] * n for _ in range(n)]
cnt2 = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            cnt2 += 1

print(cnt1, cnt2)