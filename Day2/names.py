# Author:s0cket

# 列表

names = ["west", "shuoconan", "west", "guyang"]
names.append("leihaidong")
# 插入指定位置
names.insert(1,"huangtong")
names[2] = "rendengbao"  # 替换
# 删除
# names.remove("guyang")
del names[1]
names.pop()

print(names)
print(names[1])
print(names[0:2])  # 切片
print(names[-1])
print(names[-2:])


print(names.index("west"))

print(names.count("west"))
# names.clear()

names.reverse()
print(names)

names.sort()
print(names)
# names2 = [1, 2, 3, 4]
# names.extend(names2)
# print(names,names2)

# copy 和 deepcopy
names2 = names.copy()
print(names)
print(names2)
names[2] = "WEST"
print(names)
print(names2)


for i in names:
    print(i)

print(names[0:-1:2])
print(names[::2])