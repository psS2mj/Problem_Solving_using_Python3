# date: 2022/07/26
# author: psS2mj
# brief: SWEA_1974_스도쿠 검증 (D2)

T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    temp = [0] * 9
    answer = 1

    # 1단계: 행 검증
    for i in range(9):
        temp = [0] * 9
        for j in range(9):
            temp[arr[i][j]-1] += 1
            # print("행 검증: {}번째 행 {}번째 원소 => temp: {}".format(i+1, j+1, temp))
        if temp.count(1) != 9:
            answer = 0
            break

    # 2단계: 열 검증
    if answer == 1:
        for i in range(9):
            temp = [0] * 9
            for j in range(9):
                temp[arr[j][i]-1] += 1
                # print("열 검증: {}번째 열 {}번째 원소 => temp: {}".format(i+1, j+1, temp))
            if temp.count(1) != 9:
                answer = 0
                break

    # 3단계: 3*3 검증
    if answer == 1:  # 1,4,6번째 칸 (왼쪽)
        temp = [0] * 9
        for i in range(9):
            for j in range(3):
                temp[arr[i][j]-1] += 1
                # print("3*3 검증: arr[{}][{}] 원소 => temp: {}".format(i, j, temp))
            if i in [2, 5, 8]:
                if temp.count(1) != 9:
                    answer = 0
                    break
                else:
                    temp = [0] * 9
    if answer == 1:  # 2,5,7번째 칸 (가운데)
        temp = [0] * 9
        for i in range(9):
            for j in range(3):
                temp[arr[i][3+j]-1] += 1
            if i in [2, 5, 8]:
                if temp.count(1) != 9:
                    answer = 0
                    break
                else:
                    temp = [0] * 9
    if answer == 1:  # 3,6,9번째 칸 (오른쪽)
        temp = [0] * 9
        for i in range(9):
            for j in range(3):
                temp[arr[i][6+j]-1] += 1
            if i in [2, 5, 8]:
                if temp.count(1) != 9:
                    answer = 0
                    break
                else:
                    temp = [0] * 9

    print("#{} {}".format(tc, answer))