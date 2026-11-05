#타이틀
print("="*30)
print("가위/바위/보 게임")
print("="*30)

import random

user_score = 0
compuer_scroe = 0

while True:
# 컴퓨터
    computer = random.randint(1,3)

    choices = {1:"가위", 2:"바위", 3:"보"}
    computer_choice = choices[computer]
     
#플레이어
    user_input = input("가위(1), 바위(2), 보(3), 종료(q)")

    if user_input == "q":
        break

    if not user_input.isdecimal():
        print("숫자만 입력해주세요." )
        continue
    
    user_number = int(user_input)
    
    if user_number > 3 or user_number < 1:
        print("1에서 3 사이의 숫자를 입력해주세요.")
        continue
    
    user_choice = choices[user_number]
    #무승부
    if user_choice == computer_choice:
        print (f"나: {user_choice} vs 컴퓨터: {computer_choice}")
        print("무승부")   
    #플레이어 승리
    elif ((user_choice == "가위" and computer_choice == "보") 
          or (user_choice == "바위" and computer_choice == "가위")           
          or (user_choice == "보" and computer_choice == "바위")):
        print (f"나: {user_choice} vs 컴퓨터: {computer_choice}")
        print("승리")
#플레이어 패배
    else:
        print (f"나: {user_choice} vs 컴퓨터: {computer_choice}")
        print("패배")
    
    
    print (f"나: {user_choice} vs 컴퓨터: {computer_choice}")
    # print (f"=>)
    