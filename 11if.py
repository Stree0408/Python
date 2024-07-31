# 1 
# age = int(input("당신의 나이는? "))
# if age == 20: 
#     print("당신은 20살 이 네요 ~")
# if age > 20 :
#     print("당신은 20살 보다 많네요 ~")
# if age < 20 :
#     print("당신은 20살 미만 이네요 ~")

# 2
# a = 10 
# b = 20
# if a<b: 
#     x=a+10
#     y=a*10
# print('x=',x,' ','y=',y)

# 3
# score = int(input('점수를 입력하세요 ---> '))
# if 90 <= score <= 100:   
#     grade = 'A'
# if 80 <= score < 90:
#     grade = 'B'
# if 70 <= score < 80:
#     grade = 'C'
# if 60 <= score < 70:
#     grade = 'D'
# if score < 60:
#     grade = 'F'
# print("score = %d, grade = %s" % (score, grade))

# 4 
# age = 25
# if age <= 15:
#     print("당신은 무료입장 입니다~")
# else:
#     print("당신은 1000원을 내셔야 합니다~")


# a = 25
# if a<3:
#     print(a)
# else:
#     print(100-a)
# print("---")
# print("***")

# 5
# age = 25
# if age == 10:
#     print("당신은 10살입니다")
# elif age == 20:
#     print("당신은 20살입니다")
# elif age == 30:
#     print("당신은 30살입니다")
# else:
#     print("당신은 기타누락자 !!!")

# print('***')

# 6 
# x, y = map(int, input('--->').split())
# if x > y:
#     Max = x
#     Min = y
# else:
#     Max = y
#     Min = x 
# print("Max = %d, Min = %d" % (Max,Min))

# 8 
# age = 10
# ym = "남자"
# if age == 10 and ym == "남자":
#     print("당신은 남자이고 10살 입니다 ~~")


# Question 2
# a = int(input('정수입력 : '))
# if a < 0:
#     print('{} 는 음수'.format(a))
# elif a > 0:
#     print('{} 는 양수'.format(a))

# Question 3 
# a = int(input('나이는 ? '))
# if a < 18:
#     print('당신은 입장료가 무료입니다')
# else:
#     print('당신은 입장료가 1500원입니다')

# Question 4 
# n= int(input('정수입력-->'))
# if n % 2 == 0:
#     flag=True
# else:
#     flag=False

# if flag:
#     print('{} 는 2 의 배수'.format(n))
# else: 
#     print('{} 는 2 의 배수가 아니다'.format(n))


# Question 5 
# a,b,c,d = map(int, input('구매한 물건 : ').split())
# if (a+b+c+d) >= 100000:
#     print('상품권을 받아 가세요~~')
# else: 
#     print('상품권을 받을 수 없습니다.')

# Question 6
# import random

# n1 = random.randint(1,100)
# n2 = random.randint(1,100)

# a = int(input('{}-{}='.format(n1,n2)))
# if a == n1-n2 :
#     print('맞습니다')
# else:
#     print('틀렸습니다')


# Question 7       
# import random

# n1 = random.randint(1,6)
# n2 = random.randint(1,6)
# a,b = input('두사람의 이름 입력 : ').split()
# print('{}의 주사위 숫자는 {}입니다.'.format(a,n1))
# print('{}의 주사위 숫자는 {}입니다.'.format(b,n2))
# if n1 > n2:
#     print('{}이 이겼슴니다!!!'.format(a))
# elif n2 > n1:
#     print('{}이 이겼슴니다!!!'.format(b))
# else:
#     print('비겼습니다!!!')

# Question 8 
# a = int(input('정수 입력 : '))
# if a % 2 == 0:
#     print('{}는 짝수'.format(a))
# else:
#     print('{}는 홀수'.format(a))

# Question 9 
# weight,height = map(int, input('몸무게와 키를 입력하세요 :').split())
# if (height-100) * 0.9 < weight :
#     print('다이어트가 필요하다')
# else:
#     print('다이어트 필요 없다')


# Question 10 
# a,b=map(int, input('두 수 입력 :').split())
# if b>a:
#     print(b-a)
# else: 
#     print(a-b)


# Problem 11   

# 0--->False   0만 아니면--->True    # not은 반대로 


# a=4
# if a%2==0:
# if not a%2:
#     print('oo')
# else:
#     print('xxx')
# year = int(input('--->'))
# if not year % 4 and year % 100 or not year % 400:
# if year % 4==0  and  year % 100!=0 or  year % 400==0:      # 이걸로 씀 
#     print(" 윤년 : %d"% year)
# else: 
#     print(" 평년 : %d"% year)

# Question 12
# toeic = 900
# eng = 'B'
# if toeic >=800 or eng == 'A':
#     print('길동이는 지원이 가능합니다~~')
# else:
#     print('길동이는 탈락')

# Question 13
# a,b,c,d = input('4과목의 학점을 입력하세요:').split()
# gpa = int(input('평균학점을 입력하세요: '))
# count = 0 
# if a == 'F':
#     count += 1 
# if b == 'F':
#     count += 1 
# if c == 'F':
#     count += 1 
# if d == 'F':
#     count += 1 
# if count >= 2 or gpa < 1:
#     print('상민은 학사경고를 받는다')
# else:
#     print('성민은 패스한다')

# Question 14
# import random

# cnt = random.randint(0,1)

# print('컴퓨터가 동전을 던집니다\n.\n.\n.')
# if cnt ==0:
#     print('앞면입니다 메뉴는 중국요리!')
# else:
#     print('뒷면입니다 메뉴는 일본요리!')

# Question 15 
# t = int(input('현재 온도를 입력하시오 : '))
# if t >= 25:
#     print('==>반바지를 입으세요')
# else: 
#     print('==>긴바지를 입으세요')

# Question 16
# import random 

# x = random.randint(1,100)

# print('난수를 발생합니다 : {}'.format(x))
# if x % 2 == 0 :
#     print('...짝수...')
# else:
#     print('...홀수...')

# Question 17 
# a,b,c,d = input('이름과 3과목의 점수를 입력하세요 :').split()
# b = int(b)
# c = int(c)
# d = int(d)
# if (b+c+d)/3 >= 60:
#     print('{}은 합격 하셨습니다 !'.format(a))
# else: 
#     print('{}은 탈락 하셨습니다 !'.format(a))

# Question 18
# a,b,c = map(int, input('3과목의 점수를 입력하세요 :').split())
# if a+b+c/3 >= 60 and a>40 and b>40 and c>40:
#     print('합격입니다')
# else:
#     print('불합격입니다')

# Question 19 
# a = int(input('정수를 입력하세요 : '))
# if a % 2 == 0 and a % 3 == 0 :
#     print('2와 3의 배수입니다')
# else:
#     print('2와 3의 배수가 아닙니다')

# Question 20 
# a = int(input('년를 입력하세요 :'))
# if a % 4 == 0 and a % 100 != 0 or a % 400 == 0 :
#     print('{} 은 윤년'.format(a))
# else:
#     print('{} 은 평년'.format(a))

# Question 21
# age = int(input('나이를 입력하세요 :'))
# if 10 <= age <= 19:
#     print('당신은 10대~')
# elif 20 <= age <= 29:
#     print('당신은 20대~')
# elif 30 <= age <= 39:
#     print('당신은 30대~')
# else:
#     print('기타')

# Question 22
# import random
# lottery = random.randint(10,99)
# digit1 = lottery // 10 
# digit2 = lottery % 10 

# a = int(input('복권번호를 입력하시오(10에서 99사이) : '))
# a1 = a // 10
# a2 = a % 10
# print('당첨번호는 {} 입니다'.format(lottery))
# if (digit1 == a1 or digit1 == a2) and (digit2 == a1 or digit2 == a2) :
#     print('상금은 100만원입니다.')
# elif (digit1 == a1 or digit1 == a2) or (digit2 == a1 or digit2 == a2) :
#     print('상금은 50만원입니다.')
# else:
#     print('상금은 없슴니다')

# 연산자 : 산술연산 : + - * // / %     연산순위 : * // / % + - 
#        관계연산자 : == < <= > >= != 
#        논리연산 : and or not       연산순위 : not and or 
# 연산순위  산술연산 > 관계연산 > 논리연산 
 
# Question 23  
# a,b,c = map(int, input('3개의 정수를 입력하세요 : ').split())
# if a > b > c :
#     print(a,b,c)
# if a > c > b :
#     print(a,c,b)
# if b > a > c:
#     print(b,a,c)
# if b > c > a :
#     print(b,c,a)
# if c > b > a :
#     print(c,b,a)
# if c > a > b :
#     print(c,a,b)

# or 
# a,b,c = map(int, input('3개의 정수를 입력하세요 : ').split())
# if a < b:
#     a,b = b,a 
# if a < c:
#     a,c = c,a 
# if b < c:
#     b,c = c,b
# print(a,b,c)

# Question 24 
# a,b,c = map(int, input('숫자 3개를 넣으세요 : ').split())
# Max = a 
# if b > a:
#     a,b = b,a 
# if c > a:
#     a,c = c,a
# if (b+c) > a :
#     print('=>삼각형의 결정조건이 만족합니다')
# else:
#     print('=>삼각형의 결정조건이 되지 않습니다')


# Question 25
# a,b,c,d,e,f = map(int, input('6개의 수를 입력 하세요 : ').split())
# if a > b:
#     Max = a 
# if b > a:
#     Max = b 
# if c > Max:
#     Max = c 
# if d > Max:
#     Max = d 
# if e > Max:
#     Max = e 
# if f > Max:
#     Max = f
# print('가장 큰 수는 {} 입니다'.format(Max))

# or

# a,b,c,d,e,f = map(int, input('6개의 수를 입력 하세요 : ').split())
# max = a 
# if max < b :
#     max = b
# if max < c :
#     max = c
# if max < d :
#     max = d 
# if max < e :
#     max = e 
# if max < f :
#     max = f 
# print(max)


# Question 26       
# a,b,c,d,e = map(int, input('5개의 수를 입력 하세요 : ').split())
# if a < b:
#     Min = a 
#     Min2 = b
# if b < a: 
#     Min = b 
#     Min2 = a 
# if c < Min : 
#     Min2 = Min 
#     Min = c 
# elif c < Min2:
#     Min2 = c 
# if d < Min : 
#     Min2 = Min 
#     Min = d 
# elif d < Min2:
#     Min2 = d
# if e < Min : 
#     Min2 = Min 
#     Min = e
# elif e < Min2:
#     Min2 = e 
# print('두 번째로 작은 수는 {} 입니다'.format(Min2))

# or

# a,b,c,d,e = map(int, input('5개의 수를 입력 하세요 : ').split())
# min = a

# if b<min:
#     smin = min
#     min = b
# else:
#     smin = b
    
# if c<min:
#     smin = min
#     min = c
# elif c<smin:
#     smin = c

# if d<min:
#     smin = min
#     min = d
# elif d<smin:
#     smin = d

# if e<min:
#     smin = min
#     min = e
# elif e<smin:
#     smin = e
# print('두 번째로 작은 수는 {}입니다'.format(smin))


# random.choice 쓰는법
# import random
# n = random.choice([11,7,6,8,99])
# print(n)


# Question 27 
# import random
# time = random.randint(1,24)
# sunny = random.choice([True,False])

# print('좋은 아침입니다. 지금 시각은 {}시 입니다'.format(time))
# if sunny == True:
#     print('현재 날씨가 화창합니다.')
# else:
#     print('현재 날씨가 화창하지 않습니다.')
# if 6 <= time <= 9 and sunny == True:
#     print('종달새가 노래를 합니다')
# else:
#     print('종달새가 노래를 하지 않는다')

