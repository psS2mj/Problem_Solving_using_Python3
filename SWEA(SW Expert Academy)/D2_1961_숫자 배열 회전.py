# date: 2022/07/26
# author: psS2mj
# brief: SWEA_1961_숫자 배열 회전 (D2)

def rotate(arr, N):
    new_arr = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_arr[j][N-1-i] = arr[i][j]
    return new_arr

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [0 for _ in range(N)]
    for i in range(N):
        arr[i] = list(map(int, input().split()))

    rotate90 = rotate(arr, N)
    rotate180 = rotate(rotate90, N)
    rotate270 = rotate(rotate180, N)

    print("#{}".format(tc))
    for i in range(N):
        print(*rotate90[i], sep='', end=' ')
        print(*rotate180[i], sep='', end=' ')
        print(*rotate270[i], sep='')