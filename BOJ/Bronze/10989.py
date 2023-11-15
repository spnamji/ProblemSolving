# 10989번 수 정렬하기 3
# 첫 번째 줄에 수의 개수가 주어지고 둘째 줄부터 n번째 줄까지 수가 주어진다. 해당 수는 10000보다 작거나 같은 자연수이다
# 메모리 제한이 중요한 문제!

# 기존 코드(append, sort, input사용)
import sys
n = int(sys.stdin.readline())

num = []
for i in range(n):
    num.append(int(sys.stdin.readline()))
num.sort()

for j in num:
    sys.stdout.write(str(j) + '\n')

# 메모리 공간을 고려한 풀이(계수정렬(counting sort)사용)
# 계수정렬 : 존재하는 수의 개수를 세고 정보를 바탕으로 정렬 수행
# sys.stdin.readline사용
# 배열에 접근하는 횟수를 줄여야한다.
import sys
n = int(sys.stdin.readline()) 
counts = [0] * 10001 # max만큼 만들고 이러면 한 번더 접근하여 배열을 생성하는 것이기 때문에 수의 최대값 10000까지만 담는 리스트 생성

for i in range(n):
    # counts에 바로 값을 올린다.(append사용시 메모리 재할당 발생. 메모리 효율적 사용불가)
    counts[(int(sys.stdin.readline()))] += 1

# 입력 값이 0~10000사이의 값이니 10000만큼 반복
for j in range(10001):
    if counts[j] != 0: # 10000의 길이를 가지는 리스트에 0인 값도 많음
        for k in range(counts[j]):
            print(j) # 인덱스 = 값, 인덱스위치의 값 = 해당 값의 횟수
