import random
#抽五福的方法
def Ji_fu() :
  fus=['爱国福','富强福','和谐福','友善福','敬业福']
  fu = random. sample(fus, 1)
  return fu
#打印当前拥有的所有福
def fus (fu) :
  print("当前拥有的福：")
#字典的键值对遍历方法打印福卡
  for i, j in fu.items():
    print(i, ':',j,'\t',end='')
#判断是否集齐五福
def fu_ready(fu):
#设置一个集齐的标识flag，等于1表示集齐了
  flag = 1
  for i, j in fu.items():
    if j == 0:
#有一个福卡的数量为0
      flag=0#标识为0，可以继续集福
  return flag
