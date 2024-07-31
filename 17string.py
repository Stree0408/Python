# 문자열 메소드 dir(str)       dir --> directory (경로)
# w = 'I am the Boss'

# upper()  --> 대문자로 변경 
# s = w.upper()
# print(s)


# lower()  --> 소문자로 변경
# s = w.lower()
# print(s)


# swapcase() --> 대문자는 소문자로, 소문자는 대문자로 변경
# s = w.swapcase()
# print(s)


# capitalize() --> 첫 문자를 대문자로 변경 
# w = 'i am the Boss'
# s = w.capitalize()
# print(s)


# title() --> 각 단어의 첫 글자를 대문자로 변경 
# s = w.title()
# print(s)


# strip() --> 문자열 양쪽 끝의 공백을 지운다 
# w = '   I am the Boss   '
# s = w.strip()
# print(s+'***')


# lstrip() --> 문자열 왼쪽의 공백을 지운다 
# w = '   I am the Boss   '
# s = w.lstrip()
# print(s+'***')


# rstrip() --> 문자열 오른쪽의 공백을 지운다
# w = '   I am the Boss   '
# s = w.rstrip()
# print(s+'***')


# replace() --> 문자열 특정 부분을 변경 (대체)
# print(w)
# s = w.replace('Boss', 'Leader')
# print(s)


# format() --> 틀(포맷)을 만들어 놓고 문자열을 생성 
# s = '{} is {}'.format('This', 'desk')
# print(s)


# s='123'
# l1=s.split()
# print(l1)
# l2='**'.join(l1)
# print(l2)


# split(나누기)의 반대가 join(붙히기)
# join() --> 리스트 같은 iterable 인자를 전달하여 문자열로 연결 
# s = ",".join('abcd')
# print(s)



# center() --> 정의된 문자열을 앞뒤로 특정문자로 채운 뒤 중앙에 정렬    
# w = 'I am the Boss' 
# print(w.center(30))
# print(w.center(30, '#'))



# ljust() --> 문자열 왼쪽 정렬 
# a = '123'
# print(a.ljust(10))


# rjust() --> 문자열 오른쪽 정렬 
# a = '123'
# print(a.rjust(10))


# partition() --> 전달한 문자로 문자열을 나눔(분리), 결과는 튜플(구분자도 포함)
# w = 'apple/banana'
# s = w.partition('/')
# print(s)


# split() --> 전달한 문자로 문자열을 나눔, 결과는 리스트(구분자 포함 안됨), 기본구분자는 공백    
# w = 'apple/banana'
# s = w.split('a')
# print(s)


# rsplit() --> 뒤에서 부터 전달한 문자로 문자열을 나눔   
# str = 'aaacbbcbcdddceee'
# print(str.split('c', 2))
# print(str.rsplit('c', 2))


# splitlines() --> 라인 단위로 문자열을 나눔
# str = '''abc
# 123'''
# print(str.splitlines())


# isalnum() --> 알파벳 또는 숫자인가? 
# str = 'abc123'
# print(str.isalnum())

# isalpha() --> 알파벳인가?
# str = 'abc123'
# print(str.isalpha())


# 10              0o23          0x12             ob01
# deciaml(10진수)  octal(8진수)   hexa(16진수)      binary(2진수)
# 정수 --> decimal 
# 2.8 --> float


# isdecimal() --> 10진수인가 물어보는것 
# a = '304050'
# print(a.isdecimal())


# isdigit() --> 숫자(0~9 사이의 숫자로)로 이루어진 문자안가  
# a = '30000'
# print(a.isdigit())


# isidentifier() --> 식별자로 사용 가능한가? 
# print('abc'.isidentifier())
# print('3abc'.isidentifier())


# islower() --> 소문자인가?
# print('abc'.islower())
# print(w.islower())

# isnumeric() --> 숫자인가?
# print('123'.isnumeric())

# isspace() --> 공백인가?
# print('  '.isspace())


# istitle() --> title 형식인가? (단어마다 첫 글자가 대문자인가?)
# w = 'I Am The Boss'
# print(w.istitle())


# isupper() --> 대문자인가?
# w = 'ABCD'
# print(w.isupper())


# count() --> 특정 단어(문자열)의 수를 구함, (없으면 0을 반환)
# w = 'apple  orange  apple  banana'
# print(w.count('apple'))
# print(w.count('park'))
# print(w.count(' '))


# len() --> 문자열의 글자 수는 함수를 사용하여 구한다
# w = 'apple  ornage'
# print(len(w))


# startswith() --> 특정 단어로 시작하는지 확인 
# w = 'apple banana orange'
# print(w.startswith('apple'))
# print(w.startswith('park'))


# endswith() --> 특정 단어로 끝나는지 확인 
# w = 'apple banana orange'
# print(w.endswith('orange'))

# w = 'apple banana orange   ' # --> 이거는 끝에 스페이스가 있음 
# print(w.endswith('orange'))



# find() --> 특정 단어를 찾아 인덱스를 리턴(없으면 -1을 리턴)
# w = 'apple  banana  orange'
# print(w.find('banana'))
# print(w.find(' '))
# print(w.find('  '))
# print(w.find('park'))


# rfind() --> 뒤에서부터 특정 단어를 찾아 인덱스를 리턴 (찾기는 뒤에서 찾고 index는 왼쪽부터 세는것)
# w = 'apple  banana  banana  orange'
# print(w.rfind('banana'))


# in, not in --> 특정 단어가 있는지 없는지 확인 가능 
# w = 'apple banana orange'
# print('banana' in w)
# print(' ' in w )
# print('park' not in w)


# index() --> find와 동일하지만 없을 때 예외를 발생시킴 --> 에러 뜸 
# s = 'apple banana orange'
# print(s.index('banana'))
# print(s.index('k'))   


# rindex() --> rfind와 동일하지만 없을 때 예외를 발생시킴 
# s = 'apple banana banana orange'
# print(s.rindex('banana'))
# print(s.rindex('park'))














# isdemical () --> 숫자(demical, 10진수) 인가?    
# a= '0x2'
# print()
# print(a.isdecimal())

#   2     8       10     16
#  0b010  0o71    59    0x7d
#  bin    oct     dec   hex

# print(9)
# print(bin(9))
# print(oct(9))
# print(hex(249))
# isdigit







# 1 
# s = '문자열'
# a1 = "'작은따옴표로 감싼 문자열'"
# a2 = '\'작은따옴표로 감싼 문자열\''   # \' --> '
# b = '"큰따옴표로 감싼 문자열"'
# print(s)
# print(a1)
# print(a2)
# print(b)


# 2 
# s = 'abcdef'

# print (s[0])  # 왼쪽에서 0번째 값 
# print (s[1])
# print (s[-1]) # 오른쪽에서 첫번째 값 

# print (s[1:3]) # 1~2번째 값 
# print (s[1:])  # 1번째 이후의 값 
# print(s[:-1])  # 오른쪽 1번째 다음의 값       

# print(s[::2])  # 2칸 단위로
# print(s[::-1]) # 거꾸로 


# 3 
# first = '내 이름은 '
# second = ' 홍길동 이다'
# string = first + second
# print(string)
# print('*' * 10)

# s = '안녕~'
# print(s*3+first+second)


# 4         
# string = """안녕 ~~        
# 나는 한국중학교에 다니고
# 나의 나이는 13살이야 """
# print(string)

# string = '''안녕 ~~
# 나는 한국중학교에 다니고
# 나의 나이는 13살이야'''
# print(string)

# print("""만일 우리나라에 겨울이 없다면, 봄은 그토록 즐겁지 않을 것이다
# 우리들이 이따금 역경을 맛보지 않는다면,
# 성공은 그토록 환영받지 못할 것이다""")



# 5 
# s1 = 'apple'
# s2 = 'banana'
# s1[3] ='M'    # 변경불가 --> string 변경불가 --> replace를 씀 
# s1 = s1[:3] + 'M' +s1[4:]
# print(s1)

# a='123'
# b=a
# print(id(a), id(b))

# c='123'
# d='123'
# print(id(c), id(d))

# string은 똑같은 값일 경우 같은 주소, id를 갖는다 -- 그래서 변경이 불가능하다 



# print(s1 > s2)     # ascii code 비교하기 
# print(s1 == s1)
# print(s1 != s2)
# print(s1 is s2)     # id 비교
# print(s1 is not s2)
# print(id(s1), id(s2))    

# for c in 'grape':
#     print(c, end=' ')



# 6 
# myscore = 100
# message = '내 점수는 %s 포인트'
# jke='%s: 은 축구를 잘합니다'
# p1='손흥민'
# p2='기성용'

# print(message % myscore)   # %에 myscore 변수에 저장된 값으로 대체 
# print(jke % p1)
# print(jke % p2)


# 7 
# print(ord('a'))
# print(ord('b'))
# print(ord('A'))
# print(chr(97))



# 8 
# string = "Hello, My name is 홍길동"
# print('n' in string)
# print()
# print(string.upper())  # 모두 대문자로 변환 
# print(string.lower())  # 모두 소문자로 변환 
# print('hello world'.capitalize()) # 첫 글자를 대문자로 변환 
# print(string.title()) # 단어의 시작을 대문자로 변환 
# print('Hello'.swapcase()) # 대소문자 반대로 변환 
# print(string.swapcase())
# print()

# print(string.count('e')) # 'e'의 개수 
# print(string.endswith('동')) # '동'으로 끝나면 True
# print(string.startswith('h')) # 'h'으로 시작하면 True 
# print()



# 9 
# str = '나는 C언어 프로그래밍을 좋아해!'
# print(str.replace('C언어', '파이썬')) # 문자열 대치(다른것으로 바꾸어 놓음)
# print()
# print('Hello'.ljust(10)) # 왼쪽정렬 
# print('Hello'.rjust(10)) # 오른쪽 정렬 
# print('Hello'.center(10)) # 가운데 정렬 
# print()
# print('abcdabcd'.find('cd')) # 'cd' 의 가장 작은 인덱스 
# print('abcdabcdabcd'.rfind('cd')) # 'cd' 의 가장 큰 인덱스 
# print('abcdabcd'.find('f')) # 없으면 -1 반환 
# print('abcdabcd'.index('cd')) # 'cd‘ 의 첫 인덱스 


# 10 
# string = 'fruit, apple banana grapes orange melon'
# str1 = string.split() # 공백으로 분리 
# print(str1)
# str2 = string.split(',') # ,으로 분리 
# print(str2)



# fruit = 'apple, banana, grapes,orange ,melon'
# print(fruit.partition('/'))  # 처음 /를 기준으로 3개의 문자열을 갖는 tuple 생성 
# print(fruit.rpartition(','))  # 마지막 , 를 기준으로 3개의 문자열을 갖는 tuple 생성
# print(fruit.split())  # 공백, \t \n 로 문자열을 분리하여 리스트 생성      
# print(fruit.split(',', 2))  # , 로 왼쪽에서 2단어 분리 
# print(fruit.rsplit(',', 2))  # , 로 오른쪽에서 2단어 분리 
# print()
# print('Hello world\n Hello Kim \n '.splitlines())  # 행으로 분리 
# print()
# print('Hello world\n Hello Kim \n')
# print('hello'.zfill(20))  # 자릿수에 맞게 0으로 채우기 

# print('abcdab'.translate(str.maketrans('ab', '12', 'c')))  # a는 1로 변환, b는 2로 변환, c는 삭제  
# print('abcdab'.translate(str.maketrans('ab', 'cc', 'c')))



# a='10+20'
# print(a)
# print(eval(a))  # 문자열로 된 식을 계산하는것 --> evaluate 
# print(eval(repr(20+34)))  # repr --> eval로 계산할수있는 식으로 변경해주는것 
# print(eval(repr('20+34')))



# a='''a=10+20 
# b=a+5
# print(b)
# print('aaa')
# print('dfhhfh')'''
# exec(a)  # execution --> 문자열안에 있는 식을 하나씩 실행해라 --> return값은 따로 없다 
# 리턴 값이 없을때 ‘none’이 나옴 


# a='''a=10+20
# b=a+5'''
# print(exec(a))



# 11  
# 문자열로 된 식을 실행하고, 문자열을 연결하여 봅시다
# x = 1 
# print(eval(repr(x+1)))  # 문자열 수식을 분석하여 실행
# a = 10
# exec("a = a + 20")  # 문자열 문장을 실행  
# print(a)
# print()

# A = ['hello', 'hi']
# print(''.join(A))  # 공백 없이 하나의 문자열로 연결 
# print('.'.join(A))  # 항목사이에 .을 추가하여 하나의 문자열로 연결 
# print('\n'.join(A))  # 항목사이에 \n 을 추가하여 하나의 문자열로 연결 



# 12
# s = '/user/local/bin/python' # --> 맨 끝에 있는게 파일명, 그전에 있는게 경로명, 경로(파일에 가기까지의) 폴더들 
# parts = s.split('/')
# print(parts)
# print('/'.join(parts[:-1]), parts[-1])



# 13     
# s = '''We propose programming in to start by making it possible to teach Python.
# an existing scripting language, and t$%^&$#@*&o focus on creating a new development environment
# and teaching materials for it.'''


# import re
# s1 = s.lower()
# # print(s1)
# s2 = re.sub('[^a-z]', ' ', s1)   # ^ --> not,  [] --> 범위 쓸때 대괄호 써야됨 
# # print(s2)
# ws = s2.split()
# ws.sort()
# print(ws)


# 14 
# passwd = '''noriko:x:524:500:유화정:/home/noriko:/bin/bash
# sky1004mu:x:525:500:김청:/home/sky1004mu:/bin/bash
# hyeyroung:x:526:500:이혜령:/home/hyeyroung:/bin/bash
# muu20:x:527:500:이현복:/home/muu20:/bin/bash'''

# for line in passwd.splitlines():
#     fields = line.split(':')
#     if len(fields) >= 5:
#         print(fields[4])


# 15 
# s = """
# <body bgcolor="#FFFFFF">
# Click <a href="http://www.python.org/"> Here </a>
# To connect to the most powerful tools in the world. 
# </body>
# </html>
# """

# import re  
# s1 = re.sub('<.*?>', '', s)   
# print(s1)



# Question 1 
# myStr = 'Hello, My little baby'
# print(myStr.upper())
# print(myStr.lower())
# print(myStr.title())
# print(myStr.count('b'))
# print(myStr.endswith('y'))
# print(myStr.startswith('h'))
# print(myStr.lower().startswith('h'))   # 하나의 문자열일때 이렇게 두개이상의 함수를 쓸수있다 
# myStr.split().startswith('h')   # 하지만 split()을 써버리면, 하나의 문자열이 아닌 이미 나뉘어진 후 여서 두개 이상의 함수를 쓸수없다 
# print()


# myStrlist1 = myStr.split()
# print(myStrlist1)
# myStrlist2 = myStr.split(',')
# print(myStrlist2)
# print()
# myStrfill = myStr.zfill(30)
# print(myStrfill)


# Question 2 
# st = 'good morning'
# for i in range(4):
#     print(st[i])
# print(st[:4])
# print(st[5:])
# print(st[5:8])


# Question 3 
# input1 = input('문장을 입력하세요 : ').split()
# print('해당 문장의 단어의 수는 {}개 입니다'.format(len(input1)))


# Question 4 
# mystr = 'GOOD NIGHT'
# print(mystr[1:3])
# print(mystr[4:])
# print(mystr[7:9])
# print(mystr[2:4])


# Question 5 
# 앞부터 슬라이싱
# string = 'NATURE'
# print(string[:5])
# print(string[2:4])
# print(string[2:])
# print(string[:3])


# 뒤부터 슬라이싱 
# string = 'NATURE'
# print(string[-4:-2])
# print(string[-6::1])
# print(string[-6:-3])
# print(string[-6:-4])


# Question 6
# string = ''''안녕'
# "Hello"
# 그는 이렇게 말했다. "난 파이썬을 사랑해"..'''
# print(string)


# Question 7 
# s = '에리카 종\n\n나도 따라가 봐야지 ~~'
# print(s)


# Question 8    
# str1 = '=' 
# str2 = 'Python Program'
# print(str2.center(34, str1))


# Question 9 
# str1 = 'hello'
# str2 = 'Good Morning'

# print(str1 * 5)
# for i in range(4):
#     print(str1, str2)



# Question 10 
# str1 = '나는 문자열이다., 줄 바꿈 하려면 특수문자열을 써야하고, 특수문자열을 사용하면 탭도 가능하다.'
# str2 = str1.split(', ')
# for i in str2:
#     print(i)


# Question 11 
# S = 'Somewhere on the rainbow'
# final = S.replace('on', 'over')
# print(final)


# Question 12
# s = ' /user/local/bin/python'
# final = s.split('/')
# print(final)


# Question 13
# s = 'spam ham'
# s = s.split()
# s.reverse()
# s = ' '.join(s)
# print(s)


# Question 14 
# s = ' spam Spam SpaM egg eGG Egg ham hAm'
# s = s.lower()
# print(s.count('spam'))


# Question 16  
# string = input('문자열을 입력 하세요 : ')
# print(string[::-1])


# Question 17    
# string = input('문자열을 입력하세요 : ')
# string = string.split()
# string.reverse()
# print(string)
# for i in string:
#     print(i[::-1], end='')



# Question 18  
# data = ('a', 'b', 'c')
# data = '|'.join(data)
# print(data)


# Question 20 
# print('나는' + 12 + '개의 사과를 먹었다')  # --> 애러 뜨는 이유는 12가 int이기 때문 
# print('나는' + str(12) + '개의 사과를 먹었다')
# print('나는' + '12' + '개의 사과를 먹었다')


# Question 21 
# string = input('문자열을 입력하시오: ')
# str1 = string[:2]
# str2 = string[4:]
# print(str1 + str2)


# Question 22  
# bracket = input('기호를 입력하시오: ')
# input1 = input('중간에 삽입할 문자열을 입력하시오: ')
# print(bracket[0] + input1 + bracket[-1])



# Question 23  
# date = input('오늘의 날짜 : ').split('/')
# car_number = input('차번호 : ')

# if int(date[-1]) % 2 ==0:
#     if int(car_number[-1]) % 2 ==0:
#         D = True 
#     else:
#         D = False

# elif int(date[-1]) % 2 != 0:
#     if int(car_number[-1]) % 2 != 0:
#         D = True 
#     else:
#         D = False

# if D:
#     print('오늘은 {}일 당신차량 끝번호 {}은 운행 가능 합나다.'.format(date[-1], car_number[-1]))
# else:
#     print('오늘은 {}일 당신차량 끝번호 {}은 운행하면 안 됩니다.'.format(date[-1], car_number[-1]))



# Question 24  
# string = input('문자열을 입력하세요 ') 

# import re
# final = re.sub('[0-9 ]', '', string)  # --> 대괄호 안에 스페이스 넣어서 스페이스도 같이 제거해주기 
# print(final)


# Question 25
# input1 = input('문자열을 입력하세요 : ')
# swap = input1.swapcase()
# print('대소문자 변환 결과  --> {}'.format(swap))


# Question 26  
# import re
# input1 = input('6개의 정수 입력 : ')
# final = re.sub('[ ]', '', input1)
# word = ''
# l = []
# final_list =[]

# for i in final:
#     word += i
#     l.append(word)
#     if len(word) == 3:
#         word = ''

# for i in l:
#     if len(i) == 3 or i == l[-1]:
#         final_list.append(i)

# Sum = 0 
# for i in final_list:
#     Sum += int(i)
#     print(i, end=' ')

# print()
# print('합 = {}'.format(Sum))

# or 

# import re
# input1 = input('6개의 정수 입력 : ')
# final = re.sub('[ ]', '', input1)
# l = ''
# Sum = 0 
# for i in final:
#     l+=i
#     if len(l) == 3:
#         print(l, end=' ')
#         Sum += int(l)
#         l=''
# if len(l)>0:
#     print(l)
#     Sum+=int(l)
# print('합 = {}'.format(Sum))


# Question 28
# song = '''동해물과 백두산이 말고 닳도록 하느님이 보우하사 우리나라 만세 무궁화 
# 삼천리 화려강산 대한사람 대한으로 길이 보전하세'''
# song = song.split()
# song=''.join(song)
# print(len(song))

# Question 29 
# str = '''Time is..
# Too Slow for those who Wait
# Too Swift for those who Fear 
# Too Long for those who Grieve
# Too Short for those Rejoice
# But for those who Love
# Time is not.'''
# str = str.splitlines()
# print('문자열 라인은 => {} 줄'.format(len(str)))




# 두번째 풀어보기 
# Q1
# myStr = 'Hello, My little baby'
# print(myStr.upper())    # HELLO, MY LITTLE BABY
# print(myStr.lower())    # hello, my little baby
# print(myStr.title())    # Hello, My Little Baby 
# print(myStr.count('b'))     # 2 
# print(myStr.endswith('y'))      # True 
# print(myStr.startswith('h'))    # False 
# print(myStr.lower().startswith('h'))    # True 
# print()
# myStr_list1 = myStr.split()
# print(myStr_list1)
# myStr_list2 = myStr.split(',')
# print(myStr_list2)
# print()
# myStr_fill = myStr.zfill(30)    # zfill() -> ()만큼 0이랑 string으로 채우기 (string이 오른쪽, 끝에)
# print(myStr_fill)


# Q2
# st = 'good morning'
# print(st[0])
# print(st[1])
# print(st[2])
# print(st[3])
# print(st[:4])
# print(st[5:])
# print(st[5:8])



# Q3
# sentence = input('문장을 입력하세요 : ').split()
# print('해당 문장의 단어 수는 {}개 입니다'.format(len(sentence)))


# Q4
# mystr = 'GOOD NIGHT'
# print(mystr[1:3])
# print(mystr[4:])
# print(mystr[7:9])
# print(mystr[2:4])


# Q5
# 앞부터 슬라이싱 
# string = 'NATURE'
# print(string[:5])
# print(string[2:4])
# print(string[2:])
# print(string[:3])


# 뒤부터 슬라이싱 
# string = 'NATURE'
# print(string[-4:-2])
# print(string[-6:])
# print(string[-6:-3])
# print(string[-6:-4])



# Q6
# string = ''''안녕'
# "Hello"
# 그는 이렇게 말했다. "난 파이썬을 사랑해"..'''
# print(string)


# Q7 
# s = '에리카 종\n\n나도 따라가 봐야지 ~~'
# print(s)



# Q8 
# str1 = '='
# str2 = 'Python Program'
# print(str1 * 10 + str2 + str1 * 10)

# or 

# str1 = '=' 
# str2 = 'Python Program'
# print(str2.center(34, str1))


# Q9 
# str1 = 'hello'
# str2 = 'Good Morning'

# print(str1*5)
# for i in range(4):
#     print(str1, str2)


# Q10 
# str1 = '나는 문자열이다., 줄 바꿈 하려면 특수문자열을 써야하고, 특수문자열을 사용하면 탭도 가능하다.'.split(',')
# for i in str1:
#     print(i.strip())


# Q11
# S = 'Somewhere on the rainbow'
# print(S.replace('on', 'over'))


# Q12
# s = ' /user/local/bin/python'
# print(s.split('/'))


# Q13  
# s = 'spam ham'
# s = s.split()
# s.reverse()
# print((' ').join(s))



# Q14
# s = ' spam Spam SpaM egg eGG Egg ham hAm'
# print(s.lower().count('spam'))   


# Q16
# input1 = input('문자열을 입력 하세요 : ')
# print(input1[::-1])



# Q17
# input1 = input('문자열을 입력 하세요 : ').split()
# final = ''
# for i in input1:
#     final += i
# print(final[::-1])


# or 
# input1 = input('문자열을 입력 하세요 : ').split()
# input1.reverse()
# for i in input1:
#     print(i[::-1], end='')


# Q18
# s = ('a', 'b', 'c')
# print(('|'.join(s)))



# Q20
# print('나는'+12+'개의 사과를 먹었다')   # can't concatenate int to str 
# print('나는'+str(12)+'개의 사과를 먹었다')   
# print('나는' + '12' + '개의 사과를 먹었다')


# Q21
# input1 = input('문자열을 입력하시오: ')
# print(input1[:2]+input1[4:])


# Q22
# input1 = input('기호를 입력하시오 : ')
# input2 = input('중간에 삽입할 문자열을 입력하시오: ')
# print(input1[:1]+input2+input1[1:])
# or 
# print(bracket[0] + input1 + bracket[-1])


# Q23
# date = input('오늘의 날짜 : ').split('/')
# car_num = input('차번호 : ')

# if int(date[-1]) % 2 ==0:
#     if int(car_num) % 2 ==0:
#         print('오늘은 {}일 당신차량 끝번호 {} 운행 가능 합니다'.format(date[-1], car_num[-1]))
#     else:
#         print('오늘은 {}일 당신차량 끝번호 {}은 운행하면 안 됩니다'.format(date[-1], car_num[-1]))

# elif int(date[-1]) % 2 !=0:
#     if int(car_num) % 2 !=0:
#         print('오늘은 {}일 당신차량 끝번호 {} 운행 가능 합니다'.format(date[-1], car_num[-1]))
#     else:
#         print('오늘은 {}일 당신차량 끝번호 {}은 운행하면 안 됩니다'.format(date[-1], car_num[-1]))


# Q24
# string = input('문자열을 입력하세요 ').split()
# for i in string:
#     print(i, end='')


# Q25
# string = input('문자열을 입력하세요 : ')
# print('대소문자 변환 결과 --> ', end='')
# print(string.swapcase())


# Q26   
# input1 = input('6개의 정수 입력 : ').split()
# final = ''.join(input1)

# nSum = 0 
# num = ''
# for i in range(len(final)):
#     if i % 3 ==0 and i != 0:    # if i try to convert the empty string '' to an integer using int(), error will be occurred 
#         print(num, end=' ')
#         nSum += int(num)
#         num = ''
#     num += final[i]
# nSum += int(num)
# print(num)
# print('합 = {}'.format(nSum))



# Q28
# song = '''동해물과 백두산이 말고 닳도록 하느님이 보우하사 우리나라 만세 무궁화 
# 삼천리 화려강산 대한사람 대한으로 길이 보전하세'''
# characters = song.split()
# final = ''
# for i in characters:
#     final += i 
# print('총글자 수 : {}'.format(len(final)))
    
# or 

# song = '''동해물과 백두산이 말고 닳도록 하느님이 보우하사 우리나라 만세 무궁화 
# 삼천리 화려강산 대한사람 대한으로 길이 보전하세'''
# song = song.split()
# song=''.join(song)
# print(len(song))



# Q29 
# str = '''Time is..
# Too Slow for those who Wait
# Too Swift for those who Fear
# Too Long for those who Grieve
# Too Short for those Rejoice
# But for those who Love 
# Time is not.'''

# str = str.split('\n')
# print('문자열 라인은 => {}줄'.format(len(str)))

# or 

# str = str.splitlines()
# print('문자열 라인은 => {} 줄'.format(len(str)))