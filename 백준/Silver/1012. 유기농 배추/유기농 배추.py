import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

def dfs(x, y):
    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < m and 0 <= ny < n and graph[ny][nx] == 1:
            graph[ny][nx] = -1
            dfs(nx, ny)
t = int(input())

for _ in range(t):
    # 가로, 세로, 배추의 위치
    m, n, k = map(int, input().split())
    graph = [[0 for _ in range(m)] for _ in range(n)]

    for _ in range(k):
        a, b = map(int, input().split())
        graph[b][a] = 1

    count = 0
    for a in range(m):
        for b in range(n):
            if graph[b][a] == 1:
                dfs(a, b)
                count += 1
    print(count)