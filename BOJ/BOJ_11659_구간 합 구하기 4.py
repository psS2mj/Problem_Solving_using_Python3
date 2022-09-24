# date: 2022/09/23
# author: psS2mj
# brief: BOJ_11659_구간 합 구하기 4

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
S = [0]
temp = 0

for i in arr:
    temp += i
    S.append(temp)

for i in range(M):
    s, e = map(int, input().split())
    print(S[e] - S[s-1])