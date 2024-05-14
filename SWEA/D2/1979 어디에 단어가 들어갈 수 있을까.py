import sys
input = sys.stdin.readline

t = int(input())

for test_case in range(1, t+1):
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    result = 0

    for i in range(n):
        answer = 0

        # 가로 검사
        for j in range(n):
            if arr[i][j] == 1:
                answer += 1
            if arr[i][j] == 0 or j == n-1:
                if answer == k:
                    result += 1
                answer = 0

        # 세로
        for j in range(n):
            if arr[j][i] == 1:
                answer += 1
            if arr[j][i] == 0 or j == n-1:
                if answer == k:
                    result += 1
                answer = 0
    print('#{} {}'.format(test_case,result))