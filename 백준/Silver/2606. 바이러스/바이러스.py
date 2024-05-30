import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[0] * (n+1) for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

visited = [0] * (n+1)

def dfs(i):
    visited[i] = 1
    for j in range(1, n+1):
        if graph[i][j] == 1 and visited[j] == 0:
            dfs(j)
    return sum(visited)-1

print(dfs(1))