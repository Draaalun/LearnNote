# 前言

## 内核

**内核**（提供Linux的主要功能，如硬件调度管理的能力）+系统程序封装得到完整的Linux发行版，内核可以免费开源获取。

示例：**Ubuntu**、deepin、红旗、**centos**。

基础命令相同，部分操作不同（如安装软件方式）

## 虚拟机

模拟虚拟硬件配置真实的操作系统得到虚拟机。

安装应用VM虚拟机，下载centos操作系统iso文件，虚拟机中创建虚拟机使用iso文件创建虚拟机。

<img src="D:\DeskTop\learn\linux\image-20240628110442702.png" alt="image-20240628110442702" style="zoom:67%;" />

## FinalShell

​	命令行使用便捷程度远超图形化界面，在VMware中使用命令行不方便所以使用FinalShell远程连接到Linux，直接在Windows中操作Linux。连接需要用到IP地址，端口号，Linux账号和密码。https://www.hostbuf.com/t/988.html

​	ifconfig查看IP，FinalShell中添加SSH连接Linux系统。重启虚拟机IP地址会发生变化。

## WSL

windows subsystem for linux，在windows操作系统中换取Linux系统环境，并且直连计算机硬件，不需要虚拟机虚拟硬件。

## 虚拟机快照

通过快照将当前的虚拟机的状态保存下来在之后通过快照恢复到虚拟机之前保存的状态。

<img src="C:\Users\21998\AppData\Roaming\Typora\typora-user-images\image-20240628190349136.png" alt="image-20240628190349136" style="zoom:67%;" />

# 小工具

ctrl + c 强制停止某些运行程序；

ctrl+d 退出账号的登陆（不能退出vim）；

history 查看原先的命令；

！+命令前缀自动向上搜索匹配前缀的命令；

ctrl+r输入内容去匹配历史命令，回车直接执行，左右键可以得到此命令但不执行；

ctrl+a跳到命令开头；

ctrl+e跳到命令结尾；

ctrl+左键向左跳一个单词；

ctrl+右键向右跳一个单词；

ctrl+l 可以清除终端内容，通过命令clear可以得到一样的效果；



# 命令行

## 目录

只有一个顶级目录就是**根目录 /**，Linux中层级关系用/来表示关系，windows操作系统中使用\来表示层级关系，有c盘等好几个根目录。

例：/user/hello.txt  1.开头/表示根目录 2.后面的/表示层级关系。

## 基本命令格式

commamd [-options] [parameter]

1.command 命令本身

2.-options命令的一些**选项**，可以通过选项控制命令的行为细节

3.para 命令的参数 多数用于命令的**指向目标**

ls -l /home  以列表形式显示home中的文件

cp -r test1 test2  复制test1文件成为test2

## ls命令

ls -a -l -h 路径（从当前路径算起）

ls不指定路径会列出当前文件夹下的所有内容，默认会设置在/home/用户名

-a列出全部文件，包含隐藏文件；

 -l以列表的形式展示文件信息，展示更多信息 ，选项可以组合使用-l -a，-la，-al；

-h 已阅读的形式显示文件大小 与-l配合使用 ls -lh。

## cd/pwd

cd+路径,切换到指定目录，直接执行到home目录下。

pwd print work directory  查看当前工作目录。

## 绝对路径相对路径

绝对路径 cd /home/dralun/Desktop 以根目录作为起点；

相对路径 cd  cd/Desktop 以当前目录作为起点。

返回上一级 cd..

特殊符号 

1. cd ./Desktop切换到当前目录下的Desktop内效果同cd Desktop
2. cd ..返回上一级目录，cd ../..切换回上两级目录
3. cd ~切换回home目录，cd ~/Desktop切换回home目录下的Desktop中。

## mkdir

make directory

mkdir -p 路径，-p表示可以创建不存在的父目录，相对和绝对路径都可以使用，

创建文件夹需要权限，在home目录外操作涉及权限，home目录内做什么都可以。

## 文件操作命令

### touch

touch Linux路径 ，创建文件

touch test.txt 相对目录下创建文件（是文件不是文件夹）

### cat

查看文件内容（不使用编辑器）

cat test.txt

more 同cat作用也是只需要参数路径，支持翻页，文件内容过多可以一页页显示，通过空格翻页，按q退出。

### cp、mv和rm

1. cp -r  参数一 参数二，复制文件和文件夹，-r可选，用于复制文件夹使用，表示递归，参数一表示被复制的文件和文件夹，参数二表示要复制去的地方。

2. mv 参数一 参数二 用于移动文件夹或者文件，参数一被移动的文件或者文件夹参数二移动取得地方；mv test.txt test2.txt 对于移动目标不存在的，把原文件作为新的存在。

3. rm -r-f  参数....，文件和文件夹的删除remove，一次性可以删除很多文件和文件夹，按照空格隔开。-r用于删除文件夹，-f表示强制删除。**支持用符号*模糊匹配任意内容包含空**，test\*表示匹配任何以test开头的内容，\*test表示任何以test结束的内容，\*test\*表示任何包含test的内容。root用户才会使用-f，su - root进入root，exit退出。

## 查找命令which、find

1. which +要查找的命令，查看所使用的一些列命令的系统文件放在哪里。

   [dralun@localhost ~]$ which cd
   /usr/bin/cd

2. find 起始路径 -name “被查找文件名” 

   [root@localhost ~]# find / -name test
   find: ‘/proc/51955’: No such file or directory
   find: ‘/run/user/1000/gvfs’: Permission denied
   /usr/bin/test
   /usr/lib/modules/3.10.0-957.el7.x86_64/kernel/drivers/ntb/test
   /usr/lib/alsa/init/test
   /usr/lib64/python2.7/test
   /usr/lib64/python2.7/unittest/test
   /usr/share/espeak-data/voices/test
   /usr/src/kernels/3.10.0-957.el7.x86_64/drivers/ntb/test
   /usr/src/kernels/3.10.0-957.el7.x86_64/include/config/test
   /usr/src/kernels/3.10.0-957.el7.x86_64/lib/raid6/test
   /home/dralun/dralun/test

   **也支持使用*作模糊搜索**

​	find 起始路径 -size +|-n [kMG]

​	+和-分表表示大于和小于，n表示大小数字，kMG表示大小单位，k表示kb，M表示MB，G表示GB

​	find / -size -10k查找根目录下小于10KB的文件 ，find / -size +100M查找根目录下大于100M的文件 

## grep、wc和管道符

1.通过grep命令，从文件中通过关键字过滤文件行。

grep -n 关键字 文件路径，-n可选，表示在结果中显示匹配行的行号；关键字必填，特殊符号用“”包围起来；文件路径被过滤内容的文件路径，可作为内容输入端口。

[dralun@localhost ~]$ touch test.txt
[dralun@localhost ~]$ cat test.txt
789
456
123
[dralun@localhost ~]$ grep 12 test.txt
123

[dralun@localhost ~]$ grep -n 12 test.txt
3:123

2.wc -c-m-l-w 文件路径

-c统计字节数量 -m统计字符数量 -l统计行数 -w统计单词数量  参数文件路径

3.管道符

将|左边的结果作为右边命令的输入。

[dralun@localhost ~]$ cat test.txt |grep -n 123
3:123

[dralun@localhost ~]$ ls /usr/bin | grep gtf
gtf   //在一个文件夹若干结果中筛选出gtf。

[dralun@localhost ~]$ ls -l /usr/bin | wc -l
1720  //利用ls -l列出文件行数 通过wc -l统计行数 得出文件数量

## echo、tail和重定向符

1.echo输出的内容，使用echo命令在命令行内输出指定内容，无需选项只有一个参数表示要输出的内容。

[dralun@localhost ~]$ echo hello wrold
hello wrold
[dralun@localhost ~]$ echo "hello world"
hello world
[dralun@localhost ~]$ echo \"hello world\"
"hello world"

[dralun@localhost ~]$ echo pwd
pwd
[dralun@localhost ~]$ pwd
/home/dralun
[dralun@localhost ~]$ echo **\`pwd`**
/home/dralun

2.重定向符

\>将左侧命令的结果覆盖写入到符号右侧指定的文件中

\>>将左侧命令的结果追加写入到符号右侧指定的文件中

[dralun@localhost ~]$ echo hello >> test.txt 
[dralun@localhost ~]$ cat test.txt
789
456
123
hello

[dralun@localhost ~]$ echo "gap" > test.txt 
[dralun@localhost ~]$ cat test.txt
gap

3.tail命令

tail -f -num Linux路径 ，查看文件尾部内容，跟踪文件的最新更改

-f表示持续跟踪，-num表示查看尾部多少行，默认10行

[dralun@localhost ~]$ ls >test.txt
[dralun@localhost ~]$ cat test.txt
Desktop
Documents
Downloads
Music
Pictures
Public
Templates
test.txt
Videos
[dralun@localhost ~]$ tail -3 test.txt
Templates
test.txt
Videos
[dralun@localhost ~]$ tail -f test.txt
Desktop
Documents
Downloads
Music
Pictures
Public
Templates
test.txt
Videos

持续跟踪中。。。

**小结**

[dralun@localhost ~]$ echo "我当前的工作目录是:\`pwd`">>test.txt
[dralun@localhost ~]$ cat test.txt
我当前的工作目录是:/home/dralun

## vi\vim编辑器

​	visual interface的简称，是Linux中最经典的文本编辑器，vi在命令行下对文本文件进行编辑。命令行模式下的文本编辑器。

1. 命令模式，所敲的按键编辑全部理解为命令；  
2. 输入模式，可以对文件内容进行自由编辑；
3. 底线命令模式，通常用于文件的保存和退出。

vi filename 进入命令模式，

，，，i a o进入输入模式，esc退出输入模式 ，，， 输入：进入底线命令模式，回车结束运行；，，，

wq退出命令模式。

​	**vi 文件路径 vim文件路径**，文件不存在此命令用于编辑新文件 ，文件存在编辑已有文件。

vim hello.txt 进入命令模式

i 进入插入模式， esc 返回退出，dd删除一行 ，ndd从当前行开始向下删除n行，yyp复制一行，u撤销，/搜索模式n向下继续搜索N向上继续搜索，yy复制当前行，p粘贴当前内容，ctrl+r反向撤销，gg光标到首行，G到行尾，dG当前行开始到最后行都删除，dgg从当前行开始向上都删除，d$从当前光标删除到本行结束，d0删除到行首。

：进入底线模式，此模式下wq保存并退出，q仅退出，q！强制退出，w仅仅保存，set nu显示行号。

# Linux用户和权限

## root

超级管理员，root，有系统最大操作权限，

普通用户只在home目录下创建文件夹，出了home目录大多数地方普通用户只有只读和执行权限无修改原则。

su - 用户名，-可选择，在切换用户后加载环境变量，参数用户名表示要切换的用户，exit回退到上一个用户；su - root获取root权限。

sudo 其他命令，在普通用户身份下临时获得root权限；切换到root用户执行visudo，自动通过vi编辑器打开/etc/sudoers，在文件最后添加dralun ALL=(ALL)        NOPASSWD: ALL

## 用户和用户组

针对用户的权限控制和针对用户组的权限控制。

root下创建用户组：groupadd ，groupdel；

创建用户：useradd -g -d 用户名，-g指定用户的组（不使用默认创建一个同名字组	），-d指定用户的home路径（默认在home下）；

删除用户：userdel -r 用户名，删除用户，-r不保留home目录；

id用户名，用户名是指被查看的用户；

usermod -aG 用户组用户名 ，把指定的用户加入到指定的用户组里。

getent passwd查看当前系统中有哪些用户（是passwd）。

getent group 查看系统中有哪些组。

## 查看权限管控信息

[dralun@localhost ~]$ ls -l
总用量 0
drwxr-xr-x. 2 dralun dralun 6 6月  27 20:02 Desktop
drwxr-xr-x. 2 dralun dralun 6 6月  27 20:02 Documents
drwxr-xr-x. 2 dralun dralun 6 6月  27 20:02 Downloads
drwxr-xr-x. 2 dralun dralun 6 6月  27 20:02 Music
drwxr-xr-x. 2 dralun dralun 6 6月  27 20:02 Pictures
drwxr-xr-x. 2 dralun dralun 6 6月  27 20:02 Public
drwxr-xr-x. 2 dralun dralun 6 6月  27 20:02 Templates
drwxr-xr-x. 2 dralun dralun 6 6月  27 20:02 Videos

1. -表示文件 d表示文件夹 l表示软链接
2. 第2-4位表示所属用户权限，rwx（没有权限标记位-，下同），read write execute（cd进入）
3. 5-7表示用户组权限，rwx
4. 8-10表示其他用户权限，rwx

如drwxr-xr-x，表示：文件夹，所属用户权限rwx，所属用户组权限rx，其他用户权限rx权限。

## 权限chmod、chown

1.chmod命令

修改文件、文件夹的权限信息，只有文件、文件夹的所属用户或者root用户可以修改。

chmod -R 权限 文件或文件夹。-R对文件夹内的所有内容应用相同的操作，

chmod u=rwx，g=rx，o=x hello.txt，（user group other），将文件权限修改为rwxr-x--x

chomd -R u=rwx，g=rx，o=x test，对文件夹test内的所有我呢见设置权限内容位，，，

快捷修改 chmod 751 hello.txt（每个数字对应rwx三位二进制）

2.chown命令

修改文件、文件夹的所属用户和用户组，普通用户无法修改所属为其他用户或组，此命令值适用于root用户执行。

chown -R 用户：用户组 文件或文件夹，

示例：chown root hello.txt修改hello.txt所属用户为root ，chown ：root hello.txt修改hello.txt所属用户组为root；

chown root：dralun hello.txt修改hello.txt所属用户为root，用户组修改为dralun；-R将文件夹内的所有内容适用。

# yum | apt



yum -y [install | remove | saerch]

-y 自动确认 无需手动确认安装或者卸载过程 

需要root权限或者使用sudo 。 yum install wget

Ubuntu使用apt代替yum

# systemctl命令

systemctl start|stop|status|enable|disable 服务名

NetworkManager 主网络服务 network 副网络服务 firewalld 防火墙 sshd ssh服务

# ln -s 参数1 参数2

-s创建软连接 参数一被链接的文件或文件夹 参数二要链接取得目的地

ln -s /etc/yum ~/yum 构建了快捷方式，可以链接文件或者文件夹

# date

date -d 格式化字符

1. %Y年
2. %y年后两位数字
3. %M月份
4. %d日
5. %H小时
6. %M分钟
7. %S秒
8. %s自从1970-01-01 00：00：00 UTC到现在的秒数

# IP

![image-20240705112447595](D:\DeskTop\learn\Linux\image-20240705112447595.png)

​	ens33是虚拟机使用的网卡，centos一般都是，；192.168.172.137IP地址；127.0.0.1 指代本机通讯目标是自己的时候；0.0.0.0指代本机，可以在端口绑定中确定绑定关系，在一些IP限制地址中表示允许IP的意思。

​	主机名，win和Linux都有，hostname查看主机名，hostnamectl set-hostname 新的主机名 重新设置主机名。

访问www。baidu.com--检查系统中的hosts文件是否有对应网址的IP--有直接访问IP|没有联网询问公开的DNS服务器是否有记录IP地址

​	域名解析，主机名映射，通过主机名字找到对应的计算机的IP地址，多保存在HOSTS文件夹中。

# Linux配置IP

​	用虚拟机启动Linux，由DHCP动态获取IP地址，即每次重启设备后获取一次，可能导致IP地址的频繁变更。如果远程链接LInux回很麻烦。

[dralun@localhost ~]$ su - root
Password: 
Last login: Fri Jul  5 03:24:23 UTC 2024 on pts/0
[root@localhost ~]# vim /etc/sysconfig/network-scripts/ifcfg-ens33
[root@localhost ~]# systemctl restart network

在root中进行修改ens33文件，修改DHCP为静态static，添加

IPADDR=192.168.88.130
NETMASK=255.255.255.0
GATEWAY=192.168.88.2
DNS1=192.168.88.2

# 网络传输

## ping

ping [-c num] ip或主机名

[dralun@localhost ~]$ ping -c 3 baidu.com 
PING baidu.com (110.242.68.66) 56(84) bytes of data.
64 bytes from 110.242.68.66 (110.242.68.66): icmp_seq=1 ttl=128 time=41.1 ms
64 bytes from 110.242.68.66 (110.242.68.66): icmp_seq=2 ttl=128 time=41.9 ms
64 bytes from 110.242.68.66 (110.242.68.66): icmp_seq=3 ttl=128 time=42.3 ms

[dralun@localhost ~]$ ping -c 3 110.242.68.66
PING 110.242.68.66 (110.242.68.66) 56(84) bytes of data.
64 bytes from 110.242.68.66: icmp_seq=1 ttl=128 time=43.9 ms
64 bytes from 110.242.68.66: icmp_seq=2 ttl=128 time=41.1 ms
64 bytes from 110.242.68.66: icmp_seq=3 ttl=128 time=42.5 ms

[dralun@localhost ~]$ ping -c 3 192.168.88.5
PING 192.168.88.5 (192.168.88.5) 56(84) bytes of data.
From 192.168.88.130 icmp_seq=1 Destination Host Unreachable
From 192.168.88.130 icmp_seq=2 Destination Host Unreachable
From 192.168.88.130 icmp_seq=3 Destination Host Unreachable

[dralun@localhost ~]$ ping -c 3 google.cn
PING google.cn (220.181.174.34) 56(84) bytes of data.
64 bytes from 220.181.174.34 (220.181.174.34): icmp_seq=1 ttl=128 time=25.2 ms
64 bytes from 220.181.174.34 (220.181.174.34): icmp_seq=2 ttl=128 time=26.4 ms
64 bytes from 220.181.174.34 (220.181.174.34): icmp_seq=3 ttl=128 time=26.4 ms

## wget命令

wget -b url

-b 可选后台下载，将日志写入当前工作目录的wget-log文件 url下载链接

## curl 

curl -O url 发起一个网络请求

-O可选用于下载文件 url 要发起请求的网络地址

[dralun@localhost ~]$ curl cip.cc
IP      : 140.75.184.119
地址    : 中国  山东  青岛
运营商  : 电信

数据二  : 山东省青岛市 | 电信

数据三  : 中国山东省烟台市 | 电信

URL     : http://www.cip.cc/140.75.184.119


[dralun@localhost ~]$ curl www.baidu.com

<!DOCTYPE html>
<!--STATUS OK--><html> <head><meta http-equiv=content-type content=text/html;charset=utf-8><meta http-equiv=X-UA-Compatible content=IE=Edge><meta content=always name=referrer><link rel=stylesheet type=text/css href=http://s1.bdstatic.com/r/www/cache/bdorz/baidu.min.css><title>百度一下，你就知道</title></head> <body link=#0000cc> <div id=wrapper> <div id=head> <div class=head_wrapper> <div class=s_form> <div class=s_form_wrapper> <div id=lg> <img hidefocus=true src=//www.baidu.com/img/bd_logo1.png width=270 height=129> </div> <form id=form name=f action=//www.baidu.com/s class=fm> <input type=hidden name=bdorz_come value=1> <input type=hidden name=ie value=utf-8> <input type=hidden name=f value=8> <input type=hidden name=rsv_bp value=1> <input type=hidden name=rsv_idx value=1> <input type=hidden name=tn value=baidu><span class="bg s_ipt_wr"><input id=kw name=wd class=s_ipt value maxlength=255 autocomplete=off autofocus></span><span class="bg s_btn_wr"><input type=submit id=su value=百度一下 class="bg s_btn"></span> </form> </div> </div> <div id=u1> <a href=http://news.baidu.com name=tj_trnews class=mnav>新闻</a> <a href=http://www.hao123.com name=tj_trhao123 class=mnav>hao123</a> <a href=http://map.baidu.com name=tj_trmap class=mnav>地图</a> <a href=http://v.baidu.com name=tj_trvideo class=mnav>视频</a> <a href=http://tieba.baidu.com name=tj_trtieba class=mnav>贴吧</a> <noscript> <a href=http://www.baidu.com/bdorz/login.gif?login&amp;tpl=mn&amp;u=http%3A%2F%2Fwww.baidu.com%2f%3fbdorz_come%3d1 name=tj_login class=lb>登录</a> </noscript> <script>document.write('<a href="http://www.baidu.com/bdorz/login.gif?login&tpl=mn&u='+ encodeURIComponent(window.location.href+ (window.location.search === "" ? "?" : "&")+ "bdorz_come=1")+ '" name="tj_login" class="lb">登录</a>');</script> <a href=//www.baidu.com/more/ name=tj_briicon class=bri style="display: block;">更多产品</a> </div> </div> </div> <div id=ftCon> <div id=ftConw> <p id=lh> <a href=http://home.baidu.com>关于百度</a> <a href=http://ir.baidu.com>About Baidu</a> </p> <p id=cp>&copy;2017&nbsp;Baidu&nbsp;<a href=http://www.baidu.com/duty/>使用百度前必读</a>&nbsp; <a href=http://jianyi.baidu.com/ class=cp-feedback>意见反馈</a>&nbsp;京ICP证030173号&nbsp; <img src=//www.baidu.com/img/gs.gif> </p> </div> </div> </div> </body> </html>

（返回的一个完整的网页，和浏览器输入地址打开网站是一样的）

## 端口

物理端口和虚拟端口；

计算机A-计算机B通过IP地址即可，但是A和B里面的程序不够精确，赋予程序端口号，A的某一端口访问B的某一端口。

Linux

1. 端口1-1023 公认端口，通常系统内置或者知名程序内留，SSH服务22端口，HTTPS端口的443端口，非特殊需要不要占领这个端口；
2. 注册端口1024-49151 通常随意使用，可以自行设置，松散的绑定一些程序；
3. 动态端口：49152-65535通常不会固定绑定程序，当程序对外进行网络链接时用于临时使用。多用于流量向外发送使用。

# 进程管理

程序运行中被操作系统管理，每一个程序运行便被系统注册为系统中的一个进程，并未每一个进程分配了一个独有的ID进程号。PID

ps -ef

[root@localhost ~]# ps -ef
UID         PID   PPID  C STIME TTY          TIME CMD
root          1      0  0 05:12 ?        00:00:04 /usr/lib/systemd/systemd --switched-root --system --deserialize 22
root          2      0  0 05:12 ?        00:00:00 [kthreadd]
root          3      2  0 05:12 ?        00:00:06 [ksoftirqd/0]
root          5      2  0 05:12 ?        00:00:00 [kworker/0:0H]
root          7      2  0 05:12 ?        00:00:00 [migration/0]
root          8      2  0 05:12 ?        00:00:00 [rcu_bh]
root          9      2  0 05:12 ?        00:00:11 [rcu_sched]

...

uid所属用户的ID； PID进程的ID号 ；PPID 进程的父ID ；C此时的CPU占有率； STIME进程的启动时间；TTY启动此进程的终端序号，？表示非终端启动；TIME进程占用CPU的时间 累计；CMD进程的启动命令或路径。

kill -9 进程ID 

-9表示强制关闭。

# 主机状态

## **top查看CPU内存使用情况**

![image-20240705173438350](D:\DeskTop\learn\Linux\image-20240705173438350.png)

1. top - 09:36:17当前系统时间 up  4:23启动了4.23分,  3 users三个用户登录,  load average: 0.08, 0.09, 0.17 1、5和15分钟负载
2. Tasks: 207 total：共计207个进程,   2 running:一个正在运行, 205 sleeping：205个进程休眠,   0 stopped：0个进程停止,   0 zombie：0个僵尸进程
3. %Cpu(s):  4.0 us：用户CPU的使用率,  6.7 sy：系统CPU使用率,  0.0 ni：高优先级进程占CPU时间百分比, 88.9 id：空闲CPU率,  0.0 wa：IO等待CPU占用率,  0.0 hi：CPU硬件中断率,  0.3 si：CPU软件中断率,  0.0 st：强制等待CPU占用CPU率
4. KiB Mem 物理内存:   995896 total总量：,    79016 free空闲,   520108 used使用,   396772 buff/cache占用
5. KiB Swap虚拟内存:  2098172 total,  1907964 free,   190208 used.   229872 avail Mem 
6. 表格：PR优先级越小越高，NI负值表示高优先级，VIRT使用的虚拟内存，RES使用物理内存，SHR进程使用共享内存，S进程状态S休眠R运行Z僵尸N负数I空闲，TIME+进程使用CPU时间，COMMAND进程的命令或者路径
7. top -p 只显示某个进程-d设置刷新时间-c显示产生进程的完整命令-n指定刷新次数-i不显示闲置或无用进程-u查找特定用户启动的进程

## **磁盘监控**

 iostat 查看CPU、磁盘的相关信息，iostat -x num1 num2 ，-x显示更多信息，num1刷新间隔 num2刷新几次

[root@localhost ~]# iostat -x
Linux 3.10.0-957.el7.x86_64 (localhost.localdomain)     07/05/2024      _x86_64_        (1 CPU)

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           4.36    0.01    6.33    0.25    0.00   89.05

Device:         rrqm/s   wrqm/s     r/s     w/s    **rkB**/s    **wkB**/s avgrq-sz avgqu-sz   await r_await w_await  svctm  %**util**
sda               0.68     3.14    4.34    0.80   216.05    20.36    91.98     0.02    4.85    5.50    1.33   1.49   0.76

## **网络状态监控**

sar -n DEV num1 num2

-n查看网络 DEV表示查看网络接口 num1刷新间隔 num2刷新次数

# 环境变量

env查看环境变量

[root@localhost ~]# env | grep PATH
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin:/root/bin

执行cd命令时从高到低搜索，PATH中记录了路径。：用于隔开。添加PATH export PATH=$PATH :自定义路径。

$

[root@localhost ~]# echo $PATH
/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin:/root/bin
[root@localhost ~]# echo $PWD
/root

通过$取到环境变量

用途：记录的程序路径使程序在任何地方都可以执行到。

临时设置：export 变量名=变量值；

[root@localhost ~]# export myName=dralun
[root@localhost ~]# echo $myName
dralun

永久生效：

针对某一用户：在~/.bashrc内添加export MYNAME=dralun，source .bashrc

全局环境变量:vi  /etc/profile,添加export MYNAME=dralun，source .bashrc

# 上传和下载

## 下载

在finalshell中对文件右击可以下载。

<img src="C:\Users\21998\AppData\Roaming\Typora\typora-user-images\image-20240705183804561.png" alt="image-20240705183804561" style="zoom: 50%;" />

这里可以更改dralun为root从而下载root权限的内容。

## 上传

拖拽就行。。。

# 压缩和解压

## 压缩

tar

.tar将文件简单封装在一个tar文件内没有压缩

.gz使用gzip压缩算法将文件压缩到一个文件内

tar -c-v-x-f-z-C 参数1...N

1. c创建压缩文件 
2. v显示压缩解压过程查看进度 
3. x解压模式
4.  f要创建或要解压的文件 在所有选项中必须位于最后一个  
5. z不使用z就是普通的打包模式C选择解压的目的地。

tar -cvf test.tar 1.txt 2.txt

tar -zcvf test.tar.gz 1.txt 2.txt

## 解压

tar -xvf test.tar -C /home/dralun

tar -zxvf test.tar.gz -C /home/dralun

## zip

zip -r 参数1...N

-r 被压缩的包含文件夹的时候需要使用，

zip test.zip a.txt c.txt b.txt将abc压缩到test.zip中来.

zip test.zip test c.txt b.txt将abc压缩到test.zip中来.

unzip -d 参数指定解压位置
