import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
ary = [list(map(int, list(input().strip()))) for _ in range(n)]

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]

def bfs():
    q = deque()
    q.append((0, 0, 1))
    visited[0][0][1] = 1

    while q:
        y, x, b = q.popleft()

        if y == n - 1 and x == m - 1:
            return visited[y][x][b]

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < m:
                if ary[ny][nx] == 1 and b == 1:
                    visited[ny][nx][0] = visited[y][x][1] + 1
                    q.append((ny, nx, 0))
                elif ary[ny][nx] == 0 and visited[ny][nx][b] == 0:
                    visited[ny][nx][b] = visited[y][x][b] + 1
                    q.append((ny, nx, b))

    return -1

print(bfs())