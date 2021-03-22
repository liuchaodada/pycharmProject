# 【GIT】 理解git工作流程、git插件与命令行、可视化练习、实际工作流程

## [git是什么](https://www.runoob.com/git/git-tutorial.html)


### [rcs、git与svn的区别](https://www.yiibai.com/git/git_basic_concepts.html)


### 本地版本控制

记录文件每次的更新，可以对每个版本做一个快照，或是记录补丁文件，适合个人用，如RCS。

### 集中式版本控制

SVN等CVCS集中化版本控制系统都有单一的Central VCS Server，所有的版本数据都保存在服务器上，协同开发者从服务器上同步更新或上传自己的修改。

### 分布式版本控制

每个开发者都拥有全部的副本。

git客户端不仅做本地的文件快照，还会将本地resposity完整地镜像出来，这样开发者即使可以离线在本地仓库commit，也可以在连网时push到关联远程resposity的任意branch。

镜像容灾，任何一处协同工作服务器发生故障，都可以用任何一个镜像出来的本地仓库恢复。每一次clone，都是一次对远程resposity的完整copy。

## [Git的四个组成](https://www.runoob.com/git/git-workspace-index-repo.html)

* Workspace：工作区，就是你平时存放项目代码的地方

* Index / Stage：暂存区，用于临时存放你的改动，事实上它只是一个文件，保存即将提交到文件列表信息

* local Repository：仓库区（或本地仓库），就是安全存放数据的位置，这里面有你提交到所有版本的数据。其中HEAD指向最新放入仓库的版本

* Remote Respository：远程仓库，托管代码的服务器，可以简单的认为是你项目组中的一台电脑用于远程数据交换


![理解](https://ftp.bmp.ovh/imgs/2021/03/504bc4f4d562d86c.png)
## [git工作流程](https://www.runoob.com/git/git-workflow.html)

一般工作流程如下：

* 克隆 Git clone远程仓库或git init新建本地仓库作为工作目录。
* 在克隆的资源上添加或修改文件。
* 如果其他人修改了，你可以更新资源。
* 在提交前查看修改。
* 提交修改。
* 在修改完成后，如果发现错误，可以撤回提交并再次修改并提交。

下图展示了clone远程仓库作为git仓库的工作流程：

![理解git工作流程](http://www.yiibai.com/uploads/images/201707/0707/497150749_38351.png)

下图展示了新建本地仓库作为git仓库的工作流程：

* 在工作目录中添加、修改文件；
* 将需要进行版本管理的文件放入暂存区域；
* 将暂存区域的文件提交到git仓库。

![git工作流程](https://ftp.bmp.ovh/imgs/2021/03/df7e472a4f347bf4.png)

## git文件的四种状态
* Untracked: 未跟踪, 此文件在文件夹中, 但并没有加入到git库, 不参与版本控制. 通过git add 状态变为Staged.

* Unmodify: 文件已经入库, 未修改, 即版本库中的文件快照内容与文件夹中完全一致. 这种类型的文件有两种去处, 如果它被修改, 而变为Modified. 如果使用git rm移出版本库, 则成为Untracked文件

* Modified: 文件已修改, 仅仅是修改, 并没有进行其他的操作. 这个文件也有两个去处, 通过git add可进入暂存staged状态, 使用git checkout 则丢弃修改过, 返回到unmodify状态, 这个git checkout即从库中取出文件, 覆盖当前修改 !

* Staged: 暂存状态. 执行git commit则将修改同步到库中, 这时库中的文件和本地文件又变为一致, 文件为Unmodify状态. 执行git reset HEAD filename取消暂存, 文件状态为Modified

![git文件的四种状态](https://pic2.zhimg.com/80/v2-9ed5631b956e70ec2790356311cf0691_720w.jpg)

## .gitignore忽略文件
这边不赘述了，现在都有模板，gitee和github官方模板，自己再加入忽略文件或文件夹，这里有简单介绍  **[gitignore](https://github.com/onlynight/ReadmeDemo/tree/master/Readmes/GitIgnore)**


## 搭建git，关联github和gitee

**工作中实际都会搭建私钥gitlab，但远程仓库的原理是一样的，都是ssh实现**

**注意下示例代码git命令里带<>标红的都是需要填入自己的对应参数**

![理解git仓库](https://www.runoob.com/wp-content/uploads/2015/02/git-command.jpg)

**1. 搭建本地仓库或克隆远程仓库**
```shell
$ git init 
or 
$ git clone <git@github.com:liuchaodada/pycharmProject.git>
$ git clone <git@gitee.com:liuchaodada/pycharmProject.git>
```

**2. 配置git，设置用户名和邮箱**
```shell
$ git config --global user.name "<username>"
$ git config --global user.email "<useremail>"
```
用户名可以写自己的名字或者github gitee的注册名
邮箱必须写github或gitee绑定的注册邮箱，每次commit会提交这两个信息

**3. 生成ssh密钥，测试ssh连接**
```shell
$ ssh-keygen -t rsa -C "<youremail@example.com>" -f  <rsa_github>
$ ssh-keygen -t rsa -C "<youremail@example.com>" -f <rsa_gitee>
```
后面的 your_email@youremail.com 改为你在 Github 或gitee上注册的邮箱，之后会要求确认路径和输入密码，我们这使用默认的一路回车就行。成功的话会在 ~/ 下生成 .ssh 文件夹，进去，打开 id_rsa.pub，复制里面的 key。-f 是指定密钥name，这里我建了两个密钥一个是github的一个是gitee的。

**4.添加ssh公钥到github gitee**

这部分不赘述，在gitee和github个人主页设置里有，我们生成的密钥在
/root/.ssh文件里，有两个，id_rsa_github.pub和id_rsa_gitee.pub,直接进入目录cat，复制密钥内容，到github和gitee网站内新建ssh公钥，名称自建不限制。

**5.新建远程仓库**

这部分不赘述，注意的是从2020年4月开始，github把master主分支重新命名为了main主分支，所以默认的新建仓库主分支为main。另外新建远程仓库最好与本地仓库的名称保持一致。

**6.绑定远程仓库**
```shell

$ git remote add 
<remotename> git@github:<username>/<repositoryname>.git

or
$ git remote add
<remotename> git@gitee:<username>/<repositoryname>.git

```
这里面remotename可以是远程仓库项目名称也可以自己起利于分辨的别名，username是你github或gitee的用户名地址，repositoryname是远程仓库项目名称

可以通过git remote -vv查看所有仓库和关联情况,这是我关联完github和gitee知后的remote情况
```shell
$ git remote -vv
```
![git remote -vv](https://ftp.bmp.ovh/imgs/2021/03/b0cce682ee611849.png)

**7. git push一定不会报错的git命令写法**
```shell
$ git push <远程主机名> <本地分支名>:<远程分支名>
```


