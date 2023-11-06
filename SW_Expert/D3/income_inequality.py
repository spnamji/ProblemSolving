# 10505. 소득 불균형
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    income = list(map(int, input().split()))
    N_average = sum(income)//N

    count = 0
    for i in income:
        if i <= N_average:
            count += 1
    print('#{} {}'.format(test_case, count))
