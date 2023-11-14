# 백준 1546번 평균
# 주어진 성적 n개가 있을 때 가장 높은 점수로 모든 점수를 점수/max*100을 계산했을 때의 평균값을 구하는 문제
# 내가 푼 코드
N = int(input())
score = list(map(int, input().split()))

score_max = max(score) # 최대값을 구한다.
sum = 0
for i in range(N): # 점수 수만큼 반복하며 연산을 수행하고 sum변수에 바꾼 값을 더해준다
    score[i] = score[i]/score_max*100
    sum += score[i]
print(sum/N)

# 다른 사람 풀이
n = int(input())  # 과목 수
test_list = list(map(int, input().split()))
max_score = max(test_list)

new_list = [] # 새로운 값을 넣을 리스트
for score in test_list :
    new_list.append(score/max_score *100)  # 새로운 점수 생성 및 추가
test_avg = sum(new_list)/n # sum함수를 활용하여 값의 합을 구함.
print(test_avg)
