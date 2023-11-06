input_string = input("请输入一个字符串: ")
encrypted_string = ""
for char in input_string:
    if char.isalpha():
        if char.islower():
            encrypted_char = chr(((ord(char) - ord('a') + 3) % 26) + ord('a'))
        else:
            encrypted_char = chr(((ord(char) - ord('A') + 5) % 26) + ord('A'))
        encrypted_string += encrypted_char
    else:
        encrypted_string += char
print("加密后的字符串:", encrypted_string)
