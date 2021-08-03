# List
name_list = ['jay', 'kay', 'may']
print(name_list[0])

for name in name_list:
    print(name)

for i in range(1,10):
    print(i)

name_list.insert(1, "carol")
print(name_list) # 會修改原本 list

name_list.remove("jay")
print(name_list) # 會修改原本 list
