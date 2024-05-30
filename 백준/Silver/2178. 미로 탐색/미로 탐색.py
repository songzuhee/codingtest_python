import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

graph = []

for i in range(n):
    graph.append(list(map(int, input().rstrip())))
# print(graph)

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()
        for i in range(4): # 상하좌우 네 방향으로 이동 시도
            nx = x + dx[i]
            ny = y + dy[i]

            # 새로운 좌표가 유효한 범위 내에 있고, 아직 방문하지 않은 노드(값이 1인 경우)
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = graph[x][y]+1
    return graph[n-1][m-1]

print(bfs(0,0))