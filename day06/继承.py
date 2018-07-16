


#class People:
class People(object):#新式类写法

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def eat(self):
        print("%s is eating..." % self.name)

    def talk(self):
        print("%s is talking..." % self.name)

    def sleep(self):
       print("%s is sleeping..." % self.name)

class Relation(object):
    def make_friends(self,obj):
        print("%s is making friends with %s" % (self.name ,obj.name))

class Man(People,Relation):

    def __init__(self,name,age,money):
        super(Man,self).__init__(name,age) #(新式类写法)People.__init__(self,name,age)
        self.money = money
        print("%s 一出生就有 %s money" % (self.name,self.money))

    def piao(self):
        print("%s is piaoing...20s...done." % self.name)
    def sleep(self):
        People.sleep(self)
        print("man is sleeping")

m1 = Man("yz",22,160000)
#m1.sleep()

class Woman(People,Relation):
    def get_birth(self):
        print("%s is born a baby..." % self.name)

w1 = Woman("lsx", 22)
#w1.get_birth()
m1.make_friends(w1)