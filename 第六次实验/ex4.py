psls = [75, 75, 75, 65, 85, 95, 85, 75, 75, 75, 85, 75, 75, 65, 75]
qmls = [68, 63, 70, 51, 78, 83, 75, 66, 70, 73, 85, 67, 78, 60, 66]

total_scores = []

for psl, qml in zip(psls, qmls):
    # 如果期末成绩缺失，将总成绩标记为 "旷考"
    if qml is None:
        total_scores.append("旷考")
    else:
        # 计算总成绩
        total_score = int(psl * 0.2 + qml * 0.8)
        total_scores.append(total_score)

print(total_scores)
