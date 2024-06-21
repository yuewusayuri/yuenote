# QT编写步骤(frame)

README：

学习QT早期乱写的，表达仅为个人理解，可能一个月后自己看就会忍不住笑出声（

### 1. 在widget.h内，public部分创建所需要的按键

例如：

```c++
public:
    Widget(QWidget *parent = nullptr);
    ~Widget();

    /* 0-9数字按键 */
    QPushButton *bt_num[10];
    /* 删除按键 */
    QPushButton *bt_del;
    /* 加减乘除按键 */
    QPushButton *bt_add, *bt_sub, *bt_mul, *bt_div, *bt_calc;
    /* 显示框 */
    QLineEdit   *le_frame;

    QString op;
    int num_1;
    int num_2;
    int sum;
```

在这里我们把两个操作数与之和都定义为int变量，同时创建计算、删除、0-9数字、加减乘除动作按键与显示框

### 2. 编写槽函数

按下按键的动作与数据的处理强相关，故需要声明槽函数传递信号量

```C++
public slots:
    void chop_onedata();/* 尾部字符删除 */
    void num_bt_pushed();/* 捕获数字按键 */
    void opt_bt_pushed();/* 捕获运算符 */
    void calc_bt_pushed();/* 捕获计算键 */
```

### 3. 在widge.cpp内构造所需要控件(并未真正显示)

```c++
le_frame = new QLineEdit; /* 构造控件 */
le_frame->setAlignment(Qt::AlignRight);/* 右对齐 */
bt_del = new QPushButton("<"); /* 删除键 */

for(int i=0; i<10; i++){
  bt_num[i] = new QPushButton(QString::number(i));
}

bt_add  = new QPushButton("+");
bt_sub  = new QPushButton("-");
bt_mul  = new QPushButton("*");
bt_div  = new QPushButton("/");
bt_calc = new QPushButton("=");
bt_calc->setMinimumHeight(63);/* 给“等于”按键设定最小高度，布局用 */
```

相当于对.h文件内定义的变量赋值，此处重点：

```c++
le_frame->setAlignment(Qt::AlignRight);/* 右对齐 */
/* 貌似最后一个词提示很模糊 */

for(int i=0; i<10; i++){
  bt_num[i] = new QPushButton(QString::number(i));
}
/* 
 * 巧妙利用循环构造多个有规律的按键
 * 要将循环中的i转化为字符串要使用QString::number(i)，注意有两个:
 */
bt_add  = new QPushButton("+");
/*
 * QPushButton为创建按键，括号里写"要显示的符号"
 */

bt_calc->setMinimumHeight(63);
/* 给“等于”按键设定最小高度，布局用 */
```

### 4. 布局按键(真正显示出来)

```C++
/* 布局 */
QHBoxLayout *hbox = new QHBoxLayout;
hbox->addWidget(le_frame);
hbox->addWidget(bt_del);
/* 创建hbox，加入显示框和删除键 */

QGridLayout *gbox = new QGridLayout;
int j = 0;
for(int i=1; i<10; i++){
  gbox->addWidget(bt_num[i], j, (i-1)%3, 1, 1);
  if(i%3 == 0)
    j++;
}
/* 
 * 创建gbox，网格式布局
 * 使用循环，每行四个，到尾部自动换行
 * 创建0-9数字键
 */
gbox->addWidget(bt_add, 0, 3, 1, 1);
gbox->addWidget(bt_sub, 1, 3, 1, 1);
gbox->addWidget(bt_mul, 3, 0, 1, 1);
gbox->addWidget(bt_div, 3, 2, 1, 1);
/* 创建加减乘除按键 */
gbox->addWidget(bt_num[0], 3, 1, 1, 1);
gbox->addWidget(bt_calc, 2, 3, 2, 1);
/* 创建0按键和计算键 */
QVBoxLayout *mainbox = new QVBoxLayout;
mainbox->addLayout(hbox);
mainbox->addLayout(gbox);
setLayout(mainbox);
/* 创建总布局，加入hbox和gbox的布局 */

```

### 5. 信号连接

主函数：

```c++
/* 信号与槽的连接 */
connect(bt_del, SIGNAL(clicked(bool)), this, SLOT(chop_onedata()));

for(int i=0; i<10; i++)
	connect(bt_num[i], SIGNAL(clicked(bool)), this, SLOT(num_bt_pushed()));
/* 循环构造0-9数字 */
connect(bt_add  , SIGNAL(clicked(bool)), this, SLOT(opt_bt_pushed()));
connect(bt_sub  , SIGNAL(clicked(bool)), this, SLOT(opt_bt_pushed()));
connect(bt_mul  , SIGNAL(clicked(bool)), this, SLOT(opt_bt_pushed()));
connect(bt_div  , SIGNAL(clicked(bool)), this, SLOT(opt_bt_pushed()));
connect(bt_calc , SIGNAL(clicked(bool)), this, SLOT(calc_bt_pushed()));

/* 与步骤2中所创建的槽函数相对应 */
```

- 当信号被发射时,QT代码将回调与其相连接的槽函数
- 信号的声明不在cpp文件中,而在头文件中

编写槽函数之前，要规划好对应功能的分类，多个相同功能的按键可以用循环构造，快速而简化代码量。

例如本工程的计算器：

- 0-9数字键，需要提取的数字是num1或num2
- 加减乘除运算键，需要根据按键对应的符号改变运算(例如用switch函数)
- 退格键，删除最后输入的一个字母
- 等于键，实际进行运算的按键

槽函数：

```c++
void Widget::num_bt_pushed(){
    /* 提取按键 */
    QPushButton *btx = static_cast<QPushButton *>(sender());
    /* 提取文字 */
    QString c = btx->text();
    /* 追加显示在编辑框 */
    QString data = le_frame->text();
    le_frame->setText(data + c);
}
```

循环10次对0-9数字按键的文字提取，并且显示
此处的[data + c]为字符串自动移位，而不是运算符号「+」

```c++
/* 捕获运算符 */
void Widget::opt_bt_pushed(){
    QPushButton *btx = static_cast<QPushButton *>(sender());
    op = btx->text();

    num_1 = le_frame->text().toInt(); /* 熟练掌握此用法，文字转数字 */
    le_frame->clear();
}
```

对**op**赋值为按下的按键中**显示的符号**
同时将显示框中的数字赋值给number1，并且清空显示

```c++
/* 捕获计算键 */
void Widget::calc_bt_pushed(){

    num_2 = le_frame->text().toInt();

    switch (op.toStdString().c_str()[0]) {
        case '+' : sum = num_1 + num_2; break;
        case '-' : sum = num_1 - num_2; break;
        case '*' : sum = num_1 * num_2; break;
        case '/' : sum = num_1 / num_2; break;
    }

    le_frame->setText(QString::number(sum));
}
```

按下计算键，捕获当前在**编辑框中**的number2，并且把op通过函数转化为对应的运算操作
使用le_frame->setText()函数显示出来

```c++
/* 退格 */
void Widget::chop_onedata(){
    /* 提取文字 */
    QString data = le_frame->text();
    /* 将尾部删除 */
    data.chop(1);
    /* 放回去 */
    le_frame->setText(data);
}
```

可以看出，Qt采用信号和槽实现对象部件之间的通信。信号与槽点连接，当信号被发射时，QT代码将回调与其相连接的槽函数

