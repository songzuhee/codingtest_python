import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
from collections import deque

def bfs(si, sj, h):
    q = deque()
    q.append((si, sj))
    v[si][sj] = 1

    while q: #q에 데이터가 있는 동안
        ci, cj = q.popleft()
        # 네방향, 범위내, 미방문, h보다 높은 경우
        for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = ci+di, cj+dj
            if 0 <= ni < n and 0 <= nj < n and v[ni][nj] == 0 and arr[ni][nj] > h:
                q.append((ni, nj))
                v[ni][nj] = 1
def solve(h): # h 높이에 대해 잠기지 않는 영역 개수 리턴
    cnt = 0
    for i in range(n): # 전체를 순회
        for j in range(n):
            if v[i][j] == 0 and arr[i][j] > h:
                bfs(i, j, h)
                cnt += 1
    return cnt

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# 최대값 찾기
ans = 0
for h in range(100): # 높이 0 ~ 99(최대) 까지 물 높이 지정
    v = [[0]*n for _ in range(n)]
    ans = max(ans, solve(h))
print(ans)