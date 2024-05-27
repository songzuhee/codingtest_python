def dfs(graph, v, visited):

    # v는 시작 위치
    # visited -> 방문 테이블, 시작위치는 방문했으니까 visited[v]
    visited[v] = True
    print(v, end=' ')

    # 현재 노드와 연결된 노드를 재귀적으로 호출
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
graph = [
    [],
    [2, 3, 7],
    [1, 4, 6],
    [1, 5, 7],
    [2, 6],
    [3, 7],
    [2, 4],
    [1, 3]
]

visited = [False] * 9

print("방문순서")
dfs(graph, 1, visited)