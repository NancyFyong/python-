xydm = {}
x = input("请输入学院代码：")

while x != "-1":
    y = input("请输入学院名称：")
    xydm[x] = y
    x = input("请输入学院代码：")

print('创建的字典内容是：')
for key, value in xydm.items():
    print(f"{key}: {value}")
