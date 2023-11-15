# 4344번 평균은 넘겠지
# 평균을 넘는 학생의 비율을 반올림하여 소수점 셋째 자리까지 출력하는 문제

# 내가 제출한 코드
n = int(input())
for i in range(n):
    n_score = list(map(int, input().split()))
    ave = sum(n_score[1:])/n_score[0]
    count = 0

    for j in n_score[1:]:
        if j > ave:
            count += 1
    percent = count/n_score[0]
    print(f"{percent:.3%}") # 3자리 숫자까지 퍼센트를 표현(f-string)

# 다른 사람 풀이
n = int(input())

for _ in range(n):
    nums = list(map(int, input().split()))
    avg = sum(nums[1:])/nums[0]  # 평균을 구함 (nums[0]: 학생수, nums[1:] 점수)
    cnt = 0
    for score in nums[1:]:
        if score > avg:
            cnt += 1  # 평균 이상인 학생 수
    rate = cnt/nums[0] *100 # 백분율 구하기
    print(f'{rate:.3f}%') # 소수점 3자리까지 출
