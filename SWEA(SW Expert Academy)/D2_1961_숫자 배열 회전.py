# date: 2022/07/26
# author: psS2mj
# brief: SWEA_1961_숫자 배열 회전 (D2)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [0 for _ in range(N)]
    for i in range(N):
        arr[i] = list(map(int, input().split()))
    rotate90 = [[0] * N for _ in range(N)]
    rotate180 = [[0] * N for _ in range(N)]
    rotate270 = [[0] * N for _ in range(N)]

    # 90도 회전
    for i in range(N):
        for j in range(N):
            rotate90[j][N-1-i] = arr[i][j]
    # 180도 회전
    for i in range(N):
        for j in range(N):
            rotate180[j][N-1-i] = rotate90[i][j]
    # 270도 회전
    for i in range(N):
        for j in range(N):
            rotate270[j][N-1-i] = rotate180[i][j]

    print("#{}".format(tc))
    for i in range(N):
        print(*rotate90[i], sep='', end=' ')
        print(*rotate180[i], sep='', end=' ')
        print(*rotate270[i], sep='')