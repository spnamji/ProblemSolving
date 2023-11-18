# 1976. 시각 덧셈
# 3 17 1 39 형식으로 시와 분이 2개 주어졌을 때 시와 분의 합. 시는 1~12, 분은 0~59이하의 정수

# 제출한 코
T = int(input())

for test_case in range(1, T + 1):
    time = list(map(int, input().split()))
    hour = time[0]+time[2]
    minute = time[1]+time[3]

    if minute >= 60:
        hour += minute//60
        minute = minute%60
    if hour > 12:
        hour -= 12

    print(f"#{test_case} {hour} {minute}")

# 다른 사람이 제출한 코드
T = int(input())

for t in range(1, T+1) :
    h1, m1, h2, m2 = map(int, input().split())

    m = m1 + m2
    h = h1 + h2 + m//60 # if minute의 과정을 그냥 바로 해결
    m = m%60
    if h > 12 : # 시간이 12가 넘을 경우 빼준다.
        h = (h-12)
    print("#{} {} {}".format(t, h, m))
