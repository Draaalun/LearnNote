# **Keil5 // STC-ISP**

## 原理图

STC51 // 8位 // RAM 512字节（B） // ROM 8K（Flash）//工作频率：12MHz。

![image-20240410181044229](D:\DeskTop\learn\51\image\image-20240410181044229.png)

<img src="D:\DeskTop\learn\51\image\image-20240410181341023.png" alt="image-20240410181341023" style="zoom:50%;" />

<img src="D:\DeskTop\learn\51\image\image-20240410182333671.png" alt="image-20240410182333671" style="zoom:50%;" />

C5C6用来滤波，去除电源的不稳定因素；

#### **最小系统**：

**晶振**（18，19）、**电源**vcc40接地20、**复位电路**9(高电平复位，电源开通电容瞬间相当于短路，为高电平，随后充电变为低电平)。

#### 点亮灯泡：

```c
#include <REGX52.H>
void main(){
	P2=0xFE;//1111 1110需要转换为十六进制或十进制，用十六进制
}
```

#### 闪烁灯泡：

```c
#include <REGX52.H>
#include <INTRINS.H>
void main(){
    while(1)//while才能保证程序一直在循环
    {
        P2=0xFE;
        Delay500ms();
    	P2=0xFF;
        Delay500ms();
    }
}
void Delay500ms(void)	//@12MHz
{
	unsigned char data i, j, k;

	_nop_();
	i = 4;
	j = 205;
	k = 187;
	do
	{
		do
		{
			while (--k);
		} while (--j);
	} while (--i);
}
```

#### **流水灯：**

```c
#include <REGX52.H>
#include <INTRINS.H>
void Delay500ms(void)	//@12MHz
{
	unsigned char data i, j, k;

	_nop_();
	i = 4;
	j = 205;
	k = 187;
	do
	{
		do
		{
			while (--k);
		} while (--j);
	} while (--i);
}
void main(){
    while(1)
    {
        P2=0xFE;
        Delay500ms();
    	P2=0xFD;
        Delay500ms();
        P2=0xFB;
        Delay500ms();
        P2=0xF7;
        Delay500ms();
        P2=0xEF;
        Delay500ms();
        P2=0xDF;
        Delay500ms();
        P2=0xEF;
        Delay500ms();
        P2=0x7F;
        Delay500ms();
    }
}

```

#### 流水灯PULS

```c
#include <REGX52.H>
#include <INTRINS.H>
void Delay1ms(unsigned int xms)	//@12.000MHz
{
	unsigned char data i, j;
	while(xms)
	{
	    i = 2;
    	j = 239;
    	do
    	{
    	while (--j);
    	} while (--i);
		xms--;
	}
}
void main(){
    while(1)
    {
        P2=0xFE;
        Delay1ms(500);
    	P2=0xFD;
        Delay1ms(500);
        P2=0xFB;
        Delay1ms(500);
        P2=0xF7;
        Delay1ms(500);
        P2=0xEF;
        Delay1ms(500);
        P2=0xDF;
        Delay1ms(500);
        P2=0xEF;
        Delay1ms(500);
        P2=0x7F;
        Delay1ms(500);
    }
}
```

## 51内存图

1.单片机上电IO口默认高电平；按键接地，导通时IO口为低电平，可以传到MCU；

2.sfr （Special Function Register特殊功能寄存器）似乎不是标准C 语言的关键字，而是Keil 为能直接访问80C51 中的SFR 而提供了一个新的关键词，其用法是：sfrt 变量名=地址值；如sfr P0 = 0x80，这样的一行即定义P1 与地址0x90 对应，P1 口的地址就是0x90，SFR的定义在头文件reg51.h或reg52.h中；

3.单片机头文件<REGX51.H>（存在REG51.H但是没有对位进行声明如不能直接使用P2_2）中定义了**21个特殊功能寄存器**，并且都是8位寄存器，而部分寄存器的每个位又用sbit进行了定义：
![img](D:\DeskTop\learn\51\image\56ed50d86f554f199b96e243e92251b6.jpeg)

1. 第0，1，2，3组，四个工作寄存器组，每个都包含8个8位寄存器；

2. 位寻址区，128bit，共16个byte，每一位都可以直接读地址来修改数值；

3. 堆栈区，80byte程序执行中动态分配和释放内存空间，堆栈区的大小通常可以使用SP指针来控制；

4. STR区：

   ```c
   1.P0-P3 每个端口有8个引脚，可以配置输入或输出，可以改变引脚的状态；
   2.TCON 定时器/计数器控制寄存器，用于控制定时器和计数器的工作模式、中断标志和计数器溢出标志等。
   3.TMOD：这是定时器/计数器模式寄存器，用于配置定时器和计数器的工作模式，例如定时器模式、计数器模式、自动重装载模式等。
   4.PCON：这是电源控制寄存器，用于控制微控制器的电源模式和复位。
   5.TH0/TL0、TH1/TL1：这些是定时器/计数器的高位和低位寄存器，用于存储定时器和计数器的计数值。
   6.SCON：这是串口控制寄存器，用于配置串口通信的工作模式、波特率、发送和接收中断等。
   7.IE/IP：这些是中断使能和中断优先级寄存器，用于控制中断的使能和优先级设置。
   8. PSW：这是程序状态字寄存器，用于存储和控制程序执行的状态信息，例如标志位、堆栈指针等。
   ```

   #### 按键控制LED
   
   <img src="D:\DeskTop\learn\51\image\image-20240411095934314.png" alt="image-20240411095934314" style="zoom:33%;" />

```c
#include <REGX52.H>
void main(){
//	P2_0=0;//直接点亮一位灯；
    while(1){
		if(P3_1==0){
            P2_0=0;
        }
        else{
			P2_0=0;
        }
    }
}
```

#### 消除按键抖动

```c
 while(1){
        if(P3_1==0){
            Delay1ms(20);
            while(P3_1==0);
            Delay1ms(20);
       }
```

```c
#include <REGX52.H>
void Delay1ms(unsigned int xms)	//@12.000MHz
{
	unsigned char data i, j;
	while(xms--)
	{
	    i = 2;
    	j = 239;
    	do
    	{
    	while (--j);
    	} 
        while (--i);
	}
}
void main(){
    unsigned char LEDNum=0;
    while(1){
        if(P3_1==0){
            Delay1ms(20);
            while(P3_1==0);
            Delay1ms(20);
            
            LEDNum++;
            P2_0=~LEDNum;
        }
    }
}
```

```c
#include <REGX52.H>//P3_1和P3_0按键分别使LED灯左移或者右移；
void main(){
    unsigned char LEDNum=0;
    while(1){
        if(P3_1==0){
            
            Delay1ms(20);
            while(P3_1==0);
            Delay1ms(20);
            
            LEDNum++;
            if(LEDNum>=8){
				LEDNum=0;
            }
            P2=~(0x01<<LEDNum);
        }
        if(P3_0==0){
            
            Delay1ms(20);
            while(P3_0==0);
            Delay1ms(20);
            
            if (LEDNum==0){
				LEDNum=7;
            }
            else{
                LEDNum--;
            }
            P2=~(0x01<<LEDNum);
        }
    }
}
```

#### 静态数码管

<img src="D:\DeskTop\learn\51\image\image-20240411111940120.png" alt="image-20240411111940120" style="zoom: 50%;" /><img src="D:\DeskTop\learn\51\image\image-20240411123530636.png" alt="image-20240411123530636" style="zoom:50%;" />

前面接一个74138译码器，把三位输出接到LED1~LED8，共阴极接法，直接使用即可。74HC245为双向数据缓冲器，DIR高电平数据从左到右，反之从右向左，相当于放大了驱动信号。

```c
#include <RGEX52.H>
unsigned char NixieTable[]={0x3F,0x06,0x5B,0x4F,0x66,0x6D,0x7D,0x07,0x7F,0x6F};
void Nixie(unsigned char Location,Number){
    switch(Location){//38译码器
        case 1: P2_4=1;P2_3=1;P2_2=1;break;
        case 2: P2_4=1;P2_3=1;P2_2=0;break;
        case 3: P2_4=1;P2_3=0;P2_2=1;break;
        case 4: P2_4=1;P2_3=0;P2_2=0;break;
        case 5: P2_4=0;P2_3=1;P2_2=1;break;
        case 6: P2_4=0;P2_3=1;P2_2=0;break;
        case 7: P2_4=0;P2_3=0;P2_2=1;break;
        case 8: P2_4=0;P2_3=0;P2_2=0;break;
    }
    P0=NixieTable[Number];
}
void main(){
    Nixie(3,3);
    while(1){
    }
}
```

#### 动态数码管显示

```c
#include <REGX52.H>
//数码管段码表
unsigned char NixieTable[]={0x3F,0x06,0x5B,0x4F,0x66,0x6D,0x7D,0x07,0x7F,0x6F};
//延时子函数
void Delay(unsigned int xms)
{
	unsigned char i, j;
	while(xms--)
	{
		i = 2;
		j = 239;
		do
		{
			while (--j);
		} while (--i);
	}
}
//数码管显示子函数
void Nixie(unsigned char Location,Number)
{
	switch(Location)		//位码输出
	{
		case 1:P2_4=1;P2_3=1;P2_2=1;break;
		case 2:P2_4=1;P2_3=1;P2_2=0;break;
		case 3:P2_4=1;P2_3=0;P2_2=1;break;
		case 4:P2_4=1;P2_3=0;P2_2=0;break;
		case 5:P2_4=0;P2_3=1;P2_2=1;break;
		case 6:P2_4=0;P2_3=1;P2_2=0;break;
		case 7:P2_4=0;P2_3=0;P2_2=1;break;
		case 8:P2_4=0;P2_3=0;P2_2=0;break;
	}
	P0=NixieTable[Number];	//段码输出
	Delay(1);				//显示一段时间
	P0=0x00;				//段码清0，消影//位选 段选 清零//
}
void main()
{
	while(1)
	{
		Nixie(1,1);		//在数码管的第1位置显示1
//		Delay(20);
		Nixie(2,2);		//在数码管的第2位置显示2
//		Delay(20);
		Nixie(3,3);		//在数码管的第3位置显示3
//		Delay(20);
	}
}
```

上述为单片机直接扫描，硬件设备简单并且会耗费大量的CPU时间，单片机一旦不扫描了就完蛋；

专用驱动芯片如TM1640，单片机只需要告诉他显示什么即可。（74HC595）。

#### 模块化编程

​	把主函数模糊化，分出来每个模块完成自己的功能，分出来的每个文件都是.c文件，用.h文件提供可供外部调用的函数声明，其他函数想使用其中代码时，只需要#include “XXXX.h”文件即可。

​	**预编译在代码开始之前对代码进行一些处理**：

1. #include xx.h就是把xx.h的文件内容复制粘贴过来；
2. #define PI 3.14宏定义 
3. #ifndef `__DELAY_H__`如果没有定义
4. #ifdef 若果...才进行编译；
5. #endif 与#ifndef #if匹配组成“括号”
6. 引用声明文件<>和“”的原因是，前者在安装目录下后者在自己的文件夹里。
7. 最好main.c 、Delay.c  Delay.h 和 Nixie.c  Nixie.h放在一起。

**上述代码模块化：**

```c
Delay.c
void Delay(unsigned int xms)
{
	unsigned char i, j;
	while(xms--)
	{
		i = 2;
		j = 239;
		do
		{
			while (--j);
		} while (--i);
	}
}
```

```c
Delay.h
#ifndef __DELAY_H__//都是这样写的这三行,是预编译
#define __DELAY_H__

void Delay(unsigned int xms);

#endif
```

```c
Nixie.c
#include <REGX52.H>
#include "Delay.h"	//包含Delay头文件

//数码管段码表
unsigned char NixieTable[]={0x3F,0x06,0x5B,0x4F,0x66,0x6D,0x7D,0x07,0x7F,0x6F};

//数码管显示子函数
void Nixie(unsigned char Location,Number)
{
	switch(Location)		//位码输出
	{
		case 1:P2_4=1;P2_3=1;P2_2=1;break;
		case 2:P2_4=1;P2_3=1;P2_2=0;break;
		case 3:P2_4=1;P2_3=0;P2_2=1;break;
		case 4:P2_4=1;P2_3=0;P2_2=0;break;
		case 5:P2_4=0;P2_3=1;P2_2=1;break;
		case 6:P2_4=0;P2_3=1;P2_2=0;break;
		case 7:P2_4=0;P2_3=0;P2_2=1;break;
		case 8:P2_4=0;P2_3=0;P2_2=0;break;
	}
	P0=NixieTable[Number];	//段码输出
	Delay(1);				//显示一段时间
	P0=0x00;				//段码清0，消影
}
```

```c
Nixie.h
#ifndef __NIXIE_H__
#define __NIXIE_H__

void Nixie(unsigned char Location,Number);

#endif
```

```c
main.c
#include <REGX52.H>
#include "Delay.h"	//包含Delay头文件
#include "Nixie.h"	//包含数码管头文件

void main()
{
	while(1)
	{
		Nixie(1,1);	//在数码管的第1位置显示1
		Nixie(2,2);	//在数码管的第2位置显示2
		Nixie(3,3);	//在数码管的第3位置显示3
		Nixie(4,4);	//在数码管的第4位置显示4
		Nixie(5,5);	//在数码管的第5位置显示5
		Nixie(6,6);	//在数码管的第6位置显示6
	}
}
```

#### LCD1602液晶屏

<img src="D:\DeskTop\learn\51\image\image-20240411161315541.png" alt="image-20240411161315541" style="zoom: 67%;" />

| **引脚** | **功能**                          |
| -------- | --------------------------------- |
| VSS      | 地                                |
| VDD      | 电源正极（4.5~5.5V）              |
| VO       | 对比度调节电压                    |
| RS       | 数据/指令选择，1为数据，0为指令   |
| RW       | 读/写选择，1为读，0为写           |
| E        | 使能，1为数据有效，下降沿执行命令 |
| D0~D7    | 数据输入/输出                     |
| A        | 背光灯电源正极                    |
| K        | 背光灯电源负极                    |

|              函数               |               作用               |
| :-----------------------------: | :------------------------------: |
|          LCD_Init( );           |      初始化//最多两行十六列      |
|    LCD_ShowChar (1,1, 'A' );    |   显示一个字符//一行一列显示A    |
| LCD_ShowString (1,3, 'Hello' ); | 显示字符串//一行三列开始写Hello  |
|    LCD_ShowNum (1,9,123,3);     | 显示十进制数字//1行9列3位数字123 |
| LCD_ShowSignedNum (1,13,-66,2); | 显示有符号十进制数字//可以用负数 |
|  LCD_ShowHexNum (2,1,0xA8,2)；  |         显示十六进制数字         |
|  LCD_ShowBinNum (2,4,0xAA,8);   |          显示二进制数字          |

![image-20240416114917219](D:\DeskTop\learn\51\image\image-20240416114917219.png)

```c
#include <REGX52.H>
#include "LCD1602.h"	//包含LCD1602头文件
#include "Delay.h"		//包含Delay头文件
int Result=0;
void main()
{
	LCD_Init();
	while(1)
	{
		Result++;					//Result自增
		Delay(1000);				//延时1秒
		LCD_ShowNum(1,1,Result,3);	//在LCD的1行1列显示Result，长度为3位
	}
}
```

#### 矩阵键盘

<img src="D:\DeskTop\learn\51\image\image-20240411165328526.png" alt="image-20240411165328526" style="zoom:50%;" />

​	为了减少IO口的占用，16个按键只有了8个io口扫描方法类似于数码管扫描，快速扫描整个键盘，最终实现所有按键同时检测的效果。（节省IO口）。P10-P13 0111，设置P10为低电平，用以检测S4 S8 S12 S16是否按下，按下则相对应的P14 P15 P16 P17变为低电平，从P10-P13挨个变化，扫描全键盘。

```c
#include <REGX52.H>
#include "Delay.h"		//包含Delay头文件
#include "LCD1602.h"	//包含LCD1602头文件
#include "MatrixKey.h"	//包含矩阵键盘头文件
unsigned char KeyNum;
void main()
{
	LCD_Init();							//LCD初始化
	LCD_ShowString(1,1,"MatrixKey:");	//LCD显示字符串
	while(1)
	{
		KeyNum=MatrixKey();				//获取矩阵键盘键码
		if(KeyNum)						//如果有按键按下
		{
			LCD_ShowNum(2,1,KeyNum,2);	//LCD显示键码
		}
	}
}
```

```c
unsigned char MatrixKey()
{
	unsigned char KeyNumber=0;
    
	P1=0xFF;
	P1_3=0;
	if(P1_7==0){Delay(20);while(P1_7==0);Delay(20);KeyNumber=1;}
	if(P1_6==0){Delay(20);while(P1_6==0);Delay(20);KeyNumber=5;}
	if(P1_5==0){Delay(20);while(P1_5==0);Delay(20);KeyNumber=9;}
	if(P1_4==0){Delay(20);while(P1_4==0);Delay(20);KeyNumber=13;}
	
	P1=0xFF;
	P1_2=0;
	if(P1_7==0){Delay(20);while(P1_7==0);Delay(20);KeyNumber=2;}
	if(P1_6==0){Delay(20);while(P1_6==0);Delay(20);KeyNumber=6;}
	if(P1_5==0){Delay(20);while(P1_5==0);Delay(20);KeyNumber=10;}
	if(P1_4==0){Delay(20);while(P1_4==0);Delay(20);KeyNumber=14;}
	
	P1=0xFF;
	P1_1=0;
	if(P1_7==0){Delay(20);while(P1_7==0);Delay(20);KeyNumber=3;}
	if(P1_6==0){Delay(20);while(P1_6==0);Delay(20);KeyNumber=7;}
	if(P1_5==0){Delay(20);while(P1_5==0);Delay(20);KeyNumber=11;}
	if(P1_4==0){Delay(20);while(P1_4==0);Delay(20);KeyNumber=15;}
	
	P1=0xFF;
	P1_0=0;
	if(P1_7==0){Delay(20);while(P1_7==0);Delay(20);KeyNumber=4;}
	if(P1_6==0){Delay(20);while(P1_6==0);Delay(20);KeyNumber=8;}
	if(P1_5==0){Delay(20);while(P1_5==0);Delay(20);KeyNumber=12;}
	if(P1_4==0){Delay(20);while(P1_4==0);Delay(20);KeyNumber=16;}
    
	return KeyNumber;
}
```

#### 矩阵键盘密码

```c
#include <REGX52.H>
#include "Delay.h"
#include "LCD1602.h"
#include "MatrixKey.h"
unsigned char KeyNum;
unsigned int Password,Count;
void main()
{
	LCD_Init();
	LCD_ShowString(1,1,"Password:");
	while(1)
	{
		KeyNum=MatrixKey();
		if(KeyNum)
		{
			if(KeyNum<=10)	//如果S1~S10按键按下，输入密码
			{
				if(Count<4)	//如果输入次数小于4
				{
					Password*=10;				//密码左移一位
					Password+=KeyNum%10;		//获取一位密码
					Count++;	//计次加一
				}
				LCD_ShowNum(2,1,Password,4);	//更新显示
			}
			if(KeyNum==11)	//如果S11按键按下，确认
			{
				if(Password==2345)	//如果密码等于正确密码
				{
					LCD_ShowString(1,14,"OK ");	//显示OK
					Password=0;		//密码清零
					Count=0;		//计次清零
					LCD_ShowNum(2,1,Password,4);	//更新显示
				}
				else				//否则
				{
					LCD_ShowString(1,14,"ERR");	//显示ERR
					Password=0;		//密码清零
					Count=0;		//计次清零
					LCD_ShowNum(2,1,Password,4);	//更新显示
				}
			}
			if(KeyNum==12)	//如果S12按键按下，取消
			{
				Password=0;		//密码清零
				Count=0;		//计次清零
				LCD_ShowNum(2,1,Password,4);	//更新显示
			}
		}
	}
}
```

## 定时器&中断

​	delay就是让CPU死等，再次期间做不了其他的事情，没法进行诸如按键扫描，所以使用定时器。STC89C52定时器/计数器，3个定时器（T0 T1 T2），T0/1为传统51单片机有的资源，T2为此型号单片机增加的资源。

​	模式0（13位定时器计数器）/**模式1**（16位定时器计数器）/模式2（8位自动重装系统）/模式3（两个8位定时器计数器）；

​							时钟——》计数单元——》中断系统

​	![image-20240411203330962](D:\DeskTop\learn\51\image\image-20240411203330962.png)

​	TH0+TL0总共16位最大65535；左上边为计数器脉冲，每来一个脉冲会计数加一，直到65535后会溢出，标志位TF0向中断系统申请中断；左下面是控制位。

​	SYSclk系统时钟来自外部晶振或者T0 pin，开发板12MHz，有12/6分频两种模式。C/T位控制系统晶振还是T0pin，为1前者，为0后者。

​	**中断系统**是CPU相应外界紧急事件的实时处理能力，CPU暂停当前工作去做其他事情，处理结束后继续回来做之前的工作，请求中断请求的源称为中断源。对中断源优先级进行排序，优先处理优先级高的中断。中断可以嵌套，执行中断中时，又来一个更高级的中断，去执行更高级中断，完成后继续之前的低优先级中断，再回到中断发生前节点继续运行程序。STC89C52提供8个中断，外部中断0 INT0、定时器0中断、外部中断1 INT1、定时器1中断、串口UART中断、定时器2中断、外部中断2 INT2、外部中断3 INT3。（优先级顺序从高到低）

![image-20240411210841572](D:\DeskTop\learn\51\image\image-20240411210841572.png)

![image-20240411210923832](C:\Users\21998\AppData\Roaming\Typora\typora-user-images\image-20240411210923832.png)

![image-20240411211656419](D:\DeskTop\learn\51\image\image-20240411211656419.png)

**TCON** time control，TF time float ，TR time ready（=1开始计数=0禁止计数） ，IE interrupt enable（中断1使能，低电平有效，CPU响应后消除信号），IT interrupt type（0/1选择中断信号的方式）

![image-20240411212857052](D:\DeskTop\learn\51\image\image-20240411212857052.png)

|    位     |                            功能                             |
| :-------: | :---------------------------------------------------------: |
| TMOD.7/.3 | 控制定时器1/0，=1时在INT为高且TR=1时计数=0则只由TR0单独控制 |
| TMOD.6/.2 |           =0由系统时钟输入，=1由P3.4/3.5 pin输入            |
| TMOD.5/.4 |                                                             |
|  00//01   |            13位TLx低5位THx全8位//16位THxTLx全用             |
|    10     |             8位自动重装定时器。THx溢出值放在TLx             |
|    11     |           T1不工作，TL0、TH0分别由T0/T1控制位控制           |

![image-20240412092144484](D:\DeskTop\learn\51\image\image-20240412092144484.png)

​	定时器需要**IE**中断允许寄存器、**TCON**计时器控制寄存器以及**TMOD**；（**IP**中断优先级控制寄存器，对于上表传统51优先级只有两个，STC89C52有四个，但只设置IP即与51模式兼容，谁为1谁优先级高，IP被清零时按前文述优先级排序）。各中断函数调用如下：

<img src="D:\DeskTop\learn\51\image\image-20240412093246420.png" alt="image-20240412093246420" style="zoom:50%;" />

![image-20240416175937408](C:\Users\21998\AppData\Roaming\Typora\typora-user-images\image-20240416175937408.png)



#### 按键控制LED流水灯模式

​	对比上述LED模式，既要扫描键盘又要兼顾LED流水灯输出，所以要使用中断系统；在矩阵键盘里，不停的执行获取键盘按键再LED显示；中断的初始化函数：

```c
void Timer0Init(void)
{
	TMOD &= 0xF0;		//设置定时器模式 //TMOD低四位清零 高四位不变；
	TMOD |= 0x01;		//设置定时器模式 //TMOD最低位置1，其余位置不变；
	TL0 = 0x18;		//设置定时初值 //直接再烧录软件里计算就好
	TH0 = 0xFC;		//设置定时初值
	TF0 = 0;		//清除TF0标志 溢出中断标志位
	TR0 = 1;		//定时器0开始计时 控制位
	ET0=1;
	EA=1;
	PT0=0; 
}
```

​	上述模块化代码完成了对定时器T0的初始化，设置了每秒一次溢出中断；下面中断程序直接放在主函数里，为中断时进入。000

```c
#include <REGX52.H>
#include "Timer0.h"
#include "Key.h"
#include <INTRINS.H>//引用这个库调用_crol/r函数实现循环移位。

unsigned char KeyNum,LEDMode;

void main()
{
	P2=0xFE;
	Timer0Init();
	while(1)
	{
		KeyNum=Key();		//获取独立按键键码
		if(KeyNum)			//如果按键按下
		{
			if(KeyNum==1)	//如果K1按键按下
			{
				LEDMode++;	//模式切换
				if(LEDMode>=2)LEDMode=0;
			}
		}
	}
}
void Timer0_Routine() interrupt 1
{
	static unsigned int T0Count;//设置静态变量，因为函数结束会销毁内存，加入static保留内存到函数结束，所以仍然可以存在，否则若被中断会丢失数值，不同于全局变量只可以被本函数引用。
	TL0 = 0x18;		//设置定时初值
	TH0 = 0xFC;		//设置定时初值
	T0Count++;		//T0Count计次，对中断频率进行分频
	if(T0Count>=500)//分频500次，500ms
	{
		T0Count=0;
		if(LEDMode==0)			//模式判断
			P2=_crol_(P2,1);	//LED输出
		if(LEDMode==1)
			P2=_cror_(P2,1);
	}
}
```

#### 定时器时钟

```c
#include <REGX52.H>
#include "Delay.h"
#include "LCD1602.h"
#include "Timer0.h"
unsigned char Sec=55,Min=59,Hour=23;
void main()
{
	LCD_Init();
	Timer0Init();
	LCD_ShowString(1,1,"Clock:");	//上电显示静态字符串
	LCD_ShowString(2,1,"  :  :");
	while(1)
	{
		LCD_ShowNum(2,1,Hour,2);	//显示时分秒
		LCD_ShowNum(2,4,Min,2);
		LCD_ShowNum(2,7,Sec,2);
	}
}
void Timer0_Routine() interrupt 1//每一秒进一次中断
{
	static unsigned int T0Count;
	TL0 = 0x18;		//设置定时初值
	TH0 = 0xFC;		//设置定时初值
	T0Count++;
	if(T0Count>=1000)	//定时器分频，1s
	{
		T0Count=0;
		Sec++;			//1秒到，Sec自增
		if(Sec>=60)
		{
			Sec=0;		//60秒到，Sec清0，Min自增
			Min++;
			if(Min>=60)
			{
				Min=0;	//60分钟到，Min清0，Hour自增
				Hour++;
				if(Hour>=24)
				{
					Hour=0;	//24小时到，Hour清0
				}
			}
		}
	}
}
```

## 串口通信

​	串口和其他模块进行互相通信（单片机、电脑）；51单片机内部自带**UART**（universal asynchronous receiver transmitter）通用异步收发器，实现单片机的串口通信。

​	**DB9 两排9 pin**/VGA三排，接口，前者串口通信常用，后者多传输视频现在的一般投影仪用接口。（DB9接口也用于流控制）

​	串口通信连接电脑使用USB转串口，不能直接在单片机引，因为电平不一样（注意电平协议）。像是陀螺仪模块，连接串口使单片机也可以测量姿态角；蓝牙串口，集成模块可以直接连接手机进行通信，实现手机遥控单片机。

​	简单的双向串口有两根通信线（**发送端TXD 接收端RXD**），两个设备交叉连接（单向通信只需一根），还有VCC和GND，但当电平不一致时要电平转化芯片。注意：如果双方都有独立的电源时不使用VCC线，若一方需供电一定要使用VCC供电。

​	**电平标准**：

1. TTL电平 +5v 表示1 ；0v表示0；（单片机系统）
2. RS232电平：-3~-15v表示1 ；+3~+15v表示0；
3. RS485电平：两线压差+2~+6v表示1 ；-2~-6V表示0。
4. 1与2最多传输十多米，3可以1km

​	常见的通信接口：

| 名称   | 引脚定义             | 通信方式     | 特点           |
| ------ | -------------------- | ------------ | -------------- |
| UART   | TXD、RXD             | 全双工、异步 | 点对点通信     |
| I^2C   | SCL、SDA             | 半双工、同步 | 可挂载多个设备 |
| SPI    | SCLK、MOSI、MISO、CS | 全双工、同步 | 可挂载多个设备 |
| 1-wire | DQ                   | 半双工、异步 | 可挂载多个设备 |

​	异步：通信双方各自约定通信速率，说好在一个时刻进行接受；同步：靠一根时钟线来约定通信速率；上述表中，SCL，SCLK都带有时钟线可以进行同步，异步不带有时钟线。

​	**UART：RXD/P3.0，TXD/P3.1**。四种模式，模式1：8位UART，波特率可变（这个常用）；模式2：9位UART波特率固定，用于校验（奇偶校验常用）。**先发低位**。

​	**SBUF**地址99H（串口数据缓存寄存器），读写共用地址，物理上独立但相同地址；写操作写入发送寄存器；读操作时接受寄存器。在接受发送的时候有中断TI和RI（分别由中断控制器和接受控制器控制）。

![image-20240412154948265](D:\DeskTop\learn\51\image\image-20240412154948265.png)

**SCON**（SMOD0=1时该位用于错误帧检测SMOD0=0时和SM1一起指定串行通信方式；用**01方式8位UART波特率可变**；**REN=1**允许串行接受REN=0禁止接受；TB8/RB9方式2、3使用，不管；**TI**发送中断请求标志位；**RI**：接受中断请求标志位（RI和TI硬件置位、必须软件复位））、**PCON**（只用SMOD=1波特率加倍=0不加倍和SMOD0帧错误检查）、**IE**（EA和ES置1）、**IP**（PS=1高优先级PS=0低优先级；注：STC89C52有四个优先级，只用传统51两个就行）**0100 0000**

#### 使用串口发送数据

![image-20240412202624533](D:\DeskTop\learn\51\image\image-20240412202624533.png)

​	使用的定时器模式2，8位自动重装方式；这里使用Delay的原因是由于晶振12M导致的会发送一些数值时出错，所以Delay一下，使得波特率降低，实验使用的4800baud。

​	进行串口通信要提前约定好波特率，就是在T1里产生的，设定重装值为0xF3，243，相当于计数就13个溢出一次。12M晶振每次1微秒，溢出率=1/13us=0.0769MHz，SMOD为1，所以0.0769/16=0.00480769MHz=4807HZ。和4800baud有差值。

```c
#include <REGX52.H>
#include "Delay.h"
#include "UART.h"
unsigned char Sec;
void main()
{
	UART_Init();			//串口初始化
	while(1)
	{
		UART_SendByte(Sec);	//串口发送一个字节
		Sec++;				//Sec自增
		Delay(1000);		//延时1秒
	}
}
```

```c
#include <REGX52.H>//串口初始化4800baud@12MHz
void UART_Init()
{
	SCON=0x40;
	PCON |= 0x80;
	TMOD &= 0x0F;		//设置定时器模式
	TMOD |= 0x20;		//设置定时器模式
	TL1 = 0xF3;		//设定定时初值
	TH1 = 0xF3;		//设定定时器重装值
	ET1 = 0;		//禁止定时器1中断
	TR1 = 1;		//启动定时器1
}
void UART_SendByte(unsigned char Byte)
{
	SBUF=Byte;
	while(TI==0);  //检测TI是
	TI=0;
}
```

#### 电脑向串口发

```c
#include <REGX52.H>
#include "Delay.h"
#include "UART.h"
void main()
{
	UART_Init();		//串口初始化
	while(1)
	{
		
	}
}

void UART_Routine() interrupt 4
{
	if(RI==1)	//如果接收标志位为1，接收到了数据数据就在SBUF中
	{
		P2=~SBUF;			//读取数据，取反后输出到LED
		UART_SendByte(SBUF);	//将受到的数据发回串口
		RI=0;					//接收标志位清0
	}
}
```

标记一个地方一个函数不能即在主函数又在中断函数中被打断。

串口助手里HEX模式是直接发送十六进制，文本模式是ascll值。

#### LED点阵屏

<img src="D:\DeskTop\learn\51\image\image-20240412210148852.png" alt="image-20240412210148852" style="zoom:50%;" />

常用于扩展IO口，P34串行输入，P36信号移位，P35并行输出，并不可以直接用P口来驱动高电平，因为单片机使用弱上拉的方式，低电平可以但高电平经过电阻后电流太小；所以使用驱动，或者使用三极管来放大路。（595的芯片也只是实现恒压输出，灯多的时候亮度也弱）

<img src="D:\DeskTop\learn\51\image\image-20240412211715298.png" alt="image-20240412211715298" style="zoom:50%;" />

```c
#include <REGX52.H>
#include "Delay.h"

sbit RCK=P3^5;		//RCLK
sbit SCK=P3^6;		//SRCLK
sbit SER=P3^4;		//SER

#define MATRIX_LED_PORT		P0

/**
  * @brief  74HC595写入一个字节
  * @param  Byte 要写入的字节
  * @retval 无
  */
void _74HC595_WriteByte(unsigned char Byte)
{
	unsigned char i;
	for(i=0;i<8;i++)
	{
		SER=Byte&(0x80>>i);
		SCK=1;
		SCK=0;
	}
	RCK=1;
	RCK=0;
}
/**
  * @brief  LED点阵屏显示一列数据
  * @param  Column 要选择的列，范围：0~7，0在最左边
  * @param  Data 选择列显示的数据，高位在上，1为亮，0为灭
  * @retval 无
  */
void MatrixLED_ShowColumn(unsigned char Column,Data)
{
	_74HC595_WriteByte(Data);
	MATRIX_LED_PORT=~(0x80>>Column);
	Delay(1);
	MATRIX_LED_PORT=0xFF;
}

void main()
{
	SCK=0;
	RCK=0;
	while(1)
	{
		MatrixLED_ShowColumn(0,0x3C);
		MatrixLED_ShowColumn(1,0x42);
		MatrixLED_ShowColumn(2,0xA9);
		MatrixLED_ShowColumn(3,0x85);
		MatrixLED_ShowColumn(4,0x85);
		MatrixLED_ShowColumn(5,0xA9);
		MatrixLED_ShowColumn(6,0x42);
		MatrixLED_ShowColumn(7,0x3C);
	}
}
```

## AT24C02（E2PROM）&I2C

​	**通信接口：I2C总线；容量256字节；**

​	SRAM静态（类似D触发器）DRAM动态（电容）；ROM（掩膜ROM——PROM——EPROM——E2PROM——FLASH——硬盘等）；

​	**I2C**总线 **inter IC BUS**通用数据总线（通用的通信协议），实现串口通信，两根通信线SCL（Serial Clock）、SDA（Serial Data），**同步半双工**，带数据应答的一种方式。使各个设备的通信标准统一，避免了自定义协议。

​	**一流的公司做标准 二流的公司作品牌 三流的公司做产品**。

​	0.96寸OLED，DS1301时钟芯片，MPU6050传感器都是I2C协议。

<img src="D:\DeskTop\learn\51\image\image-20240414131515999.png" alt="image-20240414131515999" style="zoom:50%;" />

1. 所有I2C设备的SCL连在一起，SDA连在一起；
2. 设备的SCL和SDA都要配置成开漏输出模式；
3. SCL和SDA各添加一个上拉电阻，阻值一般为4.7KΩ左右；
4. 开漏输出和上拉电阻的共同作用实现了“线与”的功能，此设计主要是为了解决多机通信互相干扰的问题。

**起始条件**：SCL高电平期间，SDA从高电平切换到低电平；

**终止条件**：SCL高电平期间，SDA从低电平切换到高电平；

![image-20240415113858854](D:\DeskTop\learn\51\image\image-20240415113858854.png)

**发送一个字节**：SCL低电平期间，主机将数据位依次放到SDA线上（高位在前），然后拉高SCL，从机将在SCL高电平期间读取数据位，所以SCL高电平期间SDA不允许有数据变化，依次循环上述过程8次，即可发送一个字节；

![image-20240415113951289](D:\DeskTop\learn\51\image\image-20240415113951289.png)

**接收一个字节**：SCL低电平期间，从机将数据位依次放到SDA线上（高位在前），然后拉高SCL，主机将在SCL高电平期间读取数据位，所以SCL高电平期间SDA不允许有数据变化，依次循环上述过程8次，即可接收一个字节（主机在接收之前，需要释放SDA）

![image-20240415114024152](D:\DeskTop\learn\51\image\image-20240415114024152.png)

**发送应答**：在接收完一个字节之后，主机在下一个时钟发送一位数据，数据0表示应答，数据1表示非应答;

**接收应答**：在发送完一个字节之后，主机在下一个时钟接收一位数据，判断从机是否应答，数据0表示应答，数据1表示非应答（主机在接收之前，需要释放SDA）;

![image-20240415114100312](D:\DeskTop\learn\51\image\image-20240415114100312.png)

**发送一帧数据**：向谁发什么

![image-20240415114140110](D:\DeskTop\learn\51\image\image-20240415114140110.png)

**接收一帧数据**：向谁收什么

![image-20240415114216536](D:\DeskTop\learn\51\image\image-20240415114216536.png)

**先发送再接收数据帧**（复合格式）：向谁收指定的什么

![image-20240415114250112](D:\DeskTop\learn\51\image\image-20240415114250112.png)

**字节写**：在WORD ADDRESS处写入数据DATA

![image-20240415114320462](D:\DeskTop\learn\51\image\image-20240415114320462.png)

**随机读**：读出在WORD ADDRESS处的数据DATA

![image-20240415114358647](D:\DeskTop\learn\51\image\image-20240415114358647.png)

AT24C02的固定地址为**1010**，可配置地址本开发板上为000， 所以SLAVE ADDRESS+W为**0xA0**，SLAVE ADDRESS+R为**0xA1**。

**注意：SDA要释放，设置为1。**

```c
#include <REGX52.H>

sbit I2C_SCL=P2^1;
sbit I2C_SDA=P2^0;

/**
  * @brief  I2C开始
  * @param  无
  * @retval 无
  */
void I2C_Start(void)
{
	I2C_SDA=1;
	I2C_SCL=1;
	I2C_SDA=0;
	I2C_SCL=0;
}

/**
  * @brief  I2C停止
  * @param  无
  * @retval 无
  */
void I2C_Stop(void)
{
	I2C_SDA=0;
	I2C_SCL=1;
	I2C_SDA=1;
}

/**
  * @brief  I2C发送一个字节
  * @param  Byte 要发送的字节
  * @retval 无
  */
void I2C_SendByte(unsigned char Byte)
{
	unsigned char i;
	for(i=0;i<8;i++)
	{
		I2C_SDA=Byte&(0x80>>i);
		I2C_SCL=1;
		I2C_SCL=0;
	}
}

/**
  * @brief  I2C接收一个字节
  * @param  无
  * @retval 接收到的一个字节数据
  */
unsigned char I2C_ReceiveByte(void)
{
	unsigned char i,Byte=0x00;
	I2C_SDA=1;
	for(i=0;i<8;i++)
	{
		I2C_SCL=1;
		if(I2C_SDA){Byte|=(0x80>>i);}
		I2C_SCL=0;
	}
	return Byte;
}

/**
  * @brief  I2C发送应答
  * @param  AckBit 应答位，0为应答，1为非应答
  * @retval 无
  */
void I2C_SendAck(unsigned char AckBit)
{
	I2C_SDA=AckBit;
	I2C_SCL=1;
	I2C_SCL=0;
}

/**
  * @brief  I2C接收应答位
  * @param  无
  * @retval 接收到的应答位，0为应答，1为非应答
  */
unsigned char I2C_ReceiveAck(void)
{
	unsigned char AckBit;
	I2C_SDA=1;
	I2C_SCL=1;
	AckBit=I2C_SDA;
	I2C_SCL=0;
	return AckBit;
}
```

```c
#include <REGX52.H>
#include "LCD1602.h"
#include "Key.h"
#include "AT24C02.h"
#include "Delay.h"

unsigned char KeyNum;
unsigned int Num;

void main()
{
	LCD_Init();
	LCD_ShowNum(1,1,Num,5);
	while(1)
	{
		KeyNum=Key();
		if(KeyNum==1)	//K1按键，Num自增
		{
			Num++;
			LCD_ShowNum(1,1,Num,5);
		}
		if(KeyNum==2)	//K2按键，Num自减
		{
			Num--;
			LCD_ShowNum(1,1,Num,5);
		}
		if(KeyNum==3)	//K3按键，向AT24C02写入数据
		{
			AT24C02_WriteByte(0,Num%256);
			Delay(5);
			AT24C02_WriteByte(1,Num/256);
			Delay(5);
			LCD_ShowString(2,1,"Write OK");
			Delay(1000);
			LCD_ShowString(2,1,"        ");
		}
		if(KeyNum==4)	//K4按键，从AT24C02读取数据
		{
			Num=AT24C02_ReadByte(0);
			Num|=AT24C02_ReadByte(1)<<8;
			LCD_ShowNum(1,1,Num,5);
			LCD_ShowString(2,1,"Read OK ");
			Delay(1000);
			LCD_ShowString(2,1,"        ");
		}
	}
}
```

#### **定时器扫描数码管**：

​	main直接引用time0和key、Nixie模块，设置定时扫描按键和数码管。键盘和数码管模块都需要定时器中断，所以在main里定义中断，设定时间驱动键盘和数码管（驱动函数）。这才是常用状态，CPU因此可以继承很多功能。

```c
#include <REGX52.H>
#include "Timer0.h"
#include "Key.h"
#include "Nixie.h"
#include "Delay.h"
#include "AT24C02.h"

unsigned char KeyNum;
unsigned char Min,Sec,MiniSec;
unsigned char RunFlag;

void main()
{
	Timer0_Init();
	while(1)
	{
		KeyNum=Key();
		if(KeyNum==1)			//K1按键按下
		{
			RunFlag=!RunFlag;	//启动标志位翻转
		}
		if(KeyNum==2)			//K2按键按下
		{
			Min=0;				//分秒清0
			Sec=0;
			MiniSec=0;
		}
		if(KeyNum==3)			//K3按键按下
		{
			AT24C02_WriteByte(0,Min);	//将分秒写入AT24C02
			Delay(5);
			AT24C02_WriteByte(1,Sec);
			Delay(5);
			AT24C02_WriteByte(2,MiniSec);
			Delay(5);
		}
		if(KeyNum==4)			//K4按键按下
		{
			Min=AT24C02_ReadByte(0);	//读出AT24C02数据
			Sec=AT24C02_ReadByte(1);
			MiniSec=AT24C02_ReadByte(2);
		}
		Nixie_SetBuf(1,Min/10);	//设置显示缓存，显示数据
		Nixie_SetBuf(2,Min%10);
		Nixie_SetBuf(3,11);
		Nixie_SetBuf(4,Sec/10);
		Nixie_SetBuf(5,Sec%10);
		Nixie_SetBuf(6,11);
		Nixie_SetBuf(7,MiniSec/10);
		Nixie_SetBuf(8,MiniSec%10);
	}
}

/**
  * @brief  秒表驱动函数，在中断中调用
  * @param  无
  * @retval 无
  */
void Sec_Loop(void)
{
	if(RunFlag)
	{
		MiniSec++;
		if(MiniSec>=100)
		{
			MiniSec=0;
			Sec++;
			if(Sec>=60)
			{
				Sec=0;
				Min++;
				if(Min>=60)
				{
					Min=0;
				}
			}
		}
	}
}

void Timer0_Routine() interrupt 1
{
	static unsigned int T0Count1,T0Count2,T0Count3;
	TL0 = 0x18;		//设置定时初值
	TH0 = 0xFC;		//设置定时初值
	T0Count1++;
	if(T0Count1>=20)
	{
		T0Count1=0;
		Key_Loop();	//20ms调用一次按键驱动函数
	}
	T0Count2++;
	if(T0Count2>=2)
	{
		T0Count2=0;
		Nixie_Loop();//2ms调用一次数码管驱动函数
	}
	T0Count3++;
	if(T0Count3>=10)
	{
		T0Count3=0;
		Sec_Loop();	//10ms调用一次数秒表驱动函数
	}
}

```

```
void Key_Loop(void)
{
	static unsigned char NowState,LastState;
	LastState=NowState;				//按键状态更新
	NowState=Key_GetState();		//获取当前按键状态
	//如果上个时间点按键按下，这个时间点未按下，则是松手瞬间，以此避免消抖和松手检测
	if(LastState==1 && NowState==0)
	{
		Key_KeyNumber=1;
	}
	if(LastState==2 && NowState==0)
	{
		Key_KeyNumber=2;
	}
	if(LastState==3 && NowState==0)
	{
		Key_KeyNumber=3;
	}
	if(LastState==4 && NowState==0)
	{
		Key_KeyNumber=4;
	}
}

```

```
void Nixie_Loop(void)
{
	static unsigned char i=1;
	Nixie_Scan(i,Nixie_Buf[i]);
	i++;
	if(i>=9){i=1;}
}
```

#### 温度传感器：

​	DS18B20是一种常见的数字温度传感器，其控制命令和数据都是以数字信号的方式输入输出，相比较于模拟温度传感器，具有功能强大、硬件简单、易扩展、抗干扰性强等特点。测温范围：-55°C 到 +125°C。通信接口：1-Wire（单总线）。其它特征：可形成总线结构、内置温度报警功能、可寄生供电。

![image-20240416083156981](D:\DeskTop\learn\51\image\image-20240416083156981.png)

![image-20240416083212590](D:\DeskTop\learn\51\image\image-20240416083212590.png)

​	Byte0存储温度的低位，1存储温度的高位，2 3 4作用是只能先把数据放到暂存器里然后再加指令到EEPROM里（上电时EEPROM里的值自动到暂存器里），CRC为前面八个字节的校验位。

​	单总线（1-Wire BUS）是由Dallas公司开发的一种通用数据总线。一根通信线：DQ，异步、半双工，单总线只需要一根通信线即可实现数据的双向传输，当采用寄生供电时，还可以省去设备的VDD线路，此时，供电加通信只需要DQ和GND两根线。

​	设备的DQ均要配置成开漏输出模式，DQ添加一个上拉电阻，阻值一般为4.7KΩ左右，若此总线的从机采取寄生供电，则主机还应配一个**强上拉输出电路**。

<img src="D:\DeskTop\learn\51\image\image-20240416084937273.png" alt="image-20240416084937273" style="zoom:67%;" />

**初始化**：主机将总线拉低至少480us，然后释放总线，等待15~60us后，存在的从机会拉低总线60~240us以响应主机，之后从机将释放总线

<img src="D:\DeskTop\learn\51\image\image-20240416093901194.png" alt="image-20240416093901194" style="zoom:67%;" />

**发送一位**：主机将总线拉低60~120us，然后释放总线，表示发送0；主机将总线拉低**1~15us**，然后释放总线，表示发送1。从机将在总线拉低30us后（典型值）读取电平，整个时间片应大于60us。

<img src="D:\DeskTop\learn\51\image\image-20240416095109628.png" alt="image-20240416095109628" style="zoom:67%;" />

**接收一位**：主机将总线拉低1~15us，然后释放总线，并在拉低后**15us**内读取总线电平（尽量贴近15us的末尾），读取为低电平则为接收0，读取为高电平则为接收1 ，整个时间片应大于60us。

<img src="C:\Users\21998\AppData\Roaming\Typora\typora-user-images\image-20240416095241929.png" alt="image-20240416095241929" style="zoom:67%;" />

**发送一个字节**：连续调用8次发送一位的时序，依次发送一个字节的8位（低位在前）。

<img src="D:\DeskTop\learn\51\image\image-20240416095605449.png" alt="image-20240416095605449" style="zoom:67%;" />

**接收一个字节**：连续调用8次接收一位的时序，依次接收一个字节的8位（低位在前）。

<img src="D:\DeskTop\learn\51\image\image-20240416095649466.png" alt="image-20240416095649466" style="zoom:67%;" />

**操作流程**：

•初始化：从机复位，主机判断从机是否响应

•ROM操作：ROM指令+本指令需要的读写操作

•功能操作：功能指令+本指令需要的读写操作

|  **ROM****指令**   |      **功能指令**       |
| :----------------: | :---------------------: |
|  SEARCH ROM [F0h]  |     CONVERT T [44h]     |
|   READ ROM [33h]   | WRITE SCRATCHPAD [4Eh]  |
|  MATCH ROM [55h]   |  READ SCRATCHPAD [BEh]  |
|   SKIP ROM [CCh]   |  COPY SCRATCHPAD [48h]  |
| ALARM SEARCH [ECh] |     RECALL E2 [B8h]     |
|                    | READ POWER SUPPLY [B4h] |

**温度变换**：初始化→跳过ROM →开始温度变换

<img src="D:\DeskTop\learn\51\image\image-20240416100835594.png" alt="image-20240416100835594" style="zoom:67%;" />

**温度读取**：初始化→跳过ROM →读暂存器→连续的读操作

<img src="D:\DeskTop\learn\51\image\image-20240416101203601.png" style="zoom:67%;" />

![image-20240416101328046](D:\DeskTop\learn\51\image\image-20240416101328046.png)

<img src="D:\DeskTop\learn\51\image\image-20240416101920481.png" alt="image-20240416101920481" style="zoom:33%;" />

```c
#include <REGX52.H>
//引脚定义
sbit OneWire_DQ=P3^7;

/**
  * @brief  单总线初始化
  * @param  无
  * @retval 从机响应位，0为响应，1为未响应
  */
unsigned char OneWire_Init(void)
{
	unsigned char i;
	unsigned char AckBit;
	OneWire_DQ=1;
	OneWire_DQ=0;
	i = 247;while (--i);		//Delay 500us
	OneWire_DQ=1;
	i = 32;while (--i);			//Delay 70us
	AckBit=OneWire_DQ;
	i = 247;while (--i);		//Delay 500us
	return AckBit;
}

/**
  * @brief  单总线发送一位
  * @param  Bit 要发送的位
  * @retval 无
  */
void OneWire_SendBit(unsigned char Bit)
{
	unsigned char i;
	OneWire_DQ=0;
	i = 4;while (--i);			//Delay 10us
	OneWire_DQ=Bit;
	i = 24;while (--i);			//Delay 50us
	OneWire_DQ=1;
}

/**
  * @brief  单总线接收一位
  * @param  无
  * @retval 读取的位
  */
unsigned char OneWire_ReceiveBit(void)
{
	unsigned char i;
	unsigned char Bit;
	OneWire_DQ=0;
	i = 2;while (--i);			//Delay 5us
	OneWire_DQ=1;
	i = 2;while (--i);			//Delay 5us
	Bit=OneWire_DQ;
	i = 24;while (--i);			//Delay 50us
	return Bit;
}

/**
  * @brief  单总线发送一个字节
  * @param  Byte 要发送的字节
  * @retval 无
  */
void OneWire_SendByte(unsigned char Byte)
{
	unsigned char i;
	for(i=0;i<8;i++)
	{
		OneWire_SendBit(Byte&(0x01<<i));
	}
}

/**
  * @brief  单总线接收一个字节
  * @param  无
  * @retval 接收的一个字节
  */
unsigned char OneWire_ReceiveByte(void)
{
	unsigned char i;
	unsigned char Byte=0x00;
	for(i=0;i<8;i++)
	{
		if(OneWire_ReceiveBit()){Byte|=(0x01<<i);}
	}
	return Byte;
}
```

```c
#include <REGX52.H>
#include "OneWire.h"

//DS18B20指令
#define DS18B20_SKIP_ROM			0xCC
#define DS18B20_CONVERT_T			0x44
#define DS18B20_READ_SCRATCHPAD 	0xBE

/**
  * @brief  DS18B20开始温度变换
  * @param  无
  * @retval 无
  */
void DS18B20_ConvertT(void)
{
	OneWire_Init();
	OneWire_SendByte(DS18B20_SKIP_ROM);
	OneWire_SendByte(DS18B20_CONVERT_T);
}

/**
  * @brief  DS18B20读取温度
  * @param  无
  * @retval 温度数值
  */
float DS18B20_ReadT(void)
{
	unsigned char TLSB,TMSB;
	int Temp;
	float T;
	OneWire_Init();
	OneWire_SendByte(DS18B20_SKIP_ROM);
	OneWire_SendByte(DS18B20_READ_SCRATCHPAD);
	TLSB=OneWire_ReceiveByte();
	TMSB=OneWire_ReceiveByte();
	Temp=(TMSB<<8)|TLSB;
	T=Temp/16.0;
	return T;
}
```



```c
#include <REGX52.H>
#include "LCD1602.h"
#include "DS18B20.h"
#include "Delay.h"

float T;

void main()
{
	DS18B20_ConvertT();		//上电先转换一次温度，防止第一次读数据错误
	Delay(1000);			//等待转换完成
	LCD_Init();
	LCD_ShowString(1,1,"Temperature:");
	while(1)
	{
		DS18B20_ConvertT();	//转换温度
		T=DS18B20_ReadT();	//读取温度
		if(T<0)				//如果温度小于0
		{
			LCD_ShowChar(2,1,'-');	//显示负号
			T=-T;			//将温度变为正数
		}
		else				//如果温度大于等于0
		{
			LCD_ShowChar(2,1,'+');	//显示正号
		}
		LCD_ShowNum(2,2,T,3);		//显示温度整数部分
		LCD_ShowChar(2,5,'.');		//显示小数点
		LCD_ShowNum(2,6,(unsigned long)(T*10000)%10000,4);//显示温度小数部分
	}
}
```

#### 电机：

​	直流电机是一种将电能转换为机械能的装置。一般的直流电机有两个电极，当电极正接时，电机正转，当电极反接时，电机反转。直流电机主要由永磁体（定子）、线圈（转子）和换向器组成，除直流电机外，常见的电机还有步进电机、舵机、无刷电机、空心杯电机等。

![image-20240416122250705](D:\DeskTop\learn\51\image\image-20240416122250705.png)

​	**PWM**（Pulse Width Modulation）**即脉冲宽度调制**，在具有惯性的系统中，可以通过对一系列脉冲的宽度进行调制，来等效地获得所需要的模拟参量，常应用于电机控速、开关电源等领域。PWM重要参数：**频率** = 1 / TS      **占空比** = TON / TS      **精度** = 占空比变化步距。

#### **A/D转换**

​	**运算放大器**（简称“运放”）是具有很高放大倍数的放大电路单元。内部集成了差分放大器、电压放大器、功率放大器三级放大电路，是一个性能完备、功能强大的通用放大电路单元，由于其应用十分广泛，现已作为基本的电路元件出现在电路图中，运算放大器可构成的电路有：电压比较器、反相放大器、同相放大器、电压跟随器、加法器、积分器、微分器等。

​	运算放大器电路的分析方法：虚短、虚断（负反馈条件下），输入阻抗非常大，内部放大倍数很大，接负反馈电阻实现选定倍数的放大。

**电压比较器**：同相比反相大输出VCC 反之则输出GND。

<img src="D:\DeskTop\learn\51\image\image-20240416152706758.png" alt="image-20240416152706758" style="zoom:50%;" />

**反向放大器**：V_OUT=-R2/R1×V_IN（要保证输出的电压再放大器的电压范围内）

<img src="D:\DeskTop\learn\51\image\image-20240416152817683.png" alt="image-20240416152817683" style="zoom:50%;" />

**同向放大器**：V_OUT=(1+R2/R1)×V_IN

<img src="D:\DeskTop\learn\51\image\image-20240416153739190.png" alt="image-20240416153739190" style="zoom:50%;" />

**电压跟随器**：V_OUT=V_IN （提高信号的驱动能力）

<img src="D:\DeskTop\learn\51\image\image-20240416153841650.png" alt="image-20240416153841650" style="zoom:50%;" />

**DA转换**：

<img src="D:\DeskTop\learn\51\image\image-20240416154024972.png" alt="image-20240416154024972" style="zoom: 50%;" />

<img src="D:\DeskTop\learn\51\image\image-20240416154522515.png" alt="image-20240416154522515" style="zoom: 50%;" />

**AD转换**：

<img src="D:\DeskTop\learn\51\image\image-20240416155155318.png" alt="image-20240416155155318" style="zoom:50%;" />

​	**分辨率**：指AD/DA数字量的精细程度，通常用位数表示。例如，对于5V电源系统来说，8位的AD可将5V等分为256份，即数字量变化最小一个单位时，模拟量变化5V/256=0.01953125V，所以，8位AD的电压分辨率为0.01953125V，AD/DA的位数越高，分辨率就越高。**转换速度**：表示AD/DA的最大采样/建立频率，通常用转换频率或者转换时间来表示，对于采样/输出高速信号，应注意AD/DA的转换速度。

#### 红外遥控

​	红外遥控是利用红外光进行通信的设备，由红外LED将调制后的信号发出，由专用的红外接收头进行解调输出。通信方式：单工，异步；红外LED波长：940nm；通信协议标准：**NEC**标准。

<img src="D:\DeskTop\learn\51\image\image-20240416163535017.png" alt="image-20240416163535017" style="zoom:67%;" />

​	空闲状态红外LED不亮，并且接收头OUT输出高电平。输入IN在高电平时Q2不通不发，低电平才发信号，且以38KHz的频率发光，（否则大搞率会被太阳光淹没），再把38Hz的频率提取出来。上图2则需要自行实现图1所述功能。图三为一体化红外接收头，实现接受的同时也滤除了38MHZ的成分，还原出了IN的部分，OUT输出信号，使用单片机的外部中断来进行处理。（P3.2 3.3）

<img src="D:\DeskTop\learn\51\image\image-20240416170508695.png" alt="image-20240416170508695" style="zoom:80%;" />

<img src="D:\DeskTop\learn\51\image\image-20240416175701460.png" alt="image-20240416175701460" style="zoom:80%;" />

<img src="D:\DeskTop\learn\51\image\image-20240416175717916.png" alt="image-20240416175717916" style="zoom: 33%;" />

