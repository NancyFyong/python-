n = int(input("请输入一个1000以内的正整数: "))
result = [str(x) for x in range(n + 1) if sum(map(int, str(x))) == 5]
print("数字之和为5的数:", " ".join(result))
