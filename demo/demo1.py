# q = float(input("请输入你要转换的华氏度："))
# c = (q - 32) / 1.8
# print("%.1f华氏度 = %.2f摄氏度" % (q, c))
#
#
# year = int(input("请输入你要判断的年份："))
#
#
# def is_leap_year(y):
#     if y % 400 == 0 or y % 4 == 0 and y % 100 != 0:
#         print("%d是闰年" % y)
#     else:
#         print("%d是平年" % y)
#
#
# is_leap_year(year)



#
# sum = 0
# for i in range(1, 101):
#     sum += i
# print(sum)
#
#
# q = int(input("请输入你要判断的数字（自然数）："))
# if q > 1:
#     is_prime = True
#     for i in range(2, q):
#         if q % i == 0:
#             is_prime = False
#             print("它不是质数")
#             break
#     if is_prime:
#         print("它是质数")
# else:
#     print("它不是质数")
#
#
# def is_prime(num):
#     q = num
#     if q > 1:
#         isPrime = True
#         for i in range(2, q):
#             if q % i == 0:
#                 isPrime = False
#                 break
#         if isPrime:
#             print("%d是质数" % q)
#
#
# for i in range(1, 1001):
#     is_prime(i)
#
#
# from turtle import *
# register_shape("finder.gif")
# shape = Turtle()
# shape.shape("finder.gif")
# shape.circle(200)
# mainloop()
#
#
# a = 1
# b = 1
# c = 0
#
#
# def fib():
#     global a
#     global b
#     global c
#     for i in range(18):
#         c = a + b
#         a = b
#         b = c
#
# fib()
# print(c)
#
#
# num = 0
#
# for i in range(1, 21):
#     num += i * 2 / i
#
# print(num)


# a = int(input("请输入三角形的第一条边："))
# b = int(input("请输入三角形的第二条边："))
# c = int(input("请输入三角形的第三条边："))
# if a + b > c and a + c > b and c + b > a:
#     print("它可以组成三角形")
# else:
#     print("不能组成三角形")

# a = int(input("请输入三角形的第一条边："))
# b = int(input("请输入三角形的第二条边："))
# c = int(input("请输入三角形的第三条边："))
# l = [a, b, c]
# MAX = max(l)
# l.remove(MAX)
# # if l[0] + l[1] > MAX:;
# if sum(l) > MAX:
#     print("它可以组成三角形")
# else:
#     print("不能组成三角形")

# # 寻找水仙花数
# for i in range(1000, 10000):
#     h = i // 100  # 百位
#     o = i % 100 // 10  # 十位
#     j = i % 10  # 个位
#     if h ** 3 + o ** 3 + j ** 3 == i:
#         print(i)


# while True:
#     try:
#         int(input("请输入一个数字："))
#         break
#     except ValueError:
#         print("哦，这不是，再试一次。")

# 九九乘法表
# print("九九乘法表")
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print("%dx%d=%d" % (j, i, i * j), end='\t')
#     print()

# for i in range(1, 6):
#     print(i * "*")

# for i in range(1, 6):
#     print((5 - i) * " " + i * "*")

# for i in range(1, 6):
#     print((5 - i) * " " + (i * 2 - 1) * "*" + (5 - i) * " ")

# num = {"a": 1, "b": 2, "c": 3}
# for i in num:
#     print(num[i])

# l = ["balabala", " bilibili", "hayahaya", "banabana"]
# for index, item in enumerate(l):
#     if index % 2 == 0:
#         print(item, end=" ")
#     else:
#         print(item + "\n")


a = 1
b = 2


def fu():
    print(a, b)
    c = a + b
    # a = b
    # b = c
    return c
print(fu())
