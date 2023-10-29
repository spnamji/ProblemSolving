# 1284. 수도 요금 경쟁
T = int(input())

for test_case in range(1, T + 1):
    # P : A사의 1리터당 요금, Q : B사의 기본 요금, R : B사의 기본 이용량, S : B사의 리터당 추가요금, W : 종민이의 사용량
    P, Q, R, S, W = map(int, input().split())

    A_rate = W * P
    if W > R:
        B_rate = Q + (W-R)*S
    else:
        B_rate = Q

    if A_rate < B_rate:
        print('#{} {}'.format(test_case, A_rate))
    else:
        print('#{} {}'.format(test_case, B_rate))

# 다른 사람 풀이
B = Q
if W > R:
  B += (W-R)*S # else까지 사용하지 않아도 예외의 경우에만 반영되도록
