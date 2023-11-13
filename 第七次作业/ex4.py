xydm = {
  '01': '通信与电子科学学院',
  '02': '物理与机电工程学院',
  '03': '资源与环境工程学院',
  '04': '化学化工学院',
  '05': '数学与统计学院',
  '06': '计算机科学与工程学院',
  '07': '商学院'
}

student_id = input("请输入学生的学号：")

if len(student_id) == 10:
  admission_year = student_id[:4]
  college_code = student_id[4:6]

  if college_code in xydm:
    college_name = xydm[college_code]
    grade = int(admission_year) - int(college_code)

    print(f"学生所属年级：20{admission_year}级")
    print(f"学生所属学院：{college_name}")
  else:
    print("学院代码错误，请重新输入。")
else:
  print("学号格式错误，请重新输入。")
