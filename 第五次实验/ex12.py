import random

# 可选的字符集
characters = "BCDEFGHJKLMNPQRSTUVWXYZ2346789"

# 生成一个序列号
def generate_serial():
    serial = ""
    for _ in range(5):
        group = "".join(random.choice(characters) for _ in range(5))
        serial += group + "-"
    return serial.rstrip("-")

# 生成一个产品序列号
product_serial = generate_serial()
print("生成的产品序列号:", product_serial)
