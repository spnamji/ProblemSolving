# 1940. 가랏! RC카!
T = int(input())

for test_case in range(1, T + 1):
    num = int(input())
    distance = 0
    cur_v = 0

    for i in range(num):
        command = list(map(int, input().split()))
        if command[0] == 0:
            distance += cur_v
        elif command[0] == 1:
            cur_v += command[1]
            distance += cur_v
        elif command[0] == 2:
            cur_v -= command[1]
            if cur_v < 0:
                cur_v = 0
            distance += cur_v

    print(f"#{test_case} {distance}")

# 다른 사람 풀이
T = int(input())

for test_case in range(1, T + 1):
    v = int(input())
    s = 0
    d = 0
    
    for i in range(v):
        arr = list(map(int, input().split()))
        if arr[0] == 1: # 0인 경우 현재 속력에 입력받은 속력을 더한다
            s += arr[1]
        elif arr[0] == 2: # 감속이고 0보다 작은 속도는 없으므로 s가 입력받은 속력보다 크면 빼고 작으면 0으로 고정한다.
            if s > arr[1]:
                s -= arr[1]
            else:
                s = 0
        d += s # 위에서 계산한 속도를 거리에 더한다.
    print("#%d" %test_case, d)
