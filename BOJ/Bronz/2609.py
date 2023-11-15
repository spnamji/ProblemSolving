# 2609번 최대공약수와 최소공배수
# 두 수의 최대공약수와 최소공배수를 구하는 문제

# 첫번째 제출 코드(정답은 맞으니 실행시간 초과로 인하여 오답처리. -> 유클리드 호제법을 이용한 풀이 필요)
import sys
a, b = map(int, sys.stdin.readline().split())
big, sma = 0, 0

for i in range(min(a, b), 0, -1):
    if a%i==0 and b%i == 0:
        sma = i
        break

for j in range(max(a, b), a*b+1):
    if j%a==0 and j%b == 0:
        big = j
        break
print(sma)
print(big)

# 두 번째 제출 코드
# 유클리드 호제법을 이용하여 푸는 문제
# 호제법 : 두 수가 서로 상대방 수를 나누어 원하는 수를 얻는 알고리즘
# 최대공약수 gcd : a를 b로 나눈 나머지와 b의 최대 공약수는 a와 b의 최대공약수와 같다.
#                계속해서 a를 b로 나누어서 b를 a에 나눈 나머지 b에 대입시켜서 b가 0이 될 때까지 반복하여 남는 값 a가 최대 공약수이다.
# 최소공배수 lcm : a, b의 배수중에서 공통되는 배수 중 가장 작은 값. a, b의 곱을 a, b의 최대 공약수로 나누면 된다.
#                (최소공배수 x 최대 공약수) = gcd^2 * a * b [a, b은 서로수]를 이용한 방법
import sys
def gcd(a, b):
    while b>0:
        a, b = b, a%b # 24 18 / 18 6 / 6 0
    return a # 6

def lcm(a, b):
    return a*b // gcd(a, b)

a, b = map(int, sys.stdin.readline().split())
print(gcd(a, b))
print(lcm(a, b))
