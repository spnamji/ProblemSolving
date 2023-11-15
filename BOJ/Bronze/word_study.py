# 1157번 단어공부
# 단어가 주여졌을 때 알파벳 최빈값을 출력하시오. 최빈값이 여러개이면 ?를 출력

# 내가 푼 풀이
N = input()
N_UP = N.upper() # 대소문자가 섞여있는 문자열을 uppera()로 대문자 변환
n = list(set(N_UP)) # set으로 중복되는 값이 없는 리스트를 만듬
num = []
cnt = 0

for i in n:
    num.append(N_UP.count(i)) # 각 값이 N_UP에서 몇 번 나왔는지를 num리스트에 저장

m = max(num)
for j in range(len(num)):
    if m == num[j]: # 최대횟수와 현재 인덱스의 횟수가 같으면 cnt+1. 
        cnt += 1
    elif m < num[j]:
        m = num[j]

if cnt > 1: # 2이상이면 최빈값이 2개 이상이라는 뜻
    print("?")
else:
    print(n[num.index(m)].upper())

# 다른 사람 풀이
word = input().lower() # 모두 소문자로 변환
word_list = list(set(word)) # 중복되는 값을 없애고 list로 변환
cnt = []

for i in word_list: # 값들을 넣으면서 개수 반환
  count = word.count(i) # lower한 원래 문자열에서 문자의 개수를 세고 해당 개수를 cnt배열에 반환
  cnt.append(count)
if cnt.count(max(cnt)) >= 2: # cnt최대값의 개수가 cnt에서 2개 이상이면 최빈값이 여러개
  print("?")
else:
  print(word_list[(cnt.index(max(cnt)))].upper())
