# 类变量的用途？ 大家公用的属性，节省开销
class Person:
    cn = "中国"
    def _init_(self, name, age,addr):
        self.name =name
#       self.cn = cn
p1 = Person(name,age,addr)


# 析构函数

# 在势力释放或销毁的时候自动执行的，通常用于做一些收尾工作，如关闭一些数据库链接

# 私有属性私有方法加双下划线



# 封装

# 继承
# 经典类和新式类的多继承
#     python2对经典类和新式类来说，属性的查找顺序是不同的
#     经典类：从左到右，深度优先
#     新式类：广度优先
#     python3 经典类和新式类都是广度优先
# 深度优先没有广度优先高
# 多态