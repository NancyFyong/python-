import random

choice=["石头", "剪刀", "布"]
def get_user_choice():
    while True:
        user_choice = int(input("请输入1-3的值："))
        if user_choice>=1 and user_choice <=3:
            return choice[user_choice-1]
        else:
            print("输入有误，请重新输入。")

def get_computer_choice():
    return random.choice(["石头", "剪刀", "布"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "平局"
    elif (user_choice == "石头" and computer_choice == "剪刀") or \
         (user_choice == "剪刀" and computer_choice == "布") or \
         (user_choice == "布" and computer_choice == "石头"):
        return "玩家胜利"
    else:
        return "电脑胜利"

def save_data(player_score, computer_score,winner):
    with open("game_results.txt", "a",encoding='utf-8') as file:
        file.write(f"玩家分数: {player_score}, 电脑分数: {computer_score}, 胜者: {winner}\n\n")

def print_ui():
  for i in range(25):
    print('#',end='')
  print('\n#      石头剪刀布游戏.     #')
  print('#   请您根据下列提示出拳:   #')
  for i in range(25):
    print('#',end='')
  print('\n|---------------|')
  print('|  1.石头.       |')
  print('|  2.剪刀.       |')
  print('|  3.布.        |')
  print('|---------------|')
def main():
    game_count = int(input("请输入游戏次数："))
    player_score = 0
    computer_score = 0

    for _ in range(game_count):
        print_ui()
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"玩家选择：{user_choice}")
        print(f"电脑选择：{computer_choice}")

        winner = determine_winner(user_choice, computer_choice)
        print(f"结果：{winner}\n")

        if winner == "玩家胜利":
            player_score += 1
        elif winner == "电脑胜利":
            computer_score += 1

    print("游戏结束！")
    print(f"玩家总分：{player_score}")
    print(f"电脑总分：{computer_score}")

    if player_score > computer_score:
        print("玩家胜利！")
    elif player_score < computer_score:
        print("电脑胜利")
    else:
        print("平局")
    save_data(player_score, computer_score,winner)

if __name__ == "__main__":
    main()
    # print_ui()
