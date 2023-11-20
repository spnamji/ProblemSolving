# 3052: 나머지
# 42로 나누었을 때 나머지 중 서로 다른 값이 몇 개 있는지 출력하는 문제

# set을 활용한 풀이. set은 순서가 딱히 없으니 해당 문제에서는 상관x (내 풀이)
num = []
for i in range(10):
    num.append(int(input())%42)
fin_num = set(num)

print(len(fin_num))

# for문을 활용한 풀이. not in을 사용.
arr = []
for i in range(10):
    a = int(input())
    if a%42 not in arr:
        arr.append(a % 42)
print(len(arr))
