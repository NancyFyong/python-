def is_prime(num):
  if num < 2:
    return False
  for i in range(2, int(num ** 0.5) + 1):
    if num % i == 0:
      return False
  return True


def get_primes_below_n(n):
  primes = [i for i in range(2, n) if is_prime(i)]
  return primes


# 输入一个大于2的自然数
num = int(input("请输入一个大于2的自然数: "))

# 获取小于该数字的所有素数列表
prime_list = get_primes_below_n(num)

# 输出结果
print("小于", num, "的所有素数:", prime_list)
