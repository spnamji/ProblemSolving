# 2029. 몫과 나머지 출력하기
T = int(input())

for test_case in range(1, T + 1):
    a, b = map(int, input().split()) # 두 개의 정수 입력받기
    print("#{} {} {}".format(test_case, (a//b), (a%b)))  # 몫(//)과 나머지(%) 출력
