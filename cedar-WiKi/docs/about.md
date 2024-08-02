# C++ 算法基础

## 常用库
1. iostream
cin cout
2. cstio
scanf printf getchar等输入输出函数
注: printf打印字符串
eg. printf("%s", a.c_str());
3. cstring C风格的字符数组操作
strlen、strcpy(destination,source)、strcmp(s1,s2) 
4. string

getline(cin, str) 

从输入流中获取一整行字符串 遇到换行符停止 可以输入空格

长度 str.length() 或 str.size()

检空 str.empty()

清空 str.clear()

5. algorithm
sort(begin, end, cmp)

## STL标准模板库
1. 向量vector 变长数组

需要引入vetcor头文件

初始化 vector<int> a({1, 2 ,3})

获取大小a.size()

检查为空a.empty()

清空a.clear()

a.front() <=> a[0]

a.back() <=> a[a.size-1]

添加a.push_back(x)

删除a.pop_back()

---
2. 栈stack

需要引入stack头文件

定义stack<int> s;

压入 s.push(x)

弹出 s.pop()

访问栈顶元素 s.top()

---
3. 队列queue

头文件queue

定义 queue<int> a;

插队尾 a.push(x)

弹队头 a.pop()

访问队头元素 a.front()

访问队尾元素 a.back()

检查为空 a.empty()

4. 双端队列 deque

头文件 deque

deque<int> a;

两端插入、删除

push_back() push_front()

pop_back() pop_front()

5. set

元素不重复 set<int> a;

插入a.insert(x)

删除a.erase(x)

迭代器（STL的“指针”）

set<int> ::iterator it = a.begin();

支持it++ , it--;

a.find() 返回迭代器

判断元素是否存在:

if(a.find(x) == a.end())

a.count(x) 统计个数

---
6. map

key-value映射

map<string,int> a;

a["zxs"] = 1;
a.insert({"z", 2});

## 位运算

与& 或| 非! 异或^

<<k 左移k位

1. 取第k位

a = 13 <=> 1101

(a>>2 & 1) 得 1

2. 取最低位 lowbit(a)

a & (~a + 1) <=> a & -a

a与a的补码



