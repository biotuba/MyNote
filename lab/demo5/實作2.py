# 實作二、費氏數列
times = 0
result = 0
n1 = 0
n2 = 1

for i in range(0,10):
    result = n1 + n2
    print("n",i+3, ":", result)
    n1 = n2
    n2 = result
    times += 1
