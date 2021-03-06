# 문제: N*N격자판 사과농장에서 다이아몬드 모양의 격자판만 수확하고 나머지는 새들을 위해 남겨놓을 때 수확하는 사과의 총 개수 출력

import sys
# sys.stdin = open("input.txt", 'r')
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
res = 0
s = e = n // 2 # 중간값에서 시작
for i in range(n):
    for j in range(s, e+1):
        res += a[i][j]
    if i < n//2: # 다이아몬드에서 넓어지는 구간
        s -= 1 # 시작값은 1감소 
        e += 1 # 끝값은 1증가 
    else: # 다이아몬든에서 좁혀지는 구간
        s += 1
        e -= 1
print(res)
