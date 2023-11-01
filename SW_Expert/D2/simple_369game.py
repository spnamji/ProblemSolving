# 1926. 간단한 369게임
# 3, 6, 9가 나올 때 '-'으로 표현
T = int(input())

# 문자열에 +=으로 문자를 더하면 자동으로 띄워쓰기가 된다.
for i in range(1, T+1):
    result = "" # 결과값을 넣을 문자열
    cur_num = str(i)

    count = 0
    for j in range(len(str(i))): 각 숫자의 길이만큼 반복 (10의 경우 2번)
        if int(cur_num[j]) == 3 or int(cur_num[j]) == 6 or int(cur_num[j]) == 9: # 3, 6, 9에 해당하면 -를 문자열에 추가하고 count를 +1한다.
            result += "-"
            count += 1
        elif j == len(str(i))-1: # 3, 6, 9에 해당하지 않고 마지막 문자일 때 count가 0이면('-'를 이미 추가하지 않았으면) 해당 숫자를 문자열에 더한다. 
            if count == 0:
                result += cur_num
    print(result, end=' ')

# 다른 사람 풀이 1
N = int(input())
clap = ['3', '6', '9'] # 해당되는 케이스를 넣은 리스트 생성

for i in range(1, N+1): # 입력받은 숫자만큼 반복
    count = 0
    for j in str(i): # 숫자 하나하나 반복(10의 경우 1, 0 반복)
        if j in clap: # 해당 숫자가 clap 리스트에 존재하면 count를 +1
            count += 1
    if count > 0: # 해당 숫자에대한 반복을 마치고 count가 0보다 크면(3, 6, 9가 포함이면) '-'를 i값으로 바꿈
        i = '-' * count # 33의 경우 count횟수가 2이므로 '-'를 두 번 출력
    print(i, end=' ') # count가 0인 경우 i값은 원래의 숫자값 그대로 출력

# 다른 사람 풀이 2
  # i라는 숫자에 3 6 9 가 들어간 수 만큼 -출력, 띄어쓰기 없이
  # 그 외에는 일반 숫자 출력
T = int(input())
for i in range(1, T+1): # 1 ~ 100
    i = str(i)
    clap = i.count('3') + i.count('6') + i.count('9') # 해당 숫자에서 3, 6, 9에 해당하는 횟수를 모두 더함

    if clap == 0:
        print(i, end=' ')
    else: # clap이 1이상인 경우 문자 "-"를 clap수만큼 곱한다.
        print("-" * clap, end=' ')
