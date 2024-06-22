from collections import deque
import sys

input = sys.stdin.readline
deque = deque()
n = int(input())

for i in range(n):
    a = input().split()
    if a[0] == 'push_back':
        deque.append(int(a[1]))
    elif a[0] == 'push_front':
        deque.appendleft(int(a[1]))
    elif a[0] == 'front':
        if deque:
            print(deque[0])
        else:
            print(-1)
    elif a[0] == 'back':
        if deque:
            print(deque[-1])
        else:
            print(-1)
    elif a[0] == 'pop_front':
        if deque:
            print(deque.popleft())
        else:
            print(-1)
    elif a[0] == 'pop_back':
        if deque:
            print(deque.pop())
        else:
            print(-1)
    elif a[0] == 'size':
        print(len(deque))
    elif a[0] == 'empty':
        if deque:
            print(0)
        else:
            print(1)