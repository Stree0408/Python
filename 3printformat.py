# print("100")
# print("100" + "100")
# # print("100" + 100)
# print(100+100)

# 정수형 : %d   실수형 : %f   문자형 : %s
# print("%d" % (100))
# print("**%d ... %d ..." %(100,200))
# print("total = %d won" % (100+100))

# print("%d" % 123)
# print("%15d" % 123)
# print("%015d" % 123)

# print("%f" % 123.45)
# print("%17.1f" % 123.45)
# print("%17.3f" % 123.45)

# print("%20s" % "Python")

# print("%d %d" % (65, 90))
# print("%x %x" % (65,90))
# print("%o %o" % (65,90))

# print("%10s" % ('abcd'))
# print("%-10s##" % ('abcd'))
#print("%*s" % (-10, 'abcd')) ????????????????????????????
# print("%.2s" % ('abcd'))
# print("%-10.2s..." % ('abcd'))
# print("%10.2s" % ('abcd'))

# print('%-10s***' % 'abcd')    ---> 이거만 알면됨
# print("%*s***" % (-10,'abcd'))    ????????????????????????

# 6 
# print('{},{},{}'.format('a','b','c'))
# print('{0},{1},{2}'.format('a','b','c'))
# print('{2},{1},{0}'.format('a','b','c'))
# print('{0},{1},{1},{2}'.format('a','b','c'))

# 7 
# import math
# print('{:<20}{:<20}'.format('apple','banana'))
# print('{:>20}{:>20}'.format('apple','banana'))
# print('{:^20}{:^20}'.format('apple','banana'))

# print('{0:b} {0:o} {0:d} {0:X} {0:x}'.format(1000))
# print('{0} {0:f} {0:.2f}'.format(math.pi))

# print('{:%}'.format(0.045))       ????????????????????
# print('{:,}'.format(100000000000000))  ??????????
# print(format(12345678, ','))       ????????

# 8
# name = 'Kevin'
# work = 'IT company'
# num1 = 5.3
# num2 = 4.7517
# print("i'm", name, 'and work in', work)
# print("i'm {} and work in {} ".format(name,work))
# print("This is {:8.2f}, {:8.3f}".format(num1, num2))

# 9
# from datetime import datetime

# now = datetime.now()
# print('Today is {:%y-%m-%d}'.format(now))
# print('Current time is {:%H :%M :%S}'.format(now))

# 10 
# from time import sleep
# for i in range(100):
#     msg = '\r진행률 %d%%'%(i+1)
#     print(' '*len(msg),end='')
#     print(msg,end='')
#     sleep(0.1)

# import sleep == 시간을 잠시 멈추는거
# \r == 라인의 처음으로


# Question 1 
# 하나, 둘 
# 1, 2, 3

# 작품번호:   365, 작품선호도:   9.23
# 작품번호:   468, 작품선호도:   8.12

# Question 2 
# 하나, 둘 
# 1, 2, [3, 4, 5]
# print('{0}, {1}, {2}'.format(1, 2, [3,4,5]))
# 칸이 비어도 하나, 둘, 셋

# c, b, a 
# 오렌지를 먹은 지 얼마나 오렌지

# Question 3 
# a = int(input('첫 번째 수를 입력 하세요 :'))
# b = int(input('두 번째 수를 입력 하세요 :'))
# print('\n\n{} / {} = {:.2f}'.format(a,b,a/b))

# or 
# f = int(input('첫 번째 수를 입력 하세요 :'))
# s = int(input('두 번째 수를 입력 하세요 :'))
# print('\n',f, '/', s ,'=' ,"%.2f" % (f/s))
# print('\n%d / %d =  %.2f' % (f, s, f/s))
 
# Question 4 
# print('체질량지수(BMI)를 계산해 봅시다.\n\n')
# weight = int(input('체중을 입력하세요: '))
# height = int(input('키를 입력하세요: '))
# bmi = weight / ((height/100) * (height/100))
# print('\n\nBMI는 {:.0f}% 입니다.'.format(bmi))
# print('\n\nBMI는 %d%% 입니다.'%(bmi))

# % 쓸때는 % 출력하려면 %%처럼 % 두번 써야됨

# Question 5 
# s1,s2 = input('국어 영어 점수를 입력하세요  ').split()
# s1 = int(s1)
# s2 = int(s2)
# print('국어 영어 점수의 합은 {} 점 입니다'.format(s1+s2))
# print('국어 영어 점수의 평균은 {:.1f} 점입니다'.format((s1+s2)/2))
# print('국어 영어 점수의 합은 %d 점 입니다'%(s1 + s2))
# print('국어 영어 점수의 평균은은 %.1f 점입니다' % ((s1 + s2)/2))

# Question 6 
# print('{} : 바나나를 먹으면 반하니?'.format('농담1'))
# print('{} : 시드니에 가면 꽃이 시드니?'.format('농담2'))

# Question 7 
# print('나의 절친은 {}, {}, {} 이렇게 3명이야'.format('김하나','박하늘','한이슬'))

# Question 8 
# print('나의 절친은 {2}, {1}, {0} 이렇게 3명이야'.format('김하나','박하늘','한이슬'))

# Question 9
# a = input('상품명을 입력 하세요 : ')
# b = int(input('단가를 입력 하세요 : '))
# c = int(input('수량을 입력 하세요 : '))
# print('\n\n=>%s %d 대의 가격은 %d입니다.' % (a,c,b*c))

# # Question 10 
# a = int(input('수량을 입력하세요 : '))
# b = int(input('단가를 입력하세요 : '))
# print('\n\n%6s%12s%13s' % ('amount','dis','pay'))
# print('\n\n{:>6}{:>12}{:>13}'.format('amount','dis','pay'))
# print('=' * 31)
# c = a *b
# d = c * 0.25
# e = c - d 
# print('%6d%12d%13d' % (c,d,e))

# Question 11
# a = int(input('첫 번째 수를 입력 하세요 : '))
# b = int(input('두 번째 수를 입력 하세요 : '))
# print('\n\n <<연산결과>>')
# print('{:.1f} + {:.1f} = {:.1f}'.format(a,b,a+b))
# or 
# print('%.1f + %.1f = %.1f' % (a,b,a+b))
# print('%.1f - %.1f = %.1f' % (a,b,a-b))
# print('%.1f * %.1f = %.1f' % (a,b,a*b))
# print('%.1f / %.1f = %.1f' % (a,b,a/b))

# Question 12
# a = input('이름을 입력 하세요 : ')
# b = int(input('국어점수를 입력 하세요 : '))
# c = int(input('영어점수를 입력 하세요 : '))
# d = int(input('수학점수를 입력 하세요 : '))
# print('\n\n%26s' % '** 성적표 **')
# print('\n\n%-7s%3s%7s%8s%7s%7s' % ('name','kor','eng','math','sum','ave'))
# print()
# print('=' * 39)
# print('\n%-7s%3d%7d%8d%7d%7.2f' % (a,b,c,d,b+c+d,(b+c+d)/3))

# or

# a = input('이름을 입력 하세요 : ')
# b = int(input('국어점수를 입력 하세요 : '))
# c = int(input('영어점수를 입력 하세요 : '))
# d = int(input('수학점수를 입력 하세요 : '))
# print('\n\n{:>26}'.format('** 성적표 **'))
# print('\n\n{:<7}{:>3}{:>7}{:>8}{:>7}{:>7}'.format('name','kor','eng','math','sum','ave'))
# print()
# print('=' * 39)
# print('\n{:<7}{:>3}{:>7}{:>8}{:>7}{:>7.2f}'.format(a,b,c,d,b+c+d,(b+c+d)/3))


# Question 13 
# a,b,c = input('3개의 수를 입력 하세요 : ').split()
# a = int(a)
# b = int(b)
# c = int(c)
# print('\n\n입력한 값 : {} {} {}'.format(a,b,c))
# print('합   계 : {}'.format(a+b+c))
# print('평   균 : {:.2f}'.format((a+b+c)/3)) 