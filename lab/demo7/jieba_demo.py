import jieba
# import jieba.analyse as ja
# from jieba import analyse
from jieba.analyse import extract_tags

f = open('a.txt', 'r', encoding='utf8')
article = f.read()
f.close()

jieba.load_userdict("mydict.txt") # 載入自訂字典
jieba.add_word("陳時中")
# 分詞
print(" ".join(jieba.cut(article)))

# 關鍵字
print(extract_tags(article,5))

# 載入詞典: 詞 詞頻 詞性
