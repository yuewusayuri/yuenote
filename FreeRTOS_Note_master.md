# assert断言

> 在 C 语言中,断言(assertion)是一种调试工具,它用于确保程序在某个特定点上满足某些条件.断言通常用于检查程序中的逻辑错误,确保程序的预设条件(invariants)或状态是正确的.如果断言失败(即条件评估为假),程序将立即终止执行,通常伴随着一个错误消息,这有助于开发者快速定位问题.

`assert` 将产生一个断言失败行为,这通常包括:

1. 通过 `abort()` 函数立即终止程序;
2. 如果 `assert` 宏被定义为调试模式(通常是通过编译时的 `-DDEBUG` 或 `-UNDEBUG` 标志),则可能还会生成一个错误消息,指出断言失败的位置;

断言的一个典型用途是在函数的开头检查参数的有效性:

```c
#include <assert.h>
#include <stdio.h>

void example_function(int *ptr) {
    assert(ptr != NULL);  // 确保指针不为空
    // ... 函数的其他代码 ...
}

int main() {
    int data;
    example_function(&data);  // 正确调用
    example_function(NULL);    // 这将触发断言,程序将终止
    return 0;
}
```

在上述示例中,如果 `example_function` 被传入一个空指针,断言将失败,程序将终止;

断言不应该用于检查预期会在程序正常运行过程中发生的错误(这些应该通过适当的错误处理机制来处理),而是用于捕获开发过程中的错误或假设不成立的情况.在生产环境中,通常会禁用断言(通过定义 `NDEBUG` 宏),以避免额外的运行时开销;

# 环形链表

FreeRTOS中的列表和列表项就是数据结构中的链表和节点;

FreeRTOS中的列表是一个**双向链表**;

在下方的注释中,最后一个列表项被"列表尾"所代替(不确定这么做是否规范,但便于理解);

```c
/**************第二步:打印列表和列表项的地址**************/
项目                    地址
TestList                0x2000313c
TestList->pxIndex       0x20003144
TestList->xListEnd      0x20003144
ListItem1               0x20003150
ListItem2               0x20003164
ListItem3               0x20003178
/**************************结束***************************/
按下KEY1键继续!
/*****************第三步:列表项1插入列表******************/
项目                            地址
TestList->xListEnd->pxNext      0x20003150 /* 列表项1插入列表后,列表末尾的下一个指向列表项1(固定不变) */
ListItem1->pxNext               0x20003144 /* 列表项1的下一个指向列表尾 */
TestList->xListEnd->pxPrevious  0x20003150 /* 列表尾的上一个指向列表项1 */
ListItem1->pxPrevious           0x20003144 /* 列表项1的上一个指向列表尾 */
/**************************结束***************************/
按下KEY1键继续!
/*****************第四步:列表项2插入列表******************/
项目                            地址
TestList->xListEnd->pxNext      0x20003150 /* 列表项2插入列表后,列表末尾的下一个指向列表项1(固定不变) */
ListItem1->pxNext               0x20003164 /* 列表项1的下一个指向列表项2 */
ListItem2->pxNext               0x20003144 /* 列表项2的下一个指向列表尾 */
TestList->xListEnd->pxPrevious  0x20003164 /* 列表尾的上一个指向列表项2 */
ListItem1->pxPrevious           0x20003144 /* 列表项1的上一个指向列表尾 */
ListItem2->pxPrevious           0x20003150 /* 列表项2的上一个指向列表项1 */
/**************************结束***************************/
按下KEY1键继续!
/*****************第五步:列表项3插入列表******************/
项目                            地址
TestList->xListEnd->pxNext      0x20003150 /* 列表项3插入列表后,列表末尾的下一个指向列表项1(固定不变) */
ListItem1->pxNext               0x20003164 /* 列表项1的下一个指向列表项2 */
ListItem2->pxNext               0x20003178 /* 列表项2的下一个指向列表项3 */
ListItem3->pxNext               0x20003144 /* 列表项3的下一个指向列表尾 */
TestList->xListEnd->pxPrevious  0x20003178 /* 列表尾的上一个指向列表项3 */
ListItem1->pxPrevious           0x20003144 /* 列表项1的上一个指向列表尾 */
ListItem2->pxPrevious           0x20003150 /* 列表项2的上一个指向列表项1 */
ListItem3->pxPrevious           0x20003164 /* 列表项3的上一个指向列表项2 */
/**************************结束***************************/
按下KEY1键继续!
/*******************第六步:移除列表项2********************/
项目                            地址
TestList->xListEnd->pxNext      0x20003150
ListItem1->pxNext               0x20003178 /* 列表项1的下一个指向列表项3 */
ListItem3->pxNext               0x20003144 /* 列表项3的下一个指向列表尾 */
TestList->xListEnd->pxPrevious  0x20003178 /* 列表尾的上一个指向列表项3 */
ListItem1->pxPrevious           0x20003144 /* 列表项1的上一个指向列表尾 */
ListItem3->pxPrevious           0x20003150 /* 列表项3的上一个指向列表项1 */
/**************************结束***************************/
按下KEY1键继续!
/****************第七步:列表末尾添加列表项2****************/
项目                            地址
TestList->pxIndex               0x20003144 /* 列表索引指向列表项1 */
TestList->xListEnd->pxNext      0x20003150 /* 列表项2插入列表后,列表末尾的下一个指向列表项1(固定不变) */
ListItem1->pxNext               0x20003178 /* 列表项1的下一个指向列表项3 */
ListItem2->pxNext               0x20003144 /* 列表项2的下一个指向列表尾 */
ListItem3->pxNext               0x20003164 /* 列表项3的下一个指向列表项2 */
TestList->xListEnd->pxPrevious  0x20003164 /* 列表尾的上一个指向列表项2 */
ListItem1->pxPrevious           0x20003144 /* 列表项1的上一个指向列表尾 */
ListItem2->pxPrevious           0x20003178 /* 列表项2的上一个指向列表项3 */
ListItem3->pxPrevious           0x20003150 /* 列表项3的上一个指向列表项1 */
/************************实验结束***************************/
```

# 任务调度器

使用`xTaskEndScheduler()`函数开启任务调度器,启动后则会开启任务调度,使用`xTaskEndScheduler()`停止任务调度;

函数`xTaskEndScheduler`主要做了:

1. 创建空闲任务(根据静态/动态会选择不同的方式);
2. 创建定时器任务(与上面一样);
3. 关闭中断,**但只关闭受系统管理的中断**,主要为了防止systick中断在任务调度器开启之前或开启过程中产生中断.(中断会在第一个任务运行时重新被打开);
4. 初始化相关变量,使能调度器运行标志;
5. 初始化任务运行时间统计功能的时基定时器,任务运行时间统计功能需要一个硬件定时器提供高精度的计数,这个硬件定时器就在这里进行配置,如果配置不启用任务运行时间统计功能的,就无需进行这项硬件定时器的配置;
6. 调用`xPortStartScheduler`,该函数完成启动任务调度器中与硬件架构相关的配置部分,以及启动第一个任务;

函数` prvStartFirstTask()`用于初始化启动第一个任务前的环境,主要是重新设置MSP 指针,并使能全局中断;

**函数 `prvStartFirstTask()`是一段汇编代码,解析如下所示:**

1. 首先是使用了 `PRESERVE8`,进行 **8 字节对齐**,这是因为,栈在任何时候都是需要 4 字节对齐的,而在调用入口得 8 字节对齐,在进行 C 编程的时候,编译器会自动完成的对齐的操作,**而对于汇编,就需要开发者手动进行对齐**;

2. 接下来的三行代码是为了**获得MSP 指针的初始值**;

   ```assembly
   ldr r0, =0xE000ED08 /* 0xE000ED08 为 VTOR 地址 */
   ldr r0, [ r0 ] /* 获取 VTOR 的值 */
   ldr r0, [ r0 ] /* 获取 MSP 的初始值 */
   
    /* 初始化 MSP */
    msr msp, r0
   ```

   0xE000ED08 是VTOR(向量表偏移寄存器)的地址,VTOR中保存了向量表的偏移地址.一般来说向量表是从其实地址 0x00000000 开始的,但是在有情况下,可能需要修改或重定向向量表的首地址,因此 ARM Corten-M 提供了VTOR对向量表进行从定向.而向量表是用来保存中断异常的入口函数地址,即栈顶地址的,并且向量表中的第一个字保存的就是栈底的地址;

   在 start_stm32xxxxxx.s 文件中有如下定义:
   `Vectors DCD initial_sp ; 栈底指针`

   以上就是向量表(只列出前几个)的部分内容,可以看到向量表的第一个元素就是栈指针的初始值,也就是栈底指针.在了解了这两个问题之后,接下来再来看看代码.首先是获取VTOR的地址,接着获取VTOR的值,也就是获取向量表的首地址,最后获取向量表中第一个字的数据,也就是栈底指针了;

3. 在获取了栈顶指针后,将 MSP 指针重新赋值为栈底指针.这个操作相当于**丢弃了程序之前保存在栈中的数据**,因为FreeRTOS从开启任务调度器到启动第一个任务都是不会返回的,是一条不归路,因此将栈中的数据丢弃,也不会有影响;

4. 重新赋值 MSP 后,接下来就**重新使能全局中断**,因为之前在函数 `vTaskStartScheduler()`中关闭了受FreeRTOS管理的的中断;

5. 最后使用` SVC `指令,并传入系统调用号 0,**触发SVC 中断**;

**函数 `vPortSVCHandler()`就是用来跳转到第一个任务函数中去的,该函数的具体解析如下:**

1. 首先通过 `pxCurrentTCB `获取优先级最高的就绪态任务的任务栈地址,优先级最高的就绪态任务就是系统将要运行的任务.`pxCurrentTCB` 是一个全局变量,用于指向系统中优先级最高的就绪态任务的任务控制块,在前面创建start_task任务,空闲任务,定时器处理任务时自动根据任务的优先级高低进行赋值的,具体的赋值过程在后续分析任务创建函数时,会具体分析.这里举个例子,在<FreeRTOS 移植实验>中,start_task任务,空闲任务,定时器处理任务的优先级如下表所示:

   

   |    任务名称    | 中断优先级(越大越高) |
   | :------------: | :------------------: |
   |    空闲任务    |          0           |
   | start_task任务 |          1           |
   | 定时器处理任务 |          31          |
   
   从上表可以看出,在<FreeRTOS 移植实验>中,定时器处理任务的任务优先级为 31,是系统中优先级最高的任务,因此当进入 **SVC 中断**时,`pxCurrentTCB `就是指向了定时器处理任务的任务控制块;

# 创建任务

`xTaskCreate()`为创建任务函数,它将依次执行以下操作:

1. 首先为任务的任务控制块以及任务栈空间**申请内存**,申请成功则会进入下一步;

2. 调用函数`prvInitialiseNewTask()`,初始化任务控制块中的成员变量;

   1. 调用函数`pxPortInitialiseStack()`初始化任务栈;

      > 函数 pxPortInitialiseStack()用于初始化任务栈,就是往任务的栈中写入一些重要的信息,这些信息会在任务切换的时候被弹出到 CPU 寄存器中,以恢复任务的上下文信息,这些信息就包括 xPSR 寄存器的初始值,任务的函数地址(PC 寄存器),任务错误退出函数地址(LR 寄存器),任务函数的传入参数(R0 寄存器)以及为 R1~R12 寄存器预留空间,若使用了浮点单元,那么还会有 EXC_RETURN 的值.同时该函数会返回更新后的栈顶指针.

3. 调用函数`prvAddNewTaskToReadyList()`用于将新建的任务添加到就绪态任务列表中;

   1. 以位图的方式记录就绪态任务列表中就绪态任务的优先级;
   2. 将任务的任务状态列表项插入到就绪态任务列表的末尾;


# 删除任务

`vTaskDelete()`函数可删除指定任务.若传入参数为`NULL`时,他会删除调用这个函数的**任务本身**;

> 将任务从任务所在任务状态列表(就绪态任务列表或阻塞态任务列表)中移除;
> 如果移除后列表中的列表项数量为 0, 那么就需要更新任务优先级记录,
> 因为此时系统中可能已经没有和被删除任务相同优先级的任务了;

```c
if( uxListRemove( &( pxTCB->xStateListItem ) ) == ( UBaseType_t ) 0 )
 {
 	/* 更新任务优先级记录 */
 	taskRESET_READY_PRIORITY( pxTCB->uxPriority );
 }
 ...
 /* 判断被删除的任务是否为正在运行的任务(即任务本身) */
 if( pxTCB == pxCurrentTCB )
 {
     /* 任务是无法删除任务本身的,于是需要将任务添加到任务待删除列表中
     * 空闲任务会处理任务待删除列表中的待删除任务
     */
     vListInsertEnd( &xTasksWaitingTermination,
     &( pxTCB->xStateListItem ) );
 
     /* 这个全局变量用来告诉空闲任务有多少个待删除任务需要被删除 */
     ++uxDeletedTasksWaitingCleanUp;
 
     /* 用于调试,不用理会 */
     traceTASK_DELETE( pxTCB );
 
     /* 未定义,不用理会 */
     portPRE_TASK_DELETE_HOOK( pxTCB, &xYieldPending );
 }
```

从上面的代码中可以看出,使用` vTaskDelete()`删除任务时,需要考虑两种情况,分别为待删除任务**不是当前正在运行的任务**(调用该函数的任务)和待删除任务**为当前正在运行的任务**(调用该函数的任务).第一种情况比较简单,当前正在运行的任务可以直接删除待删除任务;

而第二种情况下,待删除任务时无法删除自己的,因此需要将当前任务**添加到任务待删除列表中**,空闲任务会处理这个任务待删除列表,将待删除的任务统一删除,有关空闲任务的相关内容,在后续的章节中会进行讲解;

在待删除任务不是当前正在运行的任务这种情况下,当前正在运行的任务可以删除待删除的任务,因此调用了函数 `prvDeleteTCB()`,将待删除的任务删除;

```c
 /* 如果待删除任务不是任务本身 */
 if( pxTCB != pxCurrentTCB )
 {
     /* 此函数用于释放待删除任务占用的内存资源 */
     prvDeleteTCB( pxTCB );
 }
```

该函数主要用于释放待删除任务所占的内存空间.

# 挂起任务

`vTaskSuspend()`函数可挂起指定任务.若传入参数为`NULL`时,他会挂起调用这个函数的**任务本身**;

> 使用函数 vTaskSuspend()挂起任务时,如果任务调度器没有运行,并且待挂起的任务又是调用函数 vTaskSuspend()的任务,那么 pxCurrentTCB 需要指向其他优先级最高的就绪态任务;
> 更新 pxCurrentTCB 的操作,是通过调用函数 vTaskSwitchContext()实现的;

# 恢复任务

`vTaskResume()`函数可恢复指定任务.传入参数不能是当前正在运行的任务,也不能为`NULL`;

1. 判断待恢复的任务是否有效

   ```c
   if( ( pxTCB != pxCurrentTCB ) && ( pxTCB != NULL ) )
   ```

2. 判断任务是否被挂起

   ```c
   if( prvTaskIsTaskSuspended( pxTCB ) != pdFALSE )
   ```

3. 将待恢复任务的任务状态列表项从所在任务状态列表(挂起态任务列表)中移除

   ```c
   ( void ) uxListRemove( &( pxTCB->xStateListItem ) )
   ```

4. 将待恢复任务的任务状态列表项添加到就绪态任务列表中

   ```c
   prvAddTaskToReadyList( pxTCB );
   ```

5. 如果待恢复任务的优先级比当前正在运行的任务的任务优先级高,则需要进行任务切换

   ```c
   if( pxTCB->uxPriority >= pxCurrentTCB->uxPriority )
   {
   	taskYIELD_IF_USING_PREEMPTION();
   }
   ```

# 空闲任务

`prvIdleTask()`空闲任务主要用于处理待删除任务列表和低功耗;

1. 处理待删除任务列表中的待删除任务;

   ```c
   prvCheckTasksWaitingTermination();
   ```

2. 判断是否为抢占式调度;

   如果不使用抢占式调度,则强制切换任务,以确保其他任务(非空闲任务)可以获得 CPU 使用权,如果使能了抢占式调度,则不需要这么做,因为优先级高的就绪态任务会自动抢占 CPU 使用权;

   如果存在与空闲任务相同优先级的任务,则进行任务切换;

   ```c
   #if ( configUSE_PREEMPTION == 0 )
   {
   	taskYIELD();
   }
   #endif
   /* 宏 configIDLE_SHOULD_YIELD 用于使能空闲任务可以被同优先级的任务抢占 */
   #if ( ( configUSE_PREEMPTION == 1 ) && ( configIDLE_SHOULD_YIELD == 1 ) )
   {
    /* 如果存在与空闲任务相同优先级的任务,则进行任务切换 */
    if( listCURRENT_LIST_LENGTH(&(pxReadyTasksLists[tskIDLE_PRIORITY]))>( UBaseType_t ) 1 )
    {
    	taskYIELD();
    }
    else
    {
    	mtCOVERAGE_TEST_MARKER();
    }
   }
   #endif
   ```

   #### **==这里使用#if条件编译的优点是:==**

   #### **==把一部分本该会重复运行占用系统时间的运算转移到编译阶段,==**

   #### **==同时减小了代码的空间占用;==**

# yield

在操作系统和实时操作系统(RTOS)中,yield通常是一个系统调用或函数,用于将 CPU 的控制权交还给调度器;当一个进程或任务调用yield时,它表明它已经完成了它当前的工作,或者暂时不需要 CPU 的执行时间,因此它主动放弃 CPU 的使用权,让调度器决定下一个要执行的进程或任务;

yield通常用于**任务间的协作**,例如在某个任务完成了一部分工作后,通过调用yield让出 CPU 给其他任务执行,以确保系统能够按时满足实时性要求;

# 任务切换

**FreeRTOS的核心是任务管理,任务管理的核心是任务切换,关于任务切换的主要知识点分为以下几个:**

1. PendSV 异常
2. PendSV 中断服务函数
3. FreeRTOS 确定下一个要运行的任务
4. PendSV 异常何时触发
5. FreeRTOS 时间片调度实验

### **PendSV是什么?**

PendSV(Pended Service Call,可挂起服务调用),是一个对 RTOS 非常重要的异常.

PendSV与SVC不同,PendSV的中断是**非实时的**,即PendSV的中断可以在**更高优先级**的中断中触发,但是在更高优先级中断**结束后**才执行;

**这一特性我们称之为可挂起**;利用这一特性,PendSV的中断服务函数就会在**其他所有中断处理完成后**才执行.任务切换时,就需要用到PendSV的这个特性;

### 为什么需要PendSV?

1. **任务切换的时机**:在RTOS中,任务切换可能需要在任何时刻发生,以响应外部事件或内部条件;PendSV提供了一种机制,**允许操作系统在任何时刻请求任务切换**;
2. **中断处理的优先级**:在RTOS中,中断请求(IRQ)通常具有比任务切换更高的优先级;如果任务切换尝试在中断处理期间发生,可能会导致中断被延迟,从而影响系统的实时性;
3. **上下文切换的安全性**:在处理中断时,如果尝试进行任务切换,可能会导致上下文不安全地切换,从而产生用法错误异常(Usage Fault);

### PendSV解决的问题

1. **中断请求的延迟**:PendSV通过延迟执行任务切换,直到所有中断请求都被处理完毕,从而避免了中断请求的延迟问题;
2. **上下文切换的安全性**:PendSV确保在没有未处理的中断请求时进行任务切换,从而避免了用法错误异常;
3. **性能影响**:直接通过检查中断状态寄存器(如xPSR或NVIC)来判断是否进行任务切换可能会影响系统性能;PendSV通过其设计避免了这种性能开销;

### PendSV的相关特性

1. **最低优先级**:PendSV的中断优先级被设置为最低,确保它在所有其他中断处理完毕后执行;
2. **挂起机制**:操作系统可以通过将PendSV设置为挂起状态来请求任务切换;
3. **任务切换执行**:PendSV的中断服务函数(ISR)中包含了实际的任务切换逻辑;
4. **与SysTick的关系**:虽然SysTick通常用于周期性地触发操作系统内核以进行任务调度,但PendSV提供了一种更为灵活的任务切换机制,特别是在需要立即响应某些事件时;
5. **抢占式调度**:PendSV支持抢占式任务调度,允许高优先级任务抢占低优先级任务的执行;

PendSV在RTOS的任务切换中,起着**至关重要**的作用,**FreeRTOS的任务切换就是在PendSV中完成的;**

**可以看出,FreeRTOS 在进行任务切换的时候,会将 CPU 的运行状态,在进行任务切换前,进行保存,保存到任务的任务栈中,然后从切换后运行任务的任务栈中恢复切换后运行任务在上一次被切换时保存的 CPU 信息.**

### 简化的解释

想象你正在做几项不同的工作(任务A,任务B等),每项工作都有自己的工具箱(任务栈).当你需要从一项工作切换到另一项工作时,你需要:

1. 把你当前使用的工具(CPU寄存器中的值)放回你的工具箱(任务栈).
2. 选择你下一个要使用的工具箱(通过任务控制块TCB选择下一个任务).
3. 把你自己移动到下一个工具箱的位置(更新PSP为下一个任务的栈顶指针).
4. 从新工具箱中取出你需要的工具(CPU从下一个任务的栈中恢复寄存器状态).

在这个过程中,只有一部分工具(R4-R11寄存器)需要你手动放回和取出,其他的由你的助手(硬件)自动帮你处理.这样,你就可以平滑地在不同的工作之间切换,而不会丢失任何进度.

### **PendSV执行过程**

在 PendSV 的中断服务函数中,调用了函数 `vTaskSwitchContext()`来确定下一个要运行的任务.

```c
/* 此全局变量用于在系统运行的任意时刻标记需要进行任务切换
 * 会在 SysTick 的中断服务函数中统一处理
 * 任务任务调度器没有运行,不允许任务切换,
 * 因此将 xYieldPending 设置为 pdTRUE
 * 那么系统会在 SysTick 的中断服务函数中持续发起任务切换
 * 直到任务调度器运行
 */
xYieldPending = pdTRUE;
```

函数 `vTaskSwitchContext()`调用了函数 `taskSELECT_HIGHEST_PRIORITY_TASK()`,来将 pxCurrentTCB 设置为指向优先级最高的就绪态任务.

### **PendSV异常何时触发与最终调用**

PendSV 异常用于进行任务切换,当需要进行任务切换的时候, FreeRTOS 就会触发 PendSV 异常,以进行任务切换.

阅读原代码中可以看到,这些后实际上最终都是调用了函数 `portYIELD()`

```c
#define portYIELD()											\
{ 															\
     /* 设置中断控制状态寄存器,以触发 PendSV 异常 */			 \
     portNVIC_INT_CTRL_REG = portNVIC_PENDSVSET_BIT; 		\
                                                            \
     __dsb( portSY_FULL_READ_WRITE ); 						\
     __isb( portSY_FULL_READ_WRITE ); 						\
}
```

上面代码中宏 `portNVIC_INT_CTRL_REG` 和宏 `portNVIC_PENDSVSET_BIT` 在 portmacro.h 文件中有定义,其实是对**中断控制状态寄存器**操作,具体的代码如下所示:

```c
#define portNVIC_INT_CTRL_REG ( *( ( volatile uint32_t * ) 0xe000ed04 ) )
#define portNVIC_PENDSVSET_BIT ( 1UL << 28UL )
```

# 内核控制函数

| 函数                           | 描述                       |
| ------------------------------ | -------------------------- |
| `taskYIELD() `                 | 请求切换任务               |
| `taskENTER_CRITICAL()`         | 在任务中进入临界区         |
| ` taskEXIT_CRITICAL() `        | 在任务中退出临界区         |
| `taskEXIT_CRITICAL_FROM_ISR()` | 在中断服务函数中退出临界区 |
| `taskDISABLE_INTERRUPTS()`     | 关闭受 FreeRTOS 管理的中断 |
| `vTaskSuspendAll() `           | 挂起任务调度器             |
| ...                            | ...                        |

# 其他任务API函数

个人认为对调试很有用的函数:

1. `eTaskGetState()`:此函数用于获取指定任务的状态

   - 需在 FreeRTOSConfig.h 文件中设置配置项 `INCLUDE_eTaskGetState` 为 1

   - 获取:任务状态值\任务运行状态(如下表)

     | 状态 | eTaskState(枚举)类型 |
     | :--: | :------------------: |
     | 运行 |       eRunning       |
     | 就绪 |        eReady        |
     | 阻塞 |       eBlocked       |
     | 挂起 |      eSuspended      |
     | 删除 |       eDeleted       |
     | 非法 |       eInvalid       |

2. `uxTaskGetSystemState()`:此函数用于获取任务状态信息

   - 需在 FreeRTOSConfig.h 文件中设置配置项` configUSE_TRACE_FACILITY` 为 1;
   - 获取:任务名\优先级\任务编号;

3. `vTaskGetInfo()`:此函数用于获取指定任务的信息

   - 需在 FreeRTOSConfig.h 文件中设置配置项 `configUSE_TRACE_FACILITY` 为 1;
   - 获取:任务名\任务编号任务当前优先级\任务基优先级\堆栈基地址\堆栈历史剩余;

4. `vTaskList()`:此函数用于以"表格"形式获取系统中任务的信息;

   - 需在 FreeRTOSConfig.h 文件中同时设置配置项 `configUSE_TRACE_FACILITY`和配置项 `configUSE_STATS_FORMATTING_FUNCTIONS` 为 1;

# 记一次奇怪的bug

##### 问题描述

在使用中正点原子的**任务运行时间统计**例程时发现,当把zet6内部sram的内存分配(正点自己)的改为FreeRTOS的`pvPortMalloc()`之后就会在用户函数未使用`vPortFree()`的情况下依然报错,错误位置在`vPortFree()`内部如下区域:

```c
    /* Check the block is actually allocated. */
    configASSERT( ( pxLink->xBlockSize & xBlockAllocatedBit ) != 0 );
    configASSERT( pxLink->pxNextFreeBlock == NULL );
```

##### 问题解决

最终发现是因为使用`vTaskGetRunTimeStats()`时,打印输出的字符串**超出**了`pvPortMalloc()`申请的空间导致的;

打印的字符串占123-126个字符,却只申请了100个字节的长度.导致**实际使用了未在系统内登记申请**的23-26个字符;

在调用`vTaskGetRunTimeStats()`时,内部会先为`pxTaskStatusArray`申请空间,之后再通过sprintf格式化进字符串内;申请的时候系统把未登记却已占用的23-26个字节的区域重复申请,但是并没有返回申请错误,而是在释放的时候报错;

# 时间管理

1. 使用函数`vTaskDelay()`进行任务延时时，被延时的任务为调用该函数的任务，及调用该函数时，系统中正在运行的任务，此函数无法指定将其他任务进行任务延时。
2. 函数`vTaskDelay()`传入的参数`xTicksToDelay`是任务被延时的具体延时时间，时间的单位为**系统时钟节拍**。
3. 在使用此函数进行任务延时时，如果传入的参数为 0，那表明不进行任务延时，而是**强制进行一次任务切换**。
4. 函数`vTaskDelayUntil()`用于以一个绝对的时间阻塞任务，适用于需要按照一定频率运行的任务。函数`xTaskDelayUntil()`对任务进行延时的操作，是相对于任务上一次阻塞超时的时间，而不是相对于系统当前的时钟节拍计数器的值，因此，函数能够更准确地以一定的频率进行任务延时，更加适用于需要按照一定频率运行的任务。

# 队列

队列是用来在任务与任务或任务于中断之间传递消息的一种机制，队列也叫做消息队列。

队列是一种任务到任务、任务到中断、中断到任务数据交流的一种机制。

```c
(读取成功/读取失败)xQueueReceive(待读取的队列, 信息读取缓冲区, 阻塞超时时间) //从队列头部读取消息，并删除消息
(读取成功/读取失败)xQueuePeek(待读取的队列, 信息读取缓冲区, 阻塞超时时间) //从队列头部读取消息
(读取成功/读取失败)xQueueReceiveFromISR(待读取的队列, 信息读取缓冲区, 需要任务切换标记) //在中断中从队列头部读取消息，并删除消息
(读取成功/读取失败)xQueuePeekFromISR(待读取的队列, 信息读取缓冲区) //在中断中从队列头部读取消息
```

##### 队列锁

在队列被上锁后，可以往队列中写入消息和读取消息，但是**队列消息**的读取和写入不会影响到**队列**读取和写入阻塞任务列表中的任务阻塞，队列的写入和读取阻塞任务列表会在队列解锁后，统一处理。

即使队列上锁，任务仍然可以读取和写入队列中的消息，但这些操作不会影响那些因为队列操作而被阻塞的任务。阻塞任务列表是指那些因为队列满了而不能写入消息的任务，或者因为队列空了而不能读取消息的任务。

# 信号量

信号量是操作系统中重要的一部分，信号量是**任务间同步**的一种机制，信号量可以用在**多任务访问同一资源**时的资源管理。FreeRTOS 提供了多种信号量，按信号量的功能可分为**二值**信号量、**计数**型信号量、**互斥**信号量和**递归互斥**信号量，不同类型的信号量有其不同的应用场景;

##### 同步

“同步”指的是任务间的同步，即信号量可以使得一个任务等待另一个任务完成某件事情后，才继续执行；

##### 有序访问

而“有序访问”指的是对被多任务或中断访问的共享资源（如全局变量）的管理，当一个任务在访问（读取或写入）一个共享资源时，信号量可以防止其他任务或中断在这期间访问（读取或写入）这个共享资源;
