result_set = set()

for i in range(1000, 10000):
    digits_sum = sum(int(digit) for digit in str(i))
    if i % 11 == 0 and digits_sum == 6 and len(set(str(i))) == 4:
        result_set.add(i)

print("满足条件的四位数有：", len(result_set), "个，分别是：", result_set)
