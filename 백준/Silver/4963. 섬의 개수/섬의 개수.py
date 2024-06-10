import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x, y):
    if x < 0 or x >= h or y < 0 or y >= w:
        return False

    if graph[x][y] == 0:
        return False

    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]

    if graph[x][y] == 1:
        graph[x][y] = 0

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True

while True:
    w,h = map(int, input().split())
    if w == 0 and h == 0:
        break
    graph = []
    for i in range(h):
        graph.append(list(map(int, input().split())))

    count = 0
    for i in range(h):
        for j in range(w):
            if dfs(i, j):
                count += 1
    print(count)