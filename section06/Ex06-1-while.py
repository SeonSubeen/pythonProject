'''
파일명: Ex06-1-while.py

반복문
    어떤 수행 작업을 한번이 아니라 계속해서 수행해야 할 때 사용하는 명령어

    while 조건식:
        반복 실행코드
'''
n = 10
while n != 0:
    print(n)
    n -= 1

print(f'while문 끝나고 n의 값: {n}')