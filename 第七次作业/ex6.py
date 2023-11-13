def is_unique_date(date):
  return len(set(str(date))) == len(str(date))


birthday = None

for year in range(1, 2023):  # 小明出生年份到今天的年份
  for month in range(1, 13):
    for day in range(1, 32):
      date = year * 10000 + month * 100 + day
      if is_unique_date(date):
        birthday = date
        break

print("小明的生日是：", birthday)
