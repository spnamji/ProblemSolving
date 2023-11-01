# 1948. 날짜 계산기
# 두 개의 날짜를 입력받고 두 번째 날짜가 첫 번째 날짜의 몇일째인지를 계산
T = int(input())

for test_case in range(1, T + 1):
    last_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    one_mon, one_day, two_mon, two_day = map(int, input().split())
    cur_mon = one_mon
    day = 0
    for i in range(two_mon-one_mon+1): # 두 날짜의 월 개수만큼 반복
        if two_mon == one_mon: # 입력받은 날짜의 월이 같다면
            day += last_day[one_mon-1]
        else: # 입력받은 날짜의 월이 다르다면
            if cur_mon == one_mon: # 첫 번째 달의 날짜 계산
                day += last_day[cur_mon-1]-one_day+1 # 31-15는 16이므로 1을 더해줘야함
            elif cur_mon == two_mon: # 마지막 달일 경우
                day += two_day
            else: # 첫 번째 입력받은 달과 두 번째 입력받은 달의 사이 값들
                day += last_day[cur_mon - 1]
            cur_mon += 1 # 다음 달로 계산을 넘겨주어야함.

    print('#{} {}'.format(test_case, day))


# 다른 사람 풀이
months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for tc in range(1, int(input())+1):
    m1, d1, m2, d2 = map(int, input().split())
    ans = 0

    # 같은 달에 위치할 경우
    if m1 == m2:
        ans = d2 - d1 + 1

    else:
        # 시작하는 달
        ans = months[m1] - d1 + 1
        # 중간에 있는 달
        for i in range(m1 + 1, m2): # 마지막 달 전까지 for문으로 반
            ans += months[i]
        # 마지막 달
        ans += d2
    print(f'#{tc} {ans}')

# 다른 사람 풀이 2
months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for i in range(2, 13): # 각 월들의 합을 계산
    months[i] += months[i-1]

for tc in range(1, int(input()) + 1):
    m1, d1, m2, d2 = map(int, input().split())

    # 1월부터 첫번째 날짜의 전달까지의 총 일수
    s1 = months[m1-1]
    s1 += d1

    # 1월부터 두번째 날짜 까지의 총 일수
    s2 = months[m2-1]
    s2 += d2

    print('#{} {}'.format(tc, s2 - s1 + 1))
