
#  【WSL2】告别 VM ware 和 Virtual Box 拥抱WSL2 和 Docker **(必须先升级Windows 10)**

## **wsl2安装**

## 1. 如果是微软账号登录的win10预览版可以简化安装

要使用 `wsl --install` 简化安装命令，必须先完成以下要求：

- 注册登录微软账号，加入 Windows 预览体验计划。
- 安装 Windows 10 的预览版 （dev或beta）。
- 使用管理员模式打开powershell窗口。

满足这些要求后，可通过以下方式安装 WSL：

1. 在管理员模式下打开powershell，并输入以下命令：
```powershell
wsl.exe --install
```
2. 重启计算机

3. 为新的 Linux 分发版创建用户帐户和密码,可以在install命令加参数默认无密码root用户。

更多wsl命令 可以通过 `wsl --help`学习查看。


## 2. win10非预览版及1903版本以下的用户要先升级win10系统版本，再进行手动安装


### 步骤1 - 以管理员身份打开 PowerShell 并运行：

```powershell
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
```
这一步是启用windows subsystem linux（wsl）功能，执行命令之后重新启动计算机。

### 步骤 2 - 检查运行 WSL 2 的要求

若要更新到 WSL 2，需要 Windows 10 版本1903 及以上。

查看内部版本号，选择 Windows 徽标键 + R，然后键入“winver”，选择“确定”。


**重新启动** 计算机，以完成 WSL 安装并更新到 WSL 2。

### 步骤 3 - 下载 Linux 内核更新包

1. 下载最新包：
    - [适用于 x64 计算机的 WSL2 Linux 内核更新包](https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi)


2. 管理员模式运行上一步中下载的更新包。

### 步骤 4 - 将 WSL 2 设置为默认版本

打开 PowerShell，然后在安装新的 Linux 发行版时运行以下命令，将 WSL 2 设置为默认版本：

```powershell
wsl --set-default-version 2
```

### 步骤 5 - 安装所选的 Linux 分发

1. 打开 [Microsoft Store](https://aka.ms/wslstore)，并选择你偏好的 Linux 分发版。
![](https://docs.microsoft.com/zh-cn/windows/wsl/media/store.png)

2. 在分发版的页面中，选择“获取”。

![](https://docs.microsoft.com/zh-cn/windows/wsl/media/ubuntustore.png)

首次启动新安装的 Linux 分发版时，将打开一个控制台窗口，系统会要求你等待一分钟或两分钟，以便文件解压缩并存储到电脑上。 未来的所有启动时间应不到一秒。

然后，需要为新的 Linux 分发版创建用户帐户和密码。

![](https://docs.microsoft.com/zh-cn/windows/wsl/media/ubuntuinstall.png)

**祝贺你！现已成功安装并设置了与 Windows 操作系统完全集成的 Linux 分发！**


## **安装 Windows terminal （强烈建议）**


可以从 [Microsoft Store](https://aka.ms/terminal) 安装 Windows 终端。

安装终端后，它会将 PowerShell 设置为默认配置文件。

![](https://docs.microsoft.com/zh-cn/windows/terminal/images/dynamic-profiles.png)


## **安装docker-desktop 启用基于 wsl2 的docker服务**

因为wsl系统是Hyper-V虚拟内核，实现方式并非和真正的linux主机一样，所以没有systemd系统命令。

而我们这样也可以通过bat命令来启动和关闭 wsl2 服务。

```powershell
net stop LxssManager
net start LxssManager
```

而WLS2下通过apt install docker-ce命令安装的docker会只能无法启动用get-docker.sh安装docker，而且dockerd进程是用ubuntu传统的init方式而非systemd启动的，所以我不建议再在wsl2里面安装原生docker。

尽管实际工作中我们一般会在远程linux主机里安装docker服务，但对于统一运行风格，方便本地调试来说，wsl2内核的docker-desktop要比docker-windows等更方便、更有linux味、结合desktop也更加可视化。

### 步骤 1 - 下载

下载 [Docker Desktop Stable 2.3.0.2](https://hub.docker.com/editions/community/docker-ce-desktop-windows/)或更新版本。

### 步骤 2 - 安装

在 Docker 菜单中，选择 Settings > General。
![](https://docs.docker.com/docker-for-windows/images/wsl2-enable.png)

### 步骤 3 - 确认wsl分发版在wsl2模式下运行

要检查 WSL 模式，请运行:

```powershell
wsl.exe -l -v
```

要将现有的 Linux 发行版升级到 wsl2，请运行:

```powershell
wsl.exe --set-version (distro name) 2
```

要将 wsl2设置为 wsl 安装的默认版本，请运行:

```powershell
wsl.exe --set-default-version 2
```

### 步骤 4 - 设置默认启用的wsl2子系统

我们可以在wsl里安装Ubuntu CentOS RedHat等等多个wsl子系统，所以要设置docker-desktop后端运行默认在哪个子系统上。

**勾选自己对应安装要运行的wsl2子系统。**

![](https://docs.docker.com/docker-for-windows/images/wsl2-choose-distro.png)

点击Apply & Restart 应用并重新启动.

## 使用 vscode 、docker-desktop 和 wsl2开发

安装并打开 **[VSCode](https://code.visualstudio.com/Download)** 并搜索安装**Remote - WSL**插件。这个扩展允许在WSL中使用远程服务器，但是vscode仍运行在 Windows 上，这样开发的项目文件和环境变量，都在wsl2子系统的文件系统内，与我们windows本地的开发环境不冲突，解决了windows环境配置老大难的问题

现在，可以打开Windows Terminal开始使用 VSCode在wsl2内开发:

在powershell输入 

```powershell
wsl 

code .
```
或者切换tab页到对应wsl的工作目录里

```powershell
code .
```

## **参考**

主要参考了微软的官方文档和docker的docker-desktop文档

[wsl官方文档](https://docs.microsoft.com/zh-cn/windows/wsl/about)

[windows terminal官方文档](https://docs.microsoft.com/zh-cn/windows/terminal/get-started)

[docker-desktop官方文档](https://docs.docker.com/desktop/)