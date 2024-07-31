# 1 
# lines = 0
# while lines<10:
#     print('파이썬은 재미 있어요 ~~')
#     lines = lines + 1

# 2       
# response = '아니'
# while response == '아니':       
#     response = input('엄마, 다됐어?')
# print('먹자')

# 3 
# lines = 1 
# while lines < 10:
#     print(lines, end='  ')
#     lines = lines + 1 

# 7 
# n = int(input('정수 입력 ---> '))

# i = 1 
# nSum = 0 
# while i <= n:
#     nSum += i 
#     i += 1 
# print(" n = %d : nSum = %d" % (n, nSum))

# 8 
# nTH = int(input('정수입력 ---> '))
# i = 1 
# nSum = 0 
# while True:
#     nSum += i 
#     if nSum >= nTH:
#         break
#     i += 1
# print("i = %d : nSum = %d" % (i,nSum))

# if not n % i 
# if n % i == 0 :

# if 4%2==0:
#     print('ok')

# if not 4%2:
#     print('ok')


# 9       
# n = int(input('양의 정수 --->'))   
# i = 2 
# bprime = True
# while i < n:
#     if not n % i:          # 0 이면 무조건 False, 나머지는 True ex) -100 --> True , 500 --> True 
#         bprime = False 
#         break
#     i += 1 
# if bprime:
#     print('{}은 소수이다.'.format(n))
# else:
#     print('{}은 소수가 아니다.'.format(n))
 
# 10      
# nPrime = int(input('소수의 개수 --->'))
# k = 0 
# n = 2 
# L = []     # 결과 리스트 
# while k != nPrime:  # k < nPrime    
#     s = True
#     for i in range(2,n):
#         if not n % i: s = False; break     # 같은 줄에 쓸꺼면 semi column 쓰고 계속쓰면됨
#     if s: 
#         L.append( n)
#         k += 1 
#     n += 1 
# print('{}개의 소수, L = {}'.format(k,L))




# print('gfdjgj \' afkak' )
# print("aaa \" bbb")
# print("aaa \" bbb")
# print('aaa " bbb')      # 만약에 \' 찍고 싶지 않으면 
# print("aaa ' bbb")

# 11    
# import sys, random

# while True:
#     name = input('이름: (종료하려면 엔터키) ')
#     if name =='':
#         # sys.exit()       # break는 그 특정 loop을 끝내는거고 sys.exit()을 쓰면 모든 코드를 끝내는 것 
#         break
#     question = input('무엇에 대하여 알고 싶은거요? ')
#     print(name + '님', '\'', question, '\' 에 대하여 질문 주셨군요.') 
#     print('운명의 주사위를 굴려볼게요...')
#     answers = random.randint(1,8)
#     if answers  == 1:
#         print('네, 확실합니다. ')
#     elif answers == 2:
#         print('전망이 좋은 거 같은 데요.')
#     elif answers == 3:
#         print('믿으셔도 됩니다.')
#     elif answers == 4:
#         print('글쎄요 아닌 거 같군요.')
#     elif answers == 5:
#         print('한 점의 의심도 없이 맞습니다.')
#     elif answers == 6:
#         print('그럼요, 명백히 올바른 선택을 했습니다. ')
#     elif answers == 7:
#         print('제 답변은 No입니다.')
#     else:
#         print('나중에 다시 물어 보세요.')

# print('........')


# r1=random.randint(1,3)
# r2 = random.randrange(1,5,2)
# r3 = random.random()    # --> 0에서 1 사이의 실수 
# print(r3)


# 12 
# import random
# dice1, dice2, dice3, dice4, dice5, dice6 = [0] * 6       # 전역 변수 --> 함수 바깥에 선언된 변수 
# throwCount, serialCount = 0, 0 

# if __name__ == "__main__" :
#     while True:
#         throwCount += 1 


#         dice1 = random.randrange(1,7)
#         dice2 = random.randrange(1,7)
#         dice3 = random.randrange(1,7)
#         dice4 = random.randrange(1,7)
#         dice5 = random.randrange(1,7)
#         dice6 = random.randrange(1,7)
 
#         if dice1 == dice2 == dice3 == dice4 == dice5 == dice6 :                     # \은 문장이 너무 길때, 앞의 문장과 뒤의문장을 이을때 
#             print('6개의 주사위가 모두 동일한 숫자가 나옴 -->', dice1, dice2, dice3, dice4, dice5, dice6)
#             break
#         elif (dice1 == 1 or dice2 == 1 or dice3 == 1 or dice4 == 1 or dice5 == 1 or dice6 == 1 ) and \
#             (dice1 == 2 or dice2 == 2 or dice3 == 2 or dice4 == 2 or dice5 == 2 or dice6 == 2 )  and \
#             (dice1 == 3 or dice2 == 3 or dice3 == 3 or dice4 == 3 or dice5 == 3 or dice6 == 3 )  and \
#                 (dice1 == 4 or dice2 == 4 or dice3 == 4 or dice4 == 4 or dice5 == 4 or dice6 == 4 )  and \
#                     (dice1 == 5 or dice2 == 5 or dice3 == 5 or dice4 == 5 or dice5 == 5 or dice6 == 5 )  and \
#                         (dice1 == 6 or dice2 == 6 or dice3 == 6 or dice4 == 6 or dice5 == 6 or dice6 == 6 ):
#                         serialCount += 1 


#     print('6개가 동일한 숫자가 나올 때까지 주사위를 던진 횟수 -->', throwCount)
#     print('6개가 동일한 숫자가 나올 때까지, 1~6의 연속번호가 나온 횟수 -->', serialCount)


# Question 1 
# num = 0 
# while(num<=10):
#     num= num + 2 
# print(num)


# Question 2 
# n = 5 
# step = 0 
# sum = 0 
# while(step <= n):
#     sum += step 
#     step += 1 
# print(sum)


# Question 3   
# i = 1
# smax = 0 
# while i <= 5:
#     n = int(input('정수를 입력하세요 :'))
#     if i == 1:
#         max = n 
#     if i == 2:
#         if max < n :
#             smax = max
#             max = n 
#         else:
#             smax = n 
#     if n > max:
#         smax = max 
#         max = n 
#     elif smax < n:
#         smax = n 
#     i += 1 

# print('두 번째로 큰 수는 {} 입니다'.format(smax))


# Question 4       
# l = []  
# i = 1  
# while True:
#     a = int(input('{:<2}번째 수를 입력 : '.format(i)))
#     if a ==0:
#         break 
#     l.append(a)
#     i += 1 

# print('\n')

# j = 0 
# while j < len(l):
#     if l[j] % 2 ==0:
#         print('{} 번째수는 {:<2} -> 짝수'.format(j+1,l[j]))
#     else:
#         print('{} 번째수는 {:<2} -> 홀수'.format(j+1,l[j]))
#     j += 1 


# Question 5    
# omelet = ['egg', 'meat', 'onion', 'carrot']
# i = 0 
# while i < len(omelet):
#     print('{}번 재료는 {}'.format(i+1,omelet[i]))
#     i += 1 


# Question 6 
# n = 1 
# nSum = 0 
# while nSum <= 1000:
#     nSum += n
#     print('{:<3} {:<3}'.format(n,nSum))
#     n += 1 
# print('\n\n==> {}'.format(n-1))


# Question 7 
# height = int(input('높이를 입력하세요(m) : '))
# count = 0 

# while height >= 0.00001:
#     height *= 0.5 
#     count += 1 
# print('공이 튀긴 횟수는 {}회입니다.'.format(count))


# Question 8          # 리스트 원소들의 합을 구하는 프로그램 
# num_list= [(1,2), (3,5), (7,9), (13,15)]

# i=0
# while i<len(num_list):
#     print(num_list[i][0] + num_list[i][1])
#     i += 1 


# Question 9    
# i = 0 
# score_list= [50, 70, 40, 80, 60, 30, 78]
# while i < len(score_list):
#     if score_list[i] >= 60:
#         print('{}  번: 축하!!  합격!!!'.format(i+1))
#     else:
#         print('{}  번: 안됐군요 불합격 입니다~'.format(i+1))
#     i += 1 


# Question 10  
# n = 2 
# while n < 10:
#     print('{} 단 : '.format(n), end='')
#     for i in range(1,10):
#         print('{:>2}'.format(n*i), end=' ')
#     print()
#     n += 1 


# Question 11      
# n1 = 1
# while n1 <= 6: 
#     n2=1
#     while n2 <= 6: 
#         if n1 + n2 == 6:
#             print('{} + {} = {}'.format(n1,n2,n1+n2))
#         n2 += 1
#     n1 += 1


# Question 12 
# nSum = 0 
# i = 1
# while i <= 100:
#     if i % 3 == 0 and i % 4 ==0:
#         print(i ,end=' ')
#         nSum += i  
#     i += 1 
# print('\n합= {}'.format(nSum))  


# Question 13 
# mom  = 38
# juno = 1 
# while juno * 6 + 2 < mom:
#     juno += 1 
# print('준오나이 : {}살'.format(juno))


# Question 14    
# juno = 24
# suhyeon = 6
# minute = 0 
# while suhyeon <= juno:
#     print('{:<2}분 뒤 출발지점으로부터 이동된 거리 준오={:<2}km    수연={:<2}km'.format(minute,juno,suhyeon))
#     juno += 2
#     suhyeon += 3
#     minute += 1 


# Question 15
# print('*' * 20)
# print('\n{:>2}        {:<10}\n'.format('n','n제곱'))
# print('*' * 20)

# i = 1 
# while i <= 10:
#     print('{:>2}        {:<10}'.format(i,i**2))
#     i += 1 


# Question 16 
# import random
# while True:
#     r1 = random.randint(1,99)
#     r2 = random.randint(1,99)
#     a = int(input('{} + {} = '.format(r1,r2)))
#     if a == (r1 + r2):
#         print('잘했어요!!')
#     else:
#         print('다음번에는 잘할 수 있죠?')
    

# Question 17        
# while True:
#     korean = int(input('국어점수 : '))
#     if 0 < korean <=100:
#         break
#     else:
#         print('0~100 사이의 값을 입력하세요')

# while True:
#     english = int(input('영어점수 : '))
#     if 0 < english <=100:
#         break
#     else:
#         print('0~100 사이의 값을 입력하세요')

# while True:
#     math = int(input('수학점수 : '))
#     if 0 < math <=100:
#         break
#     else:
#         print('0~100 사이의 값을 입력하세요')

# total = korean + english + math 
# average = total / 3
# print('국어 : {}   영어 {}   수학 {}'.format(korean,english,math))
# print('총점 {}   평균 : {:.0f}'.format(total,average))


# Question 18
# A = 3
# B = 7 
# count = 0 
# while B >= A:
#     A += 0.3
#     B += 0.2
#     count += 1 
# print('{} 초후...'.format(count))


# # Question 19   
# import random

# r = random.randint(1,100)
# count = 0 
# print(r)

# while True:
#     a = int(input('숫자 : '))
#     if a == r:
#         print('축하해 {}번만에 내 비밀번호를 찾았군!!!'.format(count))
#         break 
#     if count == 5:
#         print('다음기회에...')
#         break 
#     if a > r:
#         print('그건 너무 크다구 !!!')
#     if a < r :
#         print('그건 너무 작아 ~~')
#     count += 1 


# Question 20

# 12321   232
# n = int(input())
# d = 10000

# while n >=10:
#     if n //d != n % 10:
#         break

#     n = n % d
#     n = n // 10 
#     d //= 100
     
# if n<10:
#     print('회문입니다')
# else:
#     print('회문이 아닙니다')


# Question 21    # 피보나치 수열 
# first = 0 
# second = 0
# third = 1 
# count = 1 
# a = int(input()) 
# while count < a:
#     count += 1  
#     first = second
#     second = third
#     third = first + second 
# print('{}번째 수: {}'.format(a,third))


# Question 22 
# nSum = 0 
# n = 100
# while n <= 999:
#     a = n // 100 
#     b = (n % 100) // 10 
#     c = (n % 100) % 10 
#     d = a + b + c 
#     print('{} {} {} = {:<2}'.format(a,b,c,d))
#     nSum += d 
#     n += 1 
# print('\n\n합= {}'.format(nSum))

# or  
# python에서는 casting, 즉 형 변환이 비교적 자유롭다

# nSum = 0 
# n = 100
# while n <= 999:    
#     s =str(n)
#     d = int(s[0]) + int(s[1]) + int(s[2])
#     print('{} {} {} = {:<2}'.format(s[0],s[1],s[2],d))
#     nSum += d 
#     n += 1 
# print('\n\n합= {}'.format(nSum))


# Question 23       
# import sys
# distance = int(input('몇m를 달렸나요 ?==>'))
# bdistance = 2000
# basicfee = 3000
# while bdistance <= distance:
#     if distance == 2000:
#         print('요금은 {} 원'.format(basicfee))
#         sys.exit()
#     basicfee += 600
#     bdistance += 400
# print('요금은 {} 원'.format(basicfee))

# or 

# distance = int(input('몇m를 달렸나요 ?==>'))
# basicfee = 3000
# distance -= 2000
# while distance >= 400:
#     basicfee += 600
#     distance -= 400
# if distance>0:
#     basicfee+=600
# print('요금은 {} 원'.format(basicfee))


# Question 24  
# count50, count10, count5, count1 = [0] * 4 
# a = int(input('얼마를 출금하시겠어요 ?==>'))
# print('\n')

# while a - 50000 >= 0:
#     a -= 50000
#     count50 += 1 

# while a - 10000 >= 0:
#     a -= 10000
#     count10 += 1 

# while a - 5000 >= 0:
#     a -= 5000
#     count5 += 1 

# while a - 1000 >= 0:
#     a -= 1000
#     count1 += 1 

# print('50000 원권 -- {}  매'.format(count50))
# print('10000 원권 -- {}  매'.format(count10))
# print('5000 원권 -- {}  매'.format(count5))
# print('1000 원권 -- {}  매'.format(count1))

# or 

# count=[50000,10000,5000,1000]
# a = int(input('얼마를 출금하시겠어요 ?==>'))
# print('\n')

# n=0
# while n<len(count):
#    print('{} 원권 -- {}  매'.format(count[n],a//count[n]))
#    a %= count[n]
#    n += 1 





# practice.py에서 빼온내용들 
# import re

# string = '''I love three with the passion put to use
# In my old griefs, and with my childhood's faith.
# I love thee with a love I seemed to lose
# With my lost saint - I love thee with the breath.
# Smiles, tears, of all my life! - and if God choose,
# I shall but love thee better after death.'''


# s2 = re.sub('[,.! -]', '', string)  # Remove spaces from the regular expression pattern
# print(s2)
# final = ''
# for i in s2:
#     final += i 
# print(final)