import matplotlib.pyplot as plt

# 支持中文显示

# plt.rcParams["font.sans-serif"] = ["SimHei"]

# x,y数据

x_data = [1, 2, 3, 4, 5]
y_data = [20, 30, 20, 25, 28]

plt.plot(x_data, y_data)

plt.title("简单的折线图")
plt.xlabel("x")
plt.ylabel("y")

plt.show()
