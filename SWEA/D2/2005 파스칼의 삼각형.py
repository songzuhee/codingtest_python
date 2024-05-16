import sys
input = sys.stdin.readline

t = int(input())

for _ in range(1, t+1):
    n = int(input())
    arr = [[0]*n for _ in range(n)]

    for i in range(n):
        # 열의 크기는 행의 인덱스 +1
        for j in range(i+1):
            if i == j or j == 0:
                arr[i][j] = 1
            else:
                arr[i][j] = arr[i-1][j-1] + arr[i-1][j]

    print('#{}'.format(t))

    for i in arr:
        for j in i:
            if j != 0:
                print(j, end=' ')
        print()




