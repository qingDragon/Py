

money = int(input("you have the money:"))


shop = [1,'IPHONE',5000, 2,"STARBUCKS-LATTE",31, 3,"MACPRO",12000, 4,"BICYCLE",1000]
shop2= []

print(shop)
while money >= 31:
    number = int(input(">>>"))
    print(shop[shop.index(number)+2])

    if money < shop[shop.index(number)+2]:
        print("you don't have enough money")
        break
    else:
        money = money-shop[shop.index(number)+2]
        print("you salary is :", money)
        shop2.append(shop[shop.index(number)+1])
        shop2.append(shop[shop.index(number)+2])
        print("you buy:", shop2)

else:
    print("you cannot buy anything")