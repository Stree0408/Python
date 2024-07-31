# input: 키보드에서 입력받아서 변수에 넣는것
# casting: 형 변환   ??/?

# 1 
# print('name--->', end=' ')
# name = input('name--->')
# print("안녕 ! ", name)


# 2 
# print('sign up information ')
# print('type your name: ', end='')
# name = input()
# age = input('type your age')
# print('your name and age are as follows.')
# print(name, ' ', age)

# TYPE : INT  FLOAT  STR  BOOL

# 3 
# a = input()   #DEFAULT ... STR '7'
# print(type(a))
# b = int(input())
# print(type(b))

# a,b,c = input('----> ').split()
# print(a,b,c)


# s1 = int(input('kor-->'))
# s2 = int(input('eng-->'))
# s1,s2 = input('국어 영어 점수를 입력하세요').split()
# s1 = int(s1)
# s2 = int(s2)
# print('국어 영어 점수의 합은 ', s1,s2,s1+s2)



# Question 1
# a = int(input('가로의 길이는 : '))
# b = int(input('세로의 길이는 : '))
# print('\n\n=>넓이는',a*b,'입니다')

# Question 2 
# pencil = 1000
# pen = 2000
# print('pencil =',pencil,'won')
# print('pen =',pen,'won\n\n')
# num_pencil = int(input('연필은 몇 개를 구입하시겠습니까? '))
# num_pen = int(input('펜은 몇 개를 구입하시겠습니까? '))
# total_price = (pencil * num_pencil) + (pen * num_pen)
# print('총 가격은',total_price,'원입니다.')

# Question 3 
# s1,s2,s3 = input('국어 영어 수학 점수를 입력: ').split()
# s1 = int(s1)
# s2 = int(s2)
# s3 = int(s3)
# print('\n총점은 {}점 평균은 {} 점 입니다'.format(s1+s2+s3,(s1+s2+s3)/3))

# Question 4 
# r = float(input('원의 반지름을 입력 하세요 : '))
# area = 3.14 * r * r 
# arc = 2 * 3.14 * r 
# print('\n\n원넓이 : {}'.format(area))
# print('원둘레 : {}'.format(arc))

# Question 5 
# 오백원 = int(input('500원 : '))
# 백원 = int(input('100원 : '))
# 오십원 = int(input('50원 : '))
# 십원 = int(input('10원 : '))
# print('\n\n=>동전의 금액 : {}원'.format(500*오백원+100*백원+50*오십원+10*십원))

# Question 6 
# a = int(input('초를 입력하시오 : '))
# b = a // 60 
# c = a % 60
# print('=>{}분 {}초 입니다'.format(b,c))

# or 

# t = int(input('초를 입력하시오 : '))
# s = t // 60 
# x = t % 60
# print('=>',s, '분', x,'초 입니다.')

# Question 7
# a = int(input('초를 입력하세요 : '))
# h = a // 3600
# m = (a%3600) // 60 
# s = (a%3600) % 60 
# print('\n\n=>{}시간 {}분 {}초입니다.'.format(h,m,s))


# Problem 7   물어볼꺼?????? 이렇게 쓰면 1시간보다 많을때는 1시간 88분 9초 이렇게 될텐데
# t = int(input('초를 입력하시오 : '))
# m=t//60
# t=t%60
# h=m//60
# m%=60
# hour = t // 3600
# min = (t - 3600) // 600 
# sec = (t - 3600) % 600
# print('\n\n=>',h, '시간', m,'분', t,'초입니다.')


# Question 8 
# a = input('소속을 입력 하세요 : ')
# b = input('학번을 입력 하세요 : ')
# c = input('이름을 입력 하세요 : ')
# print('\n\n=>당신은 {} 소속 {}학번 {} 이군요 ~~'.format(a,b,c))


# Question 9 
# a = int(input('받은돈 : '))
# b = int(input('상품의 총액 : '))
# print('\n\n부가세 : {}'.format(b*0.1))
# print('잔돈  : {}'.format(a-b))


# Question 10 
# year = 60 * 60 * 24 * 365
# print('1년은 {} 초입니다'.format(year))


# Question 11 
# a = int(input('몇kw를 사용하셨습니까 : '))
# 전기요금 = 1390 + 400 * a
# print('=>당신이 사용한 {}kw의 요금은 {} 원입니다'.format(a,전기요금))


# or


# a = int(input('몇Kw를 사용하셨습니까? :  '))
# basic = 1390
# kw = 400
# elec = basic + kw * a
# print('=>당신이 사용한', a, 'Kw의 요금은', elec,'원입니다')


