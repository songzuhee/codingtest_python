import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

n = int(input())
a, b = map(int, input().split())

# 촌수 관계의 개수
m = int(input())
graph = [[] for _ in range(n+1)]
arr = []
visited = [0] * (n+1)

def dfs(s, num):
    num += 1
    # 방문 처리
    visited[s] = 1

    if s == b:
        arr.append(num)

    for i in graph[s]:
        if not visited[i]:
            dfs(i, num)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

dfs(a, 0)
if len(arr) == 0:
    print(-1)
else:
    print(arr[0]-1)