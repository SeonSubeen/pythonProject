'''
파일명 :

내장 데이터 유형
    Python 변수는 다른 유형의 데이터를 저장할 수 있으며
    다른 유형은 다른 작업을 수행할 수 있다.

텍스트 유형(문자열) : str
숫자 유형 : int(정수형), float(실수형)
시퀀스 유형 : list, tuple, range
매핑 유형 : dict
세트 유형 : set
논리 유형 : bool
바이너리 유형 : bytes
없음 유형 : None
'''
# str
x = 'Hello, World'
print(type(x))

# int
x = 20
print(type(x))

# float
x = 20.5
print(type(x))

# list
x = ['피카츄', '라이츄', '파이리']
print(type(x))

# tuple
x = ('피카츄', '라이츄', '파이리')
print(type(x))

# range
x = range(6)
print(type(x))

# dict
x = {'name':'피카츄', 'skill':'백만볼트'}
print(type(x))

# set
x = {'피카츄', '라이츄', '파이리'}
print(type(x))

# bool(논리)
x = True # False
print(type(x))

# NoneType
x = None
print(type(x))

'''
변수명 = 값
값이 type에 따라 연산이 달라진다.

예) 더하기 경우
    숫자 + 숫자 = 숫자
    문자 + 문자 = 문자연결
    문자 + str(숫자) = 문자숫자연결
'''
num1 = 10
num2 = 20
result = num1 + num2
print(result)

name = 'Alice'
age = '15'
result = name + '/' + age
print(result)

name = '피카츄'
age = 28
result = name + str(age)    #문자 + str(숫자) 형변환 필요
print(result)
