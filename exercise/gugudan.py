while True:
    print('구구단 몇 단을 계산할까요(1~9)?')
    num = int(input())
    if num not in range(1, 10):
        print('구구단 게임을 종료합니다.')
        break
    print(f'구구단 {num}단을 계산합니다.')
    for i in range(1, 10):
        print(f'{num} X {i} = {num*i}')