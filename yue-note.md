# 2023

## 11

### 11-25 

##### 1.学习linux裸机开发：RTC与i2c

##### 2.在macos windows上的clion 和cubeIDE workspace全体将例程源码中openocd的stlinkf1x添加国产mcu选项（在openocd原路径中）。

​	方法：找到openocd安装目录，在target/下找到stlinkf1x.cfg，修改0x1Bxxx为0x2Bxx

##### 3.在macos windows上的clion 和cubeIDE workspace全体将8266IOT升级为ver2.0版本

##### （带PWM控制灯亮度）。

​	3.1macOS移植win较为困难，步骤如下：
​			3.1.1工程目录有许多macos生成的"._"开头的文件，需要将其一一删除。将Cmakelist的编译器路径替换，进入clion设置debug为捆绑的GDB
​			3.1.2win移植macos简单，只需要将工程文件拷贝，将原项目的Cmakelist替换即可（原因是arm-none-eabi-gcc路径不一）
​					（还需注意IncludePATH和File的路径是否正确，一般不会改变）

所以：<u>建议以后移植工程统一在windows端进行，之后再替换CmakeList，移植到macOS即可！！</u>	

##### 4.将用户的江科大学习例程（截至到RTC）从macOS移植到win的Clion

##### 5.初步学习了Source Insight的用法，初步学习了CubeMX生成Makefile，并且编译的方法

Makefile中文件路径和包含路径需要自己设置到User/目录下，并且不能混合，必须分为Inc和Src两个文件夹！！
macOS和Win，工程文件的同步安排：主要在Windows，次要在macOS，macOS尽量只用来读文档和查资料

##### 6.验证了ASRPRO的功能，初步完成语音控制WS2812灯的颜色

### 11-26

##### 1.使用模拟开关方案实现自由切换双端控制

##### 2.好用的还是SU03-T和ASRPRO，Hilink的V20直接PASS

##### 3.CAD模拟开关切换方案验证通过，器件选型完毕

|     材料     |      选型      | 数量 |   备注   |
| :----------: | :------------: | :--: | :------: |
|     MCU      |     AIR001     |  1   |   在库   |
|   语音模块   |     ASRPRO     |  1   | 再买两个 |
|  充放电管理  | ETA9740/IP5306 |  1   |  待选型  |
| 电源控制管理 |    SAM8108     |  1   |          |
|     灯珠     |     WS2812     |  32  |          |
|    锂电池    | 505060-2000mAh |  1   |          |

### 11.27

##### 1.选型完毕

##### 2.绘制了PCB，但未连线



### 11.28

##### 1.PCB绘制完毕，已发打样+正面SMT（沉金券捆绑）



### 11.29

##### 1.研究了STC-ISP搭配STC自动下载器实现自动下载STC单片机的方法

需要在”收到用户命令后复位到ISP监控程序区“中，选择为USB-CDC串口模式，并√上使用默认的内部自定义命令""@STCISP"，可以使用下方的“发送用户自定义命令开始下载”



### 11.30

##### 1.尝试了MSP430 FFT显示频谱的例程，使用了DSP库

## 12

### 12.1

##### 1.疯狂看MyGO，真TM好看！

##### 2.使用SU-03T，将AI高松灯生成的语音通过自定义语音导入，实现了小灯小灯（迫真）

HuggingFace老崩，建议使用翻译效果较好的ChatGPT翻译为日语，再以段落为形式导入AI语音生成界面中（但事后需要自己切片）
网络通畅的情况下可以直接以短句生成。最后命上与内容符合的标题，导入智能公元“自定义语音”界面下，再将原有语音一一对应起来。
使用自定义语音（默认音量）会出现喇叭破音/失真等现象，需要添加增大音量/减小音量命令（改变系统设置），上电手（嘴）动调小音量（或许还有其他自动调整音量方法待探索）。



### 12.2

##### 1.结束Linux裸机开发，进入uboot移植阶段

坑：ping不通，需要在VMWare中设置网络为桥接模式
		nfs下载文件出错:https://blog.csdn.net/qq_41709234/article/details/123160029

改完之后上不了网：改回NAT模式，IPv4的Automatic全部打开
tftp下载：Server IP -> setenv serverip 192.168.1.66

##### 2.学习了春日影

这首歌的编曲真的很棒，Verse1/2的断句都不一样，果然Elements Garden都是一帮了不起的人。

### 12.3

##### 1.PCB到货了，但是元件买晚了，下次采购元件不要犹豫太久

初步测试通过，Flash保存需要3秒左右的时间，不要太快，会导致写入数组不完全。

##### 2.今天休息日，一直在看MyGO二创和BanG Dream!相关音乐，巩固了春日影，学了一下迷星叫，这首节奏比较快。

##### 3.找到了一个使用结构体实现的spi OLED-STM32菜单开源项目

挺复杂的，希望有朝一日能弄明白（OSP_32/oled多级菜单-高级实现方法-C8T6）

### 12.4

##### 1.焊接PCB完毕

SAM8108官方手册给的PMOS扩流驱动电路存在错误，PMOS电流方向是源极流向漏极，电源电压通过体二极管给下游设备供电，瞬间击穿体二极管

##### 2.修好七星虫M3S开发板

ZET6封装有很多的“第一脚位零点”，焊接一定不能弄反了！！！

### 12.5

##### 1.更改ASRPRO-WS2812方案，使用建立线程方法实现循环闪灯。

##### 2.将胡鑫代码导入CCS方法：

① 复制工程文件夹到

```
F:\Folder\EE\Texas Instruments\User_Project_Ti\CCS Workspace //工作区
```

② 在ccs中打开文件夹，添加如Project Explorer

③ 在Project下进入Properties -> Build -> ARM Complier -> Include Options加入

```
D:\Ti-CCS\tivaware_c_series_2_1_4_178 //Tiva-Lib的目录
```

Properties -> Build->ARM Complier -> File search Path 也是如此

④ lib文件选择：

```
D:\Ti-CCS\tivaware_c_series_2_1_4_178\driverlib\ccs\Debug\driverlib.lib
```

### 12.6

##### 1.更换STM32芯片的方法（ZE/C6/C8互换）

① 在Start\下，更改startup_stm32f10x_xd.s为对应的（C6->ld C8->md ZE->hd)
② 在Keil中更换芯片型号为对应，否则可以编译无法下载
③ 在C/C++ \Define:中，添加", STM32F10X_xD"

##### 2.GB2312工程更改为UTF-8方法

① 将dir\下所有文件转化为UTF-8格式（使用批量转换软件）
② 在Keil的魔术棒下，Misc Control中添加"--no-multibyte-chars"
③ 若使用串口调试，需要在串口助手中同时选择编码格式为UTF-8

### 12.7

##### 1.研究了commonKey的检测实现方法，设计链表操作与结构体

①<img src="F:\文件\QQ\qqdata\Tencent Files\1528713506\nt_qq\nt_data\Pic\2023-12\Ori\35c5f65e1e2bc9c6302dad245e2abad0.png" alt="35c5f65e1e2bc9c6302dad245e2abad0" style="zoom:40%;" />

图中第27行处，为位域操作。所谓“位域”是把一个字节中的二进位划分为几 个不同的区域，并说明每个区域的位数。每个域有一个域名，允许在程序中按域名进行操作。这样就可以把几个不同的对象用一个字节的二进制位域来表示。

注册按键句柄使用与STM32GPIO_Init同样的方法，在初始化函数中对每个按键定义的初始化句柄取地址（&）

##### 2.新颖表达式

```
loop_count = CPUFREQ == CLK_12M ? 177 : CPUFREQ == CLK_24M ? 353 : CPUFREQ == CLK_16M ? 299 : 201 ;
```

##### 3.查阅了南京邮电大学科协的Gitee，下载了资料（EE\Resourse\南京邮电大学Git）

① Birch开发板，内含U8g2移植STM32例程
② OpenCV萌新入门（以后再看）
③ 控制ADxxxx产生低频信号的例程（在信号发生器资料内）

### 12.8

##### 1.移植了STC15W204S的OLED和printf

① **data**表示单片机内部RAM所使用的空间大小，为52字节（15W204S SRAM为256字节）。**xdata**表示单片机片外RAM所使用的空间大小（15W204S无片外RAM），为0字节。RAM用于存放变量；**code**表示程序文件的大小，为1411字节，差不多1.5KB，占用的是单片机flash的空间（15W204S 	        FLASH为4KB）。**const**则是存在在ROM中的变量（在本工程中包括OLED字库和BMP图像）

![image-20231208171243342](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\image-20231208171243342.png)

​																				**data** —> 　  可寻址片内RAM
​																				**bdata** —> 	可位寻址的片内RAM
​																				**idata** —> 　 可寻址片内RAM，允许访问全部内部RAM
​																				**pdata** —> 	分页寻址片外RAM(MOVX @R0) (256 BYTE/页) 
​																				**xdata** —> 	可寻址片外RAM(64k 地址范围FFFFH) 
​																				**code** —> 程序存储区ROM (64k 地址范围),对应MOVC @DPTR


② 变量过多，超过idata和xdata的大小，那么编译时，不会报错，但是程序运行会崩溃，可能只有部分代码在运行，即不会完整运行全部程序！！！
STC15W204S 前128KB SRAM可以直接访问，后128KBRAM需要在变量前声明idata才可以访问，否则会报OVERFLOW错误

例如： STC15W408AS片内集成512字节的SRAM，包括常规的256字节RAM (idata) 和内部扩展的256字节 XRAM (xdata)，有8K的FLASH。如果data或者xdata的编译结果大于256，那么程序就会崩溃，不能完整运行，但此时，如果其中一个RAM没有用满，那么可以在变量声明前添加idata或者xdata，将变量移至另外一个RAM，使得RAM都没有用满，则程序会正常运行。实际上，应该避免用满RAM，应该留出20~30字节的部分空间，避免在运行复杂程序时崩溃，而简单程序运行时可能正常。

③ **Keil中Memory Model和Code Rom Size说明**

C51中定义变量时如果省略存储器类型，Keil C51编译系统则会按编译模式SMALL、COMPACT和LARGE所规定的默认存储器类型去指定变量的存储区域，无论什么存储模式都可以声明变量在任何的8051存储区范围i，但是把最常用的命令如循环计数器和队列索引放在内部数据区可以显著地提高系统性能。以下介绍一下Keil编译选项Target中的Memory Model和Code Rom Size的设置。

1、**SMALL模式**

SMALL模式：在本模式中所有的变量在缺省的情况下位于8051系统的内部数据区（这和用data存储类型标识符明确声明的一样，因此对这种变量的访问数据最快），在本模式中，变量访问非常有效，然而所有的东西包括堆栈必须放在内部RAM中，堆栈大小是不确定的，它取决于函数嵌套的深度。典型的，如果连接/定位器配置为内部数据区变量可覆盖，**SMALL模式是最好的模式**，但是SMALL模式的地址空间受限，在写小型的应用程序时，变量和数据放在Data内部数据存储器中是很好的，因为访问速度快，但在较大的程序中Data区最好只存放小的变量、数据或常用的变量（如循环计数、数据索引），而大的数据则放在别的存储区域，否则Data区就容易溢出。

2、**COMPACT模式**

COMPACT模式：把变量都定位在MCS-51系统的外部数据存储器中，外部数据存储段可有最多256字节（一页 ），这是对变量的访问是通过寄存器间接寻址（MOVX @Ri）进行的。采用这种编译模式时，变量的高8位地址由P2口确定，因此，在采用这种模式的同时，必须适当改变启动程序STARTUP.A51中的参数PDATASTART和PDATALEN，用L51进行连接时还必须采用连接控制命令PDATA来对P2口地址进行定位，这样才能确保P2口为所需的高8位地址。

3、**LARGE模式**

LARGE模式中：所有函数和过程的变量以及局部变量数据段都被定义在51系统的外部数据存储器中，外部数据存储器最多可有64K，这要求用DPTR数据指针来间接地访问数据，因此，这种访问效率并不高，尤其是对2个或多个字节的变量，用这种模式访问数据程序的代码将会很大。

------

###### **所以，开发STC8H等大容量时，尽量选择SMALL模式来增加单片机访问变量的速度（默认情况下）**

如果东西加多了就会报

```
*** ERROR L121: IMPROPER FIXUP
```

这种情况下，就逐步增大**Memory Model**和**Code Rom Size**大小，直至报错消失

------

④ **STC15单片机下载相同程序，但是运行程序出现异常的可能原因**

如果程序出现异常，建议给单片机重启，在连接USB转TTL的情况下，重启应该是断开负极，而不是断开正极，因为TX、RX同样会给单片机供电。如果只断开正极（TX、RX没断开），那么程序仍然有可能会运行异常。

##### 2.对比不同喇叭在SU-03T上的功耗（使用合宙IoT Power）

4Ω3W大行程喇叭低音好，声音更有质感，功耗更大（531mA@5.2V）。带黑色腔体喇叭声音较为洪亮，但声音单薄，功耗较小（305mA@5.2V）。

##### 3.Keil F12,显示 NO information available for the selected symbol

**原因：**V6编译器不支持中文路径

**解决方法：**更改为V5或者置入全英文路径

### 12.9

##### 1.Keil 调试模式下能运行 烧录到板子中不能运行

原因：	在程序中使用了printf函数，但是却没有包含keil的微库（Micro LIB），或者对于printf函数没有进行重定向操作
解决方法：Options -> Target -> Use Micro LIB

##### 2.Keil 使用UTF-8报错#8

报错内容：

```
error: #8: missing closing quote
```

解决方法：Options -> C/C++ -> Misc Controls 添加:

```
--no-multibyte-chars
```

##### 3.Keil 生成.lib文件（以Keil C51为例）

① 把需要生成lib的Src和Inc单独创建一个Group，并且放入同名文件夹中，C/C++添加对应包含目录
② **其他不需要生成lib的Groups** 右键 -> " Options for Group 'xx' " -> "Include in Target Build" 取消打钩。此时除了需要生产Lib的Group其他都应该	出现红点
③ Options -> Output-> Create Library 打钩
④ Project Files对应的Group中，删除Src文件，添加Inc文件和Lib文件（从OUTPUT目录剪切过去，改成对应的名字）
⑤ Rebuild Project，检查是否有错误
⑥ Options -> Output-> Create Exe. 打钩，生成.hex文件

##### 4.尝试了大佬的例程@FPM383C

### 12.10

##### 1.Keil STLink无法正常Reset

解决方法：Options -> Debug -> ST-Link Settings -> Pack -> 取消Enable

##### 2.尝试了大佬的例程@wouo-ui

##### 3.学习了JXKJ的0.96OLED教程

学习过程：OLED-DrawAnonANDTomori

### 12.11

##### 1.更改了Keil 字体

```
JetBrainsMonoNL-Regular
```

效果非常好，Courier New看久了会有点细

##### 2.粗略阅读了一下AIR32的Daplink源码，并且下载了luatos Using KiCad的工程，等待学习

##### 3.记一次STM32使用I2C PinRemap引脚重映射出现卡死现象

以下为网友遇到的：

>	在调试多用户表的时候，发现如果人为短接I2C的SDA或SLK脚后，I2C的SR2的Busy标志将会置1，并且试了很多种办法也无法清除该标志位，只能复位芯片后I2C才能恢复正常。
>	导致这个问题的原因是STM32芯片的硬件I2C接口是支持多个主设备同时使用的，STM32的I2C接口会一直检查SDA和SLK的状态，当出现非自己发出的电平变化等情况后，STM32芯片则判定为是有其它I2C的主在操作总线，这样STM32的Busy（总线忙标志）则会置位，只有在检查到一次I2C协议的停止位后才会硬件清除该标志，如下说明：

![img](https://img-blog.csdnimg.cn/20210105134528450.png)

**遇到的现象**：在习惯使用的（SWI2C & HWI2C）@(PB8->SCL PB9->SDA)连接OLED的情况下，大多数情况使用江科大的SWI2C，一切正常。
今天跑某开源移植u8g2 wouo-ui（HWI2C）@(PB6->SCL PB7->SDA) 遇到了一旦连接OLED的正负极跳线就会导致STM32卡死的现象。意识到可能这就是传说中的标准库 Bug，网上搜寻方案后成功解决，但是I2C的通信速率不能调的和非重映射的一样高，原因未知。

**主要原因**：加入的OLED供电正负极跳线会导致PB6 PB7被动受到外部电平影响，内核检测到BUSY信号，故卡死。
**解决方法**：软件复位，或更换HAL 库

**步骤**：
① 重映射配置
在GPIO的RCC使能函数下，加入如下语句：

```
    RCC_APB2PeriphClockCmd(RCC_APB2Periph_AFIO, ENABLE);
    GPIO_PinRemapConfig(GPIO_Remap_I2C1, ENABLE); 	//重映射到PB8/PB9
```

② 在所有I2C1有关的配置寄存器写入任何数据之前，加入如下语句：

```
    I2C1->CR1 |= (1 << 15);
    I2C1->CR1 &= ~(1 << 15);   
```

![image-20231212012337715](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\image-20231212012337715.png)

完整的I2C初始化代码如下:

```
#define IIC_OLED_SCL_Pin        	GPIO_Pin_8
#define IIC_OLED_SCL_GPIO       	GPIOB
#define IIC_OLED_SCL_GPIO_CLK		RCC_APB2Periph_GPIOB


#define IIC_OLED_SDA_Pin        	GPIO_Pin_9
#define IIC_OLED_SDA_GPIO       	GPIOB
#define IIC_OLED_SDA_GPIO_CLK		RCC_APB2Periph_GPIOB

/*引脚初始化*/
void OLED_I2C_Init(void)
{
	I2C_InitTypeDef I2C_InitStructure = {0};
    GPIO_InitTypeDef GPIO_InitStructure = {0};						//定义GPIO结构体
    
    I2C1->CR1 |= (1 << 15);
    I2C1->CR1 &= ~(1 << 15);   // 防止重定义之前,V与G连接PB6 PB7导致的I2C卡死
    
	RCC_APB2PeriphClockCmd(IIC_OLED_SDA_GPIO_CLK,ENABLE);			//开启GPIO模块的时钟
	RCC_APB2PeriphClockCmd(IIC_OLED_SCL_GPIO_CLK,ENABLE);			//开启GPIO模块的时钟
	RCC_APB1PeriphClockCmd(RCC_APB1Periph_I2C1, ENABLE);
    
    RCC_APB2PeriphClockCmd(RCC_APB2Periph_AFIO, ENABLE);
    GPIO_PinRemapConfig(GPIO_Remap_I2C1, ENABLE); 	//重映射到PB8/PB9需要加这两行（无关位置）
    

    
    I2C_InitStructure.I2C_Mode = I2C_Mode_I2C;
    I2C_InitStructure.I2C_DutyCycle = I2C_DutyCycle_2;
    I2C_InitStructure.I2C_OwnAddress1 = 0x00;
    I2C_InitStructure.I2C_Ack = I2C_Ack_Enable;
    I2C_InitStructure.I2C_AcknowledgedAddress = I2C_AcknowledgedAddress_7bit;
    I2C_InitStructure.I2C_ClockSpeed = 285*1000;// N*1000
    I2C_Init(I2C1, &I2C_InitStructure);
    I2C_Cmd(I2C1, ENABLE);   
	
	GPIO_InitStructure.GPIO_Pin=IIC_OLED_SDA_Pin;					//配置SDA端口
	GPIO_InitStructure.GPIO_Mode = GPIO_Mode_AF_OD; 				// 设置GPIO的模式为输出模式
	GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;
	GPIO_Init(IIC_OLED_SDA_GPIO, &GPIO_InitStructure); 				// 初始化GPIO为高速开漏输出模式

	GPIO_InitStructure.GPIO_Pin=IIC_OLED_SCL_Pin;					//配置SCL端口
	GPIO_InitStructure.GPIO_Mode = GPIO_Mode_AF_OD; 				// 设置GPIO的模式为输出模式
	GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz; 				// 配置 I/O 口的速度为：50MHz
	GPIO_Init(IIC_OLED_SCL_GPIO, &GPIO_InitStructure); 				// 初始化GPIO为高速开漏输出模式
}
```



##### 4.重新学习了C语言的指针，并且写了例程验证

### 12.12

##### 1.STM32-CRC外设

##### 2.Markdown语法笔记

1. ***Ctrl + .* 组合键可以暂时切换到中文+半角标点符号的模式!**
2.  i 斜体,b 加粗
3.  "~~" -> 删除线 
4.  "==" -> 高亮
5. " >  "前置 -> 引用
   例如:

> 测试

6. "-"或"+" 加空格前置 -> 无序列表 (加Tab则变成子集)
   例如:

- 测试
- 测试2
  - 子集(再敲一下Tab)

7. 数字+"." -> 有序列表

8. "[]" + "()" -> 链接

   例如:[测试](www.baidu.com)

9. "- [ ]" + 空格 -> 任务列表(注意-后面有空格,方括号内部也有空格)

   测试:

   Todo:

   - [ ] 测试

   - [x] 测试2

10. **Win+分号或点 -> emoji/颜文字输入模式😍😂**
11. 常用快捷键

![image-20231212224634067](F:\Folder\EE\EverydayNote\yue-note.assets\image-20231212224634067.png)

##### 3.ℳ𝓎𝒢𝒪!!!!! 1𝓈𝓉 ℒ𝒾𝓋ℯ，这是什么字体？？

### 12.13

##### 1. 验证了STM32F411CEU6/ST-Link/CH343UART(**WeActStudio**)的功能

##### 2. 尝试了加入无效命令词默认返回语音,以**失败**告终.

##### 3. 接下小农的委托任务,将红外夜视眼镜加入ToDO List

### 12.14

##### 1. 验证了H750(WeActStudio)的开发板,并且跑了OpenMV的程序

##### 2 .暂时放弃了U-Boot的移植,因为太无聊

##### 3 .完成红外眼镜的主要零部件购买

+ 树莓派4B 4GB
+ HDMI-取景器OLED(目镜用)
+ 眼镜3D打印外壳

##### 4. 开始Linux驱动开发

### 12.15

##### 1. 又回到了U-Boot移植

##### 2. 树莓派到了



### 12.16

##### 1. 树莓派配环境

+ 格式化TF为FAT32

+ 烧写镜像文件(建议bullseye)

+ 配置串口 : config.txt 加入

```
enable_uart=1
```

+ 执行如下操作,防止无法输入密码

> [【树莓派】解决树莓派putty连接-输入账号pi密码raspberry后显示Access denied的问题 ](https://www.cnblogs.com/steven913/p/17289120.html)

+ putty连接后执行

```
sudo raspi-config
```

+ 打开摄像头

+ 打开串口

+ 打开VNC

+ 打开SSH

+ 查看wifi后台是否有树莓派的地址,输入VNC客户端(与putty)

+ VNC远程设置成功

+ 替换源为清华大学镜像源
  + 首先在树莓派操作系统的命令行中用nano命令编辑「/etc/apt/sources.list」文件：

```
sudo nano /etc/apt/sources.list
```

​				在每一行内容前都输入＃号，将其注释掉。然后在末尾添加：

```
deb https://mirrors.tuna.tsinghua.edu.cn/debian/ bullseye main contrib non-free
deb https://mirrors.tuna.tsinghua.edu.cn/debian/ bullseye-updates main contrib non-free
deb https://mirrors.tuna.tsinghua.edu.cn/debian/ bullseye-backports main contrib non-free
deb https://security.debian.org/debian-security bullseye-security main contrib non-free
```

​		 		接下来用nano命令编辑「/etc/apt/sources.list.d/raspi.list」文件：

```
sudo nano /etc/apt/sources.list.d/raspi.list
```

​				同样注释掉原内容，然后添加以下内容：

```
deb http://mirrors.tuna.tsinghua.edu.cn/raspberrypi/ bullseye main
```

​				按ctrl+o保存，ctrl+x退出。(或者直接ctrl+x -> 大写的Y -> ENTER ->ctrl+x)(ctrl+s保存+ctrl+x退出即可)

​				最后更新软件源

```
sudo apt-get update
```

​				如果最后显示「......Done」，说明update顺利结束，树莓派已经成功切换到清华大学镜像站了。

> [Raspbian 软件仓库](https://mirrors.tuna.tsinghua.edu.cn/help/raspbian/)

+ 安装openCV-Python

```
sudo apt-get install python3-opencv
```

+ 等待安装结束后，继续在命令行中输入指令进入Python，import openCV包，并查看其版本信息：

  ```
  python
  
  import cv2
  
  cv2.__version__
  ```

  如果命令行顺利返回openCV的版本信息，说明在树莓派中安装openCV大功告成！

### 12.17

##### 1. 批量复制配好环境的树莓派系统

1. 使用格式化工具将sd卡格式化为FAT32格式,若容量大于32GB则需要在macOS环境下格式化
2. 使用系统自带的SD Card Copier拷贝文件,等待拷贝完成进入Terminal -> sudo raspi-config -> Advanced Options -> Expand FileSystem

复制有可能会出现的问题:

> 重启电脑点击打开google chrome会出现一个小框，显示如下内容：
> The profile appears to be in use by another Google Chrome process (8879) on another computer ("previous name of the computer").  Chrome has locked the profile so that it doesn't get corrupted.  If you are sure no other processes are using this profile, you can unlock the profile and relaunch Chrome.

解决方法:

终端输入:

```
rm -rf ~/.config/chromium-browser/Singleton*
```

### 12.18

##### ✨important !!! : [Set up Clash Client on Your Raspberry Pi 4](https://kevinxli.medium.com/set-up-clash-client-on-your-raspberry-pi-4-54e77f7f7fe4) ✈️

**树莓派个人常用命令:**

```
env | grep -i proxy 
查看代理
export http_proxy="" 
关闭代理

sudo find / -iname "*opencv*" 
搜索某个目录或者文件的位置

export http_proxy=127.0.0.1:7890
export https_proxy=127.0.0.1:7890

export http_proxy=""
export https_proxy=""
export heeps_proxy=""
export no_proxy=""
批量关闭代理

sudo apt-get update
sudo apt-get upgrade

 
ls -al /dev/ | grep video
查看有多少个摄像头


sudo apt-cache search libboost
搜索某个库
sudo apt-get install libboost-all-dev 
安装所有的

du -ah /home/pi | sort -rh | head -n 10
按占用空间从大到小列出用户目录下的10个文件

sudo apt-get clean
sudo apt-get autoclean
sudo apt-get autoremove
清理不需要/旧版的软件包

sudo du -ah /tmp | sort -rh | head -n 10
按占用空间从大到小列出tmp目录下的10个文件
sudo rm -rf /tmp/*
清除tmp

sudo rm -rf ~/.local/share/Trash/*
清除垃圾箱

tar -cvf bkp_231221.tar.gz ./*
(先进入目录)将此目录下所有文件压缩为bkp_231221.tar.gz
tar -xvf my.tar.gz 
将my.tar.gz解压展开
```

##### 1. 编译了opencv3 Cpp环境

### 12.19

##### 1. 硬件(摄像头/补光灯)已经跑通,开始软件设计

### 12.20

##### 1. 软件跑通了,开始组合

##### 2. 使用MOS开关LED要比三极管更好

##### 3. 创建了备份文件

### 12.21

##### 1. 学习了阿奇-SW教程1-10课时(进度27%)

##### 2. 解决了树莓派IR画面采样大小的问题

##### 3. 完成了启动画面对接

### 12.22

##### 1. md,弄坏屏幕排线(((((天灾人祸啊!!!)))))

##### 2. 至少把结构装好了,等屏幕和电容按键到货,再手焊控制板

##### 3. 继续学习阿奇-SW教程11-12课时(进度30%)

### 12.23

##### 1. 休息一天

### 12.24

##### 1. 学习了SW(到手机支架)

##### 2. 测试了LGT8F328P,下载要按很多次RST(不好用)

### 12.25

##### 1. AG32跑了例程

##### 2. 测试了电源模块,最终使用两块并联完成,升压模块纹波很大,并联电容解决

### 12.26

##### 1. 感冒+发烧,休息一天

##### 2. 完成了C51报告和课设

### 12.27

##### 1. 感冒刚恢复,以后要当心着凉,不要熬夜,多运动.注意身体

##### 2. 初识了vivado zynq.要命的安装包体积(30GB -> 78GB -> 295GB)

### 12.28~1.2

感冒躺尸一个礼拜了，注意身体！

# 2024

## 1

### 1.3

##### 1. 焊接了按键电路，控制灯光和补光的MOS

### 1.4

##### 1. 接了两个单子，分别是门锁设计和台灯设计 

### 1.5

##### 1.完成了台灯设计和门锁设计的单子

### 1.6

##### 1. 连接了御坂眼镜的触摸部分，这个开发到后期是真的寸步难行

##### 1.完成了1单

### 1.8

##### 1.接了脑电波刺激项目

### 1.9

##### 1.完成了脑电波刺激项目，并且提交了仿真文件

### 1.10

##### 1.接了300元的智能语音电梯设计

##### 2.和李琳老师开会，获得开发板借用权利

##### 3.老师安排了设计小车售卖货架和外壳的任务

### 1.11

##### 1.完成了电梯设计实物制作与代码注释

##### 2.和14423沟通了眼镜相关事宜，建模完成最后的封口工作

### 1.12

##### 1.寄出了电梯设计实物

##### 2.接了51光感蓝牙双色台灯设计

##### 3.初步完成眼镜封口设计，准备细化

##### 4.修整了凌乱的小车，准备打印货架

### 1.13

##### 1.树莓派开机自启动可执行程序

在桌面上建立start_terminal.sh文件，用于自动执行可执行文件

```
sudo nano /home/pi/Desktop/start_terminal.sh
```

写入

```
#!/bin/sh
sleep 5
cd 可执行文件目录
lxterminal -e ./可执行文件名
```

例如：

```
#!/bin/sh
sleep 5
cd /home/pi/Desktop/User_Workspace/build/exe
lxterminal -e ./demo_Misaka_14423
```

进入自启动文件

```
sudo nano /etc/profile
```

最后一行添加启动指定可执行程序的代码

```
bash /home/pi/Desktop/start_terminal.sh &
```

**注：不加“&”时程序阻塞在此处执行，不加载桌面。**

### 1.24

##### 1. 正点原子Mini例程无法使用DAPLink下载

解决方法:

将LCD.c内第639行的:

```
__HAL_AFIO_REMAP_SWJ_DISABLE();				//禁止JTAG
```

改为:

```
__HAL_AFIO_REMAP_SWJ_NOJTAG();
```

**注意：一定要改完，编译，再下载，否则会导致无法下载程序，只能用串口下载一遍以清除SWJ禁止！！**

### 1.27

##### 1. STM32 Flash :Code、RO-data、RW-data和ZI-data是什么意思呢？

**Code** 	   代表执行的代码，程序中所有的函数，存储在rom中

**RO-data**  代表只读数据，程序中所定义的全局常量数据，存储在rom中；

**RW-data** 代表已初始化的读写数据，程序中定义并且已初始化的全局变量和静态变量，既存储在ram				 中，也存储在rom中（RW-data已初始化的数据会存储在rom中，上电会从rom搬移至ram中				 的全局区的RW data段，注意：ram中的全局区分为RW data段和 BSS data段，BSS data保				 存的是未初始化的全局变量和未初始化的所有静态变量(包括子函数里的静态变量））；

**ZI-data**   代表定义了但未初始化的可读写的全局变量和未初始化的所有静态变量，ZI英语是zero 				 initial，就是程序中用到的变量并且被系统初始化为0的变量的字节数，keil编译器默认是把你				 没有初始化的变量都赋值一个0，这些变量在程序运行时是保存在RAM中的BSS data段。

因此程序占用空间如下：

**ROM大小=Code+RO-data+RW-data**

**RAM大小=RW-data+ZI-data**

## 2

### 2.4

##### 1. Keil编译后文件转换成Bin

配置内User -> After Build -> Run#1 

```
$K\ARM\ARMCC\bin\fromelf.exe --bin --output=Bin\@L.bin !L
```

##### 2. ESP-01 正常启动方法

VCC(3.3V) 
GND
CH_PD(**EN**)(**接1K上拉电阻****,不接无法启动**)
TXD RXD(下载)
RET(不用可以悬空)
GPIO2
GPIO0(下载是接地，调试时悬空)

### 2.8

##### 1. 查了10个小时的问题-SGP30

问题的原因是因为SGP30测量时工作电流50mA，8266工作电流200mA，供电不足导致SGP30卡在初始化......

### 2.21

##### 1. 解决自带屏幕大果粒

1. 选择harmony sans sc
2. 选择字号10，全部设定

### 2.26

##### 1. 使用Keil的#pragma 消除特定警告

```c
/* 例如 */
/*..\User\Tool\NFC\nfc.c(68): warning:  #550-D: variable "status_b"  was set but never used */
#pragma diag_suppress 177
#pragma diag_suppress 550
```

直接添加到头文件即可，笔者使用情况为

```
..\HARDWARE\rc522.c(1177): warning:  #111-D: statement is unreachable
```

则在出现问题的c文件所包含的.h文件中加入以下语句即可

```C
#pragma diag_suppress 111
```

## 3

### 3.2

##### 1. 解决串口回调只执行一次

串口使用流程：

1、初始化串口，勾选使能中断（此处CubeMX只会帮你生成中断函数和安排NVIC，并不会帮你打开中断）

2、使用以下函数使能中断（在非阻塞模式下接收一定量的数据）

```C
HAL_StatusTypeDef HAL_UART_Receive_IT(UART_HandleTypeDef *huart, uint8_t *pData, uint16_t Size)
```

huart: 指向包含 UART_HandleTypeDef 结构的指针

pData: 指向数据缓冲区的指针

Size: 要接收的数据量

注意：如果设置要接受的数据量为1个字节数，那么**当接受1个字节以后就会进入回调函数**。
需要重定义回调函数

接受回调函数如下：

```C
void HAL_UART_RxCpltCallback(UART_HandleTypeDef *huart)
```

注意：如果需要多次进入回调函数，那么回调函数中，**需要重新使能接受中断。否则只能进入一次**。

##### 2. 优信电子家的485转换模块

1. MAX485：输入输出都只支持5V TTL，需要连接FT的GPIO口（stm32的UASART GPIO都是FT的）

   需要另外牵引一条GPIO控制线，同时连接DE和RE，发送的时候需要手动拉高，发送完毕拉低准备接受：

   ```c
   HAL_GPIO_WritePin(MAX485_Ctrl_GPIO_Port, MAX485_Ctrl_Pin, GPIO_PIN_SET);//拉高
   HAL_UART_Transmit(&huart3, Inquire_data, sizeof(Inquire_data), 0XFFFF); //发送数组里的字符串数据
   HAL_GPIO_WritePin(MAX485_Ctrl_GPIO_Port, MAX485_Ctrl_Pin, GPIO_PIN_RESET);//拉低，准备后面的接收
   ```

2. TTL转RS485模块

   TXD/RXD不需要错位连接，按照模块背面的丝印处理，直接:

   TXD(MODEL)-TXD(MCU)

   RXD(MODEL)-RXD(MCU)

### 3.5

##### 1. vscode环境内的cortex-debug

launch.json @ daplink

```json
{
    // 使用 IntelliSense 了解相关属性。 
    // 悬停以查看现有属性的描述。
    // 欲了解更多信息，请访问: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Cortex Debug",
            "showDevDebugOutput": "raw",
            "cwd": "${workspaceFolder}",
            "executable": "${workspaceFolder}\\USER\\build\\Target 1\\ProjectMiniSTM32.axf",
            "request": "launch",
            "type": "cortex-debug",
            "runToEntryPoint": "main",
            "servertype": "openocd",
            "configFiles": [
                "interface/cmsis-dap.cfg",
                "target/stm32f1x.cfg"
            ],

        }
    ]
}
```

### 3.6

##### 1. CLion + arm-none-eabi-gcc编译文件过大

**解决方法**：在CMakeLists.txt中加入

```
add_link_options(--specs=nano.specs)
```

### 3.7

##### 1. CLion新建工程报错

报错内容如下：

```
sbrkr.c:(.text._sbrk_r+0xc): undefined reference to `_sbrk'
```

原因：ARM gcc默认是使用startfiles，导致调用底层未实现的某些函数（malloc、 free、 sprintf…）时，编译链接失败。

推广：如果编译报undefined reference to `_sbrk' `_read' `_write' `_lseek' `_isatty' `_fstat' 也是相同原因。

**解决方法**：在CMakeLists.txt中加入

```
add_link_options(--specs=nosys.specs)
```

### 3.10

##### 1. for循环中最后一个参数使用++i还是i++

chatgpt的回答：

However, it's generally considered good practice to use `++i` in `for` loops where the value of the variable being incremented is not needed after the increment, as it can sometimes result in slightly more efficient code due to avoiding the creation of a temporary variable for the pre-increment operation.

所以尽可能地使用`++i`而并非`i++`

### 3.18

##### 1. 关于Debugger

1. 可以使用示波器直接测量SWCLK引脚观察速度

2. Keil中DAPLink显示的最高(10Mhz)是假的，但是ST-Link的4MHz是真的

3. EIDE中由于在WoA环境下无法安装ST-Link GDB Server，故无法使用ST-Link调试，但通过Openocd可以支持ST-Link和DAPLink

4. 在EIDE中，使用Openocd时候设置速度：

   ```
   ${openocd_path}\share\openocd\scripts\target\你的目标芯片型号.cfg
   ```

   中有如下代码：

   ```
   # JTAG speed should be <= F_CPU/6. F_CPU after reset is 8MHz, so use F_JTAG = 1MHz
   adapter speed 1000
   ```

   可以将1k改成10k(单位是kHz)
   

##### 2. Cortex-Debug

1. 使用daplink的launch.json

   ```json
   {
       // 使用 IntelliSense 了解相关属性。 
       // 悬停以查看现有属性的描述。
       // 欲了解更多信息，请访问: https://go.microsoft.com/fwlink/?linkid=830387
       "version": "0.2.0",
       "configurations": [
           {
               "name": "Cortex Debug",
               "showDevDebugOutput": "raw",
               "cwd": "${workspaceFolder}",
               "executable": "${workspaceFolder}\\USER\\build\\Target 1\\ProjectMiniSTM32.axf",
               "request": "launch",
               "type": "cortex-debug",
               "runToEntryPoint": "main",
               "servertype": "openocd",
               "configFiles": [
                   "interface/cmsis-dap.cfg",
                   "target/stm32f1x.cfg"
               ],
   
           }
       ]
   }
   ```

   2. 使用ST-Link的launch.json

      ```json
      {
          // 使用 IntelliSense 了解相关属性。 
          // 悬停以查看现有属性的描述。
          // 欲了解更多信息，请访问: https://go.microsoft.com/fwlink/?linkid=830387
          "version": "0.2.0",
          "configurations": [
              {
                  "name": "Cortex Debug",
                  "showDevDebugOutput": "raw",
                  "cwd": "${workspaceFolder}",
                  "executable": "D:\\Folder\\EE\\SimpleDev\\ExperimentSPACE\\OLED-DrawAnonANDTomori-ITM_SendChar\\EIDE_Project\\build\\Target 1\\Project.elf",
                  "request": "launch",
                  "type": "cortex-debug",
                  "runToEntryPoint": "main",
                  "servertype": "openocd",
                  "configFiles": [
                      "interface/stlink.cfg",
                      "target/stm32f1x.cfg"
                  ],
      
              }
          ]
      }
      ```

      

##### 3. ITM打印

1.暂时只发现能在KEIL中使用

在工程中加入以下代码：

```c
#include "stdio.h"
//////////////////////////////////////////////////////////////////
//加入以下代码,支持printf函数,而不需要选择use MicroLIB
#if 0
#pragma import(__use_no_semihosting)
//标准库需要的支持函数
struct __FILE
{
    int handle;

};

FILE __stdout;
//定义_sys_exit()以避免使用半主机模式
void _sys_exit(int x)
{
    x = x;
}
//重定义fputc函数
int fputc(int ch, FILE *f)
{
    ITM_SendChar((u8)ch);
    return ch;
}
#endif
```

### 3.21

##### 1. 嵌入式开发中后缀的重要性

**例1**

```c
float f = 1.234;
```

若不写后缀，编译器在编译的时候，右侧常浮点数默认是double类型的，当1.234赋值给f的时候，存在强制类型转换。
数据较小时不会发生错误，若数据较大则会产生溢出，结果会出现非预期值。所以在书写时，最好在常量的末尾加后缀进行严格的限制。

正确应该如下：

```c
float f = 1.234f;
```

**例2**

```c
typedef enum {
  HAL_OK = 0x0U,
    ...
} HAL_StatusTypeDef
```

右侧默认为有符号INT类型。若加入U则代表无符号整型，若为UL则是无符号长整型变量

### 3.27

##### 1. C++指针学习

```C++
// 常量指针：
const int *p = &a;
// 特点：指针的指向可以修改，指向的值不能修改
// 指针常量：
int * const p = &a;
// 特点：指针的指向不能修改，指向的值可以修改
// 都不能修改的情况
const int * const p = &a;
```

##### 2. C编译过程详细解释

1. 预编译：预处理器对C程序进行一些预处理工作，例如对宏定义的变量进行替换
   - 将所有的#define删除，并展开所有的宏定义
   - 处理所有的预编译指令，例如#if #ifdef #else #elif #endif
   - 处理#include预编译指令，将被包含的文件插入到预编译指令的位置
   - 添加行号信息/文件名信息，便于调试
   - 删除所有的注释
   - 保留所有的#pragma编译指令，因为该指令经常用来设定编译器的状态或是指示编译器完成一些特定的动作
   - **最后生成.i文件**
2. 编译：编译器将C语言翻译成汇编程序
   - 扫描/语法分析/语义分析/源代码优化/目标代码生成/目标代码优化
   - 生成汇编代码
   - 汇总符号
   - 生成.s文件
3. 汇编：汇编语言通过汇编器编译成可重定位目标程序.o，与之相反称作反汇编
   - 根据汇编指令和特定平台，将汇编指令翻译成二进制形式
   - 合并各个Section，合并符号表
   - 生成.o文件
4. 链接：将目标文件和所需的库函数用链接器进行链接
   - 合并各个.obj文件的section，合并符号表，进行符号解析
   - 符号地址重定义
   - 生成可执行文件

##### 3. C语言巩固笔记

- 变量的存储区域

  程序的局部变量存在于**栈区**（属于动态存储区），全局变量和static修饰的变量存在于**静态存储区**，动态申请的数据（例如使用malloc函数分配的内存）存在于**堆区**（也是属于动态存储区）中。

- 动态存储区、静态存储区

  动态存储区存放函数的形参、没有用static关键字声明的变量、函数调用时候的现场保护和返回地址
  函数调用开始时分配动态存储空间，函数结束时释放这些空间。如果在一个程序中两次调用同一函数，而在此函数中定义了局部变量，在两次调用时分配给这些局部变量的存储空间的地址可能是不相同的。

  这些存储空间的分配和释放是由编译器和运行时系统来管理的，在函数调用时，编译器会生成代码来为局部变量分配空间，并在函数返回时自动释放。**这些分配和释放的操作是由编译器根据函数调用的上下文和执行流程来进行的**

- 变量放在堆区和栈区的区别主要体现在以下方面：

  生命周期：堆区的变量在动态申请内存时需要手动释放（例如调用free函数）

  内存管理：堆区的内存由程序员手动管理，包括申请和释放，而战区的内存由编译器自动管理

  内存空间：堆区的内存空间较大，受限于系统可用的虚拟内存大小，而栈区的内存空间较小，受限于系统的栈大小

  访问方式：堆区的变量通过指针进行访问，而栈区的变量可以直接通过变量名进行访问

  作用范围：堆区的变量的作用范围可以跨越多个函数，而栈区的变量的左右范围仅限于所属的函数

- 栈与堆的区别：

  从申请方式/申请大小/申请效率简单比较：栈的空间由操作系统自动分配/释放，堆的内存手动分配/释放。
  栈的空间有限。堆是很大的自由存储区，栈的申请效率高，堆的申请效率低

##### 4. 数组和指针和地址

1. 数组和指针的关系
   - 数组名在大多数情况下可以被解释为指向数组第一个元素的指针，也就是说，数组名本身就是一个指针常量，指向素组首元素的地址
   - 数组名可以像指针一样进行算数运算
   - 对数组名解引用可以得到数组第一个元素的值

2. 数组的成员地址是否连续
   - 我们先来看一次使用`malloc`申请多个（数组）地址的情况。结果表明，这些地址是**连续的**
   
   - 现在，我们来看一下多次使用`malloc`申请地址的情况。我们将每次申请的内存空间地址与上一块地址
   
     （`p-1`）进行比较。结果显示，这些地址并不是连续的。实际上，系统在每次调用`malloc`时，会从相隔固定长度的位置开始分配内存。
     这是因为涉及到**内存边界对齐**的问题。虽然在虚拟地址空间上，使用`malloc`分配的内存空间是连续的，但在物理内存空间上可能是不连续的。
     对于用户来说，所有内存都是虚拟的，程序并不直接运行在物理内存上，而是运行在虚拟内存上，然后再转换到物理内存。
     虚拟内存地址到物理内存地址的转换时，由于相邻的两个字节可能位于不同的物理分页上，所以并不一定是连续的。

##### 5. 变量修饰

1. auto

   函数的局部变量，若为指定声明为static，都是动态地分配存储空间，数据存储在动态存储区中，形参和定义的局部变量都属于此类。这类局部变量称为**自动变量**

   ```C
   auto int i= 0;
   // 大多数情况下auto可以省略，不写auto则隐含指定为“自动存储类别”
   int i = 0;
   ```

   
## 4
### 4.4

##### 1. 嵌入式课程书本摘抄

1. 冯诺依曼架构和哈佛架构

   **主要区别在指令的存放位置和读取方式**

   冯诺依曼架构的计算机，取指令和取操作数通过时分复用的方式在同一总线上传输

   哈佛架构是一种将程序指令和数据分开存储的存储器结构。并且使用两条独立的总线分别与CPU，进行信息交换

2. **小端就是低位对应低地址，高位对应高地址，大端是高位对应低地址**

### 4.15

##### 1. HardFault_Handler()

99%是由于野指针和非法内存访问导致的。在HardFault函数内添加一句 `asm("bx lr");`, 并在此处加上断点。当代码运行至此处时，选择跳出，程序会跳转回出错之前最后一句执行的语句。

查看你是否在出错前的最后一次操作中访问了非法地址或使用了已经被析构的指针。 `memcpy`的目标地址和源地址重合也可能引发硬件错误。另外，如果使用指针访问了一个非对齐地址（请参考__pack()相关的说明），这是CMSIS架构中不允许的（有些架构可以修改启动文件使其支持）；例如你有四个uint8类型的数据被存储在0x03-0x07的地址内，这时候你通过强制类型转换，以float的方式读取这四个字节，就会发生非对齐访问。 虽然结构体可以通过 `__pack(1)`来压缩，编译器会对结构体变量进行处理，在读取非对齐字段时分别读取拆分的两个部分再进行合并，从而支持非对齐访问；但前述的行为却是未定义的，编译器在编译代码的时候并不知道你会以分开的方式访问这段内存，即使知道，他也无法预测栈上分配的空间是否能对齐。

常见的错误还包括使用未初始化的指针（内部可能时垃圾值，指向未知的地址）和初始化为NULL的指针（指向0x00地址）。`free`一个指针两次也可能导致错误。

## 5
### 5.19

##### 1. 移植u-boot时编译出错

1. 第一次报错信息如下:

   > include/config.h:7:22: fatal error: configs/.h: No such file or directory
   >  #include <configs/.h>

   经检查发现该头文件生成有错误，系统生成这个头文件时未报错"缺少文件"，但这个文件格式**显然不正确**，该文件是自动生成的编译过程文件，生成时缺少了某些参数，观察第四行宏定义，缺少板载文件定义目录，回到板载文件那里找原因：

   在`board/freescale/mx6ull_alientek_emmc/Kconfig`下，

   经检查确实未修改本文件为alientek的版本，修改后问题解决。

2. 第二次报错信息如下：

   > arm-linux-gnueabihf-ld.bfd:u-boot.lds:1: ignoring invalid character `#' in expression
   > arm-linux-gnueabihf-ld.bfd:u-boot.lds:1: syntax error
   > make: *** [Makefile:1171: u-boot] Error 1

   经检查发现在之前修改`include/configs/mx6ull_alientek_emmc.h`时，发现以下代码位置：

   ```c
   // #ifndef __MX6ULLEVK_CONFIG_H
   // #define __MX6ULLEVK_CONFIG_H
   
   #ifndef __MX6ULL_ALIENTEK_EMMC_CONFIG_H
   #define __MX6ULL_ALIENTEK_EMMC_CONFIG_H
   ```

   上面**双斜杠**的使用导致错误的产生，如需注释请务必严格使用斜杠+星号的组合。

3. tftp无法自动从服务器加载设备树文件

   可以自动下载zImage，但无法下载imx6ull-14x14-emmc-7-1024x600-c.dtb
   经检查发现问题出在文件名上，更改文件名为alienTek.dtb即可

   实验发现数字和`-`都不会影响读取，估计是长度问题，但是手动使用tftp命令下载是可以的，有点奇怪
   
## 6
### 6.21

使用异或也可以很容易实现多个数据的互相备份，假如有数据a、b、c，则d = a ^ b ^ c，然后把数据d备份下来。

```
当a丢失时，可使用d ^ b ^ c来恢复
当b丢失时，可使用d ^ a ^ c来恢复
当c丢失时，可使用d ^ a ^ b来恢复
```

由此可见备份了一份数据d后，丢失了其他任何一个数据，都可以通过备份数据与其它数据异或恢复回来，磁盘阵列技术raid5的数据备份原理，用的就是这个特性。