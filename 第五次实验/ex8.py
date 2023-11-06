# idcard.py

programer_1 = '你知道我的生日吗?'
print('程序员甲说：', programer_1)
programer_2 = '输入你的身份证号码。'
print('程序员乙说：', programer_2)
idcard = '433127199708092536'

# 截取生日
birthday = idcard[6:14]
formatted_birthday = f"{birthday[:4]}年{birthday[4:6]}月{birthday[6:8]}日"

print('程序员乙说：', '你是' + formatted_birthday + '出生的，所以你的生日是' + formatted_birthday)
