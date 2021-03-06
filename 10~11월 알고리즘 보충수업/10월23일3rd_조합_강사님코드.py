N = 5 # N개 중에
K = 3 # K개 고르기
arr = [1,2,3,4,5]
select = [0] * N # 각 요소의 조합 포함 여부
# idx: 인덱스
# cnt: 선택한 개수
def comb(select,idx,cnt): # cnt: 몇 개 골랐냐?
    if cnt == K: # 다 골랐을 때
        # 👨🏻‍🏫더 이상 고를 필요 없다! => 이게 우선되는 조건!!!
        # 우리가 원하는 개수의 원소를 선택한 시점
        # print(select) # K개만 선택된 것을 확인할 수 있다.
        for i in range(N):
            if select[i]:
                print(arr[i],end=" ")
        print()
        return
    if idx >= N:
        return
    # 👨🏻‍🏫인덱스에 상관없이 다 골랐으면 종료하면 된다. (순서!)

    # 요소를 조합에 포함하느냐
    select[idx] = 1
    comb(select,idx+1,cnt+1)
    # 요소를 조합헤 포함하지 않느냐
    select[idx] = 0
    comb(select,idx+1,cnt)

# 인덱스 0부터, 하나의 요소도 선택하지 않은 시점에서 시작
comb(select,0,0)  

# 👨🏻‍🏫조합, 부분집합을 구하는 것이 중요한게 아니라
# 이를 어떻게 활용할 수 있을지에 대해 고민해봐야 한다.
# 예: 요소 3개를 선택했을 때 총합이 10 초과하는 것의 개수?