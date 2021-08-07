# 實作四、文件檔的字數統計
f = open('a.txt', "r", encoding='utf8')
article = f.read()
f.close()

# print(article)
result = {}
for word in article:
    # print(word)
    if word in result:
        result[word] += 1
    else:
        result[word] = 1

print(result)