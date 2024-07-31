# 1 
# for i in range(1,3):
#     for k in range(1,4):
#         print(k)
#     print()

# and 

# for i in range(1,3):
#     for k in range(1,4):
#         print(k, end=' ')
#     print()

# 2 
# for i in range(1,3):
#     for k in range(1,4):
#         print(i,end=' ')
    # print()

# 3 
# for i in range(1,10):
#     for j in range(1, 10):
#         print(" {}*{}={:>2}, ".format(i,j,i*j), end='')
#     print()

# 4
# breads = ['호밀빵', '위트', '화이트']
# meats = ['미트볼', '쏘시지', '닭가슴살']
# vegis = ['양상추', '토마토', '오이']
# sauces = ['마요네즈', '허니 머스타드', '칠리']

# for b in breads:
#     for m in meats:
#         for v in vegis:
#             for s in sauces:
#                 print(b+"+"+m+"+"+v+"+"+s)

# print('1', '2')      # 연산결과 예측 
# print('1'+'2')
# print(1+2)
# print('1''2')
# print('abc''ddd')


# 5 
# # 행렬을 행과 열을 바꾸어(전치행렬) 출력하여 봅시다 
# A = [[1,2,3],[4,5,6]]
# # tA: A의 전치행렬, 0으로 초기화
# tA = [ [ 0 for row in range(len(A)) ] for col in range(len(A[0]))]  # [[0, 0], [0, 0], [0, 0]]


# for i in range(len(A)):  # 2 
#     for j in range(len(A[0])):  #3
#         tA[j][i] = A[i][j]

# # print(tA)   # [[1, 4], [2, 5], [3, 6]]
# print(' A = ')
# for row in A:
#     for value in row:
#         print('{0:>4}. '.format(value), end='')
#     print()

# print('tA = ')
# for row in tA:
#     for value in row:
#         print('{0:>4}. '.format(value), end= '')
#     print()



# 6) ???
# L = [10,20,30]
# it=iter(L)
# print("%d" % next(it))
# print("%d" % next(it))
# print("%d" % next(it))
# print("%d" % next(it))


# for i in range(len(A)):
#     for j in range(len(A)):

# 7    ? ??? ?  ? ? ? 
# seasons = ['Spring', 'Summer', 'Fall', 'Winter']
# for item in enumerate(seasons):
#     print(item)
# for i, value in enumerate(seasons):
#     print(i,value)
# for item in enumerate(seasons, 100):
#     print(item)

# 8 
# L = [2, 1, 3, 5, 4]
# for i,value in enumerate(L):
#     L[i] = value * 10 


# Question 1 

# 1
for i in range(1,4):
    print('{}: '.format(i), end='')
    for j in range(4):
        print(i, end='')
    print()

# 2 
for i in range(1,6):
    print('{}: '.format(i), end='')
    for j in range(4):
        print((j+1), end='')
    print()

# 3 
# for i in range(1,4):
#     print('{}: '.format(i), end='')
#     for j in range(i):
#         print((j+1),end='')
#     print()

# 4 
# for i in range(4):
#     for j in range(5):
#         print('*', end='')
#     print('\n')

# Question 2 

# 1 
# for i in range(1,4):
#     for j in range(i):
#         print('*',end=' ')
#     print()

# 2 
# for i in range(3,0,-1):
#     for j in range(i):
#         print('*', end=' ')
#     print()

# 3  
# for i in range(1,4):          
#     for j in range(1):
#         print('  ' * (4-i), end=' ')      # print('  ') 빈칸 만들라고 쓰여짐
#         for k in range(1,i+1):
#             print('*', end=' ')
#     print()              # 여기서는 사실상 print()랑 print('')랑 똑같음

# or

# for i in range(3):       # ?????? 여기서 3-i에 가로 안하면 왜 실행안되는거? string 이랑 int여서 안된다고 하는데 i가 스트링임?
#     print('  ' * (3-i), end=' ')
#     for j in range(i+1):
#         print('*', end=' ')
#     print()

# 4 
# for i in range(1,4):
#     for j in range(4-i):
#         print(' ', end=' ')
#     for k in range(i*2-1):
#         print('*' , end=' ')
#     print()

# 5     
# for i in range(1,4):
#     for j in range(i):
#         print(' ', end=' ')
#     for k in range(7-2*i):
#         print('*', end=' ')
#     print()

# or 

# for i in range(1,4):
#     print('  ' * i ,end =' ')
#     for j in range(7-2*i):
#         print('*', end=' ')
#     print()

# 6          
# n = 1 
# for i in range(1,4):
#     for j in range(i):
#         print(n, end=' ')
#         n += 1 
#     print()

# 7 
# for i in range(1,4):
#     for j in range(i):
#         print(j+1, end=' ')
#     print()

# 8   
# n = 9
# for i in range(1,4):
#     for j in range(i):
#         print(' ', end=' ')
#     for k in range(7-2*i):
#         print(n,end=' ')
#         n -= 1
#     print()

# Question 3 
# breads = ['호밀빵', '위트', '화이트']
# meats = ['미트볼','소시지','닭가슴살']
# vegetables = ['양상추','토마토','오이']
# sauces = ['마요네즈','허니머스타드','칠리']

# for i in breads:
#     for j in meats:
#         for k in vegetables:
#             for s in sauces:
#                 print('{}+{}+{}+{}'.format(i,j,k,s))

# Question 4      
# for i in range(2,10):
#     for j in range(1,10):
#         print('{}*{}={:<2}'.format(i,j,i*j), end='  ')
#     print()

# Question 5
# for i in range(1,10):
#     for j in range(2,10):
#         print('{}*{}={:<2} '.format(j,i,i*j), end =' ')
#     print()

# Question 6  print  # {:}. formaat( )  스트링이면 왼쪽 정렬, 숫자이면 오른쪽 정렬 
# print('{:^40}'.format('곱셈표'))
# print('{:8}{:4}{:4}{:4}{:4}{:4}{:4}{:4}{:4}'.format(1,2,3,4,5,6,7,8,9))
# print('{:>40}'.format('*'*37))
# for i in range(1,10):
#     print('{:<}*  '.format(i), end='')
#     for j in range(1,10):
#         print('{:>4}'.format(i*j), end='')
#     print()

  
# Question 7    
# a = int(input('수를 입력하세요  : '))  # 4 
# b = int(input('수를 입력하세요  : '))  # 6 

# for i in range(1,100):
#     c = a * i 
#     # print(c)
#     for j in range(1,100):
#         d = b * j
#         # print(d)
#         if c == d:
#             # print(c)
#             break
#     if c == d :
#         break
# print('=>{}와 {}의 최소공배수는 {}입니다'.format(a,b,c))


# Question 8  
# for i in range(100000000)  :
#     start = int(input('시작값 : '))
#     end = int(input('끝값   : '))
#     if end-start>3:
#         break
#     print('다시 입력하세요')
# print('\n')

# cnt=0
# for i in range(start+1,end):
#     print(i, end=' ')
#     cnt+=1
#     if cnt%3==0:
#         print()

# or 

# for i in range(100000000)  :
#     start = int(input('시작값 : '))
#     end = int(input('끝값   : '))
#     if end-start>3:
#         break
#     print('다시 입력하세요')
# print('\n')

# n = start + 1 

# for i in range(start+1,end):
#     for j in range(3):
#         if n == end:
#             break
#         print('{:>2}'.format(n),end=' ')
#         n += 1 
#     print()
    # if n == end:
    #     break

# or 

# for i in range(100000000)  :
#     start = int(input('시작값 : '))
#     end = int(input('끝값   : '))
#     if end < start or end - start <= 3:
#         print('다시 입력하세요')
#         continue 
#     print('\n')
#     cnt=0
#     for j in range(start+1,end):
#         print(j, end=' ')
#         cnt+=1
#         if cnt%3==0:
#             print()
#     break


# Question 9 
# l = []
# r = True 
# for i in range(2,201):
#     for j in range(2,i+1):
#         if i % j == 0 and ( i != j ):
#             r = False 
#             break
#         else:
#             r = True 
#     if r:
#         l.append(i)

# count = 0 
# for i in l:     
#         print('{:<4}'.format(i),end=' ')
#         count += 1 
#         if count % 5 == 0 :
#             print()


# Question 10 

# 내가 풀었던 방식 

# l = []
# first = [1,2,3,4,5,6,7,8,9]
# second = [1,2,3,4,5,6,7,8,9]
# third = [1,2,3,4,5,6,7,8,9]

# for i in first:
#     for j in second:
#         for k in third:
#             if i != j and j != k:
#                 l.append('{}{}{}'.format(i,j,k, end=''))
#                 # print(l)

# page = 0 
# count = 0 
# for i in l:
#     print('{:<4}'.format(i),end=' ')
#     count += 1 
#     if count % 5 == 0 :
#         print()
#     if count % 100 == 0 :
#         page += 1 
#         print('\n{}\n'.format(page))

# print('\n{}개'.format(count))
                



# or 

# 더 좋은 방식 

# page = 0 
# count = 0 
# for i in range(1,10):
#     for j in range(1,10):
#         for k in range(1,10):
#             if i != j and j != k:
#                 print('{}{}{}'.format(i,j,k), end=' ')
#                 count += 1 
#                 if count % 5 == 0 :
#                     print()
#                 if count % 100 == 0 :
#                     page += 1 
#                     print('\n{}\n'.format(page))
# print('\n\n{}개'.format(count))


# 정수 : int
# 실수 : float
# print(10/3) 
# print(10//3)
# print(10%3)
# print(10.0% 3 )         # % 쓸거면 정수여야 됨 ex) print(10.0 % 3)은 에러뜸




# Question 11  ???????? 이거 다시해야됨 
# n = int(input('수를 입력하세요 : '))
# print('결과 => ',end='')


# for i in range(10000):
#     b = True 
#     for j in range(2,n):
#         if n % j == 0 :
#             print(j, end=' * ')
#             n //= j 
#             b = False
#             break
#     if b:
#         print(n)
#         break

            
# if n % j == 0 and ( n != j ):
#             n = False 
#             break
#         else:
#             n = True 
#         if n:
#             break


# Question 12
# n = 0 
# lines = int(input('몇줄 ? '))
# for i in range(lines):
#     n += 1
#     print('   ' * (lines-i), end='')
#     for j in range(i+1):
#         i += 1
#         print('{:<3}'.format(i), end ='')      # 두자리 수 일때도있고 한자리 수 일때도 있으니 format을써서 맞춰줘야됨
#     for k in range(i-n):
#         i -= 1
#         print('{:<3}'.format(i), end='')
#     print()


# Question 13     
# count = 0 
# first = [1,2,3]
# second =[2,3,4]
# third = [3,4,5]

# for i in first:
#     for j in second:
#         for k in third:
#             # if i != j and i!= k and j != k and i< j< k:      # 둘이 똑같은 거?
#             if i != j != k and i<j<k:
#                 print(i, j, k)
#                 count += 1 
# print('총 경우의 수 : {}'.format(count))

# or 

# count = 0 

# for i in range(1,4):
#     for j in range(2,5):
#         for k in range(3,6):
#             if i != j and i!= k and j != k and i< j< k:      
#                 print(i, j, k)
#                 count += 1 
# print('총 경우의 수 : {}'.format(count))




# Question 14
# 서기 1년 1월 1일 --> 월요일 
# 2022 / 5
# 1/1 ~ 22/4 총일 수를 구하기 
# 총 일 수를 구하려면 [31,28,31,30,.....]
# 2월 29일 
# 윤년 - 366일 
# 평년 - 365 일 
# 총 일수 % 7 ---> 그 달의 시작 요일 


# year = int(input('년 : '))
# month = int(input('월 : '))
# nDays = 0 
# mDays = 0 
# print('{}< {}년 {}월>{}'.format('*'*20,year,month,'*'*20))
# print('{:<6}{:<6}{:<6}{:<6}{:<6}{:<6}{:<6}'.format('일','월','화','수','목','금','토'))

# for i in range(1,year):
#     if i % 4 == 0 and i % 100 != 0 or i % 400 == 0 :
#         nDays += 366      
#     else: 
#         nDays += 365

# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 :
#     leapyear = True
# else:
#     leapyear = False


# mDays = [31,28,31,30,31,30,31,31,30,31,30,31]
# for i in range(month-1):
#     nDays += mDays[i]

# if leapyear and month>2:
#     nDays += 1 


# blank = (nDays + 1) % 7 

# cnt = 0 
# for i in range(blank):
#     print('      ' , end=' ')
#     cnt += 1 

# for j in range(1, mDays[month-1] + 1):
#     print('{:<6}'.format(j), end=' ')
#     cnt += 1 
#     if cnt % 7 ==0 :
#         print()



# a = []
# a.append('k')
# print(a)        


# l = list(range(10))
# print(l)




# 두번째 풀기 
# Q1 
# 1
# for i in range(1,4):
#     print('{}: '.format(i), end='')
#     for j in range(4):
#         print(i,end='')
#     print()


# 2 
# for i in range(1,6):
    # print('{}: '.format(i), end='')
    # for j in range(1,5):
    #     print(j,end='')
    # print()
        

# 3 
# for i in range(1,4):
#     print('{}: '.format(i), end='')
#     for j in range(i):
#         print(j+1, end='')
#     print()


# 4 
# for i in range(4):
#     for j in range(5):
#         print('*', end='')
#     print('\n')


# Q2
# 1 
# for i in range(1,4):
#     for j in range(i):
#         print('*', end=' ')
#     print()


# 2 
# for i in range(3,0,-1):
#     for j in range(i):
#         print('*', end=' ')
#     print()


# 3 
# for i in range(1,4):
#     for j in range(4-i):
#         print(' ', end=' ')
#     for k in range(i):
#         print('*', end=' ')
#     print()


# 4 
# for i in range(1,4):
#     for j in range(4-i):
#         print(' ', end=' ')
#     for k in range(2*i - 1):
#         print('*', end=' ')
#     print()


# 5 
# for i in range(3,0,-1):
#     for j in range(4-i):
#         print(' ', end=' ')
#     for k in range(2*i - 1):
#         print('*', end=' ')
#     print()


# 6 
# start = 1 
# for i in range(1,4):
#     for j in range(i):
#         print(start, end=' ')
#         start += 1 
#     print()


# 7 
# for i in range(1,4):
#     for j in range(i):
#         print(j+1, end=' ')
#     print()


# 8 
# start = 9 
# for i in range(3,0,-1):
#     for j in range(4-i):
#         print(' ', end=' ')
#     for k in range(2*i - 1):
#         print(start, end=' ')
#         start -= 1 
#     print()


# Q3
# breads = ['호밀빵', '위트', '화이트']
# meats = ['미트볼', '소시지', '닭가슴살']
# vegetables = ['양상추', '토마토', '오이']
# sauces = ['마요네즈', '허니머스타드', '칠리']

# for b in breads:
#     for m in meats:
#         for v in vegetables:
#             for s in sauces:
#                 print(b+'+'+m+'+'+v+'+'+s)


# Q4
# for i in range(2,10):
#     for j in range(1,10):
#         print('{}*{}={:<4}'.format(i,j, i*j), end='')
#     print()


# Q5
# for i in range(1,10):
#     for j in range(2,10):
#         print('{}*{}={:<4}'.format(j,i, j*i), end='')
#     print()


# Q6
# print('{:^40}'.format('곱셈표'))
# print('{:>5}{:>4}{:>4}{:>4}{:>4}{:>4}{:>4}{:>4}{:>4}'.format(1,2,3,4,5,6,7,8,9))
# print('{:>38}'.format('*'*34))


# for i in range(1,10):
#     print('{}*  '.format(i), end='')
#     for j in range(1,10):
#         print('{:<4}'.format(i*j), end='')
#     print()


# Q7    
# input1 = int(input('수를 입력하세요 : '))
# input2 = int(input('수를 입력하세요 : '))

# for i in range(1,1000):
#     lcm_1 = input1 * i 
#     for j in range(1, 1000):
#         lcm_2 = input2 * j 
#         if lcm_1 == lcm_2:
#             break 
#     if lcm_1 == lcm_2: 
#         break 
# print('=>{}와 {}의 최소공배수는 {}입니다'.format(input1, input2, lcm_1))


# Q8  
# for i in range(10000):
#     start = int(input('시작값 : '))
#     end = int(input('끝값   : '))
#     difference = end - start 

#     if end < start or difference <= 3:
#         print('다시 입력하세요')
#         continue 
#     print('\n')

#     cnt = 0 
#     for j in range(start+1, end):
#         print('{:<3}'.format(j), end=' ')
#         cnt += 1 
#         if cnt % 3 == 0:
#             print()
#     break 



# Q9  
# prime_list = []
# for i in range(2,201):
#     r = True 
#     for j in range(2,i):
#         if i % j == 0:
#             r = False 
#             break
#     if r == True:
#         prime_list.append(i)

# cnt = 0
# for prime in prime_list:
#     print('{:<5}'.format(prime), end='')
#     cnt += 1 
#     if cnt % 5 == 0:
#         print()



# Q10
# cnt = 0 
# page = 1
# for i in range(1,10):
#     for j in range(1,10):
#         for k in range(1,10):
#             if i != j and j != k:
#                 print('{}{}{}'.format(i,j,k), end='  ')
#                 cnt += 1 
#                 if cnt % 5 == 0:
#                     print()
#                 if cnt % 100 == 0:
#                     print(page)
#                     page += 1 
#                     print('\n')
# print('\n{}'.format(page))
# print('\n{}개'.format(cnt))



# Q11   ??????
# num = int(input('수를 입력하세요 : '))
# prime_list = []


# for i in range(2,num):
#     r = True 
#     for j in range(2,i):
#         if i % j == 0:
#             r = False 
#     print(r)
#     if r:
#         prime_list.append(i)


# or 
# ???????????
# num = int(input('수를 입력하세요 : '))
# print('결과 => ', end='')


# for i in range(2,num):
#     r = True 
#     for j in range(2,i):
#         if i % j == 0:
#             r = False 

#     if r and num % i ==0:
#         print(i, end=' * ')
#         num = num // i 
# print('\b\b')


# Q12
# lines = int(input('몇줄 ? '))

# for i in range(lines):
#     for j in range(lines-i):
#         print(' ', end=' ')
#     for k in range(i+1):
#         i += 1 
#         print(i, end=' ')
#     for l in range((i-1)// 2):
#         i -= 1
#         print(i, end=' ')
#     print()


# 똑같은데 스페이싱 먖춰서 댜시 풀어봄 

# lines = int(input('몇줄 ? '))
# for i in range(lines):
#     for j in range(lines-i):
#         print('   ', end='')
#     for k in range(i+1):
#         i += 1 
#         print('{:<3}'.format(i), end='')
#     for l in range((i-1)// 2):
#         i -= 1
#         print('{:<3}'.format(i), end='')
#     print()


# Q13   
# cnt = 0 
# for i in range(1,6):
#     for j in range(1,6):
#         for k in range(1,6):
#             if (i != j and i != k and j != k) and i < j < k:
#                 print('{} {} {}'.format(i,j,k))
#                 cnt += 1 
# print('총 경우의 수 : {}'.format(cnt))


# Q14 
# 서기 1년 1월 1일 --> 월요일 
# 2022 / 5
# 1/1 ~ 22/4 총일 수를 구하기 
# 총 일 수를 구하려면 [31,28,31,30,.....]
# 2월 29일 
# 윤년 - 366일 
# 평년 - 365 일 
# 총 일수 % 7 ---> 그 달의 시작 요일 


# year = int(input('년 : '))
# month = int(input('월 : '))

# nDays = 0 
# months_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# print('{}< {}년 {}월 >{}'.format('*'*10, year, month, '*'*10))
# print('{:<5}{:<5}{:<5}{:<5}{:<5}{:<5}{:<5}'.format('S','M','T','W','T','F','S'))


# for i in range(1, year):
#     if (i % 4 == 0 and i % 100 != 0) or (i % 100 == 0 and i % 400 == 0):  # if i % 4 == 0 and i % 100 != 0 or i % 400 == 0 :
#         nDays += 366
#     else:
#         nDays += 365

# for i in range(month - 1):
#     nDays += months_list[i]
# if month > 2 and (year % 4 == 0 and year % 100 != 0) or (year % 100 == 0 and year % 400 == 0):
#     nDays += 1  # 만약 그해가 윤년이면, 하루 더하기 


# start_date = (nDays+1) % 7 
# for i in range(start_date):
#     print('     ', end='')


# new_line = 7 - start_date
# for i in range(months_list[month-1]):
#     if i == new_line:
#         print()
#     elif i % 7 == new_line:
#         print()
#     print('{:<5}'.format(i+1), end='')








# Using enumerate(열거하다)    
# names = ["홍길동", "김가나", "박하늘", "한바다", "이고은"]
# for n,i in enumerate(names):          # enumerate가 앞에 변수, 즉 n에   names가 뒤에 변수, 즉 i에 들어간다 
#     print('{} {}'.format(n,i))

# enumerate 아무것도 안주면 0부터 1씩 증가. 값을주면 그값부터 1씩증가