# 2차원배열에서의 DFS, BFS

N = 10
arr = [[0]*N for _ in range(N)] # 👨🏻‍🏫비어있는 10*10 배열을 만들어보았습니다.
# for row in arr:
#     print(*row)

# 주어지는 좌표 잘 확인하기 (r,c)
# (r,c)으로 표시되는 2차원배열에서 4방/8방으로 인접한 요소를 탐색할 때

# 2차원배열 DFS/BFS 순회를 하려면
# delta 배열을(좌표값의 변화량) 이용해 순회한다.
# 상하좌우 => 4방
dr = [-1,1,0,0] #👩🏻세로
dc = [0,0,-1,1] #👩🏻가로

r,c = 1,1
cnt = 1
for d in range(4): # 👨🏻‍🏫4방이니까 4번 돈다.
    nr = r + dr[d] # nr: 다음 r, r: 현재 row의 좌표
    nc = c + dc[d] # nc: 다음 c, c: 현재 column의 좌표
    arr[nr][nc] = cnt
    cnt += 1
# 나와 연결되어 있는 요소를 찾기 위한 방법: 4방 탐색
for row in arr:
    print(*row)