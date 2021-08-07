# function

def add(n1, n2):
    return n1 + n2

print(add(1,5))
print(add('hello','world'))
# print(add(3,'world'))
# print(add(3))
# print(add(3,4,5))

def add_multiple(nlist):
    sum = 0
    for n in nlist:
        sum += n
    return sum

print(add_multiple(range(1,11)))

## 不定參數
def add_multiple(*nlist):
    sum = 0
    for n in nlist:
        sum += n
    return sum

print(add_multiple(1,2,3,4,5))

## 參數預設值
def add(n1, n2, n3 = 1, n4 = 2):
    result = (n1 + n2) /n3 * n4
    return result

add(1,2, n4 =5) # 有預設值的可以指定參數