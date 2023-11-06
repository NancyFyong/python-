import random

# 从changsha.txt文件中读取已被占用的车牌号码
used_plates = set()
with open("changsha.txt", "r",encoding='utf-8') as file:
    for line in file:
        plate = line.strip()
        used_plates.add(plate)

# 生成20个车牌号码
print(used_plates)
generated_plates = []
for _ in range(20):
    while True:
        # 生成一个符合规则的车牌号码
        prefix = random.choice("BCDFGHJKLMNPQRSTVWXYZ")
        if random.randint(0, 1) == 0:
            middle = random.choice("BCDFGHJKLMNPQRSTVWXYZ")
            suffix = "".join([str(random.randint(0, 9)) for _ in range(3)])
        else:
            middle = random.choice("BCDFGHJKLMNPQRSTVWXYZ")
            suffix = "".join([str(random.randint(1, 9)) for _ in range(4)])

        plate = f"湘A·{prefix}{middle}{suffix}"

        if plate not in used_plates:
            used_plates.add(plate)
            generated_plates.append(plate)
            break

# 打印生成的车牌号码
for i, plate in enumerate(generated_plates):
    if i % 10 == 0 and i > 0:
        print()
    print(plate, end="  ")
