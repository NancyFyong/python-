z = 'The Python Software'
print("字符串：", z)
d = {}

for c in z:
    d[c] = d.get(c, 0) + 1

print('每个字符出现的次数是：')
for key in d:
    print(key, d[key])
