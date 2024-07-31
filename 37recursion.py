# 재귀함수 

# 1
# 1씩 감소된 값을 매개변수에 전달시켜봅시다

# def recursive(a):
#     if a == 0:
#         return 
#     recursive(a-1)
#     print(a, end=' ')

# recursive(5)


# 2 
# 1씩 증가된 값을 매개변수에 전달시켜봅시다 

# def DispNum(a):
#     if a == 3:
#         return 
#     DispNum(a+1)
#     print(a, end =' ')

# DispNum(0)


# 3 
# 재귀함수 호출결과를 예측하여 봅시다 

# def KK1(N):
#     if N == 0:
#         return 
#     KK1(N-1)
#     print(N, end=' ')

# def KK2(a, N):
#     print(a, end=' ')
#     if a == N:
#         return
#     KK2(a+1, N)
#     print(a, end=' ')


# KK1(3)  # 1 2 3 
# print()
# KK2(1,3)    # 1 2 3 2 1 


# 4  ???? 다시 보기 
# 삼향연산자를 사용한 재귀함수 결과를 예측하여 봅시다 

# def Sum1(N): return (N if N <= 1 else N+Sum1(N-1))
# def Sum1(N):
#     if N <= 1:
#         return N
#     return N + Sum1(N-1)
# print(Sum1(3))


# def Sum(a, N): return(a if N<=a else N+Sum(a, N-1))
# def Sum(a, N):
#     if N <= a:
#         return a
#     return N + Sum(a, N-1)

# print(Sum(1,3))     # 6


# def Pow(a, N): return(a if N<= 1 else a * Pow(a, N-1))
# def Pow(a, N):
#     if N <= 1:
#         return a 
#     return a * Pow(a, N-1)

# print(Pow(2,3))     # 8 


# def Fac(N): return(1 if N <= 1 else N * Fac(N-1))
# def Fac(N): 
#     if N <= 1:
#         return 1 
#     return N * Fac(N-1)

# print(Fac(3))   # 6 



# 5 
# 다음 프로그램의 실행결과를 예측하시오 

# def Disp1(a,b):
#     if a > b:
#         return 
#     print(a, end=' ')
#     Disp1(a+1, b)


# def Disp2(a,b):
#     if a < b:
#         return
#     print(a, end=' ')
#     Disp2(a-1, b)


# def Disp(a,b):
#     if b > a:
#         Disp1(a,b)
#     else:
#         Disp2(a,b)
#     print()


# a = 1 
# b = 3 
# # Disp(a,b)   # 1 2 3 
# Disp(b,a)   # 3 2 1 


# 6 
# 1부터 까지 정수의 합을 구하는 재귀함수를 살펴 봅시다 
# def sum1(n):
#     result = 0
#     for i in range(1, n+1):
#         result += i 
#     return result 


# def sum2(n):
#     if n == 1:
#         return 1
#     else:
#         return n + sum2(n-1)


# print(sum1(10))
# print(sum2(10))


# 7 
# 팩토리얼 값을 재귀함수를 이용하여 구해 봅시다 

# def fact(n):
#     if n == 0:
#         return 1 
#     return n *fact(n-1)

# print(fact(4))


# 8 
# exp(3, 2) = 3 ** 2 = 9를 재귀적으로 작성하여 봅시다 

# def exp(a, n):
#     if n == 1:
#         return a
#     else:
#         return a * exp(a, n-1)
    
# s1, s2 = input('입력 :').split()
# n1 = int(s1)
# n2 = int(s2)
# print('==>', exp(n1, n2))
# print(exp(3, 3))


# 9 
# 피보나치 수열을 재귀함수로 구해 봅시다 

# def fi(n):
#     if n <= 1:
#         return n
#     return fi(n-1) + fi(n-2)

# print(fi(0))



# Question 1 
# def recursive(n):
#     print(n, end=' ')
#     if n == 7:
#         return 
#     recursive(n+1)

# recursive(1)



# Question 2 
# def recursive(n):
#     if n == num+1:
#         return 
#     recursive(n+1)
#     print('{}일 남았습니다 !'.format(n))

# num = int(input('정수를 입력하세요 : '))
# recursive(1)
# print('--- 끝 ---')


# Question 3 
# def recursive(n):
#     if n == 0:
#         return 
#     recursive(n-1)
#     print('#', end='')

# recursive(10)


# Question 4 
# iterative
# def recursive(n):
#     if n == 0:
#         return 
#     recursive(n-1)
#     for i in range(10):
#         print('#', end='')
#     print()

# recursive(5)


# Question 5 
# def plus_one(n):
#     if n == 0:
#         return
#     plus_one(n - 1)
#     print(n, end=' ')


# def row(n):
#     if n == 0:
#         return 
#     row(n-1)
#     plus_one(10)
#     print()

# row(5)


# Question 6 
# def recursive(n):
#     if n == 0:
#         return
#     recursive(n-1)
#     for i in range(n):
#         print('#', end='')
#     print()
    
# recursive(5)

# or 

# def recursive(n):
#     if n == 0:
#         return
#     recursive(n-1)
#     print('#', end='')


# for i in range(1,6):
#     recursive(i)
#     print()


# 별 찍는거 
# for i in range(5):
#     for j in range(i+1):
#         print('#', end='')
#     print()


# Question 7   # hw   
# def recursive(n):
#     if n == 6:
#         return 
#     recursive(n+1)
#     printout(n)
#     print()


# def printout(n):
#     if n == 0:
#         return 
#     printout(n-1)
#     print('#', end = '')

# recursive(1)    


# 별 찍는거 
# for i in range(5):
#     for j in range(5-i):
#         print('#', end='')
#     print()



# 집가서 다시 하기 
# def recursive(n):
#     if n == 0:
#         return 
#     recursive(n-1)
#     printout(n)
#     print()


# def printout(n):
#     if n == 0:
#         return 
#     printout(n-1)
#     print('#', end = '')

# recursive(5)   




# Question 8
# def recursive(n):
#     if n == 0:
#         return
#     recursive(n-1)
#     for i in range(5 - n):
#         print(' ', end='')
#     for j in range(n*2 - 1):
#         print('#', end='')
#     print()

# recursive(5)


# 별 찍는거 
# for i in range(1,6):
#     for j in range(6-i):
#         print(' ', end='')
#     for k in range(i*2 - 1):
#         print('#', end='')
#     print()


# Question 9 
# def recursive(n):
#     if n == 6:
#         return 
#     recursive(n+1)
#     for i in range(5-n):
#         print(' ', end=' ')
#     for j in range(2*n - 1):
#         print('#', end=' ')
#     print()

# recursive(1)


# # or  풀어오기 
# def space(n):


# def star(n):




# for i in range(5):
#     recursive(1)






# 별 찍는거 
# for i in range(5):
#     for j in range(i):
#         print(' ', end=' ')
#     for k in range(9-2*i):
#         print('#', end=' ')
#     print()



# Question 10  
# start, end = input('시작과 끝값 입력 : ').split()
# print('두 수 사이의 짝수 --> ', end='')

# def recursive(start, end):
#     if end == start:
#         return 
#     recursive(start, end - 1)
#     if end % 2 == 0:
#         print(end, end = ' ')
    
# recursive(int(start), int(end))



# Question 11  
# def change_num(n):
#     print(n , end=' ')
#     if n == 1:
#         return 1
    
#     elif n % 2 != 0:
#         change_num(3*n + 1)

#     elif n % 2 == 0:
#         change_num(n // 2)
    
# input1 = int(input('n 값 입력 : '))
# change_num(input1)


# Question 12
# def Sum(n):
#     print(n, end='+')
#     if n == 10:
#         return n 
#     return n + Sum(n+1)

# print('\b={}'.format(Sum(1)))

# or 

# def Sum(n):
#     if n == 1:
#         return 1
#     return n + Sum(n-1)
    
# for i in range(1,11):
#     print(i, end='+')
# print('\b={}'.format(Sum(10)))


# Question 13 
# def factorial(n):
#     if n == 1:
#         return 1
#     return n * factorial(n-1)

# for i in range(1,11):
#     print('{}!={}'.format(i, factorial(i)))


# Question 14  
# def recursive(n):
#     print(n, end=' ')
#     if n == -2:
#         return 
#     recursive(n-3)

# recursive(10)


# Question 15 
# first = int(input('첫 번째수 입력 : '))
# second = int(input('두 번째수 입력 : '))

# def recursive(first, second):
#     if second == first:
#         return first
#     return second + recursive(first, second-1)

# print('{}부터 {}까지의 합 = {}'.format(first,second,recursive(first, second)))



# Question 16 
# def multiple(n):
#     if n == 1:
#         return 1 
#     return n * multiple(n-1)

# until = int(input('어디까지의 곱을 계산할까요? '))
# print(multiple(until))


# Question 17 
# def binary(num):
#     if num == 1:
#         print(num, end='')
#         return 
#     binary(num // 2)
#     print(num % 2, end='')


# ten = int(input('10진수 값 입력 : '))
# binary(ten)


# Question 18 
# def show_digit(num):
#     if num < 10:
#         print(num, end=' ')
#         return 
#     show_digit(num // 10)
#     print(num % 10, end=' ')


# input1 = int(input('정수를 입력하시오: '))
# show_digit(input1)


# Question 19   
# def digit(num):
#     print(num % 10, end=' ')
#     if num < 10:
#         return 
#     digit(num // 10)


# input1 = int(input('정수 입력 : '))
# digit(input1)


### 
# Question 20   ????
# arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# length = len(arr)
# cnt = 0

# def binary_search(find, length):

#     if arr[length] == find:
#         return True 
#     else:




# find = int(input('찾을값 : '))
# if binary_search(find):
#     print('타겟저장인덱스 : {}'.format())
# else:
#     print('탐색실패')



# Question 22 ???
# num = int(input('2의 몇승을 구할까요 : '))

# def exponential(n):
#     if n == 1:
#         return 1
#     return 2 * exponential(n-1)

# print('2의{} 승 = {}'.format(num,exponential(num)))




# Question 23
# def change_digit(num, digit):
#     if num < digit:   
#         print(num, end=' ')
#         return 
#     change_digit(num // digit, digit)
#     print(num % digit, end=' ')


# ten = int(input('10진수 값 : '))
# digit = int(input('몇진수로 바꿀까요 : '))
# change_digit(ten, digit)



# Question 24 
# def Sum(n):
#     if n == 1:
#         return 1
#     return Sum(n-1) + n ** 3


# num = int(input('n : '))
# print('합 = {}'.format(Sum(num)))


# Question 25  # ??? 프린트할때 start도 홀수이면 프린트해야됨? 시작값, 끝값도 포함? 시작 끝값 폴함해서 다시 만들어보기 
# def recursive(start, end):
#     if end == start:
#         return start 
#     recursive(start, end -1)
#     if end % 2 != 0:
#         print(end, end=' ')

# first = int(input('시작값 : '))
# second = int(input('끝 값 : '))
# recursive(first, second)


# Question 26 
# def is_palindrome(word):
#     if len(word) <= 1:
#         return True
#     else: 
#         if word[0] == word[-1]:
#             return is_palindrome(word[1:-1])
#         else:
#             return False 


# input1 = input('단어를 입력하세요 : ')
# if is_palindrome(input1):
#     print('회문 입니다')
# else:
#     print('회문이 아닙니다')