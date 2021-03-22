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

## 



