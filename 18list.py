# 5가지 컨테이너 
# - 문자열, 튜플, 리스트, 사전, set에 사용할 수 있는 유용한 기능 
# s = 'bar' # 문자열 
# t = ('b','a','r') # 튜플 (소괄호) 로 감쌈
# l = ['b','a','r'] # 리스트 [대괄호] 로 감쌈
# d = {1:'b',2:'a', 3:'r'} # 사전 {중괄호} 로 감쌈 


# <시퀀스 자료형>
# - 여러 객체를 저장하는 자료형 
# - 문자열, 리스트, 튜플 


# <시퀀스 자료형의 공통적인 연산>
# 구분      연산                 설명

# 인덱싱    [k]형식              k번 위치의 하나를 취한다. 
# 슬라이싱   [s : t : p] 형식    s부터 t 사이 구간의 값을 p 간격으로 취한다 
# 연결하기   + 연산자             두 시퀀스형 데이터를 붙여서 새로운 데이터를 만든다. 
# 반복하기   * 연산자             시퀀스형 데이터를 여러번 반복해서 새로운 데이터를 만든다 
# 멤버검사   in 연산자            어떤 값이 시퀀스 자료형에 속하는지 검사한다
# 길이정보   len() 내장함수        시퀀스형 데이터의 크기를 나타낸다. 


# 리스트는 []로 항목을 구분하며 항목을 변경할 수 있는 시퀀스 자료

# - list 매소드 (함수)
# append --> 데이터를 리스트 끝에 추가(push)한다.
# pop --> 리스트의 지정한 값 하나를 읽어내고 삭제(pop)한다.
# sort --> 리스트를 정렬한다. 
# reverse --> 리스트의 순서를 바꾼다. 
# index --> 요소를 검색한다. 
# insert --> 데이터를 지정한 위치에 삽입 
# remove --> 리스트의 지정한 값 하나를 삭제한다. 
# extend --> 리스트를 추가한다.
# count --> 요소의 개수를 알아낸다.      
# clear --> 리스트의 내용을 모두 지운다. 
# del --> 리스트에서 해당위치를 삭제한다. 
# ex1)
# fruits = ['apple', 'banana', 'cherry', 'orange']
# del fruits[2]  # remove 'cherry'
# print(fruits)  # output: ['apple', 'banana', 'orange']
# ex2)
# fruits = ['apple', 'banana', 'cherry', 'orange']
# del fruits[1:3]  # remove 'banana' and 'cherry'
# print(fruits)  # output: ['apple', 'orange']
# len --> 리스트에 포함된 항목의 개수를 샌다. 
# copy --> 리스트의 내용을 새로운 리스트에 복사한다.
# sorted --> 리스트의 항목을 정렬해서 새로운 리스트에 대입한다   


# 1 - 5 : 리스트를 생성하는 방법 
# 1 
# aa =[]
# bb = [10,20,30,40,50]
# cc = ['파이썬', '자바', 'C언어']
# dd = ['홍길동', 170, 60.4]
#
# print(aa)
# print(bb)
# print(cc)
# print(dd)

# 2 
# aa = []
# bb = []
# value = 0 

# for i in range(0, 100):
#     aa.append(value)
#     value += 2 
# # print(aa)
# for n in aa:
#     print(n, end='  ')    # 0  2  4  6  .....  198 
# print()


# for i in range(0, 100):    
#     bb.append(aa[99 - i]) 
# for n in bb:
#     print(n, end='  ')    # 198  196  ....... 0 


# 3 
# L = []
# L1 = [1, 2, 3,4,5,6,7,'Great']
# print(L1)
# print(L1[0], L1[-1])
# print(L1[1:3], L1[:])    #  L1[:] 전체를 출력하라는 얘기
# print(L1*2)
# L2 = list(range(10))
# print(L2)
# print(L2[::2]) # 2칸씩 이동
# print(L1 + L2)


# print('길이=', len(L1))
# print(4 in L2)       # in 그 안에 값이 들어있는지 


# 4 
# A = [ x for x in range(10)]    # 오른쪽 x를 한개씩 왼쪽 x으로 옮겨서 append 
# print('A=',A)
# B = [ x for x in 'abcd']
# print('B=', B)
# print('A=',A)
# print(B[1])


# 5 
# list() 로 리스트를 생성하여 봅시다

# A = list()
# print(A)
# B=list('abc')
# print(B)
# C = list(range(5))
# print(C)


# 6 
# t_list = ['apple', 'banana', 'orange', 'melon']
# for i in t_list:
#     print(i)


# 7 
# L = [ 2, 1, 3, 5, 4]
# for i in range(len(L)):
#     L[i] *= 10
# print('L= %s ' % L)           
# print('L= {}'.format(L))


# c언어에서는 
# print('[', end='')
# for d in L:
#     print('%d'%(d), end=',')

# print(']')



# 8 
# A = [1,2,3]
# B = [1,2,3]
# print(A == B)   # compare the values of the lists --> True 
# print(A is B)   # compare the id --> False 
# print(id(A), id(B))
# B = A   # ID copy 
# print(A == B)
# print(A is B)   
# print(id(A), id(B))  # id는 데이터가 저장된 시작 주소 



# 9 
# print(10 in [10,20,30])
# print(10  not in [10,20,30])    # 10이 없어야 True, 있으면 False --> 반대가 되는것 
# print([1,2,3] + [4,5,6])
# print([0,1,2] * 3)
# print(3*[0,1,2])



# 10 
# A = [10, 20, 30, 40, 40, 40, 40, 50]
# print(len(A), min(A), max(A))  # 리스트의 길이, 최소값, 최대값 
# print(A.index(30))  # 30의 인덱스 = 순서 
# print(A.index(40))  # index() --> 첫번째 순서 
# print(A.count(40))  # 40의 개수 
# print()
# A[0] = 100  # 부분변경
# print(A)
# A = [0,1,2,3,4,5]
# A[1:4] = [10,20,30]  # 부분리스트 변경
# print(A)
# A = [0,1,2,3,4,5]
# A[1:4] = []  # 부분 리스트 삭제 
# print(A)
# A = [1,2,3,4,5]
# A.append(6)  # 6 추가 
# print(A)
# A.append([100,200,300])  # 100,200,300 추가 --> list.append() takes exactly one argument 
# print(A)
# A.clear()  # 모두 삭제 --> list.clear() takes no arguments 
# print(A)


# 11    
# A = [10,20,30]
# B = A   # 얕은 복사  --> a가 변경되면 b도 바뀐다. a,b가 같은 공간을 사용하기 때문에 둘중에 하나가 바뀌면 같이 바뀐다 
# print(id(A), id(B))


# A[0] = 100
# print(A)
# print(B)
# A = [0, [1,2]]
# B = A.copy()   # 깊은 복사 --> 공간을 새로 만들어서 복사하기 때문에 서로 영향을 미치지 않는다 
# print(id(A), id(B))
# A[1] = 100 
# print(A)
# print(B)
# print()


# 12
# A = [1,2,3]
# A.extend([4,5,6])  # 리스트 확장
# print(A)
# A.insert(1,100) # 지정한 위치에 삽입 
# print(A)
# print(A.pop()) # 마지막 항목 꺼내고 삭제 --> 끝에서부터 return하고 삭제함 
# print(A)
# A.pop(1)  # 1 위치 항목 반환 후 삭제   
# print(A)
# A.remove(2)  # 처음 나오는 2 삭제 
# print(A)
# A.reverse()  # 리스트 뒤집기 
# print(A)



# 13
# 리스트에 튜플이나 리스트가 있는 경우 반복참조를 하여 봅시다 
# index == 첨자
# it = [('one', 1), ('two', 2), ('three', 3)]
# print(it[0])  
# print(it[0][0], it[0][1])
# for t in it:
#     print('name={:7} num={}'.format(t[0], t[1]))
# print()
# for name, num in it:
#     print('name={:7} num={}'.format(name, num))
# print()
# for name, num in it:
#     print(name, num)



# 14 
# list.sort() 메소드를 사용하여 정렬하여 봅시다
# 내가 만드는 함수 == function 
# 표준으로 만들어진 함수 == 메소드 method
# 숫자 정렬 
# A = [2,3,5,1,0]
# A.sort() # ascending --> 오름차순 
# print(A)    # [0, 1, 2, 3, 5]
# A.sort(reverse=True) # 역순 정렬 
# print(A)



# 문자열 정렬 
# colors = ['blue','green','orange','red','yellow','purple']
# colors.sort()
# print(colors)
# colors.sort(reverse=True)
# print(colors)



# 문자열을 대소문자 구분없이 정렬 
# L = 'Python is a Programming Language'.split()
# L.sort()  # 대문자 ascii code가 더 작아서 앞에옴 
# print(L)

# L.sort(key=str.lower)  # 모두 소문자로 변경해서 비교해라, key --> 비교하는 기준, sort할때만 바뀌어서 비교될뿐 원래 데이터는 바뀌지 않는다 
# print(L)


# 문자열 비교 정렬 
# ascii code는 문자한테만 있는것 
# L = ['123', '34', '56', '2345']    
# L.sort()
# print(L)
# 키워드로 전달된 함수를 통과한 값과 비교하여 정렬 
# L = ['123', '34', '56', '2345']
# L.sort(key=int)   # sort 할때만 바뀌어서 비교될뿐 원래 데이터는 바뀌지 않는다 
# print(L)



# 15 
# ct_list = ['apple', 'banana', 'grape', 'orange']
# print(ct_list)
# 리스트에 있는 문자열을 변경 
# ct_list[2] = 'kiwi'
# print(ct_list[0], end=' ')
# print(ct_list[1], end=' ')
# print(ct_list[2], end=' ')
# print(ct_list[3])

# 위 문자열을 2번째부터 4번째까지 출력 
# print(ct_list[2:4])

# 리스트에 또 다른 리스트 저장 
# t_list = [ct_list, ct_list]
# print(t_list)


# 리스트를 더하여 다른 리스트에 저장 
# list1 = [1,2,3,4]
# list2 = ['apple', 'banana', 'grape', 'kiwi']
# list3 = list1 + list2 
# print(list3)
# print(list1 * 2)



# 16       
# 여려가지 인수로 전달하여 인덱싱을 참조하여 봅시다 
# L = [0,1,1,2,3,5,8,13,21]
# print('next value of {0[4]} is {0[5]}'.format(L))  # 리스트 인수전달 

# print('나이:{age} 키:{height}'.format(age=23, height=175))  # 키워드 인수전달 

# info = {'size':32, 'height':173, 'age':43}
# print('나이:{age} 키:{height}'.format_map(info)) # 사전을 인수로 전달 



# 17 
# 내장함수 sorted()를 사용하여 list를 정렬하여 봅시다
# 숫자 정렬 
# A = [2,3,5,1,0]
# B = (sorted(A))
# print(B)
# print(sorted(A,reverse = True))



# 문자정렬 
# colors = ['blue', 'green', 'orange', 'red', 'yellow', 'purple']
# print(sorted(colors))
# print(sorted(colors, key=str.lower))  # 소문자 기준으로 오름차순    
# print(sorted(colors, key=str.lower, reverse=True)) # 소문자 기준으로 내림차순    
# print(sorted(colors, key=lambda s: s[-1]))  # 마지막 문자를 기준으로 sort()    
# print(sorted(colors, key=lambda s: s[-1], reverse = True)) 



# 18 
# reversed() 함수를 사용하여 리스트를 역순으로 참조하여 봅시다. --> reverse랑 sort랑 헷갈리지 말기 
# L = ['123', '34', '56', '2345']   
# for ele in reversed(L):
#     print(ele)


# 19 
# friend_list = []  
# friend = input('친구의 이름을 입력하시오: ')
# friend_list.append(friend)
# friend = input('친구의 이름을 입력하시오: ')
# friend_list.append(friend)
# friend = input('친구의 이름을 입력하시오: ')
# friend_list.append(friend)
# friend = input('친구의 이름을 입력하시오: ')
# friend_list.append(friend)
# friend = input('친구의 이름을 입력하시오: ')
# friend_list.append(friend)
# print(friend_list)


# 20 
# print('햄버거를 만들어보자.')
# basemat = ('빵','토마토','야채','소스')
# coremat = ('새우','불고기','한우','치즈')

# print('''{food}의 기본재료는 {base}이고,
# 핵심재료에 따라 이름이 달라져.'''.format(food='햄버거', base=basemat))
# print()
# for item in coremat:
#     print('핵심재료가 {core}면 {core}버거'.format(core=item))
    # print('핵심재료가 {}면 {}버거'.format(item, item))




# 21 
# import random 
# quotes = []
# quotes.append('꿈을 지녀라. 그러면 어려운 현실을 이길 수 있다.')
# quotes.append('분노는 바보들의 가슴속에서만 살아간다..')
# quotes.append('고생 없이 얻을 수 있는 진실로 귀중한 것은 하나도 없다.')
# quotes.append('사람은 사랑할 때 누구나 시인이 된다.')
# quotes.append('시작이 반이다.')
# print(quotes)
# dailyQuote = random.choice(quotes)
# print('#' * 28)
# print('#       오늘의 속담        #')
# print('#' * 28)
# print('')
# print(dailyQuote)


# 2차원 리스트 
# 22
# 3행 4열의 리스트를 만들고 출력하여 봅시다 
# list1 = []
# list2 = []
# value = 1 
# for i in range(0,3):
#     for k in range(0,4):
#         list1.append(value)
#         value += 1 
#     list2.append(list1)
#     list1 = []
# print(list2)  #list2 = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
# for i in range(0,3):
#     for k in range(0, 4):
#         print('%3d' % list2[i][k], end =' ')   
#     print('')


# 23  
# 여러가지 방법으로 리스트를 생성하여 봅시다.
# A = [num for num in range(1,6)]  # Comprehension --> 언어 이해력 연습 
# print('A=',A)

# B = [num * num for num in range(1,6)]
# print('B=',B)

# C = [num for num in range(1,21) if num%3 == 0]
# print('C=',C)

# D = [(x,x*2) for x in range(5)]
# print('D=',D)   # D = [(0, 0), (1, 2), (2, 4), (3, 6), (4, 8)]



# E = F = [[i * 3 + j for j in range(2)] for i in range(3)]
# print(E)    # E = [[0, 1], [3, 4], [6, 7]]
# print(E[0][0])
# print(E[1][0])
# print(E[2][0])
# print(E[2][1])

# print('F=',F)


# 24
# 5행5열의 리스트를 작성하여 봅시다. 
# print([0] * 5 )
# m =[[0] * 5 for i in range(5)]
# # print(m)   # m =[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
# n = 0 
# for i in range(0,5):
#     for j in range(0,5):
#         m[i][j] = n 
#         n += 1 
# # print(m)   # m =[[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19], [20, 21, 22, 23, 24]]

# for i in range(0,5):
#     for j in range(0,5):
#         print(m[i][j], end=' ')
#     print()


# 25      
# 동시에 여러개의 리스트에 접근하여 봅시다. 
# zip() --> 짝 맞춰주는 함수, 뒤에 짝 없는것은 안찍힘 
# foods = ["떡볶이", "짜장면", "라면", "피자", "맥주", "치킨", "삼겹살"]
# sides = ["오뎅", "단무지", "김치"]
# for food, side in zip(foods,sides):
#     print(food, '-->', side)


# 26 
# foods = ['떡볶이', '짜장면', '라면', '피자', '맥주', '치킨', '삼겹살']
# sides = ["오뎅", "단무지", "김치"]


# tuplist = list(zip(foods, sides))
# print(tuplist)

# dic = dict(zip(foods, sides))
# print(dic)



# 27     
# 두 시퀀스의 자료형의 모든 데이터의 조합을 만들어 봅시다. (다중포문)
# seq1 = 'abc'
# seq2 = (1,2,3)
# print([(x,y) for x in seq1 for y in seq2])   # [('a', 1), ('a', 2), ('a', 3), ('b', 1), ('b', 2), ('b', 3), ('c', 1), ('c', 2), ('c', 3)]


# 28 
# 리스트를 중첩하여 봅시다.
# L = [[row + (i*3) for row in [10, 11, 12, 13]] for i in [0,1,2]]
# print(L)    # [[10, 11, 12, 13], [13, 14, 15, 16], [16, 17, 18, 19]]




# Question 1  
# myList = [x for x in range(100,400,100)]
# print(myList)

# l = list(range(100,400,100))
# print(l)

# l=[100,400,100]

# extend와 append의 차이 
# append는 한개씩 넣을수있는데 extend는 여러개를 넣을수있다 
# l=[2,3]
# l.extend([100,400,100])
# print(l)

# l=[2,3]
# l.append([10,20,30])
# print(l)


# Question 2 
# list_odd = [1,3,5,7,9]
# list_even = [2,4,6,8,10]
# print(list_odd[-3])   # 5
# print(list_odd[1+3])  # 9 
# print(list_odd + list_even)
# print(list_odd * 2 )


# Question 3 
# l= []
# for i in range(4):
#     num = int(input('{}st number : '.format(i+1)))
#     l.append(num)

# print('4 번째 : {}'.format(l[3]))
# print('3 번째 : {}'.format(l[2]))



# Question 4 
# string = ['a', 'b', 'c', 'd', 'e', 'f']

# print(string[0:3])
# print(string[2:5])
# print(string[1:3])


# Question 5 
# import random 
# l = []
# for i in range(20):
#     n = random.randint(0,99)
#     l.append(n)  


# for i in range(len(l)):
#     if i % 5 == 0:
#         print()
#     print('[{:>2}:{:>2}]'.format(i,l[i]), end=' ')



# Question 6     
# spell = ['j', 'e', 's', 'u', 's']
# spell[2:5]= ['l','l','y']
# print(spell)


# Question 7 
# number = [2,4,8,10]
# number.insert(2,6)
# print(number)


# Question 8 
# list1 = ['a', ['b'], ['c', 'd'], 1 , [2,3], 'e']
# print(len(list1))      # 6 
# print('b' in list1)  # False 
# print(['d'] in list1)  # False 
# print('a' in list1)    # True 
# print([2,3] in list1)  # True 


# Question 9  
# l = list(range(10))
# print(l)


# list1 = []
# for i in range(len(l) + 1):
#     list1.append(i**2)
# print(list1)

# l = list(range(0,10,2))
# print(l)



# Question 10 
# int_num_a = [0,1,2,3]
# int_num_b = [4,5,6]

# int_num_c = int_num_a + int_num_b
# for i in range(-1, -(len(int_num_c)) - 1, -1):
#     print(int_num_c[i], end=' ')


# for i in reversed(int_num_c):
#     print(i, end=' ')


# Question 11 
# score = [90, 75, 30, 100, 83]
# Sum = 0 
# count = 0 
# for i in range(len(score)):
#     Sum += score[i]
#     count += 1 
# average = Sum / count 

# print('총점 = {}  평균 = {:.2f}'.format(Sum, average))

# or

# score = [90, 75, 30, 100, 83]
# Sum = sum(score) 
# average = Sum / len(score)
# print('총점 = {}  평균 = {:.2f}'.format(Sum, average))




# sort()와 sorted()의 차이
# sort()는 자기자신을 sort
# sorted()는 sort한 내용을 다른 리스트에 넣는것 

# myList = [100, 300, 200]
# myList.sort()
# print(myList)

# final = sorted(myList)
# print(final)
# print(myList)


# Question 12 
# myList = [100, 200, 300]
# print(myList)
# myList.extend([400, 300, 200])
# print(myList)
# myList.sort()
# print(myList)


# Question 13  
# myList = [1, 5, 10]
# print(myList)
# myList.insert(2,3)
# print(myList)

# num = int(input('값: '))
# for i in myList:
#     if i == num:
#         print('{} 의 위치는 {}'.format(i, myList.index(i)))




# Question 14    
# l = []
# count = 0 
# Sum = 0 
# for i in range(5):
#     num = int(input('정수를 입력하시오: '))
#     l.append(num)

# for i in l:
#     Sum += i 

# average = Sum / len(l)
# print('평균= {}'.format(average))


# Question 15 
# list = [1,2,3,4]  
# Sum = sum(list)
# print('리스트 숫자의 합 = {}'.format(Sum))


# Question 16
# myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for i in range(2,12,2):
#     k = myList.index(i)
    # myList.pop(k)
    # myList.remove(myList[k])

# print(myList)


# Question 17      
# favorite_list = ['Hotel California', 7, 'Tiger', True]
# favorite_list.reverse()
# print(favorite_list)


# Question 18   
# names = ['Lee suji', 'park sangmin', 'ha nuri']
# input1 = input()
# if input1 in names:
#     print('{} 는 연구실에 근무하고 있습니다.'.format(input1))


# Question 19 
# numlist = [5, 9, 301, 714]
# if len(numlist) != 5:
#     print('numlist 는 통과할 수 없습니다')


# Question 20 
# int_num_a = [1,2,3]
# int_num_c = int_num_a * 3 
# print(int_num_c)

 
# Question 21 
# mList = ['홍길동', '장동건', '이종석', '서태지']
# fList = ['강수영', '민소진', '남수지', '안영미']
# l = []
# for i in range(len(mList)):
#     l.append(mList[i][0])

# for i in range(len(fList)):
#     l.append(fList[i][0])

# l.sort()
# print(l)

# or

# mList = ['홍길동', '장동건', '이종석', '서태지']
# fList = ['강수영', '민소진', '남수지', '안영미']
# total_list = mList + fList
# l = []

# for i in range(len(total_list)):
#     l.append(total_list[i][0])

# print(sorted(l))


# Question 22   
# import random
# input1 = int(input('N = '))
# a = []
# b = []

# for i in range(input1):
#     a.append(random.randint(1,5))
# print(a)

# for i in range(0, len(a)-1, 2):
#     b.append(a[i]+a[i+1])

# if len(a)%2==1:
#     b.append(a[-1])
# print(b)


# Question 23 
# final_list = []
# myList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
# for i in range(0, len(myList) - 2 , 3):
#     final_list.append( [myList[i], myList[i+1], myList[i+2] ])

# if len(myList) % 3 == 1:
#     final_list.append(myList[-1])
# elif len(myList) % 3 ==2:
#     final_list.append( [myList[-2], myList[-1] ])
# print(final_list)

# or

# final_list = []
# myList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
# tmp=[]
# for i in myList:
#     tmp.append(i)
#     if len(tmp)==3:
#         final_list.append( tmp)
#         tmp=[]

# if len(tmp)>0:
#     final_list.append(tmp)
# print(final_list)



# Question 24    
# List = ['blind', 'apple', 'coin']
# List.append('zoo')
# print(List.sort())
# print(sorted(List))


# Question 25
# number = [2, 4, 5, 6, 8, 10]
# for i in range(len(number)):
#     if i == 0 :
#         Max = number[i]
#         Min = number[i]
#     elif number[i] > Max:
#         Max = number[i]
#     elif number[i] < Min:
#         Min = number[i]

# l = [Min, Max ]
# print(l)

# or

# number = [2, 4, 5, 6, 8, 10]
# l = [min(number), max(number)]
# print(l)


# Question 26 
# List = [70, 100, 80, 60, 90, 30, 20, 50]
# for i in range(len(List)):
#     if i == 0 :
#         Max = List[i]
#         Min = List[i]
#     elif List[i] > Max:
#         Max = List[i]
#     elif List[i] < Min:
#         Min = List[i]

# print('최대값 : {} ({}번째)'.format(Max, List.index(Max)))
# print('최소값 : {} ({}번째)'.format(Min, List.index(Min)))


# or 

# List = [70, 100, 80, 60, 90, 30, 20, 50]
# print('최대값 : {} ({}번째)'.format(max(List), List.index(max(List))))
# print('최소값 : {} ({}번째)'.format(min(List), List.index(min(List))))


# Question 27 
# fruits = ['apple', 'orange', 'kiwi', 'banana', 'grape']
# numbers = [100, 200, 300, 400, 500]
# final_list = []

# for i in range(len(fruits)):
#     final_list.append([fruits[i] , numbers[i]])

# print(final_list)
# final_list.sort(reverse = True)    # 아무것도 안적으면 기본이 맨앞에 있는 항목 
# print(final_list)



# Question 28 
# list_ex1 = ['risk', 'issue', 'test', 'maintenance', 'maturity']
# list_ex2 = ['security', 'plan',' design', 'systematic', 'safety']
# list_ex3 = ['maintenance', 'verifacition', 'validation']

# total_list = []
# total_list.extend([list_ex1,list_ex2,list_ex3])

# for i in range(len(total_list)):
#     for j in range(len(total_list[i])):
#         if total_list[i][j] == 'maintenance' and len(total_list[i]) >= 5:
#             available_list = 'list_ex{}'.format(i+1)

# print('시험문제로 사용할 수 있는 리스트는 {} 입니다'.format(available_list))



# Question 29    
# list1 = [x for x in range(0,60,3)]
# l = []
# final_list = []
# for i in list1:
#     l.append(i)
#     if len(l) == 5:
#         final_list.append(l)
#         l = []


# for i in range(len(final_list)):
#     for j in range(len(final_list[i])):
#         print('{:>3}'.format(final_list[i][j]), end=' ')
#     print()


# Question 32 
# season = ['spring', 'summer', 'fall', 'winter']
# season = season * 2 
# print(season)

# final_list = []
# for i in season:    # season = season * 2, len(season) == 8
#     if i in final_list:
#         final_list.append('winter')
#         continue
#     final_list.append(i)
#     print(final_list)

# print(final_list)


# or 

# season = ['spring', 'summer', 'fall', 'winter']
# season = season * 2 
# l2=[season[-1]]*4
# print(l2)
# print(season)

# season[4:8:1] = l2
# print(season)


 
# Question 33    
# import random
# dice = [1, 2, 3, 4, 5, 6]
# count = [0, 0, 0, 0, 0, 0]

# for i in range(1000):
#     n1 = random.randint(1,6)
#     for j in range(len(dice)):
#         if n1 == dice[j]:
#             count[j] += 1 

# for i in range(6):
#     print('주사위가  {} 인 경우는  {} 번'.format((i+1), count[i]))


# or 
# 간단한 방법
# import random
# count = [0, 0, 0, 0, 0, 0]

# for i in range(1000):
#     n1 = random.randint(1,6)
#     count[n1-1] += 1 

# for i in range(6):
#     print('주사위가  {} 인 경우는  {} 번'.format((i+1), count[i]))

# print(max(count), count.index(max(count)))


# Question 34 
# import random
# goodday = ['happy', 'love', 'sad', 'hot', 'angry', 'fortunate']
# n1 = random.randint(0, 5)
# print('0 ~ 5 중 원하는 번호를 선택 하세요 --> {}'.format(n1))
# print(goodday[n1])

# or 
# import random
# goodday = ['happy', 'love', 'sad', 'hot', 'angry', 'fortunate']
# n1 = random.choice(goodday)
# print('0 ~ 5 중 원하는 번호를 선택 하세요 --> {}'.format(goodday.index(n1)))
# print(n1)


# Question 35 
# participant = ['민지', '경희', '상구', '철수', '지민']
# print('공모전에 출전한 팀이다.')
# print(participant)
# print(len(participant))
# if len(participant) > 3:
#     print('팀원은 최대 3명까지 입니다. 줄이세요')


# Question 36
# import random 
# week = ['월', '토', '목', '금', '화', '수', '일']
# num = random.randint(0,6)

# print('상담 날짜 정하는 프로그램입니다.')
# print('0부터 6까지의 수 중 하나만 입력: {}'.format(num))
# print('당신의 상담은 {} 요일 입니다'.format(week[num]))


# Question 37 
# sl = ['Spam', 'egg', 'Ham']
# sl.sort(key = str.lower)
# print(sl)


# Question 38   
# strip() --> 왼쪽 오른쪽 스페이스 없애는 것 
# s = ' first item : second item : third item '
# l = []
# list1 = s.split(':')
# for i in range(len(list1)):
#     l.append(list1[i].strip())
# print(l)


# Question 39  
# ddi = ['닭', '개', '돼지', '쥐', '소', '호랑이', '토끼', '용', '뱀', '말', '양', '원숭이']
# birth = int(input('태어난 년도 : '))
# now = int(input('올해 년도 : '))
# age = now - birth
# print('당신은 {} 살이고 {} 띠 입니다'.format(age, ddi[birth%12 - 1]))






# 두번째 풀어보기 
# Q1 
# myList = []
# myList.extend([100,200,300])
# print(myList)


# Q2
# list_odd = [1,3,5,7,9]
# list_even = [2,4,6,8,10]

# print(list_odd[-3])     # 5
# print(list_odd[1+3])    # 9 
# print(list_odd + list_even)     # [1,3,5,7,9,2,4,6,8,10]
# print(list_odd * 2)     # [1,3,5,7,9,1,3,5,7,9]


# Q3
# final = []
# for i in range(1,5):
#     num = int(input('{}st number : '.format(i)))
#     final.append(num)

# print('4 번째 : {}'.format(final[3]))
# print('3 번째 : {}'.format(final[2]))


# Q4
# string = ['a', 'b', 'c', 'd', 'e', 'f']

# print(string[:3])
# print(string[2:5])
# print(string[1:3])



# Q5 
# import random 
# l = []
# for i in range(20):
#     n1 = random.randint(0, 99)
#     l.append(n1)


# for i in range(len(l)):
#     if i % 5 == 0 and i != 0:
#         print()
#     print('[{:>2}:{:>2}]'.format(i, l[i]), end=' ')



# Q6
# spell = ['j', 'e', 's', 'u', 's']
# spell[2:] = ['l', 'l', 'y']
# print(spell)


# Q7
# number = [2, 4, 8, 10]
# number.insert(2, 6)
# print(number)


# Q8
# list1 = ['a', 'b', ['c', 'd'], 1, [2,3], 'e']
# print(len(list1))   # 6 
# print(['b'] in list1)   # False 
# print(['d'] in list1)   # False 
# print('a' in list1)     # True 
# print([2,3] in list1)   # True 


# Q9 
# xs = list(i for i in range(0,20,2))
# print(xs)

# or 

# l = list(range(0,20,2))
# print(l)

# xs = list(i**2 for i in range(1,11))
# print(xs)

# xs = list(i for i in range(0,10,2))
# print(xs)

# or 

# l = list(range(0,10,2))
# print(l)



# Q10
# int_num_a = [0, 1, 2, 3]
# int_num_b = [4, 5, 6]
# int_num_c = int_num_a + int_num_b
# print(int_num_c)    # [0, 1, 2, 3, 4, 5, 6]
# for i in reversed(int_num_c):
#     print(i, end=' ')



# Q11
# score = [90, 75, 30, 100, 83]
# nSum = 0 
# for i in score:
#     nSum += i 
# print('총점 = {}  평균 = {:.2f}'.format(nSum, nSum/ len(score)))


# Q12
# myList = [100, 200, 300]
# print(myList)

# myList.extend([400, 300, 200])
# print(myList)

# myList.sort()
# print(myList)


# Q13
# myList = [1, 5, 10]
# print(myList)
# myList.insert(2, 3)
# print(myList)
# for i in range(len(myList)):
#     print(i)


# num = int(input('값: '))
# for i in myList:    # [1, 5, 3, 10]
#     if i == num:
#         print('{} 의 위치는 {}'.format(i, myList.index(i)))


# Q14
# num_list = []
# for i in range(5):
#     num = int(input('정수를 입력하시오 : '))
#     num_list.append(num)


# nSum = 0 
# for i in num_list:
#     nSum += i
# print('평균= {}'.format(nSum / len(num_list)))



# Q15
# list1 = [1, 2, 3, 4]
# nSum = list1[0] + list1[1] + list1[2] + list1[3]
# print('리스트 숫자들의 합 = {}'.format(nSum))

# or 

# list = [1,2,3,4]  
# nSum = sum(list)
# print('리스트 숫자들의 합 = {}'.format(nSum))



# Q16
# myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for i in myList:
#     if i % 2 ==0:
#         myList.remove(i)
# print(myList)


# Q17
# favorite_list = ['Hotel California', 7, 'Tiger', True]
# favorite_list.reverse()
# print(favorite_list)


# Q18
# list_names = ['Lee suji', 'park sangmin', 'ha nuri']
# name = input()
# if name in list_names:
#     print('{}는 연구실에 근무하고 있습니다.'.format(name))
# else:
#     print('{}는 연구실에 없습니다.'.format(name))


# Q19
# numlist = [5, 9, 301, 714]
# if len(numlist) == 5:
#     print('numlist 는 통과할 수 있습니다')
# else:
#     print('numlist 는 통과할 수 없습니다')


# Q20 
# int_num_a = [1, 2, 3]
# int_num_c = int_num_a * 3 
# print(int_num_c)


# Q21
# mList = ['홍길동', '장동건', '이종석', '서태지']
# fList = ['강수영', '민소진', '남수지', '안영미']
# final_list = []

# for i in mList:
#     final_list.append(i[0])

# for i in fList:
#     final_list.append(i[0])

# final_list.sort()
# print(final_list)


# or 

# mList = ['홍길동', '장동건', '이종석', '서태지']
# fList = ['강수영', '민소진', '남수지', '안영미']
# tmp_list = mList + fList
# tmp_list.sort(key=lambda s:s[0])

# final_list = []
# for i in tmp_list:
#     final_list.append(i[0])
# print(final_list)



# Q22
# import random 
# num = int(input('N = '))
# a_list = []
# b_list = []

# for i in range(num):
#     r1 = random.randint(1,5)
#     a_list.append(r1)
# print(a_list)


# nSum = 0 
# for i in range(len(a_list)):
#     if i % 2 == 0 and i != 0:
#         b_list.append(nSum)
#         nSum = 0 
#     nSum += a_list[i]
# b_list.append(nSum)
# print(b_list)




# Q23
# myList = ['a','b','c','d','e','f','g','h','i','j','k']
# final = []
# tmp = []

# for i in range(1, len(myList)+1):
#     tmp.append(myList[i-1])
#     if i % 3 == 0:
#         final.append(tmp)
#         tmp = []
# if len(myList) % 3 != 0:
#     final.append(tmp)
# print(final)



# Q24
# List = ['blind', 'apple', 'coin']
# List.append('zoo')
# List.sort()
# print(List)


# Q25
# number = [2, 4, 5, 6, 8, 10]
# max_min = []
# max_min.extend([min(number), max(number)])
# print(max_min)


# Q26
# List = [70, 100, 80, 60, 90, 30, 20, 50]
# print('최대값 : {} ({}번째)'.format(max(List), List.index(max(List))))
# print('최소값 : {} ({}번째)'.format(min(List), List.index(min(List))))


# Q27
# fruits = ['apple', 'orange', 'kiwi', 'banana', 'grape']
# numbers = [100, 200, 300, 400, 500]
# final = []

# print('병합후 : ', end='')
# for fruit, num in zip(fruits, numbers):
#     final.append([fruit, num])
# print(final)

# print('정렬후 : ', end='')
# final.sort(reverse = True)
# print(final)


# Q28          
# list_ex1 = ['risk', 'issue', 'test', 'maintenance', 'maturity']
# list_ex2 = ['security', 'plan',' design', 'systematic', 'safety']
# list_ex3 = ['maintenance', 'verifacition', 'validation']
# name_of_list = ['list_ex1', 'list_ex2', 'list_ex3']


# final = []
# final.append(list_ex1)
# final.append(list_ex2)
# final.append(list_ex3)
# # print(final)    # [['risk', 'issue', 'test', 'maintenance', 'maturity'], ['security', 'plan',' design', 'systematic', 'safety'], ['maintenance', 'verifacition', 'validation']]


# for i in range(len(final)):
#     if len(final[i]) >= 5 and 'maintenance' in final[i]:
#         print('시험문제로 사용할 수 있는 리스트는 {} 입니다'.format(name_of_list[i]))




# Q29 
# list_45 = list(x for x in range(0,60,3))

# for i in list_45:
#     print('{:>2}'.format(i), end='  ')
#     if i % 15 == 12:
#         print()


# Q32 
# season = ['spring', 'summer', 'fall', 'winter']
# season = season * 2 
# print(season)

# final_list = []
# for i in season:    # season = season * 2, len(season) == 8
#     if i in final_list:
#         final_list.append('winter')
#         continue
#     final_list.append(i)
#     print(final_list)

# print(final_list)


# or 

# season = ['spring', 'summer', 'fall', 'winter']
# season = season * 2 
# l2=[season[-1]]*4
# print(l2)
# print(season)

# season[4:8] = l2
# print(season)


# Q33 
# import random
# count = [0, 0, 0, 0, 0, 0]

# for i in range(1000):
#     n1 = random.randint(1,6)
#     count[n1-1] += 1 
    

# for i in range(6):
#     print('주사위가  {} 인 경우는  {} 번'.format((i+1), count[i]))

# print(max(count), count.index(max(count)))




# Q34
# import random
# goodday = ['happy', 'love', 'sad', 'hot', 'angry', 'fortunate']
# r1 = random.randint(0,5)
# print('0 ~ 5 중 원하는 번호를 선택 하세요 --> {}'.format(r1))
# print(goodday[r1])

# or 

# import random
# goodday = ['happy', 'love', 'sad', 'hot', 'angry', 'fortunate']
# n1 = random.choice(goodday)
# print('0 ~ 5 중 원하는 번호를 선택 하세요 --> {}'.format(goodday.index(n1)))
# print(n1)


# Q35
# team = ['민지', '경희', '상구', '철수', '지민']
# print('공모전에 출전한 팀이다.')
# print(team)
# print(len(team))
# if len(team) > 3:
#     print('팀원은 최대 3명까지 입니다. 줄이세요')



# Q36 
# import random
# week = ['월', '토', '목', '금', '화', '수', '일']
# r1 = random.randint(0,6)

# print('상담 날짜 정하는 프로그램입니다.')
# print('0부터 6까지의 수 중 하나만 입력: {}'.format(r1))
# print('당신의 상담은 {} 요일입니다.'.format(week[r1]))


# Q37
# sl = ['Spam', 'egg', 'Ham']
# sl.sort()
# print(sl)   # ['Ham', 'Spam', 'egg']
# sl.sort(key = str.lower)
# print(sl)   # ['egg', 'Ham', 'Spam']


# Q38 
# s = ' first item : second item : third item '
# s = s.strip().split(' : ')
# print(s)



# Q39 
# animal = ['닭', '개', '돼지', '쥐', '소', '호랑이', '토끼', '용', '뱀', '말', '양', '원숭이']
# birth = int(input('태어난 년도 : '))
# year = int(input('올해 년도 : '))
# print('당신은 {}살이고 {}띠 입니다'.format(year-birth, animal[(birth%12) - 1]))