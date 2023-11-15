# 2775번 부녀회장이 될테야
# a층 b호에 거주하기 위해서는 아래층 1~b호까지 사람들의 합만큼 살아야한다.
# 0층은 1호부터 i호에 i명만큼 산다
T = int(input())

for _ in range(T):
    k, n = int(input()), int(input())
    floor_zero = [i for i in range(1, n+1)] # 0층 리스트 생성

    for j in range(k): # 층만큼 반복
        for k in range(1, n): # 호실 수 -1만큼 반복(1호실 = 0번 인덱스)
            floor_zero[k] += floor_zero[k-1] # 아랫층 현재 호 + 아랫층 앞의 호
    print(floor_zero[-1])
