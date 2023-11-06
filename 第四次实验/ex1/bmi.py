def fun_bmi(person, height:float, weight:float):

  print(person +"的身高:"+str(height)+"米\t体重:"+str(weight)+"千克")
  bmi = weight / (height * height)
  return bmi
