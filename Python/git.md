# git

## 创建使用仓库

工作区—git add—暂存区(index)—git comman—本地仓库（object)

未跟踪—git add—未修改—修改文件—已修改—git add—已缓存

git init创建仓库

git status查看仓库状态

git add 添加到暂存区

git commit 提交//*git commit -m <文件名>直接提交文件，git commit 文件进入vi编辑模式，可以输入提交备注。*

###整个系统是Linux形式，可以使用git add * 提交多个文件//git add . 

git log 查看提交记录

![image-20240708124836474](D:\DeskTop\learn\Python\images\image-20240708124836474.png)

*在进入vi模式后我输入了这是第一次上传仓库*

![image-20240708125115626](D:\DeskTop\learn\Python\images\image-20240708125115626.png)

*除了刚刚添加的图片所有的内容都已经跟踪并且上传到仓库*

![image-20240708125228230](D:\DeskTop\learn\Python\images\image-20240708125228230.png)

*这里可以查看之前上传的信息*

## 回退版本

![image-20240708125539708](C:\Users\21998\AppData\Roaming\Typora\typora-user-images\image-20240708125539708.png)

###这是上面git 提交后的git status查看的界面

**git reset**

1. git reset --soft//回退到某一个版本，保存工作区和暂存区的所有工作内容
2. git reset --hard//回退到某一个版本并且丢弃工作区暂存区所有修改的内容
3. git reset --mixed//回退到某一个版本并且只保存工作区的修改内容

如果提交了很多次，想合成一个可以进行回退之后进行重新提交，这样多次的修改内容被合成了一个。多使用soft。

**git reflog**

查看操作的历史记录，以及所有过去的版本号；误操作后可以找到之前的版本号，再使用git reset进行回退。

**git diff**

查看工作区暂存区本地仓库的差异，...ui界面看的比较清楚...

## 删除文件

1. git rm 文件，直接在工作区和暂存区中删除文件，提交后之后查看状态已被删除。
2. 图形化界面直接删除，删除后进行添加到暂存区，最后提交，git add ./git add 文件，再提交 。
3. git rm --cached 文件，把文件从暂存区删除，但保留在工作区中。
4. git rm -r *递归删除某个目录下的所有子目录和文件

*删除后不要忘记提交*

