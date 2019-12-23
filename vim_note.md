% VIM Notes
% YKL

# 取得目前的文件名稱

1. %: 文件檔名
2. %:e: 副檔名
3. %:r:t 文件檔名(不含副檔名)
4. %:p 完整路徑
5. %:h 目錄路徑
6. pandoc -o %:t:r.docx %: 將目前文件轉成docx文件

# 執行外部指令

1. :! command 執行命令並顯示在cmd上
2. :silent !command 背景執行
3. :r !command 執行後將結果印在游標後
4. 選取範圍:w !cmd 將選取範圍以cmd執行

dir *.md
find "[ ]" *.md

