person = {
            "name": "Jay",
            "height": 173,
            "weight": 93,
            "handsom": True
         }

print(person)

# 取出 person 中的 weight
print(person["weight"])

# 新增一個內容、修改內容
person["year"] = 38
print(person)

# 取出值後做運算再帶回去
person["height"] += 10
print(person)

del person["weight"]
print(person)

# 遍巡
for key, value in person.items():
    print(key, value)

# 計算字母出現的次數
