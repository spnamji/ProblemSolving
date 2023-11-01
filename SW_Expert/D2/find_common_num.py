# 1204. [S/W 문제해결 기본] 1일차 - 최빈수 구하기
# 학생의 수 : 1000명, 점수 범위 : 0~100점 이하의 값
T = int(input())

for test_case in range(1, T + 1):
    test_num = input()
    score = list(map(int, input().split())) # 1000명의 학생의 점수를 받아 저장
    counts = [0]*101 # 0~100까지 점수의 빈도수를 저장할 리스트 counts
    max_num = 0 # 가장 큰 빈도수를 저장할 공간
    max_idx = 0 # 가장 빈도수가 큰 값을 저장할 변수(인덱스값)

    for i in score:
        counts[i] += 1 # 학생 1000명의 점수를 모두 확인하여 빈도수를 하나씩 더한다.

    max_num = max(counts) # 가장 큰 빈도수를 찾는다
    result = [] # 가장 큰 빈도수를 가지는 값을 저장할 리스트
    for i in range(len(counts)): # 0~100까지 점수를 반복
        if counts[i] == max_num : # 해당 점수가 가장 큰 최빈값을 가지고 있다면
            result.append(i) # 해당 인덱스(점수)를 result리스트에 추가한다.
    print('#{} {}'.format(test_num, max(result))) # 최빈수가 여러 개 일 때는 가장 큰 점수 출력
