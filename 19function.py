# 1 
# def simple():
#     print('여기는 함수!!')
# simple()



# if __name__ =='__main__':
# print('1111')
# print('2222')
# simple() # 함수 호출 

# print('1111')
# print('2222')
# simple() 



# 2 
# def sayhello():
#     print('안녕')
#     print('반가워. 이 프로그램은 파이썬 공부 프로그램이야')
#     print('기분 좋은 하루 보내~')

# sayhello()
# sayhello()


# 3 
# def print_address(name):       # name --> 매개변수, parameter --> 인수를 받는 변수
#     print('성남시 분당구 구미동')
#     print('엘레강스빌딩 2동')
#     print(name)

# print_address('홍길동')       # 홍길동 --> 인수 
# print_address('park')


# 4                   
# def signGood(when):
#     if when == 1:
#         print('Good morning')
#     elif when == 2:
#         print('Good Afternoon')
#     elif when == 3:
#         print('Good Evening')
#     else:
#         print('Good Night')
    
# signGood(1)  # --> good morning
# signGood(3)   # --> good evening
# signGood(10)   # --> good night 


# 6 
# def hap(a,b):
#     result = a + b
#     print('두 수의 합을 구해 출력해주는 함수입니다')
#     print(a,b, '의 합은 ', result, '입니다')

# hap(10,20)     # --> 인수 갯수는 여려개도 가능 
# hap(-87,172)        


# 11
# def calculate_area(radius):    
#     area = 3.14 * radius ** 2 
#     return area     # --> 로컬 변수 값을 넘겨주는 것 

# c_area = calculate_area(5.0)
# print(c_area)
# print(calculate_area(7.5))


# a = 10  # --> 전역변수 --> 전 지역에서(main,함수 등등 모든영역) 사용할 수 있는 변수  -> global(전역) 

# def f():
#     b=20  # --> 지역변수 --> 함수 안에서 선언된 변수 --> local 
#     print(a)
#     b+=1
#     print(b)

# print(a)
# f()
# # print(b)   # --> 로컬 변수여서 함수 밖에서는 사용할 수 없음
# a+=100
# print(a)
# f()


# 12 
# def abs(number):
#     if number < 0:
#         number = -number
#     return number 

# print(abs(5))
# print('-3의 절대값 구하기:', abs(-3))   # 3 
# print('10의 절대값 구하기:', abs(10))  # 10 
# print()
# temp = abs(-9)/3 * abs(20) + 3 + abs(-19)   # 9 /3 * 20 + 3 + 19 = 82 
# print('계산 결과:', temp)   # 82.0


# 13  
# 매개변수에 기본 값을 설정하여 봅시다 
# def report(message, who='Everyone'):
#     print(message, who)

# report('good morning')
# report('good morning', 'Mr.park')


# 14 
# def calc(x=10, y=20, z=30):
#     print('x=',x)
#     print('y=',y)
#     print('z=',z)

# calc()

# calc(100,200,300)
# print()
# calc(z=3, y=2, x=1)
# print()
# calc(z=500)
# print()
# calc(100, y=200, z= 300)
# print()
# calc(x=1, 2, 3)     # --> 이렇게 쓰면 에러뜸  



# 15           
# def select_even(*arg):  
    # print(type(arg), arg)  # --> 함수에서는 튜플로 패킹이된다
    # result = []
    # for num in arg:
    #     if num % 2 == 1:
    #         continue
    #     result.append(num)
    # return result 


# print(select_even(1,2,3,4))
# print(select_even(-12,2,81,99,48,20))


# a,b = 10,20 
# a,*b= 10,20,30,40,50
# print(a)
# print(b)  # --> 변수에서는 리스트로 패킹이된다  

# *a, b = 10, 20, 30, 40, 50
# print(a,b)


# l=[1,2,3]
# print(l)
# l[1]=100
# print(l)


# t=(1,2,3)
# print(t)
# t[1]=100   # 튜플은 값을 변경못한다 
# print(t)



# 16    
# def make_array(n, value =0):
#     mat = [value for j in range(n)]
#     return mat

# my_array = make_array(5,10)     # [10, 10, 10, 10, 10]
# print(my_array)



# 17 
# def make_2D_array(m, n, value=0):   # m=2, n=4, value=10
#     mat = [[value for j in range(n)] for i in range(m)]
#     return mat


# my_array = make_2D_array(2,4,10)
# print(my_array)
# print(my_array[0][0])



# 18    
# def polyFunc(x, y, z):
#     print('x = {}, y = {}, z = {}'.format(x,y,z))
#     return 3*x + 2*y + z


# print(polyFunc(1,2,3))   # 정수형 인수   --> 10 
# print(polyFunc(1.0, 2.0, 3.0))  # 실수형 인수 --> 10.0
# print(polyFunc('a','b','c'))  # 문자형 인수 --> aaabbc
# print(polyFunc(*'abc'))  # 문자열의 항목을 이용한 위치 변수 --> aaabbc  --> 아까의 반대상황 --> 하나로 묶여있던 것을 3개로 푸는거임
# print(polyFunc(*(1,2,3)))  # 튜플의 항목을 이용한 위치 변수 --> 10
# print(polyFunc(*[1,2,3]))  # 리스트의 항목을 이용한 위치 변수 --> 10 
# print(polyFunc(*{1:'a', 2:'b', 3:'c'}))  # 딕셔너리의 항목을 이용한 위치 변수 --> 10 



# 19   
# def print_odd(start, end):
#     '''주어진 범위에서 홀수를 리스트로 만들어 주는 함수입니다.
#     start 시작 값을 지정합니다.
#     end 끝 값을 지정합니다.'''
#     result = []
#     for num in range(start, end+1):
#         if num % 2 == 0 :
#             continue
#         result.append(num)
#     return result 


# help(print_odd)   # --> ''' (따움표 세게안에 내용을 넣었으면) '''  help(function)을 입력하면 그 내용이 나옴  --> 함수의 대한 내용을 ''' ''' 안에 넣어둠 
# print('-' * 50)
# print_odd.__doc__ = '''이건 연습삼아서'''  # --> 원래 ''' ''' 따움표안에 있었던 문자열을 바꾸는것 
# help(print_odd) 
# print('-' * 50)
# print(print_odd(3, 19))



# Question 1 - 실행결과를 예측하여 봅시다 
# def polyFunc(x=1, y=1, z=1):
#     print('x = {}, y = {}, z = {}'.format(x,y,z))
#     return 3*x + 2*y + z

# print(polyFunc())
# print(polyFunc(z=3))
# print(polyFunc(1, z=3, y=2))


# Question 2
# def nSum(a,b):
#     print('두개의 수를 입력하시오 : {} {}'.format(a,b))
#     print('{} + {} = {}'.format(a,b,a+b))

# nSum(8,4)    


# Question 3 
# def until(num):
#     print('몇까지 출력 할까요? ==> {}'.format(num))
#     print()
#     for i in range(1,num+1):
#         print(i)

# until(10)



# 구구단을 여러번 출력 0이면 종료, 1~9 사이가 아니면 다시 입력 
#  몇단 ? 3
# 2*1=3
# .
# .
# .
# 몇단 ? 10
# 다시입력
# 몇단 ? 4
# 4*1=1
# .
# .
# .
# 몇단 ? 0
# 종료
 


# def multiplication_table():
#     for i in range(1,10):
#         print('{} * {} = {}'.format(n,i,n*i))    


# while True:
#     n = int(input('몇 단을 출력할까요 : '))   # --> 메인 안에서 선언된 변수도 전역변수이다 (global)
#     if n == 0:
#         print('종료')
#         break       # break, continue는 반복문 안에서만 쓸 수 있음
#     elif  n >= 10 or n <= 0:
#             print('다시 입력하세요')
#             continue
#     else:
#         multiplication_table()   # --> 계속 반복해서 사용되어지는 것을 함수로 만드는 것이 좋다 


# Question 4 
# num_list= [1,2,3,4]

# def print1(l1):
#     print(l1)

# print1(num_list)


# Question 5 
# return 쓰면서 풀어본거 
# 홀수이면 --> True, 짝수이면 --> false 

# def determine(n):      
#     if n % 2 == 0:
#         return False
#     else:
#         return True          


# if determine(10):          
#     print('odd')           
# else:
#     print('even')          



# Question 6  
# import random 

# def menu(coin):
#     if coin == 1:
#         print('동전을 던지세요 --> 앞')
#         print('오늘 메뉴는 중국요리로 결정 되었습니다.')
#     else:
#         print('동전을 던지세요 --> 뒤')
#         print('오늘 메뉴는 일본요리로 결정 되었습니다.')


# if __name__ =='__main__':
#     n1 = random.choice([1,2])
#     menu(n1)


# Question 7 
# def abs(num):
#     print('수를 입력하세요 : {}'.format(num))
#     if num < 0:
#         num = -num
#     return num 

# print('절대 값은 {}입니다'.format(abs(-3)))


# Question 8 
# def determine(a,b):
#     if a > b:
#         return a 
#     elif b > a :
#         return b 

# num1, num2 = map(int, input('2개의 수를 입력 하세요 : ').split())

# print('큰 수는 {} 입니다'.format(determine(num1,num2)))


# ???????? 내가 혼자서 집에서 푼 방법 - 확인부탁 - 둘중에 어떤게 더 좋은 형태의 함수인가? (내 생각엔 밑에꺼가 더 좋은함수형태인듯 --> input을 계속 바꿀수있음)

# def determine(a,b):
#     print('2개의 수를 입력 하세요 : {} {}'.format(a,b))
#     if a > b:
#         return a 
#     elif b > a :
#         return b 
    
# print('큰 수는 {} 입니다'.format(determine(10,4)))



# or 
# 함수 두개 만들고 
# 하나에는 입력받고 
# 또 하나에는 큰 값을 리턴해주는 함수 


# def input1():
#     num1, num2 = map(int, input('2개의 수를 입력 하세요 : ').split())
#     return num1, num2 

# def determine():     
#     if a > b:
#         return a 
#     elif b > a :
#         return b 
 
# a,b=input1()           # ?????????? 이것만 적어도 실행이되는거? 왜냐하면 그냥 변수에다 저장만하는거면 원래는 실행안되야하는건데 input1()함수형태적었다고 실행되는거?
# print('큰 수는 {} 입니다'.format(determine()))


# or 

# def input1():
#     num1, num2 = map(int, input('2개의 수를 입력 하세요 : ').split())
#     return num1, num2 

# def determine():  
#     a, b= input1()    # 함수안에서 함수 불러도 됨 
#     if a > b:
#         return a 
#     elif b > a :
#         return b 

# print('큰 수는 {} 입니다'.format(determine()))



# Question 10 
# nlist=[50,40,60,10,70,100,30,20]

# def maxmin():
#     Max=Min=nlist[0]
#     for i in range(len(nlist)):
#         if nlist[i] > Max:
#             Max = nlist[i]
#         if nlist[i] < Min:
#             Min = nlist[i]
#     return Max,Min
    
# a,b=maxmin()
# print('가장 큰값 :  {}'.format(a))
# print('가장 작은값 :  {}'.format(b))

# or 

# nlist=[50,40,60,10,70,100,30,20]

# def maxmin():
#     return(max(nlist), min(nlist))
    
# a,b=maxmin()
# print('가장 큰값 :  {}'.format(a))
# print('가장 작은값 :  {}'.format(b))


# Question 11
# def sum(start,end):
#     Sum = 0 
#     for i in range(start,end+1):
#         Sum += i 
#     return Sum

# # print(sum(1,3))
# print(sum(1,10))
# print(sum(1,3) + sum(7,10))


# Question 12 
# def determine(score):
#     print('점수 : {}'.format(score))
#     grade=''                       
#     if 90 <=  score <= 100:
#         grade = 'A학점'
#     if 80 <= score <= 89:
#         grade = ('B학점')
#     if 70 <= score <= 79:
#         grade = ('C학점')
#     if 60 <= score <= 69:
#         grade = ('D학점')
#     if score < 60:
#         grade = ('F학점')
#     return grade 

# print(determine(60))


# 매개변수(parameter)는 local이다 
# Question 13         
# def input2(first,second): 
#     print('두개의 수를 입력 하세요 : {} {}'.format(first, second))
#     if first % second == 0:
#         return True
#     else:
#         return False 

# if input2(17,4):
#     print('{}은 {}의 배수입니다'.format())    # True 
# else:
#     print('{}은 {}의 배수가 아닙니다'.format())    # False 


# Question 14 
# def input5():
#     print('5과목의 점수를 입력하세요 : ')
#     a = int(input())
#     b = int(input())
#     c = int(input())
#     d = int(input())
#     e = int(input())
#     average = ((a+b+c+d+e) / 5 )
#     return average 


# if input5() >= 60:
#     print('축하 !! 합격입니다')
# else:
#     print('불합격입니다 다시 도전하세요 ~')


# 더 좋은 방법 

# def input5(first,second,third,fourth,fifth):     # global이면 안받아도된다는게 무슨말인지 
#     average = ((first+second+third+fourth+fifth) / 5 )
#     return average 


# print('5과목의 점수를 입력하세요 : ')
# a,b,c,d,e = map(int, input().split())     # a,b,c,d,e 여기다 받는 이유 ???????


# if input5(a,b,c,d,e) >= 60:
#     print('축하 !! 합격입니다')
# else:
#     print('불합격입니다 다시 도전하세요 ~')


# ? ?????? 다시 썻는데 확인부탁 
# def input5():    
#     average = ((a+b+c+d+e) / 5 )
#     return average 


# print('5과목의 점수를 입력하세요 : ')
# a,b,c,d,e = map(int, input().split())     # a,b,c,d,e 여기다 받는 이유 ??????? (위치)


# if input5() >= 60:
#     print('축하 !! 합격입니다')
# else:
#     print('불합격입니다 다시 도전하세요 ~')


# Question 15  리스트    ????????????????????????
# def f():
#     global a
#     a+=5
#     print(a)
#     print('globals :', globals())
#     print('locals :', locals())

# a = 100
# print(a) # 100 
# f()  # 105
# a+=10
# print(a) # 115
# f()  # 120 
 


# Question 16  ?????  리스트 
# def determine(name):
#     for i in list:
#         if i == name:
#             return True
#         else:
#             return False 
        
# list = ['길동', '수지', '하나', '나라', '미순']

# name1 = input('이름을 입력하세요 --> ')
# if determine(name1):
#     print('{} 의 출근확인'.format(name1))
# else:
#     print('{} 은 사원명단에 없습니다'.format(name1))


# Question 17    # ?????????? list    풀었는데 반은 디파인을 써서 풀었고 나머지는 그렇게 못풀었음 
# destination = ['춘천', '부산', '대구', '수원']
# price = [5000, 30000, 2000, 10000]
# final_list = []

# for i in range(len(destination)):
#     final_list.append([destination[i], price[i]])


# def determine_price():
#     for i in range(len(final_list)):
#         if final_list[i][0] == input1:
#             return final_list[i][1]


# input1 = input('어디를 가시겠습니까 ? --> ')
# print('요금은 {} 원 입니다'.format(determine_price()))

    



# Question 18 
# def factorial(n):
#     multiple = 1 
#     for i in range(2,n+1):
#         multiple *= i 
#     return multiple 

# input1 = int(input('정수를 입력하세요  ? --> '))
# print(factorial(input1))


# Question 19  
# def change(first,second):
#     return second, first 

# a,b = 10, 20

# print(change(a,b))


# Question 20 
# def multiple(n):
#     result = 'Ha' * n
#     return result 

# print(multiple(3))


# Question 21
# def connect(a,b):
#     connection = a + b
#     return connection


# input1 = input('첫번째 문자열 --> ')
# input2 = input('두번째 문자열 --> ')
# print(connect(input1,input2))


# Question 22
# def proceed():
#     print('\n')
#     for i in range(repeat):
#         print(string1)


# string1 = input('문자열 --> ')
# repeat = int(input('몇번 반복할까요?  --> '))

# proceed()


# Question 23  
# def determine():
#     for i in range(5):
#         word = input('단어를 입력하세요 -->')
#         if i ==0:
#             Max = Min = len(word)
#             Maxword = Minword = word
#         elif len(word) > Max:
#             Max = len(word)
#             Maxword = word
#         elif len(word) < Min:
#             Min = len(word)
#             Minword = word
#     return Maxword, Minword

# m1,m2=determine()
# print('가장 긴단어는 : {}'.format(m1))
# print('가장 짧은 단어는  : {}'.format(m2))


# Question 24   # list ?????????????  다시 풀어봤음 
# def define_Sum(list_fruit, list_animal, list_instrument):
#     Sum1, Sum2, Sum3 = 0 , 0 , 0
#     for i in range(len(list_fruit)):
#         Sum1 += len(list_fruit[i])
#     for j in range(len(list_animal)):
#         Sum2 += len(list_animal[j])
#     for k in range(len(list_instrument)):
#         Sum3 += len(list_instrument[k])
#     return Sum1, Sum2, Sum3 

# list_fruit = ['apple', 'banana','tomato', 'kiwi']
# list_animal = ['bear', 'elephant', 'monkey']
# list_instrument = ['guitar', 'piano', 'harmonica']


# first, second ,third = define_Sum(list_fruit, list_animal, list_instrument)
# print(first)
# print(second)
# print(third)


# Question 25 
# def maxmin():
#     for i in range(len(score)):
#         if i == 0:
#             Max = Min = score[0]
#         if score[i] > Max:
#             Max = score[i]
#         elif score[i] < Min:
#             Min = score[i]
#     difference = Max - Min 
#     return difference

# score = [10,40,70,60,100,20,50]
# print('점수의 차이 : {}'.format(maxmin()))



# Question 26  ???????? list --> 다시 풀어봤음 
# def change(sentence):
#     capital = sentence.upper()
#     final_list = capital.split()
#     return final_list

# sentence = input('문장을 입력하세요 : ')
# print(change(sentence))


# Question 27 
# import math 

# def area(r):
#     area1 = math.pi * (r**2)
#     return area1

# def circumference(r):
#     circumference1 = 2 * math.pi * r 
#     return circumference1


# radius = float(input('원의 반지름을 입력 하세요 : '))
# print('원의 넓이 : {:.2f}'.format(area(radius)))
# print('원의 둘레 : {:.2f}'.format(circumference(radius)))


# Question 28     ??????????? string or list

# def make_list():
#     list1 = []
#     for i in range(len(number)):
#         list1.append(number[i])



# def determine_duplicate(list1):
#     l = []
#     for i in range(len(list1)):
#         if list1[i] not in l:
#             l.append(i)
#     if len(l) == len(list1):
#         return True
#     else:
#         return False


# number = input('숫자를 입력 하세요 : ')
# final_list = make_list()
# print(final_list)
# if determine_duplicate(list1):
#     print(True)
# else:
#     print(False)



# Question 29         
# def count1(n):
#     count = 0 
#     for i in n:
#         if i == '1':
#             count += 1 
#     return count 


# number = input('수를 입력하세요 :')
# print(count1(number))


# Question 30
# def calculate_area(width,height):
#     area = (width * height) / 2 
#     return area 


# input1 = int(input('밑변 입력 --> '))
# input2 = int(input('높이 입력 --> '))
# print('면적은 {}'.format(calculate_area(input1,input2)))

 

# Question 31
# def calculate():
#     minute= seconds//60
#     second=seconds%60
#     hour=minute//60
#     minute%=60
#     return hour, minute, second

# seconds = int(input('초 입력 --> '))
# hour, minute, second = calculate()
# print('{}초는 {}시간 {}분 {}초 입니다'.format(seconds,hour,minute,second))



# Question 32   
# def determine():
#     average = (kor + eng + math) / 3 
#     if average >= 60 and (kor >= 40 and eng >= 40 and math >= 40):
#         return True 
#     else:
#         return False 

# kor, eng, math = map(int, input('국어 영어 수학 점수를 입력 하세요 : ').split())


# if determine():      # if는 여기가 True 일때만 밑에 코드를 실행하는거 
#     print('추카~~ 합격입니다.')
# else:      
#     print('아깝군요 ㅠㅠ 불합격입니다.')



# Question 33    ????????
# def primenumber(n):
#     for i in range(2,n):
#         if n % i == 0:
#             return False     
#         else:
#             return True   # 이걸 루프 밖에다가 놓아야되는데, 어떻게 실행이되는게 아니라, 잘못됬던것

# number = int(input('수를 입력하세요 : '))

# if primenumber(number):
#     print('{}은 소수입니다'.format(number))
# else:
#     print('{}은 소수가 아닙니다'.format(number))




# Queston 34
# def determine(p):
#     if len(p) >= 9:
#         return 'Good'
#     elif 9 > len(p) >= 5:
#         return 'Noraml'
#     else:
#         return 'Bad'


# password = input('password: ')
# print('Your Password : {}'.format(determine(password)))



# 두번째 풀어보기 
# Q2
# def nSum(a,b):
#     Sum = a + b
#     print('{} + {} = {}'.format(a,b, Sum))

# a, b = map(int, input('두개의 수를 입력하시오 : ').split())
# nSum(a,b)



# Q3
# def printing():
#     num = int(input('몇까지 출력 할까요? ==> '))
#     for i in range(num):
#         print(i+1)

# printing()


# Q4        
# def determine(input1):
#     print(input1)

# num_list = [1,2,3,4]
# determine(num_list)



# Q5
# def determine(n):
#     if n % 2 ==0:
#         print('{} is 짝수'.format(n))
#     else:
#         print('{} is 홀수'.format(n))

# num = int(input('수를 입력 --> '))
# determine(num)


# Q6
# import random 
# def dinner():
#     coin = random.choice(['앞', '뒤'])
#     if coin == '앞':
#         print('오늘 메뉴는 중국요리로 결정 되었습니다')
#     else:
#         print('오늘 메뉴는 일본요리로 결정 되었습니다')

# dinner()


# Q7
# def absolute_value(n):
#     if n < 0:
#         n = -n
#     return n

# num = int(input('수를 입력 하세요 : '))
# print('절대값은 {}입니다.'.format(absolute_value(num)))


# Q8 
# def determine(a,b):
#     if a > b:
#         return a
#     elif b > a:
#         return b


# a, b = map(int, input('2개의 수를 입력 하세요 : ').split())
# print('큰 수는 {}입니다'.format(determine(a,b)))



# Q10  
# def determine(l):
#     for i in range(len(l)):
#         if i == 0:
#             Max = Min = l[i]
#         else:
#             if l[i] > Max:
#                 Max = l[i] 
#             elif l[i] < Min:
#                 Min = l[i]
#     return Max, Min 
# or 
#return max(l), min(l)



# nlist = [50, 40, 60, 10, 70, 100, 30, 20]
# Max, Min = determine(nlist)
# print('가장 큰값 : {}'.format(Max))
# print('가장 작은값 : {}'.format(Min))


# Q11
# def Sum(a,b):
#     nSum = 0 
#     for i in range(a,b+1):
#         nSum += i 
#     return nSum 

# print(Sum(1,10))
# print(Sum(1,3)+Sum(7,10))


# Q12 
# def determine(s):
#     if 90 <= s <= 100:
#         print('A학점')
#     elif 80 <= s <= 89:
#         print('B학점')
#     elif 70 <= s <= 79:
#         print('C학점')
#     elif 60 <= s <= 69:
#         print('D학점')
#     elif s < 60:
#         print('F학점')


# score = int(input('점수 : '))
# determine(score)


# Q13
# def determine(a,b):
#     if a % b == 0:
#         return True 
#     else:
#         return False 


# a,b = map(int, input('두개의 수를 입력 하세요 : ').split())
# if determine(a,b):
#     print('{}은 {}의 배수입니다.'.format(a,b))
# else:
#     print('{}은 {}의 배수가 아닙니다.'.format(a,b))



# Q14
# def average():
#     print('5과목의 점수를 입력 하세요 : ')
#     nSum = 0 
#     for i in range(5):
#         score = int(input(''))
#         nSum += score 
#     mean = nSum / 5
#     return mean 


# if average() >= 60:
#     print('축하 !! 합격입니다')
# else:
#     print('불합격입니다 다시 도전하세요 ~')

    

# Q15
# def list_add(a, list1):
#     if a in list1:
#         print('이미 존재하고 있는 원소입니다')
#     else:
#         list1.append(a)
#         print('원소를 추가하였습니다')

# list_add(5, [1,3,7])
# list_add(7, [1,7,5])


# Q16
# def determine(l):
#     name = input('이름을 입력하세요 -->')
#     if name in l:
#         print('{}의 출근확인'.format(name))
#     else:
#         print('{}은 사원명단에 없습니다'.format(name))


# list1 = ['길동', '수지', '하나', '나라', '미순']
# determine(list1)


# Q17 
# def determine():
#     destination = input('어디를 가시겠습니까? --> ')
#     index = cities.index(destination)
#     print(index)
#     return prices[index]


# cities = ['춘천', '부산', '대구', '수원']
# prices = [5000, 30000, 2000, 10000]
# print('요금은 {} 원 입니다'.format(determine()))



# Q18
# def factorial(n):
#     result = 1
#     for i in range(1,n+1):
#         result *= i
#     return result 

# num = int(input('정수를 입력하세요 ? --> '))
# print(factorial(num))



# Q19
# def change(first, second):
#     return second, first 

# a, b = 10, 20
# first, second = change(a,b)
# print('a={} b={}'.format(first,second))


# Q20
# def Ha(n):
#     return 'Ha' * n
# print(Ha(3))


# Q21
# def concatenate(f,s):
#     result = f + s
#     return result 

# first = input('첫번째 문자열 --> ')
# second = input('두번째 문자열 --> ')
# print(concatenate(first,second))


# Q22
# def repeat(string,num):
#     for i in range(num):
#         print(string)


# string = input('문자열 --> ')
# num = int(input('몇번 반복할까요?'))
# repeat(string,num)



# Q23
# def determine():
#     for i in range(5):
#         input1 = input('단어를 입력하세요 -->')
#         if i == 0:
#             Max = Min = input1
#         else:
#             if len(input1) > len(Max):
#                 Max = input1
#             elif len(input1) < len(Min):
#                 Min = input1 
#     return Max, Min 


# long, short = determine()
# print('가장 긴단어는 : {}'.format(long))
# print('가장 짧은 단어는 : {}'.format(short))



# Q24
# def nSum(l):
#     Sum = 0 
#     for i in l:
#         Sum += len(i)
#     return Sum 

# fruits = ['apple', 'banana', 'tomato', 'kiwi']
# animals = ['bear', 'elephant', 'monkey']
# instruments = ['guitar', 'piano', 'harmonica']

# print(nSum(fruits))
# print(nSum(animals))
# print(nSum(instruments))



# Q25
# def difference(l):
#     Max = max(l)
#     Min = min(l)
#     result = Max - Min 
#     return result 

# score = [10, 40, 70, 60, 100, 20, 50]
# print(difference(score))



# Q26
# def reform(l):
#     final = []
#     for i in l:
#         final.append(i.capitalize())
#     return final

# sentence = input('문장을 입력 하세요 : ').split()
# print(reform(sentence))



# Q27
# import math 
# def area(r):
#     a = math.pi * (r ** 2 )
#     return a 

# def circumference(r):
#     c = 2 * math.pi * r 
#     return c 

# radius = float(input('원의 반지를을 입력 하세요 : '))
# print('원의 넓이 : {:.2f}'.format(area(radius)))
# print('원의 둘레 : {:.2f}'.format(circumference(radius)))



# Q28
# def determine(s):
#     tmp = []
#     for i in s:
#         if i in tmp:
#             return False
#         tmp.append(i)
#     return True 


# input1 = input('숫자를 입력 하세요 : ')
# print(determine(input1))



# Q29
# def determine(n):
#     cnt = 0 
#     for i in n:
#         if i == '1':
#             cnt += 1 
#     return cnt 

# num = input('수를 입력하세요 : ')
# print(determine(num))



# Q30
# def area(w,h):
#     result = (w * h) / 2
#     return result 

# width = int(input('밑변 입력 --> '))
# height = int(input('높이 입력 --> '))
# print('면적은 {}'.format(area(width, height)))


# Q31
# def determine(s):
#     hour = s // 3600 
#     minute = (s % 3600) // 60 
#     second = (s % 3600) % 60 
#     return hour, minute, second


# input1 = int(input('초 입력 --> '))
# hour, minute , second = determine(input1)
# print('{}초는 {}시간 {}분 {}초 입니다'.format(input1, hour, minute, second))


# or 


# def determine(second):
#     minute = second // 60 
#     second = second % 60 
#     hour = minute // 60 
#     minute = minute % 60 

#     return hour, minute, second


# input1 = int(input('초 입력 --> '))
# hour, minute , second = determine(input1)
# print('{}초는 {}시간 {}분 {}초 입니다'.format(input1, hour, minute, second))



# Q32
# def determine(l):
#     nSum = 0 
#     for i in l:
#         if int(i) < 40:
#             return False 
#         nSum += int(i)
#     average = nSum / len(l)
#     if average >= 60:
#         return True 
#     else: 
#         return False 


# result = input('국어 영어 수학 점수를 입력 하세요 : ').split()
# if determine(result):
#     print('추카~~ 합격입니다.')
# else:
#     print('아깝군요 ㅠㅠ 불합격입니다.')



# Q33
# def determine(n):
#     for i in range(2,n):
#         if n % i == 0:
#             return False 
#     return True 

# num = int(input('수를 입력 하세요 : '))
# if determine(num):
#     print('{}은 소수입니다.'.format(num))
# else:
#     print('{}은 소수가 아닙니다.'.format(num))



# Q34
# def determine(p):
#     if len(p) >= 9:
#         return 'Good'
#     elif 5 <= len(p) < 9:
#         return 'Normal'
#     elif len(p) < 5:
#         return 'Bad'

# password = input('password: ')
# print('Your Password : {}'.format(determine(password)))