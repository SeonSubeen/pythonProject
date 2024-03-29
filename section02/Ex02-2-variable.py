'''
파일명: Ex02-2-variable.py

변수(variable)
    파이썬에서 변수는 데이터를 저장하고 관리하는데 사용되는 식별자

    지정된 메모리 위치를 가리키며, 해당 메모리 위치에 값을 저장하거나 검색할 수 있다.

변수명 규칙
    영문, 한글, 숫자, 밑줄(_)로 구성된다.
    특수문자는 사용할 수 없다.
    대소문자를 구분한다.
    변수명의 첫글자를 숫자로 사용할 수 없다.
    키워드(list, dict, if, for, and 등)는 사용할 수 없다.
'''
# 변수 선언 방법
# 변수명 = 값
name = 'Alice'
print(name)
age = 25
print(age)
address = '''우편번호 12345 서울시 영등포구 여의도동 123-45'''
print(address)

'''
잘못된 변수명 예시
'''
# 2mybar = 'Python1'
# my-var = 'Python2'
# my var = 'Python3'

'''
여러 값 할당
    Python을 사용하면 한줄에 여러 변수에 값을 할당할 수 있다.
'''
x, y, z = "피카츄", "라이츄", "파이리"
print(x)
print(y)
print(z)

'''
여러 변수에 대한 하나의 값
    한줄에 여러 변수에 동일한 값을 할당할 수 있다.
    
Ctrl + d 줄복사
'''
x = y = z = '꼬부기'
print(x)
print(y)
print(z)

