cnt = 0
def dfs(i, result, numbers, target):
    global cnt
    if i == len(numbers):
        if target == result:
            cnt += 1
            return
    else:
        dfs(i+1, result+numbers[i], numbers, target)
        dfs(i+1, result-numbers[i], numbers, target)
        
def solution(numbers, target):
    result = 0
    dfs(0, result, numbers,target)
    return cnt