name_set = {'周','林','黃', '黃'}
print(name_set) # 重複的會自己合併，沒有順序性

name_set.add('王')
print(name_set) # 重複的會自己合併，沒有順序性

name_set.remove('王')
print(name_set) # 刪除

name_setb =name_set.union({'李','陳'})
print(name_setb) # 聯集

# 遍巡
for name in name_setb:
    print(name)

