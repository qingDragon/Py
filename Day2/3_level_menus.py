# ------ Author:West--------
data = {
    "北京": {
        "昌平": {
            "沙河": ["老男孩","北航"],
            "天通苑": {},
            "回龙观": {}
        },
        "朝阳": {
        },
        "海淀": {
            "五道口": ["搜狐","google","网易"]
            ,
            "中关村":["爱奇艺","汽车之家","youku"]
            ,
            "上地": {
                "百度": {}
            }
        }
    },
    "上海": {
        "闵行": {
            "人民广场":{
                "炸鸡店":{}
            }
        },
        "闸北": {},
        "浦东": {}
    },
    "江苏": {
    }
}
exit_msg = False
while not exit_msg:
    for item in data:
        print(item)
    choice = input("第一次选择：")
    if choice in data:
        while not exit_msg:
            for item in data[choice]:
                print(item)
            choice2 = input("第二次选择：")
            if choice2 in data[choice]:
                while not exit_msg:
                    for item in data[choice][choice2]:
                        print(item)
                    choice3 = input("第三次选择：")
                    if choice3 in data[choice][choice2]:
                        for item in data[choice][choice2][choice3]:
                            print(item)
                        choice4 = input("最后一层，按b返回上层")
                        if choice4 == "b":
                            pass
                        elif choice4 == "q":
                            exit_msg = True
                    if choice3 == "b":
                        break
                    elif choice3 == "q":
                        exit_msg = True

            if choice2 == "b":
                break
            elif choice2 == "q":
                exit_msg = True



