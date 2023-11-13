class ContactBook:
  def __init__(self):
    self.contacts = {}

  def add_contact(self, name, phone_number):
    self.contacts[name] = phone_number
    print(f"联系人 {name} 已添加")

  def update_contact(self, name, new_phone_number):
    if name in self.contacts:
      self.contacts[name] = new_phone_number
      print(f"联系人 {name} 的电话已更新")
    else:
      print(f"联系人 {name} 不存在")

  def delete_contact(self, name):
    if name in self.contacts:
      del self.contacts[name]
      print(f"联系人 {name} 已删除")
    else:
      print(f"联系人 {name} 不存在")

  def display_contacts(self):
    if not self.contacts:
      print("通讯录为空")
    else:
      print("通讯录:")
      for name, phone_number in self.contacts.items():
        print(f"{name}: {phone_number}")


# 示例使用
contact_book = ContactBook()
contact_book.add_contact("Alice", "1234567890")
contact_book.add_contact("Bob", "9876543210")
contact_book.display_contacts()

contact_book.update_contact("Alice", "5555555555")
contact_book.update_contact("Charlie", "1111111111")

contact_book.delete_contact("Bob")
contact_book.delete_contact("David")

contact_book.display_contacts()
