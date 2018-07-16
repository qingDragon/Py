# Author:s0cket


name = input("name:")
age = int(input("age:"))#input输入默认字符串类型，需要强制转换
job = input("job:")
salary = input("salary:")

# name = input("name:")
# age = input("age:")
# job = input("job:")
# salary = input("salary:")

# 第一种方式
# info = '''
# ------ info of '''+name+'''------
# Name:'''+name + '''
# Age:''' + age + '''
# Job:''' + job + '''
# Salary:'''+salary

# 第二种方式
info2 = '''
------ info of {_name} ------
Name:{_name}
Age:{_age}
Job:{_job}
Salary:{_salary}
'''.format(_name=name,
           _age=age,
           _job=job,
           _salary=salary)

# 第三种方式
info3 = '''
------ info of {0} ------
Name:{0}
Age:{1}
Job:{2}
Salary:{3}
'''.format(name, age, job, salary)


info4 = '''
------ info of %s ------
Name:%s
Age:%d
Job:%s
Salary:%s
''' % (name, name, age, job, salary)

print(info4)
