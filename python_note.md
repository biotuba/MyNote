python --version //顯示python 版本
python -m pip --version //顯示pip版本
python -m pip install --upgrade pip //升級pip版本
python -m pip list //列出已下載的套件
python -m pip show pip

# 資料型態

## List
``` python
# List
a_list = [1,2,3,4,5]

# append: 附加在list 後方
a_list.append(3)

# pop: 彈出list最後一個元素
a_list.pop()

```


# 爬蟲

## 套件

1. python -m pip install requests
2. pip install Selenium 
3. pip install beautifulsoup4
4. pip install html5lib //解析html5，也可安裝xml, lxml ...

## Selenium
### Web Driver 屬性

屬性|說明
name|瀏覽器名稱
title|目前開啟網頁之標題
current_url|目前開啟網頁之URL
page_source|目前開啟網頁之原始碼
session_id|網頁連線id
capabilities|瀏覽器功能設定

方法	 說明
get_window_position()	 取得瀏覽器視窗左上角位置
set_window_position(x, y)	 設定瀏覽器視窗左上角位置
get_window_size()	 取得瀏覽器視窗大小
set_window_size(x, y)	 設定瀏覽器視窗大小
maximize_window()	 將瀏覽器視窗最大化
minimize_window()	 將瀏覽器視窗最小化

方法	 說明
back()	 按瀏覽器 "上一頁" 鈕
forward()	 按瀏覽器 "下一頁" 鈕
refresh()	 按瀏覽器 "更新" 鈕
quit()	 按瀏覽器 "關閉" 鈕, 同時關閉驅動程式
close()	 按瀏覽器 "關閉" 鈕

方法	 說明
save_screenshot(filename)	 將目前網頁儲存為 png 檔案下載

## BeautifulSoap

### 用法
```python
# BeautifulSoup(htmlDoc, parser): 讀入html並以指定的parser解析
soup = BeautifulSoup(pageSource, "html5lib")

# prettify(): 格式化html
soup.prettify()

# find_all( node_name ): 找出所有節點
soup.find_all('a')

# get( attr_name ): 取出節點中的屬性
tag.get('title')

# select( css ): 以css方式搜尋
soup.select('#id')

# select_one( css): 以CSS方式搜尋，第一個match
soup.select_one('#id').text

```

## re 正規表達示

### 用法
``` python
# .sub( pattern, replace, string): 取代
re.sub(r'^\s+', '', str(tag.string))

# .match( pattern , string) m 


```


# Google API
## Setup
``` bash
py -m pip install google-api-python-client
py -m pip install google-auth-oauthlib
```
# SQLite
## Setup
1. choco install sqlite
2. python import
```
already in python3
py
import sqlite3
sqlite3.version
sqlite3.sqlite_version

```
## How to Use

