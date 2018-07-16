# Author:s0cket

import copy

person = ["name",["saving",100]]

# p1 = copy.copy(person)
# p2 = person[:]
# p3 = list(person)

p1 = person[:]
p2 = person[:]

p1[0] = "yz"
p2[0] = "lsx"

print(p1)
print(p2)

p1[1][1] = 50

print(p1)
print(p2)
# 浅copy的一个作用是创建关联信息（夫妻银行存钱）