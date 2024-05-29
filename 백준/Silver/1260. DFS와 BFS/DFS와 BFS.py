import sys
input = sys.stdin.readline

n, m, v = map(int, input().split())

graph = [[0] * (n+1) for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    # 무방향 그래프이기 때문에 [a][b] [b][a] 둘다 1 설정
    graph[a][b] = graph[b][a] = 1
# print(graph)

visited = [0] * (n+1)
visited2 = visited.copy()

def dfs(i):
    visited[i] = 1
    print(i, end=' ')

    for j in range(1, n+1):
        if graph[i][j] == 1 and visited[j] == 0:
            dfs(j)

def bfs(V):
    queue = [V]
    visited2[V] = 1 #방문처리
    while queue:
        V = queue.pop(0) #방문 노드 제거
        print(V, end = ' ')
        for i in range(1, n+1):
            if(visited2[i] == 0 and graph[V][i] == 1):
                queue.append(i)
                visited2[i] = 1

dfs(v)
print()
bfs(v)