# ---------Author:West-----------


products_list = [
    ("IPHONE", 5000),
    ("MAC PRO",12000),
    ("BIKE", 800),
    ("WATCH", 1000),
    ("STARBUCKS", 31)
]

user_choose_list = []

salary = input("Please input you salary:")

# 判断输入是不是整数
if salary.isdigit():
    salary = int(salary)
    while True:
        # 打印商品编号和商品信息
        for index, item in enumerate(products_list):
            print(index, item)
        # 用户输入商品编号
        products_id = input("Please choose products_id:")
        # 判断商品编号是不是整数
        if products_id.isdigit():
            products_id = int(products_id)
            # 判断输入的整数编号是否在规定范围内
            if 0 <= products_id < len(products_list):
                p_item = products_list[products_id]
                # 判断工资数额够不够买商品编号对应的商品
                if p_item[1] <= salary:
                    # 将买入的商品加入到新的列表中，工资减掉买到的商品价格，并打印购买信息
                    user_choose_list.append(p_item)
                    salary = salary-p_item[1]
                    print("Added %s in your shopping cart,your current balance is %s" % (p_item, salary))
                # 不够买对应编号的商品就打印提示
                else:
                    print("you have salary:", salary)
            else:
                print("Product code[%s] is not exist!" % products_id)
        elif products_id == "q":
            print("------shopping_list------")
            for p in user_choose_list:
                print(p)
            print("Your current balance:", salary)
            exit()
        else:
            print("Invalid input")

else:
    print("Invalid input")





