input_string = input("请输入一个字符串: ")
input_string = input_string.lower()  # 将字符串转换为小写以便不区分大小写

# 创建一个字典来存储字母和它们的出现次数
letter_count = {}

for char in input_string:
    if char.isalpha():
        if char in letter_count:
            letter_count[char] += 1
        else:
            letter_count[char] = 1

# 找出出现次数最多的字母
most_common_letter = max(letter_count, key=letter_count.get)
count = letter_count[most_common_letter]

print(f"字母{most_common_letter}，{most_common_letter}出现了{count}次")
