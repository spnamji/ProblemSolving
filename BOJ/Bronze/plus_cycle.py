# 1110 더하기 사이클
# 먼저 주어진 수가 10보다 작다면 앞에 0을 붙여 두 자리 수로 만들고, 각 자리의 숫자를 더한다. 
# 그 다음, 주어진 수의 가장 오른쪽 자리 수와 앞에서 구한 합의 가장 오른쪽 자리 수를 이어 붙이면 새로운 수
# 26부터 시작한다. 2+6 = 8이다. 새로운 수는 68이다. 6+8 = 14이다. 새로운 수는 84이다. 8+4 = 12이다. 새로운 수는 42이다. 4+2 = 6이다. 새로운 수는 26

# 내가 푼 풀이
N = input()
new = ''
sum = ''
t_N = N
count = 0

while new != N: # 처음 입력받은 N값과 반복하여 생성한 새로운 정수값이 같지 않으면 반
    count += 1
    if len(N) < 2: # 10보다 작다면 0을 붙여 두 자리수로 만들어 준다.
        N = N+'0'
        t_N = N # 현재 새로운 수로 계산하기 때문에 값 변경
    sum = str(int(t_N[:1]) + int(t_N[1:])) # 새로운 수의 각 자리를 더한다
    new = t_N[-1] + sum[-1] # 새로운 수의 마지막과 더한 값의 마지막을 더해 새로운 수를 구한다
    t_N = new
print(count)

# 다른 사람 풀이 (int로 푼 방법)
n = int(input())
num = n
cnt = 0

while True:
  a = num//10 # 앞 자리수
  b = num % 10 # 뒷 자리수
  c = (a+b)%10 # 더한 값의 뒷 자리수
  num = (b*10) + c # 기존 수의 뒷자리를 십의 자리로, c를 일의자리로 해서 더한다.
  
  cnt = cnt + 1
  if(num == n):
    break
print(cnt)
