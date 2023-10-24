# 1945. 간단한 소인수분해
# 2, 3, 5, 7, 11순서대로 인수분해(나누기)를 한 횟수를 기록하고 출력하는 문제.
T = int(input())

for test_case in range(1, T + 1):
    num = int(input())
    case_num = [0, 0, 0, 0, 0] # 각 횟수를 기록하기 위한 리스트
    j = 0 # 횟수를 기록하는 임시 변수
    for i in [2, 3, 5, 7, 11]: # 소인수분해이므로 가장 작은 값부터 계산한다.
        while num % i == 0: # 나누어 떨어질 때 까지 나눈
            case_num[j] += 1
            num //= i # 계산할 때 마다 값을 나눈다.
        j += 1

    print("#{} {} {} {} {} {}".format(test_case, case_num[0], case_num[1], case_num[2], case_num[3], case_num[4]))


# 또 다른 풀이
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    
    lst = [2,3,5,7,11]
    cnt =[0, 0, 0, 0, 0]
    # i(밑)으로 나누었을 때 나머지가 0이면 지수 1 추가 + N으로 나누기
    # i로 나누어지지 않을 때까지 
    for i in range(5):
        while N % lst[i] == 0:
            cnt[i] += 1
            N //= lst[i]
    print(f'#{tc}', *cnt) # 리스트의 주소를 넘겨줌
