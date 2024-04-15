import sys
input = sys.stdin.readline

# 테스트 케이스의 수
T = int(input())

for _ in range(T):
    # H == 층, W == 방의 개수, N == 손님의 방문 순서
    H, W, N = map(int, input().split())

    # 층수
    floor = N % H
    # 방 번호
    room = (N // H) + 1

    if floor == 0:
        floor = H
        room -= 1
    print(floor * 100 + room)