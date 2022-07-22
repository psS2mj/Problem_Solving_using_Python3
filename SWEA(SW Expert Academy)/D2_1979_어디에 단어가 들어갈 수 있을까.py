# date: 2022/07/23
# author: psS2mj
# brief: SWEA_1979_어디에 단어가 들어갈 수 있을까 (D2)

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [0 for _ in range(N)]
    for i in range(N):
        arr[i] = list(map(int, input().split()))
    answer = 0

    # 가로 체크
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[i][j] == 1:
                cnt += 1
            elif arr[i][j] == 0:
                if cnt == K:
                    answer += 1
                    cnt = 0
                else:
                    cnt = 0
            if j == N-1:
                if cnt == K:
                    answer += 1
            # print("arr[{}][{}] 값: {} cnt: {}, answer: {}".format(i, j, arr[i][j], cnt, answer))

    # 세로 체크
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[j][i] == 1:
                cnt += 1
            elif arr[j][i] == 0:
                if cnt == K:
                    answer += 1
                    cnt = 0
                else:
                    cnt = 0
            if j == N-1:
                if cnt == K:
                    answer += 1
            # print("arr[{}][{}] 값: {} cnt: {}, answer: {}".format(j, i, arr[j][i], cnt, answer))

    print("#{} {}".format(tc, answer))
