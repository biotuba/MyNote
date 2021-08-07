# 檔案讀取寫入
import jieba.analyse # jieba 中文分詞

# 1. 放在同一個資料夾，相對路徑

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

# 體驗結巴
keyword = jieba.analyse.extract_tags(article,5) 
print(keyword)
