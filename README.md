# 【Python自动化训练营4期】
## （一）python脚本编写实战 
## 动态导入模块与基本函数编程
### 课后作业
原有存款 1000元， 发工资之后存款变为2000元
### 定义模块
1. money.py saved_money = 1000
2. 定义发工资模块 send_money，用来增加收入计算
3. 定义工资查询模块 select_money，用来展示工资数额
4. 定义一个start.py ，启动文件展示最终存款金额
#### [作业地址](https://gitee.com/liuchaodada/pycharmProject/tree/main/salary)
#### 运行效果![运行效果](https://s4.ax1x.com/2021/03/19/6fMHDU.png)


## （二）python脚本编写实战 
## 面对对象与函数式编程
### 课后作业
#### 1、自己写一个面向对象的例子：

比如创建一个类（Animal）【动物类】，类里有属性（名称，颜色，年龄，性别），类方法（会叫，会跑）

创建子类【猫】，继承【动物类】，

复写父类的__init__方法，继承父类的属性，

添加一个新的属性，毛发=短毛，

添加一个新的方法， 会捉老鼠，

复写父类的‘【会叫】的方法，改成【喵喵叫】

创建子类【狗】，继承【动物类】，

复写父类的__init__方法，继承父类的属性，

添加一个新的属性，毛发=长毛，

添加一个新的方法， 会看家，

复写父类的【会叫】的方法，改成【汪汪叫】

调用 name== ‘main’：

创建一个猫猫实例

调用捉老鼠的方法

打印【猫猫的姓名，颜色，年龄，性别，毛发，捉到了老鼠】。

创建一个狗狗实例

调用【会看家】的方法

打印【狗狗的姓名，颜色，年龄，性别，毛发】。

#### 2、使用yaml 来管理猫猫，狗狗的属性

#### [作业地址](https://gitee.com/liuchaodada/pycharmProject/tree/main/animal)
#### 运行效果
![屏幕截图 2021-03-23 032147.png](https://ae04.alicdn.com/kf/U9e3b7718b651488fb8d63fe2e05cb538P.jpg)
![屏幕截图 2021-03-23 032034.png](https://ae04.alicdn.com/kf/U9e3b7718b651488fb8d63fe2e05cb538P.jpg)

## （三）pytest测试框架实战 
## parameterize结合yaml参数化
### 作业

1. 补全计算器（加法，除法）的测试用例
2. 使用数据驱动完成测试用例的自动生成
3. 在调用测试方法之前打印【开始计算】，在调用测试方法之后打印【计算结束】

**坑1: 除数为0的情况**

**坑2: 自己发现**

#### [作业地址](https://gitee.com/liuchaodada/pycharmProject/tree/main/pytest_practice/calculator)
#### 运行效果
![](https://ftp.bmp.ovh/imgs/2021/04/185892637434a42d.png)


## （四）pytest+allure+jenkins测试框架实战 
## pytest fixture和 allure实战
### 作业

课后作业
1、上节课的作业，使用fixture 实现setup/teardown 功能，
2、实现 参数化的功能
3、生成测试 报告

#### [作业地址](https://gitee.com/liuchaodada/pycharmProject/tree/main/pytest_practice/allure_demo)
#### 运行效果
![](https://ftp.bmp.ovh/imgs/2021/04/542635539887bc4b.png)
![](https://ftp.bmp.ovh/imgs/2021/04/67dd4c42a1eff81b.png)
![](https://ftp.bmp.ovh/imgs/2021/04/2b9c7bbe049e40a4.png)

## （五）selenium实战 企业微信
## 复用浏览器跳过QR码免登录
### 作业

课后作业：使用序列化的方法用cookie登录企业微信

#### [作业地址](https://gitee.com/liuchaodada/pycharmProject/blob/main/selenium_practice/wechatwork_getcookies_login)
#### 运行效果
![](https://ftp.bmp.ovh/imgs/2021/04/37819024afcea507.png)
