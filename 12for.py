# for i in range(0, 5, 1):
#     print(i, end=' ')

# print()
# l=[1,2,5,7,9]
# for i in l:
#     print(i, end=' ')
#     print('****')

# for d in 'gaag':
#     print(d)

# iterator : repeat

# 6 
# n = int(input('--->'))
# nSum = 0
# for i in range(1, n+1):
#     print("n= %d " % i )
#     nSum += i
# print("Sum = %d " % nSum)

# 7 
# n = int(input('---> '))
# nSum = 0 
# for i in range(0,n+1,4):     #nSum = sum(range(0, n+1, 4))
#     nSum += i 
# print("n = %d : nSum = %d" % (n, nSum))


# 'A':65 ~ 'Z':90    'a':97 ~ 'z':122    '0':48 ~ '9':57
# 'A'   ASCII code 알아보기
# print(ord('a'))
# 65 code 값의 문자 알아보기
# print(chr(65))



# 0x == 16진수 나타날때 쓰는거, 지금은 무시

# 8       ?????????????????????
# nAlphabet = nHanGul = nOthers = 0
# for s in "Python?파이썬!":
#     if 0x41 <= ord(s) <= 0x5A or 0x61 <= ord(s) <= 0x7A:
#         print('Alphabet = ', s)
#         nAlphabet += 1
#     elif 0xAC00 <= ord(s) <= 0xD7A3:
#         nHanGul += 1
#         print('HanGul = ', s)
#     else:
#         print('Others = ', s)
#         nOthers += 1  


# print("\n알파벳 = %d" % nAlphabet)
# print("한글  = %d" % nHanGul)
# print("기타  = %d" % nOthers)

# l = '12345'
# print(l)
# print(l[0])
# print(l[4])

# len 익숙해지기

# l = '1234567'
# print(len(l))
# print(len(l)-1)

# l = [1,2,3,4,5,6]
# print(len(l))

# l = (1,2,3,4,5,6)
# print(len(l))

# l = {1,2,3,4,5,6}
# print(len(l))

# 9 
# sID = input("주민번호 입력 : ")    #숫자만 13자리
# W = (2,3,4,5,6,7,8,9,2,3,4,5)
# nSum = 0 
# for i in range(len(sID) - 1 ):
#     nSum += W[i] * int(sID[i])
#     print(sID[i])
# nCheckDigit = (11 - nSum % 11 ) % 10 

# if int(sID[-1]) == nCheckDigit:
#     print("{}은 올바른 주민번호".format(sID))
# else:
#     print("{}은 잘못된 주민번호".format(sID))

# 10 
# year, month, day = map(int, input('년 월 일 --->').split())
# nDays = 0 
# # 년도 처리
# for y in range(1,year):
#     if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
#        nDays += 366
#     else:
#         nDays += 365
        
# # 월 처리
# mDays = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)   # 월별 날짜
# for m in range(month-1):
#     nDays += mDays[m]

# # 당해(year)년도 윤년판단
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 and month>2:
#     nDays += 1 
#     #윤년이고 2월보다 크면
#     # 2월이 29일
#     #1/1/1/ ~ 어제까지 총 일수

# # 일처리 
# sWeek = "일월화수목금토"
# k = nDays%7 
# print("{}년 {}월 {}일은 {}요일입니다.".format(year, month, day, sWeek[k]))



   
# # 당해(year)년도 윤년판단
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 and month>2:
#     nDays +=1
#  #윤년이고 2월보다 크면
#      # 2월이 29일 
#      # #1/1/1 ~ 어제까지 총 일수
# #일처리
# sWeek = '일월화수목금토'
# k = nDays%7
# print("{0}년 {1}월 {2}일은 {3}요일입니다.".format(year, month, day, sWeek[k]))

# 11
# names =["홍길동", "강강찬", "김가을"]
# for n in names:
#     print("힘내라!!! ", n)


# Question 1 
# for i in range(3):
#     print(i)

# Question 2 
# for i in range(5,0,-1):
#     print(i, end=' ')

# ex) 
# a = 's'
# print(a + '*')
# --> s*

# Question 3 
# for spelling in 'PYTHON_SPELLING':
#     print(spelling + '*' , end =' ')

# Question 4 
# for i in range(1,11):
#     print('{}.. 파이썬은 재미 있어요 ~~'.format(i))

# Question 5
# for i in range(2,21):
#     print(i, end=' ')

# Question 6
# for i in range(10,55,5):
#     print(i, end=' ')

# Question 7 
# a = input('이름 :')
# b = int(input('문제 개수:'))
# print('*' * 20 )
# count = 0 
# for i in range(b):
#     c = input('문제를 해결했나요>(y/n) : ')
#     if c == 'y':
#         count += 1 
# print('{}학생은 총 {} 문제를 해결했습니다'.format(a,count))

# Question 8
# print('*** 카운트 다운 ~~')
# for i in range(10,0,-1):
#     print('{} 일 남았습니다'.format(i))
# print('드디어 Dday 입니다!!!')

# Question 9  
# for i in range(1,11):
#     print(i, end=' ')
#     if i % 3 == 0 :
#         print()

# break continue

# for i in range(1, 10, 1):
#     print(i)
#     if i == 3:
#         break
# print('....')

# continue --> 아래 코드를 실행하지 않고 건너뜀 

# for i in range(1,10,1):
#     if i % 2 == 0:
#         continue
#     else:
#         print(i)
#     print('****')


# Question 10  
# a = 1000
# count = 0 
# for i in range(1000000):
#     a *= 1.07
#     count += 1 
#     if a >= 2000:
#         break
# print('{}년이 걸립니다.'.format(count))

# or (without using count)

# s = 1000
# for i in range(1,1000):
#     s *= 1.07
#     if s >= 2000:
#         break
# print('{}년이 걸립니다.'.format(i))

    
# Question 11
# l = [1,2,5,6,9]    
# for i in l:
#     print('9 * {} = {}'.format(i,(9*i)))

# or (한번에 푸는 방법)

# for i in [1,2,5,6,9]:
#     print('9 *',i,'= ',9*i)


# Question 12
# a = int(input('몇 단을 출력 할까요 : '))
# for i in range(1,a+3):
#     print('{} * {} = {}'.format(a,i,a*i))

# \b 앞에 글자 지우는거 

# Question 13
# Sum = 0 
# for i in range(1,11):
#     print(i, end='+')
#     Sum += i 
# print('\b={}'.format(Sum))

# ex)
# for i in range(3):
#     print(i)
# print('***')


# Question 14 
# print('4!=', end='')
# multiple = 1 
# for i in range(4,0,-1):
#     print(i, end='*')
#     multiple *= i 
# print('\b={}'.format(multiple))


# Question 15 
# Sum = 0
# a = int(input('몇개의 수를 입력하시겠습니까  ? : '))
# for i in range(1,a+1):
#     b = int(input('{}번째 수를 넣으세요 : '.format(i)))
#     Sum += b
# print('=>합={}'.format(Sum))

# Question 16
# a = int(input('막대#의 높이 : '))
# for i in range(a):
#     print('#', end='')

# Question 17
# count = 0
# a = int(input('숫자를 입력하세요: '))
# for i in range(1,a):
#     if i % 3 == 0:
#         count += 1 
# print('=>1부터 {} 사이에 존재하는 3의 배수는 {}개 입니다.'.format(a,count))

# Question 18
# a = int(input('정수를 입력하세요 : '))
# print('=>{} 의 약수는 '.format(a), end='')
# for i in range(1,a+1):
#     if a % i == 0:
#         print(i, end =' ')
# print('\b입니다')

# Question 19
# Sum = 0
# for i in range(1,100000):
#     a = int(input('{}번째 정수를 입력하세요 : '.format(i)))
#     if a == 999:
#         break
#     Sum += a 
#     Average = Sum / i
# print('=>합계 : {}'.format(Sum))
# print('=>평균 : {}'.format(Average))

# Question 20 
# Sum = 0 
# a = 2 
# for i in range(15):
#     Sum += a 
#     print(a, end='+')
#     a += 6 
# print('\b \n합={}'.format(Sum))      # \b 다음에 \n가 올때는 space 한칸이 있어야 \b가 작동함

# Question 21
# Sum = 0 
# a = 2 
# for i in range(10):
#     Sum += a
#     print(a, end=' ')
#     a *= 3
# print('\n합={}'.format(Sum))

# Question 22
# count = 1 
# Mgrade = int(input('나의 점수는 : '))
# for i in range(1,6):
#     Fgrade = int(input('{}번 친구의 점수 :  '.format(i)))
#     if Fgrade > Mgrade:
#         count += 1 
# print('\n\n=> 나는 {}등 입니다'.format(count))
    
# Question 23    
# a = int(input('입력될 수의 개수는 : '))
# print('\n')
# for i in range(1,a+1):
#     b = int(input('{}번째 수를 입력하세요 : '.format(i)))
#     if i == 1:
#         Max = Min = b 
#     if b > Max:
#         Max = b 
#     elif b < Min:
#         Min = b
# print('\n\n=>최대값={}'.format(Max))
# print('최소값={}'.format(Min))

# Question 24 
# Sum = 0 
# for i in range(1,5):
#     Sum += i 
#     print('{} 까지의 합={}'.format(i,Sum))


# Question 25    
# print('=' * 12)
# print('{:>2}{:>9}'.format('n','nsqr'))
# print('=' * 12)
# print()
# for i in range(1,6):
#     print('{:>2}{:>7}'.format(i,i**2))


# Question 26
# Sum = 0 
# for i in range(1,11):
#     Sum += i 
#     print(i, end=' ')
#     if i % 3 == 0:
#         print('== 합 {}\n'.format(Sum) )
# print('   == 합 {}'.format(Sum))


# Question 27 
# a = int(input('몇 번 출력 ? : '))
# print('\n')
# for i in range(1,a+1):
#     print('You did a good job! - {}번쩨'.format(i))

# Question 28     
# names = ["홍길동","김가나","박하늘","한바다","이고은"]
# for i in range(5):
#     print('{} {}'.format(i,names[i]))

# or 
   
# Using enumerate(열거하다)    
# names = ["홍길동", "김가나", "박하늘", "한바다", "이고은"]
# for n,i in enumerate(names):          # enumerate가 앞에 변수, 즉 n에   names가 뒤에 변수, 즉 i에 들어간다 
#     print('{} {}'.format(n,i))

# enumerate 아무것도 안주면 0부터 1씩 증가. 값을주면 그값부터 1씩증가

# list 뽑는 방법
# number = [1,2,3,4,5 ]
# print(number[1])
# l=['aaa','bbb','ccc']
# print(l[1])

# Question 29 
# word_list = ['scramble','kindly','do','learn']
# for i in word_list:
#     print('un{}'.format(i))

# Question 30
# for i in range(1,6):
#     print('{}번째 알파벳은 {}'.format(i, chr(96+i)))

# or

# alphabet = 'abcde'
# for i in range(1,6):
#     print('{} 번째 알파벳은 {}'.format(i,alphabet[i-1]))

# Question 31
# score = [100, 30, 50, 70, 80, 60]
# for i in score:
#     if i >= 70:
#         print('{} 번 학생은 통과'.format(i))
#     else:
#         print('{} 번 학생은 불합격입니다'.format(i))

# Question 32 
# fruits = ['딸기','사과','바나나','수박','포도']
# for i in range(4,-1,-1):
#     print(fruits[i])
 
# Question 33      
# mixlist = ['a','5','b','g','3','8','6','m']
# for i in mixlist:
#     if 97 <= ord(i) <= 122:
#         print('{} => 문자'.format(i))
#     elif 48 <= ord(i) <= 57:
#         print('{} => 숫자'.format(i))

# Question 34 
# mixlist = ['apple', '5', 'banana', 'grape', 3, 8, 6, 'melon']
# for i in mixlist:
#     if type(i) == str:
#         print('{} => 문자열'.format(i))
#     elif type(i) == int:
#         print('{} 숫자'.format(i))


# Question 35
# a = int(input('수를 입력하세요  : '))
# b = int(input('수를 입력하세요  : '))
# print('\n')
# for i in range(1,a+1):                        # division or modulo by zero == error
#     if a % i == 0 and b % i == 0:
#         Max = i
# print('=>{}과 {}의 최대공약수는 {}입니다'.format(a,b,Max)) 


# Question 36
# count = 0 
# a = 100 
# for i in range(1,10000):
#     a -= i 
#     count += 1 
#     if a < 0 :
#         break
# print('=> 처음으로 음수가 되는 변수의 값과 n의 값은 : {} {}'.format(a,count))

# or

# a = 100
# for i in range(1,100):
#     a -= i
#     if a < 0:
#         print('=> 처음으로 음수가 되는 변수의 값과 n의 값은 : {}  {}'.format(a,i))
#         break

# Question 37          
# a = int(input('수를 입력하세요  : '))
# r = True
# for i in range(2,a):
#     if a % i == 0:
#         r = False 
#         break  
# if r:
#     print('=>소수')
# else:
#     print('=>소수가 아님')

    
# Question 38
# a = 100
# for i in range(1,51):
#     print('{} + {} = {}'.format(i,a,i+a))
#     a -= 1
# print('합 = {} * {} = {}'.format(i+a+1, i, (i+a+1) * i ))

# Question 39 
# a = 0 
# b = 0
# c = 1 
# Sum = 0 

# num = int(input('수열의 개수를 입력하세요  : '))
# print('\n')
# for i in range(num):
#     Sum += c 
#     print(c, end ='+')
#     a = b 
#     b = c 
#     c = a + b 
# print('\b \n합={}'.format(Sum))

# Question 40 
# Sum = 0 
# for i in range(5,55,5):
#     if i % 2 != 0:
#         print(i, end=' ')
#         Sum += i
# print('\n합={}'.format(Sum))

# Question 41

# 1
# a = 1 
# Sum = 0 
# for i in range(7):
#     print(a , end=' + ')
#     Sum += a
#     a += (i+1)
# print('\b\b \n합= {}'.format(Sum))

# 2
# Sum = 0 
# for i in range(10):
#     if (i+1) % 2 != 0 :
#         print((i+1), end=' - ')
#         Sum += i 
#     elif (i+1) % 2 == 0 :
#         print((i+1), end=' + ')
#         Sum -= i 
# print('\b\b \n합={}'.format(Sum))

# or

# sum = 0
# p=1
# for i in range (1,11):
#     i2=i*p  
#     print(i2,end='')
#     sum += i2 
#     if p<0:
#         print('+', end='')
#     p= -p # p=p * -1
# print('\b \n합={}'.format(sum))

# 3 
# p = 1 
# Sum = 0 
# for i in range(5,55,5):
#     i2 = i * p 
#     Sum += i2
#     print(i2, end='')
#     if p < 0 :
#         print('+', end='')
#     p = -p
# print('\b \n합={}'.format(Sum))

# 4 
# Sum = 0 
# i2 = 1
# p = 1 
# for i in range(7):
#     i3 = i2 * p 
#     print(i3, end='')
#     Sum += i3
#     i2 += (i+1)
#     p = -p
#     if (i+1) % 2 ==0:
#         print(end ='+')
# print('\n합= {}'.format(Sum))


# 4)
# sum=0
# p=1
# i2 = 1
# for i in range(7):
#     i2 += i
#     i3 = i2 * p
#     print(i3, end='')
#     sum += i3
#     if p < 0:
#         print('+', end='')
#     p= -p
# print('\n합={}'.format(sum))



# Question 42
# Sum = 0 
# oddsum = 0 
# a = int(input('첫 번째수를 입력하세요 : '))
# b = int(input('두 번째를 입력하세요 : '))
# print('=>사이의 수 : ', end='')
# for i in range(a+1,b):
#     print(i, end=' ')
#     Sum += i 
#     if i % 2 != 0:
#         oddsum += i 
# print('\n합={}'.format(Sum))
# print('홀수의 합={}'.format(oddsum))

# Question 43        
# Sum = 0 
# a = input('정수를 입력 하세요  : ')
# print('\n\n각 자리의 값  : ', end='')
# for i in a:
#     i = int(i)
#     print(i, end=' ')
#     Sum += i 
# print('\n각 자리값 의 합 : {}'.format(Sum))

# 스트링 뽑기 
# a = '12345'
# print(a, a[1],a[2])
# 12345 2 3 

# Question 44 
# a = input('정수를 입력 하세요  : ')
# print('\n')
# for i in range(len(a)-1, -1, -1):
#     print('{}의 자리 :{}'.format(10 ** (4-i),a[i]))

# a='4567'
# for i in a:
#     print(-int(i))

# a ='4567'
# for i in a:           # a에 있는 값을 앞에서부터 차례로 i에 담는다 
#     print(a[i])       # 이 말은 a[4], 근데 4번째가 없음으로 에러가뜬다 


# hint for Question 45 
# a=''
# a+='1'
# print(a)
# 1

# a+='5'
# print(a)
# 15
# a = int(a)
# b = a *3 

# Question 45 
# a = input('정수를 입력 하세요  : ')
# b = ''
# print('뒤집은 값 : ', end='')
# for i in range(len(a)-1,-1,-1):
#     b += a[i]
# print(b)
# print('3배수  값 : {}'.format(int(b)*3))

# Question 46      
# for i in range(1,11):
#     a = int(input('{}번째수를 입력하세요 : '.format(i)))
#     b = 10 - a
#     if b < 0:
#         b = -b
#     if i == 1: 
#         Minb = b          # 비교는 Minb로
#         Mina = a          # 하지만 원하는 값은 a이기 때문에 Mina라는 변수에 a를 저장
#     if b < Minb:
#         Minb = b 
#         Mina = a 
# print('\n\n=>10에 가장 가까운 수는 {}'.format(Mina))

# or 

# for i in range(1,11):
#     a = int(input('{}번째수를 입력하세요 : '.format(i)))
#     b = abs(10 - a)            # 절대값 구하는 함수 abs
#     if i == 1: 
#         Minb = b 
#         Mina = a 
#     if b < Minb:
#         Minb = b 
#         Mina = a 
# print('\n\n=>10에 가장 가까운 수는 {}'.format(Mina))


# Problem 46


# 절대값 구하는 함수 d= abs(d)
# for i in range(1,11):
#     n = int(input('{}번째수를 입력하세요 : '.format(i)))
#     d = n - 10
#     if d < 0 :
#         d = -d
#     if i == 1 :
#         minn = n 
#         mind = d
#     if d< mind :
#         mind = d
#         minn = n
# print('=>10에 가장 가까운 수는 {}'.format(minn))


# Question 47 
# oddsum = 0 
# evensum = 0 
# multiple3 = 0 
# count = 0 
# multiple34 = 0 
# for i in range(1,31):
#     if i % 2 != 0 :
#         oddsum += i 
#     elif i % 2 == 0:
#         evensum += i 
#     if i % 3 == 0:
#         multiple3 += i 
#     if i % 3 == 0 and i % 4 == 0:
#         count += 1
#         multiple34 += i 
# print('홀수의 합 = {}'.format(oddsum))
# print('짝수의 합 = {}'.format(evensum))
# print('3의 배수의 합 = {}'.format(multiple3))
# print('3과 4의 공배수의 개수 = {}개  합={}'.format(count,multiple34))

# Question 48  
# Sum = 0 
# for i in range(1,11):
#     print(i, end=' ')
#     if i % 3 == 0:
#         Sum = i + (i-1) + (i-2)
#         print('== 합 {}'.format(Sum))
# print('   == 합 {}'.format(i))

# or 

# Sum = 0 
# for i in range(1,11):
#     Sum += i 
#     print(i, end=' ')
#     if i % 3 == 0:
#         print('== 합 {}'.format(Sum))
#         Sum = 0 
# print('   == 합 {}'.format(Sum))


# Question 49 
# Sum = 0 
# for i in range(1,1000):
#     a = float(input('몸무게를 입력하시오(0:종료) : '))
#     if a == 0:
#         break
#     if a < 0 or a >= 200:
#         continue 
#     if i == 1:
#         Max = Min = a 
#     if a < Min:
#         Min = a 
#     if a > Max:
#         Max = a 
#     Sum += a

# print('\n\n최대값 : {:.2f}'.format(Max))
# print('최소값 : {:.2f}'.format(Min))
# print('합={:.2f}'.format(Sum))
# print('평균={:.2f}'.format(Sum/(i-1)))        # i 계산할때 break 걸린거는 취소, 하지만 continue 걸린거는 그대로 count 


    

# Question 50 
# import random

# n = random.randint(1,100)


# for i in range(10000):
#     a = int(input('정답을 넣으세요 : '))
#     if a < 0:
#         break
#     if n > a:
#         print('{}보다는 큰 수를 넣으세요 ~'.format(a))
#     elif n < a:
#         print('{}보다는 작은 수를 넣으세요 ~'.format(a))
#     if n == a:
#         print('\n\n축하합니다 ~~ 드디어 정답을 맞추셨군요 !!!')
#         break

# Question 51
# time.sleep()         # ()초 동안 멈춰라 --> ()초 동안 멈추고 코드가 나옴

# import time, random
# l = []
# for i in range(5):
#     l.append(random.randint(1,9))
# print('기억력 테스트입니다\n화면에 보이는 숫자를 기억하였다가 다시 쓰면 됩니다.')
# print('다음의 숫자를 기억하세요  => ' , end=' ')
# for d in l:
#     print(d, end=' ')
# print()         # 원래는 바로 time.sleep() 쓰면 되는데 for문 쓰고 바로 time.sleep() 쓰면 파이썬에서 time.sleep()이 제데로 작동안돼서 이렇게 씀 
# time.sleep(2)
# for i in range(20):
#     print()

# count = 0 

# u = list(map(int, input('기억한 숫자를 입력 하세요 : ').split()))     # 한 줄에 입력된 숫자를 split()으로 잘라서 int 형으로 바꾼 후에 리스트에 넣어라 
# for i in range(len(l)):
#     if l[i] == u[i]:
#         count += 1 

# print('{}개 맞았습니다!!!'.format(count))



# Question 52
# nDays = 0 
# year = int(input('년도 : '))
# for i in range(1,year+1):
#     if i % 4 ==0 and i % 100 != 0 or i % 400 == 0:
#         nDays += 366
#     else:
#         nDays += 365
# print('1년부터 {}냔도까지는 {}일'.format(year,nDays))


# Question 53    
# a = int(input('수를 입력하세요 : '))
# r = True
# for i in range(2,a):
#     if a % i == 0:
#         r = False 
#         break
# if r:
#     print('결과 => 소수')
# else:
#     print('결과 => 소수가 아닙니다')




# 43 힌트
# s=input()
# print(s)
# print(int(s[0]))
# print(s[1])


# s='476'

# for d in s:
#     print(s[0])

# print()
# for d in range(len(s)):
#     print(d, s[d])

# Problem 43
# sum1 = 0 
# s = input('정수를 입력 하세요: ')
# print('각 자리의 값 :', end=' ')
# for i in range(len(s)):
#     print((int(s[i])), end=' ')
#     sum1 += int(s[i])
# print('\n각 자리값의 합 : {}'.format(sum1))

# Problem  44
# a = 1
# s = input('정수를 입력하세요  : ')
# for i in range(a,len(s)+1):
#     print('{}의 자리 :{}'.format(a, int(s[-i])))
#     a *= 10
    
# Problem 45 

# s='123'
# print(s)
# s1=int(s[::-1])
# print(s1)

# s = input('정수를 입력하세요 : ')
# print('뒤집은 값 : {}'.format(int(s[::-1])))
# print('3배수 값 : {}'.format(int(s[::-1])*3))






# 두번째 풀어보기 
# Q1
# for i in range(3):
#     print(i)


# Q2
# for i in range(5,0,-1):
#     print(i, end=' ')


# Q3
# for spelling in 'PYTHON_SPELLING':
#     print(spelling + '*')   


# Q4
# for i in range(1,11):
#     print('{}.. 파이썬은 재미 있어요 ~~'.format(i))


# Q5
# for i in range(2,21):
#     print(i, end=' ')


# Q6
# for i in range(10,55,5):
#     print(i, end=' ')


# Q7
# name = input('이름: ')
# questions = int(input('문제 개수: '))
# print('*' * 20)

# cnt = 0
# for i in range(questions):
#     result = input('문제를 해결했나요>(y/n) : ')
#     if result == 'y':
#         cnt += 1 
# print('{}학생은 총 {} 문제를 해결했습니다'.format(name, cnt))


# Q8
# print('*** 카운트 다운 ~~')
# for i in range(10,0,-1):
#     print('{} 일 남았습니다'.format(i))
# print('드디어 Dday 입니다!!!')


# Q9
# for i in range(1,11):
#     print(i, end='  ')
#     if i % 3 == 0:
#         print()


# Q10 
# money = 1000
# cnt = 0
# for i in range(10000):
#     if money >= 2000:
#         break
#     cnt += 1
#     money *= 1.07
# print('{}년이 걸립니다.'.format(cnt))


# or (without using count)
# money = 1000
# for i in range(1,10000):
#     money *= 1.07
#     if money >= 2000:
#         break
# print('{}년이 걸립니다.'.format(i))



# Q11 
# list1 = [1,2,5,6,9]
# for i in list1:
#     print('9 * {} = {}'.format(i, 9*i))


# Q12
# num = int(input('몇 단을 출력 할까요 : '))
# for i in range(1,10):
#     print('{} * {} = {}'.format(num, i, num*i))


# Q13
# nSum = 0 
# for i in range(1,11):
#     print(i, end='+')
#     nSum += i
# print('\b={}'.format(nSum))


# Q14 
# print('4!=', end='')
# factorial = 1 
# for i in range(4, 0, -1):
#     print(i, end='*')
#     factorial *= i 

# print('\b={}'.format(factorial))


# Q15
# num = int(input('몇개의 수를 입력하시겠습니까? : '))
# nSum = 0

# for i in range(1, num+1):
#     input1 = int(input('{}번째 수를 넣으세요 : '.format(i)))
#     nSum += input1
# print('=>합={}'.format(nSum))


# Q16
# num = int(input('막대#의 높이 : '))
# for i in range(num):
#     print('#' ,end='')


# Q17
# num = int(input('숫자를 입력하세요: '))
# cnt = 0 
# for i in range(1, num):
#     if i % 3 == 0:
#         cnt += 1 
# print(f'=>1부터 {num} 사이에 존재하는 3의 배수는 {cnt}개입니다')


# Q18
# num = int(input('정수를 입력하세요 : '))
# print('=>{} 의 약수는 '.format(num), end='')
# for i in range(1, num+1):
#     if num % i ==0:
#         print(i, end=' ')
# print('\b입니다')


# Q19
# nSum = 0 
# for i in range(1,100000):
#     input1 = int(input(f'{i}번째 정수를 입력하세요 : '))
#     if input1 == 999:
#         break
#     nSum += input1

# print(f'=>합계 : {nSum}')
# print(f'=>평균 : {nSum/ (i-1)}')



# Q20  
# num = 2
# nSum = 0 

# for i in range(15):
#     print(num, end='+')
#     nSum += num
#     num += 6

# print(f'\b \n합={nSum}')    # \b 다음에 \n가 올때는 space 한칸이 있어야 \b가 작동함



# Q21
# num = 2
# nSum = 0 

# for i in range(10):
#     print(num, end=' ')
#     nSum += num 
#     num *= 3 

# print('\n합={}'.format(nSum))


# Q22
# my_score = int(input('나의 점수는 : '))
# cnt = 1 
# for i in range(1,6):
#     score = int(input('{}번 친구의 점수 : '.format(i)))
#     if score > my_score:
#         cnt += 1 
# print('=> 나는 {}등 입니다'.format(cnt))


# Q23
# num = int(input('입력될 수의 개수는 : '))
# print('\n')
# Max = 0 
# Min = 0 

# for i in range(1,num+1):
#     input1 = int(input('{}번째수를 입력하세요 : '.format(i)))
#     if i == 1:
#         Max = Min = input1 
#     elif input1 > Max:
#         Max = input1 
#     elif input1 < Min:
#         Min = input1 

# print('\n\n=>최대값={}'.format(Max))
# print('=>최소값={}'.format(Min))
    

# Q24
# nSum = 0 
# for i in range(1,5):
#     nSum += i 
#     print('{} 까지의 합={}'.format(i, nSum))


# Q25
# print('*' * 15)
# print('n    n의제곱')
# print('*' * 15)

# for i in range(1,6):
#     print('{:<4}{:>5}'.format(i, i*i))


# Q26
# nSum = 0
# for i in range(1,11):
#     print(i, end='  ')
#     nSum += i 
#     if i % 3 == 0:
#         print('== 합 {}'.format(nSum))
# print('     == 합 {}'.format(nSum))


# Q27
# num = int(input('몇 번 출력 ? : '))
# for i in range(1, num+1):
#     print('You did a good job! - {}번째'.format(i))


# Q28
# names = ['홍길동', '김가나', '박하늘', '한바다', '이고은']
# for i in range(len(names)):
#     print(i, names[i])


# Q29
# word_list = ['scramble', 'kindly', 'do', 'learn']
# for i in word_list:
#     print('un{}'.format(i))


# 30 
# for i in range(1,6):
#     print('{} 번째 알파벳은 {}'.format(i, chr(96+i)))


# 31
# score = [100, 30, 50, 70, 80, 60]
# for i in score:
#     if i >= 70:
#         print('{} 번 학생은 통과'.format(i))
#     else:
#         print('{} 번 학생은 불합격입니다'.format(i))


# Q32
# fruits = ['딸기', '사과', '바나나', '수박', '포도']
# for i in range(len(fruits) -1, -1, -1):
#     print(fruits[i])


# Q33   
# mixlist = ['a', '5', 'b', 'g', '3', '8', '6', 'm']
# for i in mixlist:
#     if 97 <= ord(i) <= 122:
#         print('{} => 문자'.format(i))
#     else:
#         print('{} => 숫자'.format(i))


# Q34  
# mixlist = ['apple', '5', 'banana', 'grape', 3, 8, 6, 'melon']
# for i in mixlist:
#     if type(i) == str:
#         print('{} => 문자열'.format(i))
#     elif type(i) == int:
#         print('{} 숫자'.format(i))


# Q35
# gcd = greatest common divisor 
# input1 = int(input('수를 입력하세요 : '))
# input2 = int(input('수를 입력하세요 : '))
# print('\n')
# gcd = 0 

# for i in range(1,input1 + 1 ):
#     if (input1 % i == 0) and (input2 % i ==0):
#         gcd = i 
# print('=>{}과 {}의 최대공약수는 {}입니다.'.format(input1, input2, gcd ))


# Q36
# start = 100 
# value = 1 
# count = 0

# for i in range(10000):
#     if start < 0:
#         break 
#     start -= value 
#     value += 1 
#     count += 1 

# print('=> 처음으로 음수가 되는 변수의 값과 n의 값은 : {}  {}'.format(start, count))


# or 

# start = 100
# for i in range(1, 1000):
#     start -= i 
#     if start < 0:
#         print('=> 처음으로 음수가 되는 변수의 값과 n의 값은 : {}  {}'.format(start, i))
#         break 


# Q37 
# input1 = int(input('수를 입력하세요 : '))
# r = True 
# for i in range(2, input1):
#     if input1 % i ==0:
#         r = False 

# if r:
#     print('=>소수')
# else:
#     print('=>소수가 아님')


# Q38 
# for i in range(1,51):
#     print('{:<4}+ {:<4}= {:<4}'.format(i, (101-i), i+ (101-i)))
# print('합= {} * {} = {}'.format(101, i, 101*i))

# or 

# a = 100
# for i in range(1,51):
#     print('{} + {} = {}'.format(i,a,i+a))
#     a -= 1
# print('합 = {} * {} = {}'.format(i+a+1, i, (i+a+1) * i ))


# Q39 
# num = int(input('수열의 개수를 입력하세요 : '))
# nSum = 0 
# a = 0 
# b = 1 
# for i in range(num):
#     print(b, end='+')
#     nSum += b 
#     c = a + b 
#     a = b 
#     b = c 
    
# print('\b \n합={}'.format(nSum))


# or


# a = 0 
# b = 0
# c = 1 
# Sum = 0 

# num = int(input('수열의 개수를 입력하세요  : '))
# print('\n')
# for i in range(num):
#     Sum += c 
#     print(c, end ='+')
#     a = b 
#     b = c 
#     c = a + b 
# print('\b \n합={}'.format(Sum))



# Q40 
# nSum = 0
# for i in range(5,50,5):
#     if i % 2 != 0:
#         nSum += i 
#         print(i, end=' ')

# print('\n합={}'.format(nSum))
    

# Q41
# 1
# start = 1 
# nSum = 0
# for i in range(1,8):
#     print(start, end=' + ')
#     nSum += start 
#     start += i

# print('\b\b \n합= {}'.format(nSum))


# 2 
# nSum = 0 
# for i in range(1,11):
#     if i % 2 != 0:
#         nSum += i
#         print(i, end=' - ')
#     else:
#         nSum -= i 
#         print(i, end=' + ')

# print('\b\b \n합= {}'.format(nSum))


# or  

# nSum = 0
# p = 1
# for i in range (1,11):
#     i2=i*p  
#     print(i2,end='')
#     nSum += i2 
#     if p<0:
#         print('+', end='')
#     p= -p # p=p * -1
# print('\b \n합={}'.format(nSum))


# 3
# nSum = 0 
# for i in range(5,55,5):
#     if i % 2 != 0:
#         nSum += i
#         print(i, end=' - ')
#     else:
#         nSum -= i 
#         print(i, end=' + ')

# print('\b\b \n합= {}'.format(nSum))

    
# or 
# nSum = 0 
# p = 1 
# for i in range(5,55,5):
#     i2 = i * p 
#     nSum += i2
#     print(i2, end='')
#     if p < 0:
#         print('+', end='')
#     p = -p

# print('\b \n합={}'.format(nSum))


# 4 
# nSum = 0 
# start = 1 
# p = 1 
# for i in range(7):
#     start += i 
#     i2 = start * p 
#     print(i2, end='')
#     nSum += i2 
#     if p <0:
#         print('+', end='')
#     p = -p

# print('\n합={}'.format(nSum))


# Q42
# input1 = int(input('첫 번째수를 입력하세요 : '))
# input2 = int(input('두 번째수를 입력하세요 : '))
# nSum = 0 
# odd_Sum = 0 

# print('=>사이의 수 : ', end='')
# for i in range(input1 + 1, input2):
#     print(i, end=' ')
#     nSum += i 
#     if i % 2 != 0:
#         odd_Sum += i 

# print('\n합={}'.format(nSum))
# print('홀수의 합={}'.format(odd_Sum))


# Q43
# input1 = input('정수를 입력 하세요: ')
# print('각 자리의 값  : ', end='')
# nSum = 0 

# for i in input1:
#     print(i, end=' ')
#     nSum += int(i)

# print('\n각 자리값의 합 : {}'.format(nSum))


# Q44
# input1 = input('정수를 입력 하세요: ')

# for i in range(len(input1)):
#     print('{}의 자리 : {}'.format(10 ** i, input1[-(i+1)]))


# Q45
# input1 = input('정수를 입력하세요 : ')
# reverse = ''
# print('뒤집은 값 : ', end='')
# for i in range(len(input1)):
#     reverse += input1[-(i+1)]

# print(reverse)
# print('3배수  값 : {}'.format(int(reverse) * 3))


# Q46 
# for i in range(1,11):
#     input1 = int(input('{}번째수를 입력하세요 : '.format(i)))
#     difference = input1 - 10
#     if difference < 0:
#         difference = -difference 
    
#     if i == 1:
#         Min_difference = difference 
#         Min = input1 
#     elif difference < Min_difference:
#         Min_difference = difference
#         Min = input1 

# print('\n\n=>10에 가장 가까운 수는 {}'.format(Min))


# Q47
# odd_Sum = 0
# even_Sum = 0
# multiples_three = 0
# common_multiples = 0
# cnt = 0 
# for i in range(1,31):
#     if i % 2 != 0:
#         odd_Sum += i
#     else:
#         even_Sum += i 

#     if i % 3 == 0:
#         multiples_three += i
#     if i % 3 == 0 and i % 4 == 0:
#         cnt += 1 
#         common_multiples += i 

# print('홀수의 합 = {}'.format(odd_Sum))
# print('짝수의 합 = {}'.format(even_Sum))
# print('3의 배수의 합 = {}'.format(multiples_three))
# print('3과 4의 공배수의 개수 = {}개  합={}'.format(cnt, common_multiples))



# Q48  
# nSum = 0 
# for i in range(1,11):
#     print(i, end=' ')
#     nSum += i 
#     if i % 3 == 0:
#         print('== 합 {}'.format(nSum))
#         nSum = 0 

# print('   == 합 {}'.format(nSum))


# Q49 
# nSum = 0 
# cnt = 0 
# for i in range(1,10000):
#     weight = float(input('몸무게를 입력하시오(0:종료) : '))
#     if weight == 0:
#         break 
#     elif weight < 0 or weight >= 200:
#         cnt += 1 
#         continue

#     nSum += weight 

#     if i == 1:
#         Max = Min = weight 
#     else:
#         if weight > Max:
#             Max = weight 
#         elif weight < Min:
#             Min = weight 

# print('\n')
# print('최대값 : {:.2f}'.format(Max))
# print('최소값 : {:.2f}'.format(Min))
# print('합={:.2f}'.format(nSum))
# print('평균={:.2f}'.format(nSum / (i-1-cnt)))


# Q50
# import random 
# r1 = random.randint(1,100)
# # print(r1)

# for i in range(10000):
#     guess = int(input('정답을 넣으세요 : '))
#     if guess < 0:
#         break 
#     elif r1 > guess:
#         print('{}보다는 큰 수를 넣으세요 ~'.format(guess))
#     elif r1 < guess:
#         print('{}보다는 작은 수를 넣으세요 ~'.format(guess))
#     else:
#         break

# print('\n\n축하합니다 ~~ 드디어 정답을 맞추셨군요 !!!')


# Q51       
# import time, random 

# print('기억력 테스트입니다\n화면에 보이는 숫자를 기억하였다가 다시 쓰면 됩니다.\n다음의 숫자를 기억하세요 => ', end='')
# num_list = []
# for i in range(5):
#     num_list.append(random.randint(1,9))
# for num in num_list:
#     print(num, end=' ')

# print('\n...............화면을 지운다')

# time.sleep(2)   # ()초 동안 멈춰라 --> ()초 동안 멈추고 코드가 나옴
# for i in range(25):
#     print()


# cnt = 0 
# guess_list = list(map(int, input('기억한 숫자를 입력 하세요 : ').split()))  # 한 줄에 입력된 숫자를 split()으로 잘라서 int 형으로 바꾼 후에 리스트에 넣어라
# for i in range(len(num_list)):
#     if num_list[i] == guess_list[i]:
#         cnt += 1 
# print('{}개 맞았습니다!!!'.format(cnt))



# Q52
# year = int(input('년도 : '))
# nDays = 0 

# for i in range(1, year+1):
#     if i % 4 == 0 and i % 100 != 0 or i % 400 ==0:
#         nDays += 366
#     else:
#         nDays += 365 
# print('1년부터 {}년도까지는 {} 일'.format(year, nDays))



# Q53
# num = int(input('수를 입력하세요 : '))
# r = True 
# for i in range(2,num):
#     if num % i == 0:
#         r = False 

# if r:
#     print('결과 => 소수')
# else:
#     print('결과 => 소수가 아닙니다')
