# learngit

## 1.上传文件
(1) 进入文件目录

(2) git add read.txt

(3) git commit -m "注释"

(4) git push

***
## 2.远程仓库里已经有文件，将远程仓库与本地关联

#git初始化

'git init'
#设置remote地址

'git remote add  origin 地址'

#获取远程仓库master分支上的内容

'git pull origin master'

#将当前分支设置为远程仓库的master分支

'git branch --set-upstream-to=origin/master master'

#将本地全部文件加入git版本管理 .的意思是将当前文件夹下的全部文件放到版本管理中

'git add .'

#提交文件 使用-m 编写注释

'git commit -m "注释"'

#推送到远程分支

'git push'



