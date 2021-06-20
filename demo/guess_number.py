print("今日有物不知其数, 五五数之剩三, 三三数之剩二, 四四数之剩一, 问几何？")
a = False
while not a:
    num = int(input("输入这个数字："))
    if num % 5 == 3 and num % 3 == 2 and num % 4 == 1:
        print("答对了！")
        a = True
    else:
        print("猜错了")

