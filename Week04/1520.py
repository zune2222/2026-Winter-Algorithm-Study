import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

m, n = map(int, input().split())
ary = [list(map(int, input().split())) for _ in range(m)]

dp = [[-1] * n for _ in range(m)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(y, x):
    if y == m - 1 and x == n - 1:
        return 1
    
    if dp[y][x] != -1:
        return dp[y][x]
    
    dp[y][x] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < n and 0 <= ny < m and ary[ny][nx] < ary[y][x]:
            dp[y][x] += dfs(ny, nx)
    
    return dp[y][x]

print(dfs(0, 0))