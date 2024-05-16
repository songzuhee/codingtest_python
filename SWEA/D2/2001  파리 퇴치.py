import sys
input = sys.stdin.readline

t = int(input())

for test_case in range(1, t+1):
    n, m = map(int, input().split())
    arr = []

    # 2차원 배열 데이터 입력 받기
    for i in range(n):
        arr.append(list(map(int, input().split())))

    a = 0
    for i in range(n-m+1):
        for j in range(n-m+1):
            max_num = 0
            for k in range(m):
                for l in range(m):
                    max_num += arr[i+k][j+l]
            if max_num > a:
                a = max_num

    print('#{} {}'.format(test_case, a))

