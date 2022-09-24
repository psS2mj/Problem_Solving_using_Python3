# date: 2022/09/24
# author: psS2mj
# brief: BOJ_1253_좋다

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

cnt = 0
for k in range(N):
    find = arr[k]
    i = 0
    j = N-1
    while i < j:
        if arr[i] + arr[j] == find:
            if i != k and j != k:
                cnt += 1
                break
            elif i == k:
                i += 1
            elif j == k:
                j -= 1
        elif arr[i] + arr[j] < find:
            i += 1
        else:
            j -= 1
print(cnt)