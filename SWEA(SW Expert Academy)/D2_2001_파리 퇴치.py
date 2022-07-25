# date: 2022/07/25
# author: psS2mj
# brief: SWEA_2001_파리 퇴치 (D2)

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [0 for _ in range(N)]
    for i in range(N):
        arr[i] = list(map(int, input().split()))

    result = []
    for i in range(N-M+1):
        temp = 0
        for j in range(N-M+1):
            for m in range(M):
                for n in range(M):
                    temp += arr[i+m][j+n]
                    # print("arr[{}][{}]: {}, 연산 후 temp: {}".format(i+m, j+n, arr[i+m][j+n], temp))
            result.append(temp)
            temp = 0

    print("#{} {}".format(tc, max(result)))