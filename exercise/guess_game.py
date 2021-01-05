import random

guess_number = random.randint(1,100)
user_number = 0
count = 0
while user_number != guess_number:
    user_number = int(input("숫자를 입력하세요 : "))
    count += 1
    if user_number > guess_number:
        print("숫자가 너무 큽니다.")
    else:
        print("숫자가 너무 작습니다.")
else:
    print("정답 {0}을 {1}번 만에 맞췄습니다!".format(guess_number, count))
