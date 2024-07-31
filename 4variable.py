# 1 
# import keyword
# print(keyword.kwlist)
# print(len(keyword.kwlist))

# 3
# int float str bool
# int_Var = 10
# float_var = 3.14
# boolVar = False
# strVar = "안녕"

# print(type(int_Var))
# print(type(float_var))
# print(type(boolVar))
# print(type(strVar))
 
# 4 
# a = 100
# b = a 


# k1 = 10
# k2 = 20
# k3 = 3

# k1 = 20
# k2 = 10
# k3 = 3
# r = k1 + k2 + k3


# print(b)
# print(r)

# 5 
# x=x+1 == x+=1   x=x-1 == x-=1   x=x%2 == x%=2
# x = 1
# print(x)
# x += 1 # x = x+1
# print(x)
# x -= 1 
# print(x)

# 6 
# a = b = c = 0
# print(a, b, c)

# a,b = 10, 20
# print(a, b)

# a, b = b, a 
# print(a, b)

# a, * b = 1,2,3,4,5,6
# print(a,b)

# *a, b = 1, 2, 3 
# print(a,b)

# a,b,c = [1,2,3]
# print(a,b,c)

# a,b,c="456"
# print(a, b, c)  ??????
 
# 7 
# a = 1 + 2
# b = 1 - 2
# c = 1 * 2
# d = 1 / 2 
# e = 1 // 2 
# f = 1 % 2 
# print('a:{0}, b:{1}, c:{2}, d:{3}, e:{4}, f:{5}'.format(a,b,c,d,e,f))
# p = 2 * 3
# print("p=%d" %p)

# a:3, b:-1, c:2, d:0.5, e:0, f:1
# # p=6

# 8 
# a,b,c = (10,20,30)     # sep = ' '
# print('a=',a, '.','b=',b,'.','c=',c)
# print('a= %d, b=%d, c=%d' % (a,b,c))
# print('a= {}, b={}, c={}'.format(a,b,c))

# a= 10 . b= 20 . c= 30
# a= 10, b=20, c=30
# a= 10, b=20, c=30

# Question 1 
# X,Y,Z = 1,2,1.5
# print(X)
# print(X * Y)
# print(X + Y + Z)
# print(2X)      ?????????????????????? 이게 왜 안되는거? 그냥 21나오면 안되는거? 스트링이 아니기 때문에 그렇게 못나오는거?

# print(2 * X)
# print(2.0 * X)
# print(X - 1.0)
# print(X -1)
# print(Z - 0.5)
# print(XZ)    ?????????????????
# print(X * Z)

# 1
# 2
# 4.5
# error
# 2
# 2.0
# 0.0
# 0
# 1.0
# error
# 1.5

# Question 2 
# a = 5
# b = 7
# result = a * b
# print('{} * {} = {}'.format(a,b,result))


# Question 3
# portion = 123456 / 789
# the_rest = 123456 % 789
# print('몫   = {}'.format(portion))
# print('나머지 = {}'.format(the_rest))

# Question 4 
# a = 150 // 71
# b = 150 % 71
# print('학생들이 각각 받을 사탕의 수: %s개'%(a))    ???????????? 여기원래 %d 써야되는거 아니에요?
# print('남는 사탕의 수           : %s개'%(b))


# Question 5   ???????????
# num = 1
# name = 'sam'
# kor = 90
# eng = 85
# math = 95
# sum = kor + eng + math
# ave = sum / 3
# print('{}{:>5}{:>5}{:>5}{:>5}{:>5}{:>5}'.format('num','name','kor','eng','math','sum','ave'))
# print('{:>3}{:>5}{:>5}{:>5}{:>5}{:>5}{:>5.0f}'.format(num,name,kor,eng,math,sum,ave))


# Question 6
# num1 = 5
# num2 = 2
# sum = num1 + num2 
# subtract = num1 - num2
# multiply = num1 * num2
# divide = num1 / num2
# print('{} + {} = {}'.format(num1,num2,sum))
# print('{} - {} = {}'.format(num1,num2,subtract))
# print('{} * {} = {}'.format(num1,num2,multiply))
# print('{} / {} = {}'.format(num1,num2,divide))

# Question 7 
# name = '홍길동'
# blood = 'O'
# height = 165.5
# age = 18
# weight = 80.20
# print('이름  : {}'.format(name))
# print('혈핵형 : {}형'.format(blood))
# print('키   : {}Cm'.format(height))
# print('나이  : {}살'.format(age))
# print('몸무게 : {:.2f} kg'.format(weight))

# Question 8
# A,B = 10,20
# print('<<교환하기 전 각 변수의 값>>')
# print('A 의 값 = {}'.format(A))
# print('B 의 값= {}'.format(B))
# A,B=B,A
# print('<<교환 후의 각 변수의 값>>')
# print('A 의 값 = {}'.format(A))
# print('B 의 값= {}'.format(B))

# Question 9 
# a,b,c = 10,20,30
# print('교환 전 : a={} b={} c={}'.format(a,b,c))
# a,b,c = c,a,b
# print('교환 후 : a={} b={} c={}'.format(a,b,c))


