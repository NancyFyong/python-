pw = input("请输入密码：")
pws = [0, 0, 0, 0]  # 列表元素分别表示密码长度，包含了密码中含有数字、大写字母、小写字母的情况
strength = {5: '强', 4: '中', 3: '中等偏弱', 2: '弱', 1: '差'}

if 6 < len(pw) <= 8:
    pws[0] = 1
elif len(pw) > 8:
    pws[0] = 2

for x in pw:
    if x.isdigit():
        pws[1] = 1
    elif x.isupper():
        pws[2] = 1
    elif x.islower():
        pws[3] = 1

n = pws.count(1)
print('密码的强度为', strength[n])
