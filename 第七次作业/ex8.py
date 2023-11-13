s1 = {"姓名": "乔峰", "班级": "1班", "数学": 88, "语文": 87, "英语": 90}
s2 = {"姓名": "段誉", "班级": "2班", "数学": 98, "语文": 77, "英语": 95}
s3 = {"姓名": "阿朱", "班级": "1班", "数学": 78, "语文": 83, "英语": 80}
s4 = {"姓名": "阿紫", "班级": "1班", "数学": 75, "语文": 80, "英语": 86}
s5 = {"姓名": "虚竹", "班级": "2班", "数学": 93, "语文": 85, "英语": 96}

# （1）遍历输出1班学生的成绩单
print("1班学生的成绩单：")
for student in [s1, s3, s4]:
    print(student)

# （2）求出每个学生的总成绩后加到原有字典中然后打印每个学生信息
students = [s1, s2, s3, s4, s5]
for student in students:
    student["总成绩"] = sum(value for key, value in student.items() if key not in ["姓名", "班级"])
    print(student)

# （3）求出每门课的平均成绩并输出
subjects = ["数学", "语文", "英语"]
for subject in subjects:
    average_score = sum(student[subject] for student in students) / len(students)
    print(f"{subject}的平均成绩：{average_score:.2f}")

# （4）找出数学低于平均分的学生，打印他们的姓名，班级，数学成绩
math_average = sum(student["数学"] for student in students) / len(students)
below_average_math_students = [student for student in students if student["数学"] < math_average]

print("数学低于平均分的学生：")
for student in below_average_math_students:
    print(f"姓名：{student['姓名']}, 班级：{student['班级']}, 数学成绩：{student['数学']}")
