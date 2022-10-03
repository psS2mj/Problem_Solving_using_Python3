# date: 2022/10/03
# author: psS2mj
# brief: BOJ_8974_희주의 수학시험

a, b = map(int, input().split())
arr = [0] * b

temp = 1
cnt = 1
for i in range(b):
    if cnt == 0:
        temp += 1
        cnt = temp
    arr[i] = temp
    cnt -= 1

result = 0
for i in range(a-1, b):
    result += arr[i]

print(result)