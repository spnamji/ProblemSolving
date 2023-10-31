# 1959. 두 개의 숫자열
# 두 개의 숫자열의 곱셈중 가장 큰 값을 출력
# 2중 for문을 통해 서로 마주보는 숫자들을 곱한 후 더했을 때의 최대값을 구한다.

T = int(input())

for test_case in range(1, T + 1):
    num1_len, num2_len = map(int, input().split())
    num_str1 = list(map(int, input().split()))
    num_str2 = list(map(int, input().split()))
    result = 0

    if num1_len < num2_len: # 2번째 숫자열이 더 길 경
        for i in range(num2_len-num1_len+1): # 작은 숫자열을 넘어가지 않게 돌려가며 곱하는 규칙
            sum = 0
            for j in range(num1_len):
                sum += num_str1[j]*num_str2[i+j]
            if sum > result: # 더 큰 값을 result에 넣는다.
                result = sum
    else: # 첫 번째 숫자열이 더 길 경
        for i in range(num1_len-num2_len+1):
            sum = 0
            for j in range(num2_len):
                sum += num_str2[j]*num_str1[i+j]
            if sum > result:
                result = sum

    print('#{} {}'.format(test_case, result))

# 다른 사람 풀이
t = int(input())
for tc in range(1, t + 1) :
    n, m = map(int, input().split())
    a = list(input().split())
    b = list(input().split())

    result = 0
    for i in range(abs(n - m) + 1) : # 길이를 따로 비교하지 않고 값을 뺀 다음 절대값을 취해서 +1을 한다.
        value = 0
        for j in range(min(n, m)) : # 내부 for문은 더 작은 숫자열의 길이로 반복
            if len(a) > len(b) : # a의 길이가 더 길 경우
                value += int(a[j+i]) * int(b[j])
            elif len(a) < len(b) : # b의 길이가 더 길 경우
                value += int(a[j]) * int(b[j+i])
            else : # 길이가 같다면 같은 인덱스를 곱한다.
                value += int(a[j]) * int(b[j])
        if value > result : # 내부 for문으로 생성된 값을 비교하여 result갱신
            result = value

    print('#%d %d' % (tc, result))
