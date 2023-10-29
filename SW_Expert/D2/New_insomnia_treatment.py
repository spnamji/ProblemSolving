# 내 풀이
T = int(input())

result_list = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] # 비교할 결과 리스트
for test_case in range(1, T + 1):
    current_list = [0 for i in range(10)] # 센 숫자를 넣는 리스트

    N = int(input())
    count = 1 # 반복 횟수
    num = N
    while current_list != result_list: # 결과 리스트와 같을 때까지 반복
        while num != 0: # 현재 숫자 N의 요소들 추출하는 while문
            cur_num = num%10
            num //= 10
            if current_list[cur_num] != 1: # 해당 요소의 값이 리스트에 없으면 추가
                current_list[cur_num] = 1
                continue
            else:
                continue
        if current_list != result_list: # 결과리스트와 현재 리스트가 같지 않으면
            count += 1 # 반복 횟수를 추가
            num = N*count # xN의 숫자로 다시 반복
        else:
            break
    print('#{} {}'.format(test_case, count*N))


# 다른 사람 풀이 1
t = int(input())

for i in range(1, t + 1) :
    n = input() # 정수 n을 입력받음
    value = int(n)
    data = [0] * 10 # 각 자리수의 번호를 센 횟수가 담겨질 리스트 data
    while True :
        for j in range(len(n)) : # n의 길이만큼 반복(인덱스 값이 j에 들어감)
            data[int(n[j])] += 1 # 입력받은 정수 n의 j번째 값을 인덱스 넘버로 자리수의 번호를 센 횟수 추가
                                 # n[0]이 1이면 data[1]에 +1이 된다.
        if not data.count(0) : # data문자열에 0이 없다면
            print('#%d %d' % (i, int(n))) # n을 출력
            break
        n = str(value + int(n)) # 0이 존재할 경우 원래의 값을 저장해둔 value+n을 한 후 반복한다.

# 다른 사람 풀이 2
T = int(input())
for x in range(1, T+1):
    N = int(input())
    count = 0
    
    zero_to_nine = [str(i) for i in range(10)] # 0~9까지의 값을 str형태로 list에 넣는다
    while zero_to_nine: # zer0_to_nice 리스트가 빌 때 까지 반복한다.
        count += 1
        room = N * count
        room = str(room)

        for c in room: # room변수의 값을 c에 하나씩 넣는다.
            if c in zero_to_nine: # 만약 c가 zero_to_nine리스트에 있다면
                zero_to_nine.remove(c) # zero_to_nine리스트에서 c를 제거한다.

    print('#{} {}'.format(x, room))
