import random

random_numbers = tuple(random.randint(1, 100) for _ in range(40))

# 将前十个数按升序排列
sorted_first_ten = sorted(random_numbers[:10])

# 将后十个数按降序排列
sorted_last_ten = sorted(random_numbers[-10:], reverse=True)

print("前十个数按升序排列:", sorted_first_ten)
print("后十个数按降序排列:", sorted_last_ten)
