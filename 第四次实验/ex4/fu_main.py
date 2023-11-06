from Ji_fu_test import Ji_fu
from Ji_fu_test import fu_ready
from Ji_fu_test import fus
print("开始集福了……")
#定义一个五福字典保存用户的福卡
fu={'爱国福':0,'富强福':0,'和谐福':0,'友善福':'0','敬业福':0}
#用一个while语句循环获取五福，直到集齐为止
count=0#设置一个计数器，记录集福的次数
while fu_ready(fu) == 0:#集齐标识为0
  input("\n按下<enter>键获取福卡：")
  getfu = Ji_fu()[0]
#进行抽卡
  print('获取了: ',getfu)
  print(getfu)
  fu[getfu] += 1
#将抽到的卡加入五福字典，相应数量+1
  fus(fu)
#调用方法打印当前拥有的五福
  fu_ready (fu)
#调用方法判断是否集齐
  count +=1
print("\n***五福已经集齐，真是有福之人***")
print("一共集福",count,'次')
