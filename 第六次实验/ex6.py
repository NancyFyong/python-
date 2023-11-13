score = [['Angle', '0121701100106', 99],
         ['Jack', '0121701100107', 86],
         ['Tom', '0121701100109', 65],
         ['Smith', '0121701100111', 100],
         ['Bob', '0121701100115', 77],
         ['Lily', '0121701100117', 59]]

# 按姓名排序
sorted_by_name = sorted(score, key=lambda x: x[0])
print("按姓名排序:", sorted_by_name)

# 按学号排序
sorted_by_id = sorted(score, key=lambda x: x[1])
print("按学号排序:", sorted_by_id)

# 按成绩排序
sorted_by_score = sorted(score, key=lambda x: x[2])
print("按成绩排序:", sorted_by_score)
