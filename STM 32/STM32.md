# STM32

​	ST公司开发的基于ARM Cortex-M内核开发的32位微控制器。ARM是ARM公司也是ARM内核处理器，公司是半导体知识产权提供商（IP），生产ARM内核，半导体厂商完善内核周边电路并且生产芯片。目前由高端系列主流系列和低功耗以及无线系列。

​	目前Cortex系列有cortex-A和cortex-R、cortex-M，RM系列嵌入式领域，A系列适用于手机领域（苹果高通都是采用ARM芯片架构的，苹果基于ARM的M1芯片），R系列硬盘控制器之类比较少的应用场景，M系列microcontro，单片机领域。

​	STM32F1属于主流系列，使用**Cortex-M3**，72MHz，RAM20K（SARAM），ROM64K（Flash），供电2~3.6v标准3.3V，封装LQFP48。

| **英文缩写** | **名称**               | **英文缩写** | **名称**           |
| ------------ | ---------------------- | ------------ | ------------------ |
| **NVIC**     | **嵌套向量中断控制器** | CAN          | CAN通信            |
| **SysTick**  | **系统滴答定时器**     | USB          | USB通信            |
| RCC          | 复位和时钟控制         | RTC          | 实时时钟           |
| GPIO         | 通用IO口               | CRC          | CRC校验            |
| AFIO         | 复用IO口               | PWR          | 电源控制           |
| EXTI         | 外部中断               | BKP          | 备份寄存器         |
| TIM          | 定时器                 | IWDG         | 独立看门狗         |
| ADC          | 模数转换器             | WWDG         | 窗口看门狗         |
| DMA          | 直接内存访问           | *DAC         | 数模转换器         |
| USART        | 同步/异步串口通信      | *SDIO        | SD卡接口           |
| I2C          | I2C通信                | *FSMC        | 可变静态存储控制器 |
| SPI          | SPI通信                | *USB OTG     | USB主机接口        |

​	前两个位内核所有，后面四个为本芯片STM32F1C8T6芯片所没有。

<img src="D:\DeskTop\learn\STM 32\image\image-20240417110127397.png" alt="image-20240417110127397" style="zoom: 67%;" />





## 引脚定义

<img src="D:\DeskTop\learn\STM 32\image\image-20240417111435277.png" alt="image-20240417111435277" style="zoom:80%;" />

​	**红色电源相关；蓝色最小系统相关；绿色IO口功能口；**FT表示可以容忍5V电压否则就是3.3V电压；两个功能都需要同一个引脚时可以把一个功能重映射到新的端口上。

<img src="D:\DeskTop\learn\STM 32\image\image-20240417171416847.png" alt="image-20240417171416847" style="zoom: 50%;" />

一般常用第一种，第二种系统存储器种有bootloader程序，作用是接受串口数据再刷新到主闪存中，用作串口下载程序；

![image-20240417171950272](C:\Users\21998\AppData\Roaming\Typora\typora-user-images\image-20240417171950272.png)

**下表对应启动函数的选择**（为Start文件中的md.s文件结尾）

| **缩写** | **释义**           | **Flash****容量** | **型号**          |
| -------- | ------------------ | ----------------- | ----------------- |
| LD_VL    | 小容量产品超值系列 | 16~32K            | STM32F100         |
| MD_VL    | 中容量产品超值系列 | 64~128K           | STM32F100         |
| HD_VL    | 大容量产品超值系列 | 256~512K          | STM32F100         |
| LD       | 小容量产品         | 16~32K            | STM32F101/102/103 |
| **MD**   | 中容量产品         | 64~128K           | STM32F101/102/103 |
| HD       | 大容量产品         | 256~512K          | STM32F101/102/103 |
| XL       | 加大容量产品       | 大于512K          | STM32F101/102/103 |
| CL       | 互联型产品         | -                 | STM32F105/107     |

•建立工程文件夹，Keil中新建工程，选择型号

•工程文件夹里建立Start、Library、User等文件夹，复制固件库里面的文件到工程文件夹

•工程里对应建立Start、Library、User等同名称的分组，然后将文件夹内的文件添加到工程分组里

•工程选项，C/C++，Include Paths内声明所有包含头文件的文件夹

•工程选项，C/C++，Define内定义USE_STDPERIPH_DRIVER

•工程选项，Debug，下拉列表选择对应调试器，Settings，Flash Download里勾选Reset and Run

<img src="D:\DeskTop\learn\STM 32\image\image-20240419195800849.png" alt="image-20240419195800849" style="zoom: 50%;" /><img src="D:\DeskTop\learn\STM 32\image\image-20240419200214463.png" alt="image-20240419200214463" style="zoom: 67%;" />

start中一表示启动，学习芯片对应md后缀的启动文件，二三为内核寄存器描述文件，第四个表述外设寄存器以及对应的地址，五六表示配置时钟；user中第二个配置库函数头文件的包含关系和参数检查的函数定义，两个it是存放中断函数

**启动函数**

![image-20240612185016459](D:\DeskTop\learn\STM 32\image\image-20240612185016459.png)

**systeminit**

![image-20240612185116381](D:\DeskTop\learn\STM 32\image\image-20240612185116381.png)



## **AHB，APB1，APB2外设时钟控制&基本结构**



void RCC_AHBPeriphClockCmd(uint32_t RCC_AHBPeriph, FunctionalState NewState);

void RCC_APB2PeriphClockCmd(uint32_t RCC_APB2Periph, FunctionalState NewState);

void RCC_APB1PeriphClockCmd(uint32_t RCC_APB1Periph, FunctionalState NewState);

均为第一个参数选择外设，第二个参数控制enable或者disable；可去对应rcc.c文件查找相关外设是那个文件。

<img src="D:\DeskTop\learn\STM 32\image\image-20240417110725085.png" alt="image-20240417110725085" style="zoom: 67%;" />

四个驱动单元：  ─ Cortex™-M3内核DCode总线(D-bus)，和系统总线(S-bus)  ─ 通用DMA1和通用DMA2 

四个被动单元  ─ 内部SRAM  ─ 内部闪存存储器  ─ FSMC  ─ AHB到APB的桥(AHB2APBx)，它连接所有的APB设备

ICode总线  该总线将Cortex™-M3内核的指令总线与闪存指令接口相连接。**指令预取在此总线上完成**。 

DCode总线  该总线将Cortex™-M3内核的DCode总线与闪存存储器的数据接口相连接(**常量加载和调试访问**)。  

系统总线  此总线连接Cortex™-M3内核的系统总线(外设总线)到总线矩阵，**总线矩阵协调着内核和DMA间的访问**。  

DMA总线  此总线将DMA的AHB主控接口与总线矩阵相联，总线矩阵协调着CPU的**DCode和DMA**到 SRAM、闪存和外设的访问。  

总线矩阵  总线矩阵协调内核系统总线和DMA主控总线之间的访问仲裁，仲裁利用轮换算法。

AHB/APB桥(APB)  两个AHB/APB桥在AHB和2个APB总线间提供同步连接，APB1操作速度限于36MHz，APB2操作于全速(最高72MHz)。 

## GPIO控制

•GPIO（General Purpose Input Output）通用输入输出口

•可配置为8种输入输出模式

•引脚电平：0V~3.3V，部分引脚可容忍5V

•输出模式下可控制端口输出高低电平，用以驱动LED、控制蜂鸣器、模拟通信协议输出时序等

•输入模式下可读取端口的高低电平或电压，用于读取按键输入、外接模块电平信号输入、ADC电压采集、模拟通信协议接收数据等

<img src="D:\DeskTop\learn\STM 32\image\image-20240419202455200.png" alt="image-20240419202455200" style="zoom:67%;" /> 

```c
    点灯PC13口（高电平）直接使用寄存器：
    RCC->APB2ENR = 0x00000010;开c口 
    GPIOC->CRH = 0x00300000;c口配置寄存器
    GPIOC->ODR = 0x00002000;c口输出寄存器
    后面使用库函数
	RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOC,ENABLE);开启时钟
	GPIO_InitTypeDef GPIO_InitStruct;
	GPIO_InitStruct.GPIO_Mode=GPIO_Mode_Out_OD;
	GPIO_InitStruct.GPIO_Pin=GPIO_Pin_13;
	GPIO_InitStruct.GPIO_Speed=GPIO_Speed_50MHz;
	GPIO_Init(GPIOC,&GPIO_InitStruct);  初始化c口 前面为配置c口
    GPIO_SetBits(GPIOC,GPIO_Pin_13);设置电平
```

使用gpio进行输出首先开启时钟，即RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOC,ENABLE)；在开启始终后进行输出口配置。

### IO口基本结构

<img src="D:\DeskTop\learn\STM 32\image\image-20240419202732231.png" alt="image-20240419202732231" style="zoom: 50%;" />

​	**推挽**输出下强输出模式，寄存器堆IO口有绝对控制权；但是再**开漏**模式下Pmos管无效，只有Nmos工作，此时寄存器置一下管也断开也就是高阻模式，为零时下管导通此时为低电平输出，可以用作通信模式，外接上拉电阻实现多设备之间的通信，也可以直接外接5v电源实现5v的电源输出；当引脚被配置为输入模式此时处于关闭状态，两个mos管均无效。

​	输入则是浮空或者上拉与下拉模式。

​	不进行初始化默认是浮空输入的模式，引脚不会输出电平。

| **模式名称** | **性质** |                      **特征**                      |
| :----------: | :------: | :------------------------------------------------: |
|   浮空输入   | 数字输入 |      可读取引脚电平，若引脚悬空，则电平不确定      |
|   上拉输入   | 数字输入 | 可读取引脚电平，内部连接上拉电阻，悬空时默认高电平 |
|   下拉输入   | 数字输入 | 可读取引脚电平，内部连接下拉电阻，悬空时默认低电平 |
|   模拟输入   | 模拟输入 |           GPIO无效，引脚直接接入内部ADC            |
|   开漏输出   | 数字输出 |    可输出引脚电平，高电平为高阻态，低电平接VSS     |
|   推挽输出   | 数字输出 |      可输出引脚电平，高电平接VDD，低电平接VSS      |
| 复用开漏输出 | 数字输出 |    由片上外设控制，高电平为高阻态，低电平接VSS     |
| 复用推挽输出 | 数字输出 |      由片上外设控制，高电平接VDD，低电平接VSS      |

<img src="D:\DeskTop\learn\STM 32\image\image-20240613101547869.png" alt="image-20240613101547869" style="zoom:25%;" />

常用按钮模式采用上拉电阻模式，按键按下时为低电平，其他为内置上拉电阻保持的高电平。

<img src="D:\DeskTop\learn\STM 32\image\image-20240613101723175.png" alt="image-20240613101723175" style="zoom:25%;" />

此模式则要使用上拉模式或浮空模式，按键按下时为低电平，其他为外部和内部上拉保持高电平。

### GPIO部分库函数

 void GPIO_DeInit(GPIO_TypeDef* GPIOx);	//复位所指定的**GPIO**外设
void GPIO_AFIODeInit(void);	//复位**AFIO**外设
void GPIO_Init(GPIO_TypeDef* GPIOx, GPIO_InitTypeDef* GPIO_InitStruct);	//用结构体参数来**初始化GPIO口**，定义结构体变量再给结构体赋值，最后调用这个函数
void GPIO_StructInit(GPIO_InitTypeDef* GPIO_InitStruct);	//把结构体变量赋予一个默认值

uint8_t GPIO_ReadInputDataBit(GPIO_TypeDef* GPIOx, uint16_t GPIO_Pin);	//下四个为GPIO的**读入函数**
uint16_t GPIO_ReadInputData(GPIO_TypeDef* GPIOx);
uint8_t GPIO_ReadOutputDataBit(GPIO_TypeDef* GPIOx, uint16_t GPIO_Pin);
uint16_t GPIO_ReadOutputData(GPIO_TypeDef* GPIOx);

void GPIO_SetBits(GPIO_TypeDef* GPIOx, uint16_t GPIO_Pin);	//下四个为GPIO的**写入函数**
void GPIO_ResetBits(GPIO_TypeDef* GPIOx, uint16_t GPIO_Pin);
void GPIO_WriteBit(GPIO_TypeDef* GPIOx, uint16_t GPIO_Pin, BitAction BitVal);//第二个参数只能为Bit_RESET\Bit_SET，或使用(BitAction)0 强制把0或者1转换为对应类型。

void GPIO_Write(GPIO_TypeDef* GPIOx, uint16_t PortVal);



void GPIO_PinLockConfig(GPIO_TypeDef* GPIOx, uint16_t GPIO_Pin);	//锁定引脚 不能更改

void GPIO_EventOutputConfig(uint8_t GPIO_PortSource, uint8_t GPIO_PinSource);	//这两条配置GPIO的输出功能
void GPIO_EventOutputCmd(FunctionalState NewState);



void GPIO_PinRemapConfig(uint32_t GPIO_Remap, FunctionalState NewState);	//**引脚重映射**
void GPIO_EXTILineConfig(uint8_t GPIO_PortSource, uint8_t GPIO_PinSource);	//配置**AFIO**的数据选择器，选择想要的中断引脚



void GPIO_ETH_MediaInterfaceConfig(uint32_t GPIO_ETH_MediaInterface);	//**以太网外设**

## C语言相关

尝试用加粗部分，尤其uint8_t.

| **关键字**         | **位数** | **表示范围**             | **stdint****关键字** | **ST****关键字** |
| ------------------ | -------- | ------------------------ | -------------------- | ---------------- |
| char               | 8        | -128 ~ 127               | **int8_t**           | s8               |
| **unsigned char**  | 8        | 0 ~ 255                  | **uint8_t**          | u8               |
| short              | 16       | -32768 ~ 32767           | **int16_t**          | s16              |
| unsigned short     | 16       | 0 ~ 65535                | **uint16_t**         | u16              |
| int                | 32       | -2147483648 ~ 2147483647 | **int32_t**          | s32              |
| unsigned int       | 32       | 0 ~ 4294967295           | **uint32_t**         | u32              |
| long               | 32       | -2147483648 ~ 2147483647 |                      |                  |
| unsigned long      | 32       | 0 ~ 4294967295           |                      |                  |
| long long          | 64       | -(2^64)/2 ~ (2^64)/2-1   | **int64_t**          |                  |
| unsigned long long | 64       | 0 ~ (2^64)-1             | **uint64_t**         |                  |
| float              | 32       | -3.4e38 ~ 3.4e38         |                      |                  |
| double             | 64       | -1.7e308 ~ 1.7e308       |                      |                  |

•#**define**：用一个字符串代替一个数字，便于理解，防止出错；提取程序中经常出现的参数，便于快速修改，\#define ABC 12345；

•**typedef**：将一个比较长的变量类型名换个名字，便于使用，typedef unsigned char uint8_t;

•**struct**：数据打包，不同类型变量的集合；struct{char x; int y; float z;} StructName;

•**enum**：定义一个取值受限制的整型变量，用于限制变量取值范围；enum{FALSE = 0, TRUE = 1} EnumName;

```c
typedef enum {mon=1,tue=2,wed=3} week_7;

//

week_7 week;
```



## OLED

<img src="D:\DeskTop\learn\STM 32\image\image-20240421201406803.png" alt="image-20240421201406803" style="zoom:80%;" />

| **函数**                               | **作用**             |
| -------------------------------------- | -------------------- |
| OLED_Init();                           | 初始化               |
| OLED_Clear();                          | 清屏                 |
| OLED_ShowChar(1,  1, 'A');             | 显示一个字符         |
| OLED_ShowString(1, 3,  "HelloWorld!"); | 显示字符串           |
| OLED_ShowNum(2, 1, 12345, 5);          | 显示十进制数字       |
| OLED_ShowSignedNum(2, 7, -66, 2);      | 显示有符号十进制数字 |
| OLED_ShowHexNum(3, 1, 0xAA55, 4);      | 显示十六进制数字     |
| OLED_ShowBinNum(4, 1, 0xAA55, 16);     | 显示二进制数字       |

四阵脚多使用i2c通信七针脚多是spi通信。

## 中断

•中断：在主程序运行过程中，出现了特定的中断触发条件（中断源），使得CPU暂停当前正在运行的程序，转而去处理中断程序，处理完成后又返回原来被暂停的位置继续运行；

•中断优先级：当有多个中断源同时申请中断时，CPU会根据中断源的轻重缓急进行裁决，优先响应更加紧急的中断源；

•中断嵌套：当一个中断程序正在运行时，又有新的更高优先级的中断源申请中断，CPU再次暂停当前中断程序，转而去处理新的中断程序，处理完成后依次进行返回；

<img src="D:\DeskTop\learn\STM 32\image\image-20240421205326455.png" alt="image-20240421205326455" style="zoom:80%;" />

•68个可屏蔽中断通道，包含EXTI、TIM、ADC、USART、SPI、I2C、RTC等多个外设；

•使用NVIC统一管理中断，每个中断通道都拥有16个可编程的优先等级，可对优先级进行分组，进一步设置抢占优先级和响应优先级；

下表为中断向量表，程序执行到中断处时跳转到中断地址再执行跳转到指定函数的位置，图中地址值为各中断对应在存储中位置。

<img src="D:\DeskTop\learn\STM 32\image\image-20240421205933368.png" alt="image-20240421205933368" style="zoom: 80%;" />

<img src="C:\Users\21998\AppData\Roaming\Typora\typora-user-images\image-20240421205958338.png" alt="image-20240421205958338" style="zoom: 80%;" />

<img src="C:\Users\21998\AppData\Roaming\Typora\typora-user-images\image-20240421210019204.png" alt="image-20240421210019204" style="zoom: 80%;" />

<img src="D:\DeskTop\learn\STM 32\image\image-20240421210113496.png" alt="image-20240421210113496" style="zoom: 80%;" />

```c
`void EXTI_DeInit(void);`
`void EXTI_Init(EXTI_InitTypeDef* EXTI_InitStruct);`
`void EXTI_StructInit(EXTI_InitTypeDef* EXTI_InitStruct);`
`void EXTI_GenerateSWInterrupt(uint32_t EXTI_Line);`
    主函数中使用
`FlagStatus EXTI_GetFlagStatus(uint32_t EXTI_Line);`
`void EXTI_ClearFlag(uint32_t EXTI_Line);`
    中断函数中使用
`ITStatus EXTI_GetITStatus(uint32_t EXTI_Line);`
`void EXTI_ClearITPendingBit(uint32_t EXTI_Line);`
```

中断函数名称，调用中断函数时只能使用这些名字（放在启动文件里）

```c
            ; External Interrupts
            DCD     WWDG_IRQHandler            ; Window Watchdog
            DCD     PVD_IRQHandler             ; PVD through EXTI Line detect
            DCD     TAMPER_IRQHandler          ; Tamper
            DCD     RTC_IRQHandler             ; RTC
            DCD     FLASH_IRQHandler           ; Flash
            DCD     RCC_IRQHandler             ; RCC
            DCD     EXTI0_IRQHandler           ; EXTI Line 0
            DCD     EXTI1_IRQHandler           ; EXTI Line 1
            DCD     EXTI2_IRQHandler           ; EXTI Line 2
            DCD     EXTI3_IRQHandler           ; EXTI Line 3
            DCD     EXTI4_IRQHandler           ; EXTI Line 4
            DCD     DMA1_Channel1_IRQHandler   ; DMA1 Channel 1
            DCD     DMA1_Channel2_IRQHandler   ; DMA1 Channel 2
            DCD     DMA1_Channel3_IRQHandler   ; DMA1 Channel 3
            DCD     DMA1_Channel4_IRQHandler   ; DMA1 Channel 4
            DCD     DMA1_Channel5_IRQHandler   ; DMA1 Channel 5
            DCD     DMA1_Channel6_IRQHandler   ; DMA1 Channel 6
            DCD     DMA1_Channel7_IRQHandler   ; DMA1 Channel 7
            DCD     ADC1_2_IRQHandler          ; ADC1_2
            DCD     USB_HP_CAN1_TX_IRQHandler  ; USB High Priority or CAN1 TX
            DCD     USB_LP_CAN1_RX0_IRQHandler ; USB Low  Priority or CAN1 RX0
            DCD     CAN1_RX1_IRQHandler        ; CAN1 RX1
            DCD     CAN1_SCE_IRQHandler        ; CAN1 SCE
            DCD     EXTI9_5_IRQHandler         ; EXTI Line 9..5
            DCD     TIM1_BRK_IRQHandler        ; TIM1 Break
            DCD     TIM1_UP_IRQHandler         ; TIM1 Update
            DCD     TIM1_TRG_COM_IRQHandler    ; TIM1 Trigger and Commutation
            DCD     TIM1_CC_IRQHandler         ; TIM1 Capture Compare
            DCD     TIM2_IRQHandler            ; TIM2
            DCD     TIM3_IRQHandler            ; TIM3
            DCD     TIM4_IRQHandler            ; TIM4
            DCD     I2C1_EV_IRQHandler         ; I2C1 Event
            DCD     I2C1_ER_IRQHandler         ; I2C1 Error
            DCD     I2C2_EV_IRQHandler         ; I2C2 Event
            DCD     I2C2_ER_IRQHandler         ; I2C2 Error
            DCD     SPI1_IRQHandler            ; SPI1
            DCD     SPI2_IRQHandler            ; SPI2
            DCD     USART1_IRQHandler          ; USART1
            DCD     USART2_IRQHandler          ; USART2
            DCD     USART3_IRQHandler          ; USART3
            DCD     EXTI15_10_IRQHandler       ; EXTI Line 15..10
            DCD     RTCAlarm_IRQHandler        ; RTC Alarm through EXTI Line
            DCD     USBWakeUp_IRQHandler       ; USB Wakeup from suspend
```

### NVIC

<img src="D:\DeskTop\learn\STM 32\image\image-20240421210422837.png" alt="image-20240421210422837" style="zoom:67%;" />

NVIC的中断优先级由优先级寄存器的4位（0~15）决定，这4位可以进行切分，分为**高n位的抢占优先级和低4-n位的响应优先级**；

抢占优先级高的可以中断嵌套，响应优先级高的可以优先排队，抢占优先级和响应优先级均相同的按中断号排队。

| **分组方式** | **抢占优先级**  | **响应优先级**  |
| :----------: | :-------------: | :-------------: |
|    分组0     |  0位，取值为0   | 4位，取值为0~15 |
|    分组1     | 1位，取值为0~1  | 3位，取值为0~7  |
|    分组2     | 2位，取值为0~3  | 2位，取值为0~3  |
|    分组3     | 3位，取值为0~7  | 1位，取值为0~1  |
|    分组4     | 4位，取值为0~15 |  0位，取值为0   |

### EXTI

•EXTI（Extern Interrupt）外部中断

•EXTI可以监测指定GPIO口的电平信号，当其指定的GPIO口产生电平变化时，EXTI将立即向NVIC发出中断申请，经过NVIC裁决后即可中断CPU主程序，使CPU执行EXTI对应的中断程序；

•支持的触发方式：**上升沿/下降沿/双边沿/软件触发**；

•支持的GPIO口：所有GPIO口，但相同的Pin不能同时触发中断，PA0和PB0不能同时用；

•通道数：16个GPIO_Pin，外加PVD输出、RTC闹钟、USB唤醒、以太网唤醒；

触发响应方式：中断响应/事件响应；

<img src="D:\DeskTop\learn\STM 32\image\image-20240421211341182.png" alt="image-20240421211341182" style="zoom:80%;" />

**AFIO**数据选择器在**GPIOA0/B0/C0...之间进行数据选择**，所以他们不能同时作为中断；

​	在其他方面用作**复用功能引脚重映射**。

### 示例

1.RCC开启GPIO和AFIO，

2.配置EXTI和NVIC，

3.写中断函数，函数名为固定不可更改。

```c
#include "stm32f10x.h"                  // Device header
#include "stm32f10x_conf.h"

uint16_t CountSensor_Count;				//全局变量，用于计数

/**
  * 函    数：计数传感器初始化
  * 参    数：  无
  * 返 回 值：无
  */
void CountSensor_Init(void)
{
	/*开启时钟*/
	RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOB, ENABLE);		//开启GPIOB的时钟
	RCC_APB2PeriphClockCmd(RCC_APB2Periph_AFIO, ENABLE);		//开启AFIO的时钟，外部中断必须开启AFIO的时钟
	
	/*GPIO初始化*/
	GPIO_InitTypeDef GPIO_InitStructure;
	GPIO_InitStructure.GPIO_Mode = GPIO_Mode_IPU;
	GPIO_InitStructure.GPIO_Pin = GPIO_Pin_14;
	GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;
	GPIO_Init(GPIOB, &GPIO_InitStructure);						//将PB14引脚初始化为上拉输入
	
	/*AFIO选择中断引脚*/
	GPIO_EXTILineConfig(GPIO_PortSourceGPIOB, GPIO_PinSource14);//将外部中断的14号线映射到GPIOB，即选择PB14为外部中断引脚
	
	/*EXTI初始化*/
	EXTI_InitTypeDef EXTI_InitStructure;						//定义结构体变量
	EXTI_InitStructure.EXTI_Line = EXTI_Line14;					//选择配置外部中断的14号线
	EXTI_InitStructure.EXTI_LineCmd = ENABLE;					//指定外部中断线使能
	EXTI_InitStructure.EXTI_Mode = EXTI_Mode_Interrupt;			//指定外部中断线为中断模式
	EXTI_InitStructure.EXTI_Trigger = EXTI_Trigger_Falling;		//指定外部中断线为下降沿触发
	EXTI_Init(&EXTI_InitStructure);								//将结构体变量交给EXTI_Init，配置EXTI外设
	
	/*NVIC中断分组*/
	NVIC_PriorityGroupConfig(NVIC_PriorityGroup_2);				//配置NVIC为分组2
																//即抢占优先级范围：0~3，响应优先级范围：0~3
																//此分组配置在整个工程中仅需调用一次
																//若有多个中断，可以把此代码放在main函数内，while循环之前
																//若调用多次配置分组的代码，则后执行的配置会覆盖先执行的配置
	
	/*NVIC配置*/
	NVIC_InitTypeDef NVIC_InitStructure;						//定义结构体变量
	NVIC_InitStructure.NVIC_IRQChannel = EXTI15_10_IRQn;		//选择配置NVIC的EXTI15_10线
	NVIC_InitStructure.NVIC_IRQChannelCmd = ENABLE;				//指定NVIC线路使能
	NVIC_InitStructure.NVIC_IRQChannelPreemptionPriority = 1;	//指定NVIC线路的抢占优先级为1
	NVIC_InitStructure.NVIC_IRQChannelSubPriority = 1;			//指定NVIC线路的响应优先级为1
	NVIC_Init(&NVIC_InitStructure);								//将结构体变量交给NVIC_Init，配置NVIC外设
}

/**
  * 函    数：获取计数传感器的计数值
  * 参    数：无
  * 返 回 值：计数值，范围：0~65535
  */
uint16_t CountSensor_Get(void)
{
	return CountSensor_Count;
}

/**
  * 函    数：EXTI15_10外部中断函数
  * 参    数：无
  * 返 回 值：无
  * 注意事项：此函数为中断函数，无需调用，中断触发后自动执行
  *           函数名为预留的指定名称，可以从启动文件复制
  *           请确保函数名正确，不能有任何差异，否则中断函数将不能进入
  */
void EXTI15_10_IRQHandler(void)
{
	if (EXTI_GetITStatus(EXTI_Line14) == SET)		//判断是否是外部中断14号线触发的中断
	{
		/*如果出现数据乱跳的现象，可再次判断引脚电平，以避免抖动*/
		if (GPIO_ReadInputDataBit(GPIOB, GPIO_Pin_14) == 0)
		{
			CountSensor_Count ++;					//计数值自增一次
		}
		EXTI_ClearITPendingBit(EXTI_Line14);		//清除外部中断14号线的中断标志位
													//中断标志位必须清除
													//否则中断将连续不断地触发，导致主程序卡死
	}
}
```

## TIM（Timer）定时器

•定时器可以对输入的时钟进行计数，并在计数值达到设定值时触发中断；

•16位计数器、预分频器、自动重装寄存器的时基单元，在72MHz计数时钟下可以实现最大59.65s的定时；

•不仅具备基本的定时中断功能，而且还包含内外时钟源选择、输入捕获、输出比较、编码器接口、主从触发模式等多种功能；

•根据复杂度和应用场景分为了**高级定时器、通用定时器、基本定时器**三种类型；

| **类型**   | **编号**               | **总线** |                           **功能**                           |
| ---------- | ---------------------- | -------- | :----------------------------------------------------------: |
| 高级定时器 | TIM1、TIM8             | APB2     | 拥有通用定时器全部功能，并额外具有重复计数器、死区生成、互补输出、刹车输入等功能 |
| 通用定时器 | TIM2、TIM3、TIM4、TIM5 | APB1     | 拥有基本定时器全部功能，并额外具有内外时钟源选择、输入捕获、输出比较、编码器接口、主从触发模式等功能 |
| 基本定时器 | TIM6、TIM7             | APB1     |              拥有定时中断、主模式触发DAC的功能               |

•	STM32F103C8T6**定时器**资源：TIM1、TIM2、TIM3、TIM4

### 基本定时器

**两大功能定时中断和主模式触发DAC；**

![image-20240614095429795](D:\DeskTop\learn\STM 32\image\image-20240614095429795.png)

​	*UI为更新中断U为更新事件*

**中断**

1. 内部时钟为72MHz，进入预分频器进行分频，对输入的基准频率进行提前分频，16位可以设置最大65536分频，且只能选择内部时钟；
2. 计数器上升沿+1，且自动归零产生中断，只能向上计数；
3. 自动重装寄存器计数值等于自动重装值，即从0计数到重装值后产生中断，称为更新中断。
4. 中断通过NVIC经过配置通道后进入到CPU。

**·主模式触发**DAC

在进行DAC转换中不需要通过中断频繁进行，只需把更新事件通过主模式映射到TRGO，然后TRGO就会直接触发DAC。

### 通用定时器

<img src="D:\DeskTop\learn\STM 32\image\image-20240424202302754.png" alt="image-20240424202302754" style="zoom: 150%;" />

1.**计数器**存在向上向下以及中央对齐的计数方式，向上同基本定时器计数到重装值后产生中断，向下为从重装值递减到零后产生中断，中间对齐为从0先向上自增到达重装值后申请中断，之后向下递减到0后申请中断，依次循环。

2.时钟源可以在内部时钟以及外部时钟之间进行选择，TIMx_ETR连接外部时钟在经过输入滤波等后作为时钟，称为**外部时钟模式二**。

3.TRGI也可以提供时钟，**外部时钟模式一**，TR0TR0TR2TR3分别来自其他定时器的TRGO输出，可以实现定时器的级联；

例如：首先初始化TIM3然后使用主模式把更新事件映射到TRGO上，接着初始化ITR2（对应TIM3的TRGO），接着选择外部时钟模式一，至此完成TIM3的更新事件驱动了TIM2的时基单元也就实现了定时器的级联。

4.时钟还可通过**TIMx_CH1**获得还可通过**TI1FP1及TI2FP2**获得。

### 高级定时器

**时基单元包含**： 

● 计数器寄存器(TIMx_CNT)  

● 预分频器寄存器 (TIMx_PSC)  

● 自动装载寄存器 (TIMx_ARR)  

● 重复次数寄存器 (TIMx_RCR) 

![image-20240425100542745](D:\DeskTop\learn\STM 32\image\image-20240425100542745.png)

### 定时中断基本结构

![image-20240424202450985](D:\DeskTop\learn\STM 32\image\image-20240424202450985.png)

```c
void TIM_DeInit(TIM_TypeDef* TIMx);//恢复定时器
void TIM_TimeBaseInit(TIM_TypeDef* TIMx, TIM_TimeBaseInitTypeDef* TIM_TimeBaseInitStruct);//配置时基单元
void TIM_Cmd(TIM_TypeDef* TIMx, FunctionalState NewState);//运行控制定时器
void TIM_ITConfig(TIM_TypeDef* TIMx, uint16_t TIM_IT, FunctionalState NewState);//对定时器进行中断输出控制
void TIM_InternalClockConfig(TIM_TypeDef* TIMx);//内部时钟模式
void TIM_ITRxExternalClockConfig(TIM_TypeDef* TIMx, uint16_t TIM_InputTriggerSource);//ITR外部时钟模式
void TIM_TIxExternalClockConfig(TIM_TypeDef* TIMx, uint16_t TIM_TIxExternalCLKSource,
                                uint16_t TIM_ICPolarity, uint16_t ICFilter);//TIX编码器模式
void TIM_ETRClockMode1Config(TIM_TypeDef* TIMx, uint16_t TIM_ExtTRGPrescaler, uint16_t TIM_ExtTRGPolarity,
                             uint16_t ExtTRGFilter);//ETR外部时钟一
void TIM_ETRClockMode2Config(TIM_TypeDef* TIMx, uint16_t TIM_ExtTRGPrescaler, 
                             uint16_t TIM_ExtTRGPolarity, uint16_t ExtTRGFilter);//ETR外部时钟二
void TIM_ETRConfig(TIM_TypeDef* TIMx, uint16_t TIM_ExtTRGPrescaler, uint16_t TIM_ExtTRGPolarity,
                   uint16_t ExtTRGFilter);//配置ETR的极性选择和极性滤波等
```



### 时序图

#### **分频器时序：**

<img src="D:\DeskTop\learn\STM 32\image\image-20240424203137975.png" alt="image-20240424203137975" style="zoom: 50%;" />

​								计数器计数频率：**CK_CNT = CK_PSC / (PSC + 1)**

预分频控制寄存器是直接读写用的寄存器，而缓冲寄存器是直接起作用的寄存器。

![image-20240425102058615](D:\DeskTop\learn\STM 32\image\image-20240425102058615.png)

#### 计数器时序

![image-20240425103319669](D:\DeskTop\learn\STM 32\image\image-20240425103319669.png)

​				•计数器溢出频率：CK_CNT_OV = CK_CNT / (ARR + 1)   = CK_PSC / (PSC + 1) / (ARR + 1)

#### 计数器无预装时序

![image-20240614113948960](D:\DeskTop\learn\STM 32\image\image-20240614113948960.png)

#### 计数器有预装时序

![image-20240614114009561](D:\DeskTop\learn\STM 32\image\image-20240614114009561.png)

### RCC时钟树

![image-20240614114208492](D:\DeskTop\learn\STM 32\image\image-20240614114208492.png)

### 定时器中断示例

1.RCC开启时钟

2.选择时基单元的时钟源

3.配置时基单元

4.配置中断输出控制，允许更新中断到NVIC

5.配置NVIC，打开中断通道，分配优先级

6.运行控制，使能定时器。

#### 内部时钟

```c
#include "stm32f10x.h"                  // Device header

/**
  * 函    数：定时中断初始化
  * 参    数：无
  * 返 回 值：无
  */
void Timer_Init(void)
{
	/*开启时钟*/
	RCC_APB1PeriphClockCmd(RCC_APB1Periph_TIM2, ENABLE);			//开启TIM2的时钟
	
	/*配置时钟源*/
	TIM_InternalClockConfig(TIM2);		//选择TIM2为内部时钟，若不调用此函数，TIM默认也为内部时钟
	
	/*时基单元初始化*/
	TIM_TimeBaseInitTypeDef TIM_TimeBaseInitStructure;				//定义结构体变量
	TIM_TimeBaseInitStructure.TIM_ClockDivision = TIM_CKD_DIV1;		//时钟分频，选择不分频，此参数用于配置滤波器时钟，不影响时基单元功能
	TIM_TimeBaseInitStructure.TIM_CounterMode = TIM_CounterMode_Up;	//计数器模式，选择向上计数
	TIM_TimeBaseInitStructure.TIM_Period = 10000 - 1;				//计数周期，即ARR的值
	TIM_TimeBaseInitStructure.TIM_Prescaler = 7200 - 1;				//预分频器，即PSC的值
	TIM_TimeBaseInitStructure.TIM_RepetitionCounter = 0;			//重复计数器，高级定时器才会用到
	TIM_TimeBaseInit(TIM2, &TIM_TimeBaseInitStructure);				//将结构体变量交给TIM_TimeBaseInit，配置TIM2的时基单元	
	
	/*中断输出配置*/
	TIM_ClearFlag(TIM2, TIM_FLAG_Update);						//清除定时器更新标志位
																//TIM_TimeBaseInit函数末尾，手动产生了更新事件
																//若不清除此标志位，则开启中断后，会立刻进入一次中断
																//如果不介意此问题，则不清除此标志位也可
	
	TIM_ITConfig(TIM2, TIM_IT_Update, ENABLE);					//开启TIM2的更新中断
	
	/*NVIC中断分组*/
	NVIC_PriorityGroupConfig(NVIC_PriorityGroup_2);				//配置NVIC为分组2
																//即抢占优先级范围：0~3，响应优先级范围：0~3
																//此分组配置在整个工程中仅需调用一次
																//若有多个中断，可以把此代码放在main函数内，while循环之前
																//若调用多次配置分组的代码，则后执行的配置会覆盖先执行的配置
	
	/*NVIC配置*/
	NVIC_InitTypeDef NVIC_InitStructure;						//定义结构体变量
	NVIC_InitStructure.NVIC_IRQChannel = TIM2_IRQn;				//选择配置NVIC的TIM2线
	NVIC_InitStructure.NVIC_IRQChannelCmd = ENABLE;				//指定NVIC线路使能
	NVIC_InitStructure.NVIC_IRQChannelPreemptionPriority = 2;	//指定NVIC线路的抢占优先级为2
	NVIC_InitStructure.NVIC_IRQChannelSubPriority = 1;			//指定NVIC线路的响应优先级为1
	NVIC_Init(&NVIC_InitStructure);								//将结构体变量交给NVIC_Init，配置NVIC外设
	
	/*TIM使能*/
	TIM_Cmd(TIM2, ENABLE);			//使能TIM2，定时器开始运行
}

/* 定时器中断函数，可以复制到使用它的地方
void TIM2_IRQHandler(void)
{
	if (TIM_GetITStatus(TIM2, TIM_IT_Update) == SET)
	{
		
		TIM_ClearITPendingBit(TIM2, TIM_IT_Update);
	}
}
*/
```

#### 外部时钟

```c
#include "stm32f10x.h"                  // Device header

/**
  * 函    数：定时中断初始化
  * 参    数：无
  * 返 回 值：无
  * 注意事项：此函数配置为外部时钟，定时器相当于计数器
  */
void Timer_Init(void)
{
	/*开启时钟*/
	RCC_APB1PeriphClockCmd(RCC_APB1Periph_TIM2, ENABLE);			//开启TIM2的时钟
	RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOA, ENABLE);			//开启GPIOA的时钟
	
	/*GPIO初始化*/
	GPIO_InitTypeDef GPIO_InitStructure;
	GPIO_InitStructure.GPIO_Mode = GPIO_Mode_IPU;
	GPIO_InitStructure.GPIO_Pin = GPIO_Pin_0;
	GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;
	GPIO_Init(GPIOA, &GPIO_InitStructure);						//将PA0引脚初始化为上拉输入
	
	/*外部时钟配置*/
	TIM_ETRClockMode2Config(TIM2, TIM_ExtTRGPSC_OFF, TIM_ExtTRGPolarity_NonInverted, 0x0F);
																//选择外部时钟模式2，时钟从TIM_ETR引脚输入
																//注意TIM2的ETR引脚固定为PA0，无法随意更改
																//最后一个滤波器参数加到最大0x0F，可滤除时钟信号抖动
	
	/*时基单元初始化*/
	TIM_TimeBaseInitTypeDef TIM_TimeBaseInitStructure;				//定义结构体变量
	TIM_TimeBaseInitStructure.TIM_ClockDivision = TIM_CKD_DIV1;		//时钟分频，选择不分频，此参数用于配置滤波器时钟，不影响时基单元功能
	TIM_TimeBaseInitStructure.TIM_CounterMode = TIM_CounterMode_Up;	//计数器模式，选择向上计数
	TIM_TimeBaseInitStructure.TIM_Period = 10 - 1;					//计数周期，即ARR的值
	TIM_TimeBaseInitStructure.TIM_Prescaler = 1 - 1;				//预分频器，即PSC的值
	TIM_TimeBaseInitStructure.TIM_RepetitionCounter = 0;			//重复计数器，高级定时器才会用到
	TIM_TimeBaseInit(TIM2, &TIM_TimeBaseInitStructure);				//将结构体变量交给TIM_TimeBaseInit，配置TIM2的时基单元	
	
	/*中断输出配置*/
	TIM_ClearFlag(TIM2, TIM_FLAG_Update);						//清除定时器更新标志位
																//TIM_TimeBaseInit函数末尾，手动产生了更新事件
																//若不清除此标志位，则开启中断后，会立刻进入一次中断
																//如果不介意此问题，则不清除此标志位也可
																
	TIM_ITConfig(TIM2, TIM_IT_Update, ENABLE);					//开启TIM2的更新中断
	
	/*NVIC中断分组*/
	NVIC_PriorityGroupConfig(NVIC_PriorityGroup_2);				//配置NVIC为分组2
																//即抢占优先级范围：0~3，响应优先级范围：0~3
																//此分组配置在整个工程中仅需调用一次
																//若有多个中断，可以把此代码放在main函数内，while循环之前
																//若调用多次配置分组的代码，则后执行的配置会覆盖先执行的配置
	
	/*NVIC配置*/
	NVIC_InitTypeDef NVIC_InitStructure;						//定义结构体变量
	NVIC_InitStructure.NVIC_IRQChannel = TIM2_IRQn;				//选择配置NVIC的TIM2线
	NVIC_InitStructure.NVIC_IRQChannelCmd = ENABLE;				//指定NVIC线路使能
	NVIC_InitStructure.NVIC_IRQChannelPreemptionPriority = 2;	//指定NVIC线路的抢占优先级为2
	NVIC_InitStructure.NVIC_IRQChannelSubPriority = 1;			//指定NVIC线路的响应优先级为1
	NVIC_Init(&NVIC_InitStructure);								//将结构体变量交给NVIC_Init，配置NVIC外设
	
	/*TIM使能*/
	TIM_Cmd(TIM2, ENABLE);			//使能TIM2，定时器开始运行
}

/**
  * 函    数：返回定时器CNT的值
  * 参    数：无
  * 返 回 值：定时器CNT的值，范围：0~65535
  */
uint16_t Timer_GetCounter(void)
{
	return TIM_GetCounter(TIM2);	//返回定时器TIM2的CNT
}

/* 定时器中断函数，可以复制到使用它的地方
void TIM2_IRQHandler(void)
{
	if (TIM_GetITStatus(TIM2, TIM_IT_Update) == SET)
	{
		
		TIM_ClearITPendingBit(TIM2, TIM_IT_Update);
	}
}
*/
```

### 输出比较

**OC** output compare，输出比较可以通过比较CNT（时基单元中普通的计数器）与CCR寄存器（捕获比较寄存器，是输入和捕获共同使用）值的关系，来对输出电平进行置1、置0或翻转的操作，用于**输出一定频率和占空比的PWM波形**。

每个高级定时器和通用定时器都拥有4个输出比较通道，可以同时输出思路PWM波形，有各自的CCR寄存器，但是共用一个CNT计数器；高级定时器的前3个通道额外拥有死区生成和互补输出的功能，用于驱动三项无刷电机。

```c
void TIM_OC1Init(TIM_TypeDef* TIMx, TIM_OCInitTypeDef* TIM_OCInitStruct);
void TIM_OC2Init(TIM_TypeDef* TIMx, TIM_OCInitTypeDef* TIM_OCInitStruct);
void TIM_OC3Init(TIM_TypeDef* TIMx, TIM_OCInitTypeDef* TIM_OCInitStruct);
void TIM_OC4Init(TIM_TypeDef* TIMx, TIM_OCInitTypeDef* TIM_OCInitStruct);

TIM_OCStructInit(&TIM_OCInitStructure);	//结构体初始化，给所有的变量都初始值
```

#### PWM

![image-20240614200151986](D:\DeskTop\learn\STM 32\image\image-20240614200151986.png)

#### **输出比较通道（通用）**

![image-20240614200643660](C:\Users\21998\AppData\Roaming\Typora\typora-user-images\image-20240614200643660.png)

| **模式**           |                           **描述**                           |
| ------------------ | :----------------------------------------------------------: |
| 冻结               |                  CNT=CCR时，REF保持为原状态                  |
| 匹配时置有效电平   |                   CNT=CCR时，REF置有效电平                   |
| 匹配时置无效电平   |                   CNT=CCR时，REF置无效电平                   |
| **匹配时电平翻转** |                    CNT=CCR时，REF电平翻转                    |
| 强制为无效电平     |               CNT与CCR无效，REF强制为无效电平                |
| 强制为有效电平     |               CNT与CCR无效，REF强制为有效电平                |
| PWM**模式**1       | 向上计数：CNT<CCR时，REF置有效电平，CNT≥CCR时，REF置无效电平  向下计数：CNT>CCR时，REF置无效电平，CNT≤CCR时，REF置有效电平 |
| PWM**模式**2       | 向上计数：CNT<CCR时，REF置无效电平，CNT≥CCR时，REF置有效电平  向下计数：CNT>CCR时，REF置有效电平，CNT≤CCR时，REF置无效电平 |

![image-20240614202021100](D:\DeskTop\learn\STM 32\image\image-20240614202021100.png)

​													（此图为模式一）

- PWM频率： Freq = CK_PSC / (PSC + 1) / (ARR + 1)
- PWM占空比： Duty = CCR / (ARR + 1)
- PWM分辨率： Reso = 1 / (ARR + 1)

#### 输出比较通道（高级）

![image-20240614200726359](D:\DeskTop\learn\STM 32\image\image-20240614200726359.png)

OC1和OC1N为互补输出，分别控制推挽输出的两个输入端口（用于驱动电机）；加入死区发生器，在上管关闭时延迟一小段事件再打开下管（下管时也同）。

#### 舵机&直流电机

1.舵机是一种根据输入PWM信号占空比来控制输出角度的装置，输入PWM信号要求：周期为20ms，高电平宽度为0.5ms~2.5ms。

2.直流电机是一种将电能转换为机械能的装置，有两个电极，当电极正接时，电机正转，当电极反接时，电机反转；直流电机属于大功率器件，GPIO口无法直接驱动，需要配合电机驱动电路来操作；TB6612是一款双路H桥型的直流电机驱动芯片，可以驱动两个直流电机并且控制其转速和方向

<img src="D:\DeskTop\learn\STM 32\image\image-20240614204408451.png" alt="image-20240614204408451" style="zoom:50%;" />

<img src="D:\DeskTop\learn\STM 32\image\image-20240614204528295.png" alt="image-20240614204528295" style="zoom:50%;" />

#### 示例

1.RCC开启时钟，把TIM外设和GPIO外设时钟打开

2.配置时基单元包括前面的时钟源选择

3.配置输出比较单元，CCR的值、输出比较模式、极性选则（选择有效电平为高或者低）、输出使能

4.配置GPIO 把用到的输出口设置为**复用**推挽输出模式。

```c
#include "stm32f10x.h"                  // Device header

/**
  * 函    数：PWM初始化
  * 参    数：无
  * 返 回 值：无
  */
void PWM_Init(void)
{
	/*开启时钟*/
	RCC_APB1PeriphClockCmd(RCC_APB1Periph_TIM2, ENABLE);			//开启TIM2的时钟
	RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOA, ENABLE);			//开启GPIOA的时钟
	
	/*GPIO重映射*/
//	RCC_APB2PeriphClockCmd(RCC_APB2Periph_AFIO, ENABLE);			//开启AFIO的时钟，重映射必须先开启AFIO的时钟
//	GPIO_PinRemapConfig(GPIO_PartialRemap1_TIM2, ENABLE);			//将TIM2的引脚部分重映射，具体的映射方案需查看参考手册
//	GPIO_PinRemapConfig(GPIO_Remap_SWJ_JTAGDisable, ENABLE);		//将JTAG引脚失能，作为普通GPIO引脚使用
	
	/*GPIO初始化*/
	GPIO_InitTypeDef GPIO_InitStructure;
	GPIO_InitStructure.GPIO_Mode = GPIO_Mode_AF_PP;
	GPIO_InitStructure.GPIO_Pin = GPIO_Pin_0;		//GPIO_Pin_15;
	GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;
	GPIO_Init(GPIOA, &GPIO_InitStructure);							//将PA0引脚初始化为复用推挽输出	
																	//受外设控制的引脚，均需要配置为复用模式		
	
	/*配置时钟源*/
	TIM_InternalClockConfig(TIM2);		//选择TIM2为内部时钟，若不调用此函数，TIM默认也为内部时钟
	
	/*时基单元初始化*/
	TIM_TimeBaseInitTypeDef TIM_TimeBaseInitStructure;				//定义结构体变量
	TIM_TimeBaseInitStructure.TIM_ClockDivision = TIM_CKD_DIV1;     //时钟分频，选择不分频，此参数用于配置滤波器时钟，不影响时基单元功能
	TIM_TimeBaseInitStructure.TIM_CounterMode = TIM_CounterMode_Up; //计数器模式，选择向上计数
	TIM_TimeBaseInitStructure.TIM_Period = 100 - 1;					//计数周期，即ARR的值
	TIM_TimeBaseInitStructure.TIM_Prescaler = 720 - 1;				//预分频器，即PSC的值
	TIM_TimeBaseInitStructure.TIM_RepetitionCounter = 0;            //重复计数器，高级定时器才会用到
	TIM_TimeBaseInit(TIM2, &TIM_TimeBaseInitStructure);             //将结构体变量交给TIM_TimeBaseInit，配置TIM2的时基单元
	
	/*输出比较初始化*/
	TIM_OCInitTypeDef TIM_OCInitStructure;							//定义结构体变量
	TIM_OCStructInit(&TIM_OCInitStructure);							//结构体初始化，若结构体没有完整赋值
																	//则最好执行此函数，给结构体所有成员都赋一个默认值
																	//避免结构体初值不确定的问题
	TIM_OCInitStructure.TIM_OCMode = TIM_OCMode_PWM1;				//输出比较模式，选择PWM模式1
	TIM_OCInitStructure.TIM_OCPolarity = TIM_OCPolarity_High;		//输出极性，选择为高，若选择极性为低，则输出高低电平取反
	TIM_OCInitStructure.TIM_OutputState = TIM_OutputState_Enable;	//输出使能
	TIM_OCInitStructure.TIM_Pulse = 0;								//初始的CCR值
	TIM_OC1Init(TIM2, &TIM_OCInitStructure);						//将结构体变量交给TIM_OC1Init，配置TIM2的输出比较通道1
	
	/*TIM使能*/
	TIM_Cmd(TIM2, ENABLE);			//使能TIM2，定时器开始运行
}

/**
  * 函    数：PWM设置CCR
  * 参    数：Compare 要写入的CCR的值，范围：0~100
  * 返 回 值：无
  * 注意事项：CCR和ARR共同决定占空比，此函数仅设置CCR的值，并不直接是占空比
  *           占空比Duty = CCR / (ARR + 1)
  */
void PWM_SetCompare1(uint16_t Compare)
{
	TIM_SetCompare1(TIM2, Compare);		//设置CCR1的值
}
```

### 输入捕获

​	**IC**（Input Capture）输入捕获。输入捕获模式下，当**通道输入引脚出现指定电平跳变**时，当前**CNT的值将被锁存到CCR**中，可用于测量PWM波形的频率、占空比、脉冲间隔、电平持续时间等参数。每个高级定时器和通用定时器都拥有4个输入捕获通道，可配置为**PWMI**模式，**同时测量频率和占空比**，可配合主从触发模式，实现硬件**全自动测量**。

<img src="D:\DeskTop\learn\STM 32\image\image-20240615153346381.png" alt="image-20240615153346381" style="zoom:67%;" />

#### 输入通道捕获

对比通用定时器图查看

![image-20240615154644061](C:\Users\21998\AppData\Roaming\Typora\typora-user-images\image-20240615154644061.png)

#### 主从触发模式

![image-20240615155255190](C:\Users\21998\AppData\Roaming\Typora\typora-user-images\image-20240615155255190.png)

**主模式**将定时器内部的信号，映射到TRGO引脚；

**从模式**接受其他外设或者自身外设的一些信号，用于控制自身定时器的运行，也就是被别的信号控制；

**触发源选择**选择从模式的触发信号源，选择指定一个信号触发TRGI去触发从模式。

**例如**选择TI1FP1触发TRGI后触发Reset，从模式自动清零，实现硬件全自动测量。

注意：**Reset**只能使用通道一和通道二，对于通道三和四只能开启捕获中断在中断种手动清零。

#### 输入捕获基本结构

<img src="C:\Users\21998\AppData\Roaming\Typora\typora-user-images\image-20240615161447649.png" alt="image-20240615161447649" style="zoom:80%;" />

#### PWMI基本结构

使用两个通道同时捕获一个引脚，可以同时测量周期和占空比。

![image-20240615162701766](D:\DeskTop\learn\STM 32\image\image-20240615162701766.png)

#### 示例

```c
#include "stm32f10x.h"                  // Device header

/**
  * 函    数：输入捕获初始化
  * 参    数：无
  * 返 回 值：无
  */
void IC_Init(void)
{
	/*开启时钟*/
	RCC_APB1PeriphClockCmd(RCC_APB1Periph_TIM3, ENABLE);			//开启TIM3的时钟
	RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOA, ENABLE);			//开启GPIOA的时钟
	
	/*GPIO初始化*/
	GPIO_InitTypeDef GPIO_InitStructure;
	GPIO_InitStructure.GPIO_Mode = GPIO_Mode_IPU;
	GPIO_InitStructure.GPIO_Pin = GPIO_Pin_6;
	GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;
	GPIO_Init(GPIOA, &GPIO_InitStructure);							//将PA6引脚初始化为上拉输入
	
	/*配置时钟源*/
	TIM_InternalClockConfig(TIM3);		//选择TIM3为内部时钟，若不调用此函数，TIM默认也为内部时钟
	
	/*时基单元初始化*/
	TIM_TimeBaseInitTypeDef TIM_TimeBaseInitStructure;				//定义结构体变量
	TIM_TimeBaseInitStructure.TIM_ClockDivision = TIM_CKD_DIV1;     //时钟分频，选择不分频，此参数用于配置滤波器时钟，不影响时基单元功能
	TIM_TimeBaseInitStructure.TIM_CounterMode = TIM_CounterMode_Up; //计数器模式，选择向上计数
	TIM_TimeBaseInitStructure.TIM_Period = 65536 - 1;               //计数周期，即ARR的值
	TIM_TimeBaseInitStructure.TIM_Prescaler = 72 - 1;               //预分频器，即PSC的值
	TIM_TimeBaseInitStructure.TIM_RepetitionCounter = 0;            //重复计数器，高级定时器才会用到
	TIM_TimeBaseInit(TIM3, &TIM_TimeBaseInitStructure);             //将结构体变量交给TIM_TimeBaseInit，配置TIM3的时基单元
	
	/*输入捕获初始化*/
	TIM_ICInitTypeDef TIM_ICInitStructure;							//定义结构体变量
	TIM_ICInitStructure.TIM_Channel = TIM_Channel_1;				//选择配置定时器通道1
	TIM_ICInitStructure.TIM_ICFilter = 0xF;							//输入滤波器参数，可以过滤信号抖动
	TIM_ICInitStructure.TIM_ICPolarity = TIM_ICPolarity_Rising;		//极性，选择为上升沿触发捕获
	TIM_ICInitStructure.TIM_ICPrescaler = TIM_ICPSC_DIV1;			//捕获预分频，选择不分频，每次信号都触发捕获
	TIM_ICInitStructure.TIM_ICSelection = TIM_ICSelection_DirectTI;	//输入信号交叉，选择直通，不交叉
	TIM_ICInit(TIM3, &TIM_ICInitStructure);							//将结构体变量交给TIM_ICInit，配置TIM3的输入捕获通道
	
	/*选择触发源及从模式*/
	TIM_SelectInputTrigger(TIM3, TIM_TS_TI1FP1);					//触发源选择TI1FP1
	TIM_SelectSlaveMode(TIM3, TIM_SlaveMode_Reset);					//从模式选择复位
																	//即TI1产生上升沿时，会触发CNT归零
	
	/*TIM使能*/
	TIM_Cmd(TIM3, ENABLE);			//使能TIM3，定时器开始运行
}

/**
  * 函    数：获取输入捕获的频率
  * 参    数：无
  * 返 回 值：捕获得到的频率
  */
uint32_t IC_GetFreq(void)
{
	return 1000000 / (TIM_GetCapture1(TIM3) + 1);		//测周法得到频率fx = fc / N，这里不执行+1的操作也可
}

```

### Encoder Interface 编码器接口

编码器接口可接收增量（正交）编码器的信号，根据编码器旋转产生的正交信号脉冲，自动控制CNT自增或自减，从而指示编码器的位置、旋转方向和旋转速度。每**个高级定时器和通用定时器都拥有1个编码器接口**，两个输入引脚借用了输入捕获的通道1和通道2。

![image-20240616111219593](D:\DeskTop\learn\STM 32\image\image-20240616111219593.png)

![image-20240616113119929](C:\Users\21998\AppData\Roaming\Typora\typora-user-images\image-20240616113119929.png)

**正转状态都向上计数，反转状态都向下计数**。

#### 编码器接口基本结构

![image-20240616112333770](D:\DeskTop\learn\STM 32\image\image-20240616112333770.png)

#### 示例

1.RCC开启时钟，开启GPIO和定时器的时钟

2.配置GPIO，设置端口为输入模式

3.配置时基单元

4.配置输入捕获单元，只有滤波器和极性两个参数可用

5.配置编码器接口模式

6.timcmd启动定时器

```c
#include "stm32f10x.h"                  // Device header

/**
  * 函    数：编码器初始化
  * 参    数：无
  * 返 回 值：无
  */
void Encoder_Init(void)
{
	/*开启时钟*/
	RCC_APB1PeriphClockCmd(RCC_APB1Periph_TIM3, ENABLE);			//开启TIM3的时钟
	RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOA, ENABLE);			//开启GPIOA的时钟
	
	/*GPIO初始化*/
	GPIO_InitTypeDef GPIO_InitStructure;
	GPIO_InitStructure.GPIO_Mode = GPIO_Mode_IPU;
	GPIO_InitStructure.GPIO_Pin = GPIO_Pin_6 | GPIO_Pin_7;
	GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;
	GPIO_Init(GPIOA, &GPIO_InitStructure);							//将PA6和PA7引脚初始化为上拉输入
	
	/*时基单元初始化*/
	TIM_TimeBaseInitTypeDef TIM_TimeBaseInitStructure;				//定义结构体变量
	TIM_TimeBaseInitStructure.TIM_ClockDivision = TIM_CKD_DIV1;     //时钟分频，选择不分频，此参数用于配置滤波器时钟，不影响时基单元功能
	TIM_TimeBaseInitStructure.TIM_CounterMode = TIM_CounterMode_Up; //计数器模式，选择向上计数
	TIM_TimeBaseInitStructure.TIM_Period = 65536 - 1;               //计数周期，即ARR的值
	TIM_TimeBaseInitStructure.TIM_Prescaler = 1 - 1;                //预分频器，即PSC的值
	TIM_TimeBaseInitStructure.TIM_RepetitionCounter = 0;            //重复计数器，高级定时器才会用到
	TIM_TimeBaseInit(TIM3, &TIM_TimeBaseInitStructure);             //将结构体变量交给TIM_TimeBaseInit，配置TIM3的时基单元
	
	/*输入捕获初始化*/
	TIM_ICInitTypeDef TIM_ICInitStructure;							//定义结构体变量
	TIM_ICStructInit(&TIM_ICInitStructure);							//结构体初始化，若结构体没有完整赋值
																	//则最好执行此函数，给结构体所有成员都赋一个默认值
																	//避免结构体初值不确定的问题
	TIM_ICInitStructure.TIM_Channel = TIM_Channel_1;				//选择配置定时器通道1
	TIM_ICInitStructure.TIM_ICFilter = 0xF;							//输入滤波器参数，可以过滤信号抖动
	TIM_ICInit(TIM3, &TIM_ICInitStructure);							//将结构体变量交给TIM_ICInit，配置TIM3的输入捕获通道
	TIM_ICInitStructure.TIM_Channel = TIM_Channel_2;				//选择配置定时器通道2
	TIM_ICInitStructure.TIM_ICFilter = 0xF;							//输入滤波器参数，可以过滤信号抖动
	TIM_ICInit(TIM3, &TIM_ICInitStructure);							//将结构体变量交给TIM_ICInit，配置TIM3的输入捕获通道
	
	/*编码器接口配置*/
	TIM_EncoderInterfaceConfig(TIM3, TIM_EncoderMode_TI12, TIM_ICPolarity_Rising, TIM_ICPolarity_Rising);
																	//配置编码器模式以及两个输入通道是否反相
																	//注意此时参数的Rising和Falling已经不代表上升沿和下降沿了，而是代表是否反相
																	//此函数必须在输入捕获初始化之后进行，否则输入捕获的配置会覆盖此函数的部分配置
	
	/*TIM使能*/
	TIM_Cmd(TIM3, ENABLE);			//使能TIM3，定时器开始运行
}

/**
  * 函    数：获取编码器的增量值
  * 参    数：无
  * 返 回 值：自上此调用此函数后，编码器的增量值
  */
int16_t Encoder_Get(void)
{
	/*使用Temp变量作为中继，目的是返回CNT后将其清零*/
	int16_t Temp;
	Temp = TIM_GetCounter(TIM3);
	TIM_SetCounter(TIM3, 0);
	return Temp;
}

```

## ADC数模转换

​	ADC（Analog-Digital Converter）模拟-数字转换器。ADC可以将引脚上连续变化的模拟电压转换为内存中存储的数字变量，建立模拟电路到数字电路的桥梁。

​	**12位逐次逼近型ADC**，1us转换时间。输入电压范围：0~3.3V，转换结果范围：0~4095（2^12-1）。18个输入通道，可测量16个外部（GPIO口）和2个内部信号源（温度传感器cpu温度和内部参考电压1.2v的基准电压）。

​	规则组和注入组两个转换单元，一次性启动一个组，连续转换多个口，常规使用规则组和应对突发事件按的注入组。模拟看门狗自动监测输入电压范围，检测指定的某些通道，对超过或低于设定的阈值的模拟量进行中断操作。

​	STM32F103C8T6 ADC资源：ADC1、ADC2，10个外部输入通道。

![image-20240617090950962](D:\DeskTop\learn\STM 32\image\image-20240617090950962.png)

![image-20240617092239425](D:\DeskTop\learn\STM 32\image\image-20240617092239425.png)

### 转换模式

•单次转换，非扫描模式。一个通道每次都要触发，存在数据寄存器然后设置EOC标志位。

<img src="D:\DeskTop\learn\STM 32\image\image-20240617092653800.png" alt="image-20240617092653800" style="zoom:50%;" />

•连续转换，非扫描模式。一次触发之后连续一直转换。

<img src="D:\DeskTop\learn\STM 32\image\image-20240617092819489.png" alt="image-20240617092819489" style="zoom:50%;" />

•单次转换，扫描模式。对指定的通道进行转换，转换过程需要DMA不断把寄存器中的数值运走。

<img src="C:\Users\21998\AppData\Roaming\Typora\typora-user-images\image-20240617092929461.png" alt="image-20240617092929461" style="zoom:50%;" />

•连续转换，扫描模式

<img src="C:\Users\21998\AppData\Roaming\Typora\typora-user-images\image-20240617093139666.png" alt="image-20240617093139666" style="zoom:50%;" />

#### 数据对齐

<img src="C:\Users\21998\AppData\Roaming\Typora\typora-user-images\image-20240617093349298.png" alt="image-20240617093349298" style="zoom:50%;" />

#### 示例

1.RCC开启ADC1和GPIO

2.设置ADC时钟以及配置GPIO端口

3.选择通道并对ADC进行初始化

4.ADC使能并且校准

（使用单词转换非扫描的方式也可以实现多通道的ADC，把规则通道设置作为函数放入AD_GetValue中，在主函数中进行选择设置。）

```c
#include "stm32f10x.h"                  // Device header

/**
  * 函    数：AD初始化
  * 参    数：无
  * 返 回 值：无
  */
void AD_Init(void)
{
	/*开启时钟*/
	RCC_APB2PeriphClockCmd(RCC_APB2Periph_ADC1, ENABLE);	//开启ADC1的时钟
	RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOA, ENABLE);	//开启GPIOA的时钟
	
	/*设置ADC时钟*/
	RCC_ADCCLKConfig(RCC_PCLK2_Div6);						//选择时钟6分频，ADCCLK = 72MHz / 6 = 12MHz
	
	/*GPIO初始化*/
	GPIO_InitTypeDef GPIO_InitStructure;
	GPIO_InitStructure.GPIO_Mode = GPIO_Mode_AIN;
	GPIO_InitStructure.GPIO_Pin = GPIO_Pin_0;
	GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;
	GPIO_Init(GPIOA, &GPIO_InitStructure);					//将PA0引脚初始化为模拟输入
	
	/*规则组通道配置*/
	ADC_RegularChannelConfig(ADC1, ADC_Channel_0, 1, ADC_SampleTime_55Cycles5);		//规则组序列1的位置，配置为通道0
	
	/*ADC初始化*/
	ADC_InitTypeDef ADC_InitStructure;						//定义结构体变量
	ADC_InitStructure.ADC_Mode = ADC_Mode_Independent;		//模式，选择独立模式，即单独使用ADC1
	ADC_InitStructure.ADC_DataAlign = ADC_DataAlign_Right;	//数据对齐，选择右对齐
	ADC_InitStructure.ADC_ExternalTrigConv = ADC_ExternalTrigConv_None;	//外部触发，使用软件触发，不需要外部触发
	ADC_InitStructure.ADC_ContinuousConvMode = DISABLE;		//连续转换，失能，每转换一次规则组序列后停止
	ADC_InitStructure.ADC_ScanConvMode = DISABLE;			//扫描模式，失能，只转换规则组的序列1这一个位置
	ADC_InitStructure.ADC_NbrOfChannel = 1;					//通道数，为1，仅在扫描模式下，才需要指定大于1的数，在非扫描模式下，只能是1
	ADC_Init(ADC1, &ADC_InitStructure);						//将结构体变量交给ADC_Init，配置ADC1
	
	/*ADC使能*/
	ADC_Cmd(ADC1, ENABLE);									//使能ADC1，ADC开始运行
	
	/*ADC校准*/
	ADC_ResetCalibration(ADC1);								//固定流程，内部有电路会自动执行校准
	while (ADC_GetResetCalibrationStatus(ADC1) == SET);
	ADC_StartCalibration(ADC1);
	while (ADC_GetCalibrationStatus(ADC1) == SET);
}

/**
  * 函    数：获取AD转换的值
  * 参    数：无
  * 返 回 值：AD转换的值，范围：0~4095
  */
uint16_t AD_GetValue(void)
{
	ADC_SoftwareStartConvCmd(ADC1, ENABLE);					//软件触发AD转换一次
	while (ADC_GetFlagStatus(ADC1, ADC_FLAG_EOC) == RESET);	//等待EOC标志位，即等待AD转换结束
	return ADC_GetConversionValue(ADC1);					//读数据寄存器，得到AD转换的结果
}

```

### DMA（Direct Memory Access）直接存储器存取

​	数据转运小助手，DMA可以提供**外设（DAC、串口等）和存储器或者存储器（sram和flash等）和存储器之间的高速数据传输**，无须CPU干预，节省了CPU的资源。

​	12个独立可配置的通道： DMA1（7个通道）， DMA2（5个通道）。每个通道**都支持软件触发和特定的硬件触发**（是所有的软件触发和部分硬件触发）。STM32F103C8T6 DMA资源：DMA1（7个通道）。

#### 存储器地址

![image-20240617164445365](C:\Users\21998\AppData\Roaming\Typora\typora-user-images\image-20240617164445365.png)

#### DMA框图

1.总线矩阵左边为主动单元可以进行主动读写右边被动单元寄存器的内容。

2.ICode对接Flash接口，dcode和系统总线对接右边被动存储器，DMA即有主动也有被动。

3.DMA请求就是触发DMA，为硬件触发事件，入DAC、串口完成后通过DMA转运。

4.DMA内部仲裁器用于调度各个通道防止产生冲突。

5.如果通过总线直接访问flash只读不可写入，所以dma的目的地址不能是flash的存储区域（只能通过flash接口控制器写入）。

6.Sram可以自由读写但外设寄存器有些存在只读。

<img src="C:\Users\21998\AppData\Roaming\Typora\typora-user-images\image-20240617165241718.png" alt="image-20240617165241718" style="zoom:80%;" />

#### DMA基本结构图

​	如图，转运方向有三种，从外设到存储器，从存储器到存储器和从存储器到存储器（不能写入flash）；对转运双方需要设置起始地址和数据宽度以及地址是否自增；传输寄存器由ARR进行自动重装后自减计数，存储器转运对应的次数后，DMA自动回归初始位置，方便可开始新一轮转运；触发源有硬件和软件触发，

​	写传输计数器时必须先关闭DMA，再进行写操作。

**DMA工作要求传输计数器大于零，开启使能，存在触发源。**

![image-20240617170724930](D:\DeskTop\learn\STM 32\image\image-20240617170724930.png)

#### DMA请求

​	对应上图的下半部分，由M2M设置，1为软件触发，适用于存储器到存储器的转换，0为硬件触发，一般涉及外设；开关控制还是cmd函数。每个通道的硬件触发通道都不同，想使用某个信号就必须使用对应的通道，若使用软件触发就可以自由选择。

​	优先级选择就是仲裁器，设定通道的优先顺序后发送DMA请求。

​	若果是硬件请求要利用ADC_DMACmd（ADC1，ENABLE）来开启ADC1和DMA的配合工作（如图，ADC1和TIM2CH3TIM4CH1）

<img src="C:\Users\21998\AppData\Roaming\Typora\typora-user-images\image-20240617172142983.png" alt="image-20240617172142983" style="zoom:80%;" />

#### 数据宽度与对齐

符合右对齐，把小数据放到大数据里高位补零，反之舍弃高位

<img src="C:\Users\21998\AppData\Roaming\Typora\typora-user-images\image-20240617172849624.png" alt="image-20240617172849624" style="zoom:67%;" />

#### 一些实际转运示例

##### 数据转运+DMA

存储器到存储器

<img src="C:\Users\21998\AppData\Roaming\Typora\typora-user-images\image-20240617173143571.png" alt="image-20240617173143571" style="zoom:80%;" />

1.RCC开启时钟

2.DMA_Init初始化参数

3.开关控制DMA_Cmd

```c
#include "stm32f10x.h"                  // Device header
uint16_t MyDMA_Size;					//定义全局变量，用于记住Init函数的Size，供Transfer函数使用
/**
  * 函    数：DMA初始化
  * 参    数：AddrA 原数组的首地址
  * 参    数：AddrB 目的数组的首地址
  * 参    数：Size 转运的数据大小（转运次数）
  * 返 回 值：无
  */
void MyDMA_Init(uint32_t AddrA, uint32_t AddrB, uint16_t Size)
{
	MyDMA_Size = Size;					//将Size写入到全局变量，记住参数Size
	
	/*开启时钟*/
	RCC_AHBPeriphClockCmd(RCC_AHBPeriph_DMA1, ENABLE);						//开启DMA的时钟
	
	/*DMA初始化*/
	DMA_InitTypeDef DMA_InitStructure;										//定义结构体变量
	DMA_InitStructure.DMA_PeripheralBaseAddr = AddrA;						//外设基地址，给定形参AddrA
	DMA_InitStructure.DMA_PeripheralDataSize = DMA_PeripheralDataSize_Byte;	//外设数据宽度，选择字节
	DMA_InitStructure.DMA_PeripheralInc = DMA_PeripheralInc_Enable;			//外设地址自增，选择使能
	DMA_InitStructure.DMA_MemoryBaseAddr = AddrB;							//存储器基地址，给定形参AddrB
	DMA_InitStructure.DMA_MemoryDataSize = DMA_MemoryDataSize_Byte;			//存储器数据宽度，选择字节
	DMA_InitStructure.DMA_MemoryInc = DMA_MemoryInc_Enable;					//存储器地址自增，选择使能
	DMA_InitStructure.DMA_DIR = DMA_DIR_PeripheralSRC;						//数据传输方向，选择由外设到存储器
	DMA_InitStructure.DMA_BufferSize = Size;								//转运的数据大小（转运次数）
	DMA_InitStructure.DMA_Mode = DMA_Mode_Normal;							//模式，选择正常模式
	DMA_InitStructure.DMA_M2M = DMA_M2M_Enable;								//存储器到存储器，选择使能
	DMA_InitStructure.DMA_Priority = DMA_Priority_Medium;					//优先级，选择中等
	DMA_Init(DMA1_Channel1, &DMA_InitStructure);							//将结构体变量交给DMA_Init，配置DMA1的通道1
	
	/*DMA使能*/
	DMA_Cmd(DMA1_Channel1, DISABLE);	//这里先不给使能，初始化后不会立刻工作，等后续调用Transfer后，再开始
}

/**
  * 函    数：启动DMA数据转运
  * 参    数：无
  * 返 回 值：无
  */
void MyDMA_Transfer(void)
{
	DMA_Cmd(DMA1_Channel1, DISABLE);					//DMA失能，在写入传输计数器之前，需要DMA暂停工作
	DMA_SetCurrDataCounter(DMA1_Channel1, MyDMA_Size);	//写入传输计数器，指定将要转运的次数
	DMA_Cmd(DMA1_Channel1, ENABLE);						//DMA使能，开始工作
	
	while (DMA_GetFlagStatus(DMA1_FLAG_TC1) == RESET);	//等待DMA工作完成
	DMA_ClearFlag(DMA1_FLAG_TC1);						//清除工作完成标志位
}

```



##### ADC扫描模式+DMA

<img src="C:\Users\21998\AppData\Roaming\Typora\typora-user-images\image-20240617173215439.png" alt="image-20240617173215439" style="zoom:80%;" />

```c
#include "stm32f10x.h"                  // Device header

uint16_t AD_Value[4];					//定义用于存放AD转换结果的全局数组

/**
  * 函    数：AD初始化
  * 参    数：无
  * 返 回 值：无
  */
void AD_Init(void)
{
	/*开启时钟*/
	RCC_APB2PeriphClockCmd(RCC_APB2Periph_ADC1, ENABLE);	//开启ADC1的时钟
	RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOA, ENABLE);	//开启GPIOA的时钟
	RCC_AHBPeriphClockCmd(RCC_AHBPeriph_DMA1, ENABLE);		//开启DMA1的时钟
	
	/*设置ADC时钟*/
	RCC_ADCCLKConfig(RCC_PCLK2_Div6);						//选择时钟6分频，ADCCLK = 72MHz / 6 = 12MHz
	
	/*GPIO初始化*/
	GPIO_InitTypeDef GPIO_InitStructure;
	GPIO_InitStructure.GPIO_Mode = GPIO_Mode_AIN;
	GPIO_InitStructure.GPIO_Pin = GPIO_Pin_0 | GPIO_Pin_1 | GPIO_Pin_2 | GPIO_Pin_3;
	GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;
	GPIO_Init(GPIOA, &GPIO_InitStructure);					//将PA0、PA1、PA2和PA3引脚初始化为模拟输入
	
	/*规则组通道配置*/
	ADC_RegularChannelConfig(ADC1, ADC_Channel_0, 1, ADC_SampleTime_55Cycles5);	//规则组序列1的位置，配置为通道0
	ADC_RegularChannelConfig(ADC1, ADC_Channel_1, 2, ADC_SampleTime_55Cycles5);	//规则组序列2的位置，配置为通道1
	ADC_RegularChannelConfig(ADC1, ADC_Channel_2, 3, ADC_SampleTime_55Cycles5);	//规则组序列3的位置，配置为通道2
	ADC_RegularChannelConfig(ADC1, ADC_Channel_3, 4, ADC_SampleTime_55Cycles5);	//规则组序列4的位置，配置为通道3
	
	/*ADC初始化*/
	ADC_InitTypeDef ADC_InitStructure;											//定义结构体变量
	ADC_InitStructure.ADC_Mode = ADC_Mode_Independent;							//模式，选择独立模式，即单独使用ADC1
	ADC_InitStructure.ADC_DataAlign = ADC_DataAlign_Right;						//数据对齐，选择右对齐
	ADC_InitStructure.ADC_ExternalTrigConv = ADC_ExternalTrigConv_None;			//外部触发，使用软件触发，不需要外部触发
	ADC_InitStructure.ADC_ContinuousConvMode = ENABLE;							//连续转换，使能，每转换一次规则组序列后立刻开始下一次转换
	ADC_InitStructure.ADC_ScanConvMode = ENABLE;								//扫描模式，使能，扫描规则组的序列，扫描数量由ADC_NbrOfChannel确定
	ADC_InitStructure.ADC_NbrOfChannel = 4;										//通道数，为4，扫描规则组的前4个通道
	ADC_Init(ADC1, &ADC_InitStructure);											//将结构体变量交给ADC_Init，配置ADC1
	
	/*DMA初始化*/
	DMA_InitTypeDef DMA_InitStructure;											//定义结构体变量
	DMA_InitStructure.DMA_PeripheralBaseAddr = (uint32_t)&ADC1->DR;				//外设基地址，给定形参AddrA
	DMA_InitStructure.DMA_PeripheralDataSize = DMA_PeripheralDataSize_HalfWord;	//外设数据宽度，选择半字，对应16为的ADC数据寄存器
	DMA_InitStructure.DMA_PeripheralInc = DMA_PeripheralInc_Disable;			//外设地址自增，选择失能，始终以ADC数据寄存器为源
	DMA_InitStructure.DMA_MemoryBaseAddr = (uint32_t)AD_Value;					//存储器基地址，给定存放AD转换结果的全局数组AD_Value
	DMA_InitStructure.DMA_MemoryDataSize = DMA_MemoryDataSize_HalfWord;			//存储器数据宽度，选择半字，与源数据宽度对应
	DMA_InitStructure.DMA_MemoryInc = DMA_MemoryInc_Enable;						//存储器地址自增，选择使能，每次转运后，数组移到下一个位置
	DMA_InitStructure.DMA_DIR = DMA_DIR_PeripheralSRC;							//数据传输方向，选择由外设到存储器，ADC数据寄存器转到数组
	DMA_InitStructure.DMA_BufferSize = 4;										//转运的数据大小（转运次数），与ADC通道数一致
	DMA_InitStructure.DMA_Mode = DMA_Mode_Circular;								//模式，选择循环模式，与ADC的连续转换一致
	DMA_InitStructure.DMA_M2M = DMA_M2M_Disable;								//存储器到存储器，选择失能，数据由ADC外设触发转运到存储器
	DMA_InitStructure.DMA_Priority = DMA_Priority_Medium;						//优先级，选择中等
	DMA_Init(DMA1_Channel1, &DMA_InitStructure);								//将结构体变量交给DMA_Init，配置DMA1的通道1
	
	/*DMA和ADC使能*/
	DMA_Cmd(DMA1_Channel1, ENABLE);							//DMA1的通道1使能
	ADC_DMACmd(ADC1, ENABLE);								//ADC1触发DMA1的信号使能
	ADC_Cmd(ADC1, ENABLE);									//ADC1使能
	
	/*ADC校准*/
	ADC_ResetCalibration(ADC1);								//固定流程，内部有电路会自动执行校准
	while (ADC_GetResetCalibrationStatus(ADC1) == SET);
	ADC_StartCalibration(ADC1);
	while (ADC_GetCalibrationStatus(ADC1) == SET);
	
	/*ADC触发*/
	ADC_SoftwareStartConvCmd(ADC1, ENABLE);	//软件触发ADC开始工作，由于ADC处于连续转换模式，故触发一次后ADC就可以一直连续不断地工作
}
```

## 通信接口

| **名称** | **引脚**             | **双工** | **时钟** | **电平** | **设备** |
| -------- | -------------------- | -------- | -------- | -------- | -------- |
| USART    | TX、RX               | 全双工   | 异步     | 单端     | 点对点   |
| I2C      | SCL、SDA             | 半双工   | 同步     | 单端     | 多设备   |
| SPI      | SCLK、MOSI、MISO、CS | 全双工   | 同步     | 单端     | 多设备   |
| CAN      | CAN_H、CAN_L         | 半双工   | 异步     | 差分     | 多设备   |
| USB      | DP、DM               | 半双工   | 异步     | 差分     | 点对点   |

### USART  

<img src="D:\DeskTop\learn\STM 32\image\image-20240618110700484.png" alt="image-20240618110700484" style="zoom:67%;" />

•**波特率**：串口通信的速率

•**起始位**：标志一个数据帧的开始，固定为低电平

•**数据位**：数据帧的有效载荷，1为高电平，0为低电平，低位先行

•**校验位**：用于数据验证，根据数据位计算得来

•**停止位**：用于数据帧间隔，固定为高电平

<img src="C:\Users\21998\AppData\Roaming\Typora\typora-user-images\image-20240618111323705.png" alt="image-20240618111323705" style="zoom:67%;" />

<img src="C:\Users\21998\AppData\Roaming\Typora\typora-user-images\image-20240618111339656.png" alt="image-20240618111339656" style="zoom:67%;" />

​	**USART**（Universal Synchronous/Asynchronous Receiver/Transmitter）通用同步/异步收发器

​	USART是STM32内部集成的硬件外设，可根据数据寄存器的一个字节数据自动生成数据帧时序，从TX引脚发送出去，也可自动接收RX引脚的数据帧时序，拼接为一个字节数据，存放在数据寄存器里。自带波特率发生器，最高达**4.5Mbits**/s。可配置数据位长度（8/9）、停止位长度（0.5/1/1.5/2），可选校验位（**无校验**/奇校验/偶校验），支持同步模式、硬件流控制、DMA、智能卡、IrDA、LIN。

​	STM32F103C8T6 USART资源： **USART1、 USART2、 USART3**。

#### USART框图

​	TDR数据进入发送移位寄存器数据TXE数据置1，外部数据也立马进入TDR，发送移位寄存器在发送控制器的作用下，向右移位发送到TX引脚，低位先行，完成后新的数据自动从TDR转移到发送移位寄存器。

​	数据从RX引脚进入到接受移位寄存器，在接收控制器下读取RX电平，先放在最高位后右移，完成后整体转移到RDR中来，接受移位寄存器自动执行接受下一次数据，RXNE置1，执行数据读出操作。

​	SCLK时钟输出兼容其他协议。

​	唤醒单元实现多设备功能。

​	中断控制配置中断是不是能通向NVIC，TXE和RXNE判断发送状态和接受状态的必要标志位，波特率发生器产生发送器时钟和接收器时钟到发送控制器和接受控制器控制移位。

![image-20240618115021905](C:\Users\21998\AppData\Roaming\Typora\typora-user-images\image-20240618115021905.png)

#### USART基本结构

<img src="C:\Users\21998\AppData\Roaming\Typora\typora-user-images\image-20240618115144284.png" alt="image-20240618115144284" style="zoom:67%;" />

#### 配置停止位

<img src="C:\Users\21998\AppData\Roaming\Typora\typora-user-images\image-20240618174155214.png" alt="image-20240618174155214" style="zoom: 50%;" />



#### 起始位侦测

​	以波特率的16倍频率进行采样，出现第一个0检测到下降沿，接下来在起始位进行采样，在3、5、7，8、9、10进行采样，要求每三位里至少有两个0，两个0一个1的情况会在状态寄存器置一个NE噪声标志位，若三位里只有一个1则不算检测到起始位忽略前面的数据重新捕捉下降沿。

​	通过后就由空闲进入到起始位，8、9、10次采样则算是数据中央，此后采样一直在此保证采样位置在正中央。

<img src="C:\Users\21998\AppData\Roaming\Typora\typora-user-images\image-20240618175121761.png" alt="image-20240618175121761" style="zoom: 50%;" />

#### 数据采样

​	由于起始位侦测中已经对齐数据所以直接采用8、9、10位进行数据采样，连续采样三次，全1全0则采样正确，或者两次1一次0两次0一次1也可以但是也会置位NE。

<img src="C:\Users\21998\AppData\Roaming\Typora\typora-user-images\image-20240618180524416.png" alt="image-20240618180524416" style="zoom:50%;" />

#### 波特率发生器

1.发送器和接收器的波特率由波特率寄存器BRR里的DIV确定

2.计算公式：波特率 = fPCLK2/1 / (16 * DIV)

<img src="C:\Users\21998\AppData\Roaming\Typora\typora-user-images\image-20240618181556434.png" alt="image-20240618181556434" style="zoom:50%;" />

​	DIV分为整数部分和小数部分可以实现更细腻的分频。如设置9600波特率，9600=72M/（10*DIV）--DIV=468.75---转换二进制得111010100.11，所以BRR写入此数（库函数自动实现）。

#### 串口发送接受示例

HEX**数据包**

<img src="D:\DeskTop\learn\STM 32\image\image-20240619092140601.png" alt="image-20240619092140601" style="zoom:67%;" />

<img src="C:\Users\21998\AppData\Roaming\Typora\typora-user-images\image-20240619094417174.png" alt="image-20240619094417174" style="zoom:67%;" />

**文本数据包**

<img src="D:\DeskTop\learn\STM 32\image\image-20240619093052309.png" alt="image-20240619093052309" style="zoom:67%;" />



```c
#include "stm32f10x.h"                  // Device header
#include <stdio.h>
#include <stdarg.h>

uint8_t Serial_RxData;		//定义串口接收的数据变量
uint8_t Serial_RxFlag;		//定义串口接收的标志位变量

/**
  * 函    数：串口初始化
  * 参    数：无
  * 返 回 值：无
  */
void Serial_Init(void)
{
	/*开启时钟*/
	RCC_APB2PeriphClockCmd(RCC_APB2Periph_USART1, ENABLE);	//开启USART1的时钟
	RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOA, ENABLE);	//开启GPIOA的时钟
	
	/*GPIO初始化*/
	GPIO_InitTypeDef GPIO_InitStructure;
	GPIO_InitStructure.GPIO_Mode = GPIO_Mode_AF_PP;
	GPIO_InitStructure.GPIO_Pin = GPIO_Pin_9;
	GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;
	GPIO_Init(GPIOA, &GPIO_InitStructure);					//将PA9引脚初始化为复用推挽输出
	
	GPIO_InitStructure.GPIO_Mode = GPIO_Mode_IPU;
	GPIO_InitStructure.GPIO_Pin = GPIO_Pin_10;
	GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;
	GPIO_Init(GPIOA, &GPIO_InitStructure);					//将PA10引脚初始化为上拉输入
	
	/*USART初始化*/
	USART_InitTypeDef USART_InitStructure;					//定义结构体变量
	USART_InitStructure.USART_BaudRate = 9600;				//波特率
	USART_InitStructure.USART_HardwareFlowControl = USART_HardwareFlowControl_None;	//硬件流控制，不需要
	USART_InitStructure.USART_Mode = USART_Mode_Tx | USART_Mode_Rx;	//模式，发送模式和接收模式均选择
	USART_InitStructure.USART_Parity = USART_Parity_No;		//奇偶校验，不需要
	USART_InitStructure.USART_StopBits = USART_StopBits_1;	//停止位，选择1位
	USART_InitStructure.USART_WordLength = USART_WordLength_8b;		//字长，选择8位
	USART_Init(USART1, &USART_InitStructure);				//将结构体变量交给USART_Init，配置USART1
	
	/*中断输出配置*/
	USART_ITConfig(USART1, USART_IT_RXNE, ENABLE);			//开启串口接收数据的中断
	
	/*NVIC中断分组*/
	NVIC_PriorityGroupConfig(NVIC_PriorityGroup_2);			//配置NVIC为分组2
	
	/*NVIC配置*/
	NVIC_InitTypeDef NVIC_InitStructure;					//定义结构体变量
	NVIC_InitStructure.NVIC_IRQChannel = USART1_IRQn;		//选择配置NVIC的USART1线
	NVIC_InitStructure.NVIC_IRQChannelCmd = ENABLE;			//指定NVIC线路使能
	NVIC_InitStructure.NVIC_IRQChannelPreemptionPriority = 1;		//指定NVIC线路的抢占优先级为1
	NVIC_InitStructure.NVIC_IRQChannelSubPriority = 1;		//指定NVIC线路的响应优先级为1
	NVIC_Init(&NVIC_InitStructure);							//将结构体变量交给NVIC_Init，配置NVIC外设
	
	/*USART使能*/
	USART_Cmd(USART1, ENABLE);								//使能USART1，串口开始运行
}

/**
  * 函    数：串口发送一个字节
  * 参    数：Byte 要发送的一个字节
  * 返 回 值：无
  */
void Serial_SendByte(uint8_t Byte)
{
	USART_SendData(USART1, Byte);		//将字节数据写入数据寄存器，写入后USART自动生成时序波形
	while (USART_GetFlagStatus(USART1, USART_FLAG_TXE) == RESET);	//等待发送完成
	/*下次写入数据寄存器会自动清除发送完成标志位，故此循环后，无需清除标志位*/
}

/**
  * 函    数：串口发送一个数组
  * 参    数：Array 要发送数组的首地址
  * 参    数：Length 要发送数组的长度
  * 返 回 值：无
  */
void Serial_SendArray(uint8_t *Array, uint16_t Length)
{
	uint16_t i;
	for (i = 0; i < Length; i ++)		//遍历数组
	{
		Serial_SendByte(Array[i]);		//依次调用Serial_SendByte发送每个字节数据
	}
}

/**
  * 函    数：串口发送一个字符串
  * 参    数：String 要发送字符串的首地址
  * 返 回 值：无
  */
void Serial_SendString(char *String)
{
	uint8_t i;
	for (i = 0; String[i] != '\0'; i ++)//遍历字符数组（字符串），遇到字符串结束标志位后停止
	{
		Serial_SendByte(String[i]);		//依次调用Serial_SendByte发送每个字节数据
	}
}

/**
  * 函    数：次方函数（内部使用）
  * 返 回 值：返回值等于X的Y次方
  */
uint32_t Serial_Pow(uint32_t X, uint32_t Y)
{
	uint32_t Result = 1;	//设置结果初值为1
	while (Y --)			//执行Y次
	{
		Result *= X;		//将X累乘到结果
	}
	return Result;
}

/**
  * 函    数：串口发送数字
  * 参    数：Number 要发送的数字，范围：0~4294967295
  * 参    数：Length 要发送数字的长度，范围：0~10
  * 返 回 值：无
  */
void Serial_SendNumber(uint32_t Number, uint8_t Length)
{
	uint8_t i;
	for (i = 0; i < Length; i ++)		//根据数字长度遍历数字的每一位
	{
		Serial_SendByte(Number / Serial_Pow(10, Length - i - 1) % 10 + '0');	//依次调用Serial_SendByte发送每位数字
	}
}

/**
  * 函    数：使用printf需要重定向的底层函数
  * 参    数：保持原始格式即可，无需变动
  * 返 回 值：保持原始格式即可，无需变动
  */
int fputc(int ch, FILE *f)
{
	Serial_SendByte(ch);			//将printf的底层重定向到自己的发送字节函数
	return ch;
}

/**
  * 函    数：自己封装的prinf函数
  * 参    数：format 格式化字符串
  * 参    数：... 可变的参数列表
  * 返 回 值：无
  */
void Serial_Printf(char *format, ...)
{
	char String[100];				//定义字符数组
	va_list arg;					//定义可变参数列表数据类型的变量arg
	va_start(arg, format);			//从format开始，接收参数列表到arg变量
	vsprintf(String, format, arg);	//使用vsprintf打印格式化字符串和参数列表到字符数组中
	va_end(arg);					//结束变量arg
	Serial_SendString(String);		//串口发送字符数组（字符串）
}

/**
  * 函    数：获取串口接收标志位
  * 参    数：无
  * 返 回 值：串口接收标志位，范围：0~1，接收到数据后，标志位置1，读取后标志位自动清零
  */
uint8_t Serial_GetRxFlag(void)
{
	if (Serial_RxFlag == 1)			//如果标志位为1
	{
		Serial_RxFlag = 0;
		return 1;					//则返回1，并自动清零标志位
	}
	return 0;						//如果标志位为0，则返回0
}

/**
  * 函    数：获取串口接收的数据
  * 参    数：无
  * 返 回 值：接收的数据，范围：0~255
  */
uint8_t Serial_GetRxData(void)
{
	return Serial_RxData;			//返回接收的数据变量
}

/**
  * 函    数：USART1中断函数
  * 参    数：无
  * 返 回 值：无
  * 注意事项：此函数为中断函数，无需调用，中断触发后自动执行
  *           函数名为预留的指定名称，可以从启动文件复制
  *           请确保函数名正确，不能有任何差异，否则中断函数将不能进入
  */
void USART1_IRQHandler(void)
{
	if (USART_GetITStatus(USART1, USART_IT_RXNE) == SET)		//判断是否是USART1的接收事件触发的中断
	{
		Serial_RxData = USART_ReceiveData(USART1);				//读取数据寄存器，存放在接收的数据变量
		Serial_RxFlag = 1;										//置接收标志位变量为1
		USART_ClearITPendingBit(USART1, USART_IT_RXNE);			//清除USART1的RXNE标志位
																//读取数据寄存器会自动清除此标志位
																//如果已经读取了数据寄存器，也可以不执行此代码
	}
}

```

#### 串口收发HEX数据包



```c

/**
  * 函    数：USART1中断函数
  * 参    数：无
  * 返 回 值：无
  * 注意事项：此函数为中断函数，无需调用，中断触发后自动执行
  *           函数名为预留的指定名称，可以从启动文件复制
  *           请确保函数名正确，不能有任何差异，否则中断函数将不能进入
  */
void USART1_IRQHandler(void)
{
	static uint8_t RxState = 0;		//定义表示当前状态机状态的静态变量
	static uint8_t pRxPacket = 0;	//定义表示当前接收数据位置的静态变量
	if (USART_GetITStatus(USART1, USART_IT_RXNE) == SET)		//判断是否是USART1的接收事件触发的中断
	{
		uint8_t RxData = USART_ReceiveData(USART1);				//读取数据寄存器，存放在接收的数据变量
		
		/*使用状态机的思路，依次处理数据包的不同部分*/
		
		/*当前状态为0，接收数据包包头*/
		if (RxState == 0)
		{
			if (RxData == 0xFF)			//如果数据确实是包头
			{
				RxState = 1;			//置下一个状态
				pRxPacket = 0;			//数据包的位置归零
			}
		}
		/*当前状态为1，接收数据包数据*/
		else if (RxState == 1)
		{
			Serial_RxPacket[pRxPacket] = RxData;	//将数据存入数据包数组的指定位置
			pRxPacket ++;				//数据包的位置自增
			if (pRxPacket >= 4)			//如果收够4个数据
			{
				RxState = 2;			//置下一个状态
			}
		}
		/*当前状态为2，接收数据包包尾*/
		else if (RxState == 2)
		{
			if (RxData == 0xFE)			//如果数据确实是包尾部
			{
				RxState = 0;			//状态归0
				Serial_RxFlag = 1;		//接收数据包标志位置1，成功接收一个数据包
			}
		}
		
		USART_ClearITPendingBit(USART1, USART_IT_RXNE);		//清除标志位
	}
}

```

### I2C通信

inter IC BUS--SCL serial clock 串行时钟线 --SDA serial data 串行数据线

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

<img src="C:\Users\21998\AppData\Roaming\Typora\typora-user-images\image-20240619113438253.png" alt="image-20240619113438253" style="zoom:67%;" />

​	若想写入多个字节，重复多次写入数据的过程，地址值自动加一。

**接收一帧数据**：向谁收什么

![image-20240415114216536](D:\DeskTop\learn\51\image\image-20240415114216536.png)

<img src="C:\Users\21998\AppData\Roaming\Typora\typora-user-images\image-20240619114902792.png" alt="image-20240619114902792" style="zoom:67%;" />

**先发送再接收数据帧**（复合格式）：向谁收指定的什么

![image-20240415114250112](D:\DeskTop\learn\51\image\image-20240415114250112.png)

**字节写**：在WORD ADDRESS处写入数据DATA

![image-20240415114320462](D:\DeskTop\learn\51\image\image-20240415114320462.png)

**随机读**：读出在WORD ADDRESS处的数据DATA

![image-20240415114358647](D:\DeskTop\learn\51\image\image-20240415114358647.png)

![image-20240619115913893](C:\Users\21998\AppData\Roaming\Typora\typora-user-images\image-20240619115913893.png)

​	指定地址寻址为1101000，读写标志位0代表写入，接受应答后，再发送一个字节表示地址，写入从机的地址指针里，寄存器指针指向0x19，Sr重复一个起始条件，重新寻址找到地址，读写标志位为1，开始读数据。也可以再两个读写过程之间加入终止，以上过程变成了两条时序。多次执行最后一部分多次执行为连续读出一片寄存器，只需要再最后一个读取数据后选择非应答前面的数据都要应答。

#### MPU6050

​	MPU6050是一个6轴姿态传感器，可以测量芯片自身X、Y、Z轴的加速度、角速度参数，通过数据融合，可进一步得到姿态角，常应用于平衡车、飞行器等需要检测自身姿态的场景。3轴加速度计（Accelerometer）：测量X、Y、Z轴的加速度，3轴陀螺仪传感器（Gyroscope）：测量X、Y、Z轴的角速度。

​	陀螺仪具有动态稳定性，不具有静态稳定性；加速度计是静态稳定和动态不稳定；对两个进行互补滤波得到基本稳定的姿态角。

​	**16位ADC**采集传感器的模拟信号，量化范围：-32768~32767，加速度计满量程选择：±2、±4、±8、±16（g），陀螺仪满量程选择： ±250、±500、±1000、±2000（°/sec角速度的单位每秒旋转了多少度），可配置的数字低通滤波器，可配置的时钟源，可配置的采样分频。

​	I2C从机地址：1101000 （AD0=0） 1101001 （AD0=1）

#### I2C外设简介

​	STM32内部集成了硬件I2C收发电路，可以由硬件自动执行时钟生成、起始终止条件生成、应答位收发、数据收发等功能，减轻CPU的负担，支持多主机模型，支持7位/10位地址模式，支持不同的通讯速度，标准速度(高达100 kHz)，快速(高达400 kHz)。支持DMA，兼容SMBus协议。

​	STM32F103C8T6 硬件I2C资源：I2C1、I2C2。

#### I2C框图

<img src="C:\Users\21998\AppData\Roaming\Typora\typora-user-images\image-20240622190054933.png" alt="image-20240622190054933" style="zoom:50%;" />

<img src="C:\Users\21998\AppData\Roaming\Typora\typora-user-images\image-20240622190945769.png" alt="image-20240622190945769" style="zoom:50%;" />

​	移位寄存器和数据寄存器DR相互配合，I2C高位先行，移位寄存器向左移位。发送时最高位先出，一个SCL时钟移位一次，移位八次，由高位到低位依次放到SDA线上。接受时数据通过GPIO从右边依次移位进来。硬件都要配置成复用开漏输出模式，GPIO状态交由片上外设来控制。

### SPI通信

​	SPI（Serial Peripheral Interface）是由Motorola公司开发的一种通用数据总线。四根通信线：SCK（Serial Clock）、MOSI（Master Output Slave Input）主机输出从机输入、MISO（Master Input Slave Output）主机输入从机输出、SS（Slave Select）从机选择。**同步，全双工**，支持总线挂载多设备（一主多从）。

​	所有SPI设备的SCK、MOSI、MISO分别连在一起，主机另外引出多条SS控制线，分别接到各从机的SS引脚，输出引脚配置为**推挽输出**，输入**引脚配置为浮空或上拉输入**。MISO引脚当未被选中的从机SS保持高电平期间，MISO一直为高阻态避免了冲突，当SS为低电平时才允许MISO为推挽输出。

<img src="C:\Users\21998\AppData\Roaming\Typora\typora-user-images\image-20240622200132242.png" alt="image-20240622200132242" style="zoom:50%;" />

​	上升沿集体左移，主机输出从机输出，下降沿采样输入，主机输入，从机输入。8个时钟后，完成主机和从机的数据交换。所有的数据交换都基于上述过程，对与单项收发也是上述过程，只不过有一方会忽略另一方的数据。

<img src="C:\Users\21998\AppData\Roaming\Typora\typora-user-images\image-20240622201516451.png" alt="image-20240622201516451" style="zoom:50%;" />

#### **基本时序单元**

​	1.起始条件：SS从高电平切换到低电平；终止条件：SS从低电平切换到高电平。

<img src="C:\Users\21998\AppData\Roaming\Typora\typora-user-images\image-20240622202259182.png" alt="image-20240622202259182" style="zoom:50%;" />



​	2.交换一个字节（模式1）

CPOL=0：空闲状态时，SCK为低电平

CPHA=1：SCK第一个边沿移出数据，第二个边沿移入数据

<img src="C:\Users\21998\AppData\Roaming\Typora\typora-user-images\image-20240626182646348.png" alt="image-20240626182646348" style="zoom:50%;" />

​	**3.交换一个字节（模式0）**常用

CPOL=0：空闲状态时，SCK为低电平

CPHA=0：SCK第一个边沿移入数据，第二个边沿移出数据

<img src="C:\Users\21998\AppData\Roaming\Typora\typora-user-images\image-20240626183356466.png" alt="image-20240626183356466" style="zoom:50%;" />

​	4.发送指令

向SS指定的设备，发送指令（0x06）

<img src="C:\Users\21998\AppData\Roaming\Typora\typora-user-images\image-20240626183801866.png" alt="image-20240626183801866" style="zoom:50%;" />

​	5.指定地址写

向SS指定的设备，发送写指令（0x02），随后在指定地址（Address[23:0]）下，写入指定数据（Data）

![image-20240626190140797](C:\Users\21998\AppData\Roaming\Typora\typora-user-images\image-20240626190140797.png)

​	6.指定地址读

向SS指定的设备，发送读指令（0x03），随后在指定地址（Address[23:0]）下，读取从机数据（Data）                       

![image-20240626190318177](C:\Users\21998\AppData\Roaming\Typora\typora-user-images\image-20240626190318177.png)

​	7.写入操作时：

•写入操作前，必须先进行写使能

•每个数据位只能由1改写为0，不能由0改写为1

•写入数据前必须先擦除，擦除后，所有数据位变为1

•擦除必须按最小擦除单元进行

•连续写入多字节时，最多写入一页的数据，超过页尾位置的数据，会回到页首覆盖写入

•写入操作结束后，芯片进入忙状态，不响应新的读写操作

​	8.读取操作时：

•直接调用读取时序，无需使能，无需额外操作，没有页的限制，读取操作结束后不会进入忙状态，但不能在忙状态时读取

## RTC

### Unix时间戳

​	Unix 时间戳（Unix Timestamp）定义为从UTC/GMT的1970年1月1日0时0分0秒开始所经过的秒数，不考虑闰秒。时间戳存储在一个秒计数器中，秒计数器为32位/64位的整型变量。世界上所有时区的秒计数器相同，不同时区通过添加偏移来得到当地时间。

<img src="C:\Users\21998\AppData\Roaming\Typora\typora-user-images\image-20240627155112090.png" alt="image-20240627155112090" style="zoom:80%;" />

|                           **函数**                           |                **作用**                |
| :----------------------------------------------------------: | :------------------------------------: |
|                    time_t time(time_t*);                     |              获取系统时钟              |
|              struct tm* gmtime(const  time_t*);              | 秒计数器转换为日期时间（格林尼治时间） |
|            struct tm* localtime(const  time_t*);             |   秒计数器转换为日期时间（当地时间）   |
|                 time_t mktime(struct  tm*);                  |   日期时间转换为秒计数器（当地时间）   |
|                 char* ctime(const  time_t*);                 |    秒计数器转换为字符串（默认格式）    |
|               char* asctime(const struct tm*);               |    日期时间转换为字符串（默认格式）    |
| size_t strftime(char*, size_t, const  char*, const struct tm*); |   日期时间转换为字符串（自定义格式）   |

<img src="C:\Users\21998\AppData\Roaming\Typora\typora-user-images\image-20240627171947660.png" alt="image-20240627171947660" style="zoom:80%;" />

### BKP简介

​	BKP（Backup Registers）备份寄存器

BKP可用于存储用户应用程序数据。当VDD（2.0~3.6V）电源被切断，他们仍然由VBAT（1.8~3.6V）维持供电。当系统在待机模式下被唤醒，或系统复位或电源复位时，他们也不会被复位。TAMPER引脚产生的侵入事件将所有备份寄存器内容清除

•RTC引脚输出RTC校准时钟、RTC闹钟脉冲或者秒脉冲

•存储RTC时钟校准寄存器

•用户数据存储容量：

 20字节（中容量和小容量）/ 84字节（大容量和互联型）

<img src="C:\Users\21998\AppData\Roaming\Typora\typora-user-images\image-20240627172100694.png" alt="image-20240627172100694" style="zoom:50%;" />

### RTC

•RTC（Real Time Clock）实时时钟

•RTC是一个独立的定时器，可为系统提供时钟和日历的功能

•RTC和时钟配置系统处于后备区域，系统复位时数据不清零，VDD（2.0~3.6V）断电后可借助VBAT（1.8~3.6V）供电继续走时

•32位的可编程计数器，可对应Unix时间戳的秒计数器 ，20位的可编程预分频器，可适配不同频率的输入时钟。

•可选择三种RTC时钟源：

 1.HSE时钟除以128（通常为8MHz/128）

 2.LSE振荡器时钟（通常为32.768KHz）

 3.LSI振荡器时钟（40KHz）

<img src="C:\Users\21998\AppData\Roaming\Typora\typora-user-images\image-20240627172631936.png" alt="image-20240627172631936" style="zoom:67%;" />

