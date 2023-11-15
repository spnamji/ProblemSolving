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
