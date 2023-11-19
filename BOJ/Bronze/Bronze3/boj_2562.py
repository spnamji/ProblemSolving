# 9개의 값을 입력받고 최대값과 몇 번째 수인지 출력
num = []
for i in range(9):
    num.append(int(input()))
m = max(num)

print(m)
print(num.index(m)+1)
