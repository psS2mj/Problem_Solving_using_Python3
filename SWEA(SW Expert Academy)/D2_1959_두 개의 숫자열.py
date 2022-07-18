# date: 2022/07/18
# author: psS2mj
# brief: SWEA_1959_두 개의 숫자열 (D2)

def calculate(size, long, short):
    for i in range(size):  # 긴 쪽 시작 인덱스 지정
        for j in range(len(short)):  # 짧은 쪽 길이 만큼 곱셈 연산
            result[i] += short[j] * long[i+j]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))

    size = max(N, M) - min(N, M) + 1
    result = [0] * size
    if len(arr1) >= len(arr2):
        calculate(size, arr1, arr2)
    else:
        calculate(size, arr2, arr1)

    print("#{} {}".format(tc, max(result)))