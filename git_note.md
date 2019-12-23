% YKL
% Git
% 2019 12 5

# Git

## 安裝

```bash
choco install bash
```

## 基本功能

### 建立
``` bash
// 查看版本
git --version 

// 設定帳號與信箱
git config --global user.name "biotuba"
git config --global user.email "biotuba@gmail.com"

// 建立一個repo/專案，新增一個資料夾後cd到裡面
git init

// 加入檔案到 *待commit* 中
git add <FileName>
git add *.*

// Commit
git commit -m "my first worm"

// 將本地端和遠端連結起來
// -u: --set-upstream，使分支追踨指定的遠端分支。只要做過一次  
//     並且成功push，之後就不用再帶remote name跟branch name
git remote add origin https://github.com/biotuba/Worm.git
git push -u origin master

```

### 取得Clone
```bash
git clone <網址>

```

## 建立分支

1. 建立分支但維持在目前的分支  
   git branch [name]

2. 建立並切換至新的分支  
   git checkout -b [name]

## 切換分支

1. git checkout [name]
