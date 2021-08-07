# while

times = 0 # 初始值

while times < 10: # 判斷條件
    print(times)
    times += 1 # 累進

# 累加
times = 0
result = 0
while times < 10:
    result += times + 1
    times += 1
    print(result)


# 不固定次數
print("不固定次數 loop")

result = 0
end = 50
while result <= 50:
    result = result + 1

print("最後加的是", result)