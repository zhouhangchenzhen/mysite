# # http://nbviewer.jupyter.org/github/LearnXu/pydata-notebook/tree/master/
#
# # https://github.com/wesm/pydata-book
# #
# # http://www.runoob.com/python/python-object.html
# # a=5;b=6;c=7
# # print(a,b,c)
# # ##所有的事物都是对象（object）
# # ##python中，number string ,data structure,function,class,module 都有自己的box
# #
# # ##调用函数和对象的方法
# # ##result=f(x,y,z)
# # ##动态参考，强类型，object refrence 是没有自带类型，但是可以通过type来查看类型：
# # a=5
# # print(type(a))
# #
# # ##python 是强类型，每一个object都是明确的类型，所以 "5"+5，不能成了，二VB回吧'5'转化为整数，2⃣而 Java会把5转为字符串
# # ##但是int 和float  会隐性转换
# # a=4.5
# # boy=2
# # c="5"
# # print("a is {0},boy is {1},c is {2}".format(type(a),type(boy),type(c)))
# #
# # print(a/b)
# #
# # ##由于object类型很重要，因此可以用isinstance函数来观察object的类型
# # print(isinstance(a,int))
# # ##判定美国object是否属于某个类型中的一个
# # print(isinstance(a,(int,float)))
# # ##属性（attributes）指在当前这个object中，还有其他的python object.方法（method）指当前object自带的一些函数，这些函数可防伪object内部数据
# #
# # a="foo"
# # print(a.casefold())
#
# ##python元组
# # tuple=('runnoob',786,2.23,'john',70.2)
# # tinytuple=(123,'john')
# # print (tuple )#输出完整元组
# # print(tuple[0])#输出元组的第一个元素
# # print(tuple[1:3])#输出第二个至第三个元素
# # print(tuple[2:])#输出从第三个到最后一个元素
# # print(tuple+tinytuple) #打印组合的元组
# #print(tuple(2)=100) 这个程序是非法到
# #python dictionar #dictionary 是除了list 之外python最灵活的内置数据结构类型。list 是有序的对象集合 ；dictionary 是无序的对象集合
# # dict={}
# # dict['one']='this is one'
# # dict[2]='this is two'
# # tinydict={'name':'john','code':6347,'dept':'sexl'}
# # print(dict['one'])# 输出为'one'的数值
# # print(dict[2]) #输出键为2的值
# # print(tinydict)#输出完整的字典
# # print(dict)#输出完整的字典
# # print(tinydict.keys())#输出所有键
# # print(tinydict.values())#输出所有值
#
# ##python 数据转换
# # print(int(8.0))# 将x转换为一个整数
# # print(float(8))#转为一个浮点数
# # print(complex(8.8))#创建一个浮点数
# # print(str(8.8))#转换为字符串
# # print(repr(8.8))#转换为表达式字符串
# # s=["runoob",786,2.23,'john',70.2]
# # s1=tuple(s)#将序列转为一个元组
# # print(type(s1))
# # s2=list(s1)
# # s1[0]=100
# # print(list(s2))
# # s[0]=100
# # print(s2)
# # print(type(s2))
# # template='{0:0.2f} {1:s} are worth us${2:d}'
# # print(template.format(4.56678,'zhou hang',10)) #{0:.2f}第一参数为float类型，去小数点后两位；{1:s}把第二个参数变为string类型
# #                                                 #{2:d}把第三个参数变为一个精确的整数
# # # bytes and unicode
# # val="espanol"
# # print(val)
# # ##utf-8 (8-bit unicode transformation format )是一种争对unicode的可变长度字符编码 ，又称为万国码。
# # val_utf8=val.encode('utf-8')
# # print(val_utf8)
# # type(val_utf8)
# # val_utf8.decode('utf-8')
# # val.encode('latin1')
# # ##type casting
# # a='3.14159'
# # fval=float(s)
# # type(fval)
# # int(fval)
# # bool(fval)
# # bool(0)
# ##time and date
# # from datetime import datetime,date,time
# # dt=datetime(2011,10,29,20,30,21)
# # print(dt.day)
# # print(dt.minute)
# # print(dt.date())
# # print(dt.time())
# # print(dt.strftime)
#
# # 控制流 control flow  if elif and else for loops while loops
# # number=23
# # guess=int(input('输入一个整数：'))
# # if guess==number:
# #     print("恭喜你猜对了")
# # elif guess<number:
# #     print("猜小了")
# # else:
# #     print("猜大了")
# #
# # x=int(input('输入一个数：'))
# # if x<0:
# #     print('负数')
# # elif x==0:
# #     pass
# # else:
# #     print('正数')
# ##range函数返回一个能阐述序列的迭代器
# # print(range(10))
# # print(list(range(10)))
# # print(list(range(0,20,2)))
# # print(list(range(5,0,-1)))
# ##range 一个常用法是通过index迭代程序
# # seq=[1,2,3,4]
# # print(len(seq))
# # print(range(len(seq)))
# # print(list(range(len(seq))))
# # for i in range(len(seq)):
# #     val=seq[i]
# #     print(i)
# #     print(val)
# ##ternary expressions
# # value=true-expr if condition else false-expr
#
#
# # x=5
# # print('non-negative') if x>=0 else print('negative')
#
#
# ##if 的基本用法
# # falg=False
# # name="周航"
# # if name=="周航":
# #     falg=True
# #     print("欢迎老婆")
# # else:
# #     print(name)
#
# ##判断条件为多个数值时可以使用下面的形式
# # num=int(input("输入一个你想的整数"))
# # if num==3:
# #     print("老板你的数等于3")
# # elif num==2:
# #     print("老婆你的数是2")
# # elif num==1:
# #     print("老婆你的数等于2")
# # elif num<0:
# #     print('老婆你的数小于0')
# # else:
# #     print('你猜测不对')
#
#
# ##python多个条件语句，如果判断多个条件同时可以使用and;判断多个条件有一个成了时使用or
# # num=int(input("输入一个数值："))
# # if num>=0 and num<=10:
# #     print('you number is between 0 and 10')
# # if num<0 or num>100:
# #     print('you number is less 0 or bigger than 100')
#
# # ##简单语句组，可以在同一行的位置上使用if条件判断语句
# # var=90
# # if(var==100):print('变量var的值为100')
# # print('再见')
# #
# # var=90
# # if(var==100):
# #     print('变量var的值为100')
# # print('再见')
#
# # python 复合布尔表达式计算采用短路规则，即如果通过前面的部分已经计
# # 算出整个表达式的值，则后面的部分不再计算。如下面的代码将正常执行不会报除零错误：
# # a=0
# # b=1
# # if (a>0) and (b/a>2):
# #     print('yes')
# # else:
# #     print('no')
#
# # if (a>0) or (b/a>2):
# #     print('yes')
# # else:
# #     print('no')
#
#
# ##python循环语句
# ##python提供了for循环和while循环
# ##while loop ,在给定判定条件为true时执行loop，否则退出loop
# ##for loop ,重复执行语句
# ##嵌套循环，在while循环体中嵌套for loop
# ##循环控制语句，break 在语句执行过程中终止循环，并跳出整个循环
# ##continue，在语句块终止当前循环，跳出改循环，执行下一次循环
# ##pass 是空语句，保持程序完整性
# # numbers=[12,37,5,42,8,3]
# # even=[]
# # odd=[]
# # while len(numbers)>0:
# #     nb=numbers.pop()   ##pop() 方法用于删除并返回数组的最后一个元素
# #     if(nb%2==0):
# #         even.append(nb)
# #     else:
# #         odd.append(nb)
# # print(even)
# # print(odd)
#
# # count=0
# # while(count<9):
# #     print('现在count是：',count)
# #     count=count+1
# #     print('the count is :',count)
# # print('再见')
# ##continue 和break 用法
#
# ##continue 跳过循环
# # i=1
# # while i<10:
# #     i+=1
# #     if i%2>0:
# #         continue
# #     print(i)
# #
# # i=1
# # while i<10:
# #     i+=1
# #     if i%2>0:
# #
# #         print(i)
# ##break是退出整个循环
# # i=1
# # while i<10:
# #     i+=1
#
# #     if i%2>0:
# #         break
# #     print(i)
# # ##无限循环语句
# # var=1
# # while var==1:
# #     num=float(input("输入一个数值："))
# #     print('你输入的数字为：',num)
# # print('再见')
#
# ##循环使用else 语句
# # count=0
# # while count<5:
# #     print(count,'is less than 5')
# #     count=count+1
# # else:
# #     print(count,'is not less than 5')
#
# # import random
# # s=int(random.uniform(1,10))
#
# # m=int(input('输入整数：'))
# # count=1
# # while m!=s:
# #     count=count+1
# #     if m>s:
# #         print('老婆你的数猜大了')
# #         m=int(input('老婆从新输入整数：'))
# #     if m<s:
# #         print('老婆你猜小了')
# #         m=int(input('老婆从新输入整数：'))
# #     if m==s:
# #         print('老婆你太棒了,你猜了',count,'次就猜对了')
# #         break
#
# # ###改进版本的剪刀石头布
# # import random
# # while 1:
# #     s1=input("老婆输入你的拳头：")
# #     s2 = int(random.randint(1, 3))
# #     print(s2)
# #     print(s1)
# #     if s1=="剪刀":
# #         nb=1
# #     elif s1=="石头":
# #         nb=2
# #     elif s1=="布":
# #         nb=3
# #     print(nb)
# #
# #     if nb==s2:
# #         print("老婆我们平了")
# #         s1=input("老婆再来输入你的拳头：")
# #     if nb==1 and s2==2:
# #         print("老婆的剪刀碰到我的石头了，你输了")
# #         break
# #     elif nb==1 and s2==3:
# #         print('老婆你的剪刀太厉害了剪了我的小弟第，你赢了')
# #         break
# #     elif nb==2 and s2==1:
# #         print("老婆你石头太厉害了砸了我的剪刀，你赢了")
# #         break
# #     elif nb==2 and s2==3:
# #         print('老婆你的石头不行被我的布包了，你输了')
# #         break
# #     elif nb==3 and s2==1:
# #         print('老婆你的布不行被我剪刀剪了，你输了')
# #     elif nb==3 and s2==2:
# #         print('老婆你的布太厉害了，把我石头包了，你赢了')
# #         break
#
# ## for iterating_var in sequence statements
# ##
# # for letter in 'python':
# #     print('the current letter:',letter)
#
#
# ##
# import  ray.dataframe as pd
#
# ##
# words = ['cat', 'window', 'defenestrate']
# print(len(words))
#
# for w in words:
#     print(w,len(w))
#
# for index in range(len(words)):
#     print(words[index])
#
# for w in words[:]:
#     if len(w)>6:
#         words.insert(1,w)
# print(words)
# ##enumerate
# seasons=['spring','summer','fall','winter']
# print(list(enumerate(seasons)))
#


from __future__ import unicode_literals
from pyecharts import Bar
from pyecharts import online

online() # 使用远程 jshost
bar = Bar("我的第一个图表", "这里是副标题")
bar.use_theme('dark')
bar.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90])
bar.render()
bar