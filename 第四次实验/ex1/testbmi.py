from bmi import fun_bmi
if __name__=="__main__":
  name=input("输入姓名:")
  height=float(input("输入身高:"))
  weight=float(input("输入体重:"))
  bmi=fun_bmi(name,height,weight)
  if bmi<18.5:
    print("消瘦")
  elif bmi<=24:
    print("正常")
  else:
    print("肥胖")
