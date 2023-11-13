import random

ls = [random.randint(1, 100) for _ in range(20)]
print(ls)

new_ls = []  # 用于存储不是3的倍数的元素
for num in ls:
    if num % 3 != 0:
        new_ls.append(num)

# 降序排列
new_ls.sort(reverse=True)

print(new_ls)
