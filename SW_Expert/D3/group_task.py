# 13218. 조별과제
# 3인 1조로 만들 수 있는 조의 최대수
T = int(input())

for test_case in range(1, T + 1):
    student_num = int(input())
    print('#{} {}'.format(test_case, (student_num//3))) # 정수 몫을 구하기
