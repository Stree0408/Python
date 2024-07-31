# - 딕셔너리 : 키와 값(value)의 쌍으로 항목이 구성 
# 딕셔너리 변수 = {키:값1, 키:값2, 키:값3 ...}
# - key는 중복될 수 없다.
# - 변경 할 수 없는 자료형(tuple)만 dictionary의 key가 될 수 있다. (list와 사전은 안됨)
# - dictionary는 순서가 정해져 있지 않다.
# - dictionary 구조는 index 값이 아닌 key 값으로 value를 찾을 수 있다. 



# 딕셔너리 매소드 
# d = dict()
# d.clear() --> 사전 d의 모든 요소를 삭제 
# d.copy() --> 사전을 복사 
# d.get(key[, x]) --> 값이 존재하면 d[key]를 반환하고 아니면 x를 반환 
# d.setdefault(key[, x]) --> get() 매소드와 동일, 값이 존재하지 않을 때 값을 설정d[key]=x
# d.update(b) --> 사전 b의 모든 항목을 d에 갱신. for k in b.keys():d[k]=b[k]
# d.popitem() --> (키,값) 튜플을 반환하고 사전에서 항목제거 
# d.pop(key) --> key 항목의 값을 반환하고 사전에서 제거 
# d.fromkeys(seq[, value]) --> seq와 value를 이용하여 만든 새로운 사전을 반환



# 1 - 다양한 방법으로 dictionary 만들기 
# my_dict = {}
# print(type(my_dict))
# print(my_dict)
# my_dict_1 = {'fishing':'낚시질', 'fishing banks':'어초', 'fishing boat':'낚싯배'}
# print(my_dict_1)

# my_dict_2 = {1:'수소', 2:'헬륨', 2:'리튬', 3:'리튬'}    # key cannot be repeated 
# print(my_dict_2)    # {1:'수소', 2:'리튬', 3:'리튬'}

# my_dict_3 = {'name':'mr.Kang', 14003:[3,2,0,1]}
# print(my_dict_3)

# my_dict_4 = dict([(1,'서울'), (2,'부산')])    # dict expected at most 1 argument
# print(my_dict_4)

# my_dict_5 = {'name':'찬열', 'age':25, 'manager':'SM', 'job':'singer'}
# print(my_dict_5)

# price = {('떡볶이','김밥'):'3000원', ('라면','만두'):'4000원'}  # tuple을 key 값으로 사용 
# print(price)



# 2 - 내장 방식으로 딕셔너리를 만들어 봅시다.
# d1 ={w : 1 for w in 'abcdef'}
# print(d1)   # {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 1}



# 3 - 다음과 같은 두 개의 리스트로 딕셔너리를 만들어 봅시다. 
# keys = ['one', 'two', 'three']
# values = [1,2,3,4,5,6]
# d = dict(zip(keys, values))
# print(d)

# for k in d:
#     print(k)
# print()

# for k, v in d.items():    
#     print(k,v)

# print(d.items())    # key와 value, set을 items라고 부른다



# 4 - 두개의 시퀀스로 딕셔너리를 만들어 봅시다. 
# a1 = 'abcd'
# a2 = (1, 2, 3, 4)
# d1 = {x:y for x,y in zip(a1,a2)}
# print(d1)


# d2 = {w:k for k,w in [(1,'one'), (2, 'two'), (3, 'three')]}
# print(d2)   # {'one':1, 'two':2, 'three':3}

# l=['apple', 'banana', 'grape', 'kiwi', 'strawberry']
# for n, d in enumerate(l, 100):
#     print(n,d)


# d3 = {w:k+1 for k,w in enumerate(['one', 'two', 'three'])}    
# print(d3)    # {'one':1, 'two':2, 'three':3}


# 5 - 다중 for문을 사용하여 딕셔너리를 만들어 봅시다.
# d = {(k,v):k for k in range(3) for v in range(2)}
# print(d)    # {(0,0):0, (0,1):0, (1,0):1, (1,1):1, (2,0):2, (2,1):2}



# 6 - 영한사전을 만들고 검색하여 봅시다.
# english_dict = dict()
# english_dict['one'] = '하나'
# english_dict['two'] = '둘'
# english_dict['three'] = '셋'
# print(english_dict)

# word = input('단어를 입력하시오: ')
# print(english_dict[word])



# 7 - 딕셔너리에서 값을 가져오기, 수정, 추가를 하여 봅시다.
# my_phone = {'홍길동':'111-1111', '강감찬':'222-2222', '김가나':'333-3333'}
# print(my_phone)
# print(my_phone['홍길동'])
# print(my_phone.get('홍길동'))
# print(my_phone.get('qkrc', 'kim'))
# print()


# my_phone['홍길동'] = 'xxx'  # 항목 수정하기 
# print(my_phone)
# print()


# my_phone['샤이니'] = '444-4444'     # 항목 추가하기 
# my_phone['도깨비'] = '000'
# print(my_phone)



# 8 - 딕셔너리에서 값을 삭제하여 봅시다. 
# my_idol = {'직업':'가수', '나이':18, '이름':'수지', '생일':'1994-10-10'}
# print(my_idol)
# print()

# print(my_idol.pop('이름'))  # 항목 가져오면서 삭제하기 
# print(my_idol)
# print()


# del my_idol['나이']     # 항목 삭제하기 
# print(my_idol)
# print()

# print(my_idol.popitem())    # 임의의 항목 가져오면서 삭제하기 
# print(my_idol)
# print()
# my_idol.clear()     # 사전 비우기 
# print(my_idol)
# del my_idol   # deleting it from memeory 
# print(my_idol) --> 에러 뜸(the variable no longer exists)


# 9 - 딕셔너리 관련 매소드를 살펴 봅시다.
# d = {'one':1, 'two':2, 'three':3}

# d2 = d.copy()   # 사전 복사 
# print(d2)

# d['four'] = 4   # 새항목 추가 
# print(d)

# d3 = {'nine':9, 'ten':10}
# print(d3.keys())       # ['nine', 'ten']
# d.update(d3)    # add or update the key-value pairs of one dictionary(d) with the key-value pairs from another dictionary(d3).
# update --> 여러개를 추가(리스트의 extend와 비슷 )
# print(d)

# d.popitem()
# print(d)

# d.pop('two')
# print(d)



# 10 
# print('-------- for in a set --------')
# for a in {1,2,3}:
#     print('a = ', a)

# # print('-------- for in a dict')
# D = {'one':1, 'two':2, 'three':3}
# for key in D:   # for key in D.keys()
#     print('key = ', key)

# for value in D.values():
#     print('value = ', value)

# for item in D.items():  # type(item) == tuple
#     print('item = ', item)

# for key,value in D.items():
#     print('key={0} : value={1}'.format(key, value))



# 11 - 다음과 같은 두 개의 리스트로 딕셔너리를 만들어 봅시다. 
# keys = ['one', 'two', 'three', 'four']
# values = [1,2,3,4]
# d = dict(zip(keys,values))
# print(d)


# 12 - fromkeys() 매소드로 각키에 동일한 값을 할당하여 봅시다.
# d1 = {}.fromkeys('abcde',1)
# print(d1)
# d1 = dict.fromkeys('abcde',1)
# print(d1)

# 이렇게 쓰면 안됨 
# fromkeys() --> 값을 얕은 복사해서 그럼 
# d2 = {}.fromkeys('abcde', [])   # 여기 value가 list일때는 쓰면 안됨 
# print(d2)      
# d2['b'].append(5)
# print(d2)



# 13 - 개별적인 값 객체를 사용할 수 있도록 하여 봅시다. 
# d = dict((c, []) for c in 'abcde')
# print(d)
# d['a'].append(10)    
# print(d)



# 14  
# s = '''We propose to start by making it possible to teach programming in Python,
# an existing scripting language, and to focus on creating
# creating a new development environment and teaching materials for it.'''

# import re
# s2 = re.sub('[,.]', '', s.lower())
# # print(s2)
# ws = s2.split()
# # print(ws)


# import collections 
# print(collections.Counter(ws))  # 딕셔너리로 반환 
# print(sorted(list(collections.Counter(ws).items())))



# 15 - 딕셔너리를 활용하여 음식의 궁합을 출력하는 프로그램을 작성하여 봅시다.
## 변수 선언 부분 ##
# foods = {'떡볶이':'오뎅',
#          '짜장면':'단무지',
#          '라면':'김치',
#          '피자':'피클',
#          '맥주':'땅콩',
#          '치킨':'치킨무',
#          '삼겹살':'상추'}
# myfood = input(str(list(foods.keys()))) + ' 중 좋아하는 음식은?'


## 메인 코드 부분 ##
# while True:
    # myfood = input( (str(list(foods.keys()))) + '중 좋아하는 음식은?' )
    # if myfood in foods:
    #     print('<%s> 궁합 음식은 <%s>입니다.'%(myfood, foods.get(myfood)))
    # elif myfood == '끝':
    #     break
    # else:
    #     print('그런 음식이 없습니다. 확인해 보세요.')



# 16 - 2개의 딕셔너리를 병합하여 봅시다.  
# from itertools import chain 
# from collections import defaultdict 

# dict1 = {'bookA':1, 'bookB':2, 'bookC':3}
# dict2 = {'bookC':2, 'bookD':4, 'bookE':5}
# dict3 = defaultdict(list)

# for k,v in chain(dict1.items(), dict2.items()):
#     dict3[k].append(v)
# print(dict3)

# for k,v in dict3.items():
#     print(k,v)



# 17 - 존재하지 않는 key에 대해 접근할 경우 에러를 생각해 봅시다. 
# animals = ['dog', 'cat', 'rabbit', 'tiger', 'cat', 'cat', 'rabbit']
# dic = {}

# for animal in animals:
#     dic[animal] += 1 



# 18 - 위의 에러를 해결하여 봅시다.
# 1)
# animals = ['dog', 'cat', 'rabbit', 'tiger', 'cat', 'cat', 'rabbit']
# dic = {}

# for animal in animals:
#     # key가 있다면 1 증가 
#     if animal in dic.keys():
#         dic[animal] += 1 
#     # key가 없다면 1로 초기화 
#     else:
#         dic[animal] = 1 
# print(dic)


# 2) 
# from collections import defaultdict

# animals = ['dog', 'cat', 'rabbit', 'tiger', 'cat', 'cat', 'rabbit']
# dic = defaultdict(int)  
# # print(dic)
# for animal in animals:
#     dic[animal] += 1 

# print(dic)
# print(dic['door'])
# print(dic)


# 19 - default 값을 set으로 주었을 때 defaultdict를 사용하여 봅시다.  # ????? 아직 set안배움 
# from collections import defaultdict

# animals = [('dog', 'Ricky'), ('cat', )]




# 20 - default 값을 list로 주었을 때 defaultdict를 사용하여 봅시다. 
# from collections import defaultdict

# animals = [('dog', 'Ricky'), ('cat', 'Momo'), ('rabbit', 'Jimmy'), 
#            ('cat', 'Chars'), ('cat', 'Pipy'), ('dog', 'Ricky'), ('dog', 'Ricky')]
# dic = defaultdict(list)

# for animal, name in animals:
#     dic[animal].append(name)   

# print(dic)      # {'dog':['Ricky', 'Ricky', 'Ricky'], 'cat':['Momo', 'Chars', 'Pipy'], 'rabbit':['Jimmy']}




# 문제 풀어보기 
# Question 1 
# animals = {1:'고양이', 2:'개', 3:'말', 4:'물고기'}
# print(animals)


# Question 2 
# foods = {'오뎅':1000, '순대':2000, '만두':3000, '스테이크':4000}
# selection = input('주문항목을 선택하세요=> ')

# print('선택하신 {}의 가격은 {} 입니다'.format(selection, foods[selection]))



# Question 3 - 여기 나오는 개념 중요 
# L1 = [1,2,3]
# L2 = [4,5,6]
# d = {'low':L1, 'high':L2}   # {'low':[1,2,3], 'high':[4,5,6]}
# d1={'ddd':L1}
# print(d)
# e = d   # 얕은복사 
# L1[0]=99
# print(d)
# print(d1)

# f = d.copy()    # 깊은복사 
# d['low'] = [10,20,30]
# d['high'][1] = 500  
# print(e)    # {'low':[10,20,30], 'high':[4,500,6]}
# print(f)    # {'low':[1,2,3], 'high':[4,500,6]}



# Question 4 
# coffees = {'Americano':2000, 'Cafe latte':2500, 'Green Tea':3000, 'Mocha latte':4500}

# selection = input('품목을 선택하세요 => ')
# if selection in coffees:
#     print('{}가 있습니다'.format(selection))
# else:
#     print('{}는 없어요~~~'.format(selection))



# Question 5 
# stationary = {'연필':200, '펜': 800, '지우개':500, '자':300}
# print(stationary.values())



# Question 6 
# menu = {'돈가스':'5000원', '생선가스':'5500원', '우동':'2500원', '초밥 세트':'9000원'}
# print(menu.items())
# for food,price in menu.items():
#     print('{}  :  {}'.format(food,price))


# Question 7 
# dic = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5}
# print(sorted(dic.items()))
# print(sorted(dic.items(), key=lambda x: x[1]))   # 교재 이부분 닶 잘못된거같음 



# Question 8   
# s = 'one two one two three four'
# s = s.split()
# dic = {}
# for i in s:
#     dic[i] = 0
# print(dic)
# print(list(dic))


# or 
# using set 

# s = 'one two one two three four'
# s = s.split()
# s = set(s)  # set도 중복없앰
# print(s)





# Question 9 
# fruits = {'배':[2000,3], '사과':[1500, 5], '딸기':[1800, 2 ], '참외': [2300,5]}
# nSum = 0
# for i in fruits:
#     if fruits[i][1] < 5:
#         print('{}는 사야함'.format(i))
#         print('{}를 살 더 필요한 돈은 {}원'.format(i, fruits[i][0] * (5 - fruits[i][1])))
#         nSum += fruits[i][0] * (5 - fruits[i][1])
#     else:
#         print('{}는 살 필요 없음'.format(i))
# print('총 비용은 {}원'.format(nSum))



# Question 10
# tel = {'min': '010-3455-1235', 'jin':'010-2222-3312', 'jay':'010-6949-2341',
#        'ken':'010-9999-9999', 'ain':'010-2222-2222'}

# person = input('누구의 번호를 찾을까요? --> ')
# if person in tel.keys():
    # print(tel[person])
#     print(tel.get(person))
# else:
#     print('그런 이름은 없어')




    
# Question 11
# idlist = {'가나':1234, '길동':1111, '민수':4321, '수민':2345}

# ID = input('ID입력 :')
# password = int(input('패스워드 입력:'))

# if ID in idlist.keys():
#     if idlist[ID] == password:
#         print('{}님 가입확인 되었습니다'.format(ID))
#     else:
#         print('P/W를 확인하세요')
# else:
#     print('가입이 안되어 있네요~~')



# Question 12
# dic = dict()
# while True:
#     input1 = int(input('1.단어등록  2.단어찾기  3.종료  ==>'))
#     if input1 == 1:
#         eng = input('영어 : ')
#         kor = input('한글 : ')
#         dic[eng] = kor
#     elif input1 == 2:
#         search = input('찾고싶은단어 : ')
#         if search in dic:
#             print(dic[search])
#         else:
#             print('그런단어는 등록되어 있지 않습니다 ㅠㅠ')
#     elif input1 == 3:
#         break 





# Question 13
# result = {'Prodo':97, 'Sally':88, 'Neo':70, 'Brown':99, 'Mini':70}
# nSum = sum(result.values())
# average = nSum / len(result)
# print('평균 : {}'.format(average))




# Question 14 
# alphabets = {'a':'w', 'b':'x', 'c':'y', 'd':'z'}

# input1 = input('입력 ==> ')
# final = ''
# for i in input1:
#     if i in alphabets.keys():
#         final += alphabets[i]
#     elif i in alphabets.values():
#         for j in alphabets:
#             if alphabets[j] == i:
#                 final += j 
#     else:
#         final += i 
# print(final)


# or 
# alphabets = {'a':'w', 'b':'x', 'c':'y', 'd':'z'}






# Question 15 
# countries = {'kr':'대한민국', 'us':'미국', 'jp':'일본', 'de':'독일', 'sk':'슬로바키아', 'hu':'헝가리', 'no':'노르웨이'}
# for eng,kor in countries.items():
#     print('{}  :  {}'.format(eng,kor))



# Question 16  
# import random
# problems = {'파이썬':'최근에 가장 떠오르는 프로그래밍 언어',
#             '변수':'데이터를 저장하는 메모리 공간',
#             '함수':'작업을 수행하는 문장들의 집합에 이름을 붙인것',
#             '리스트':'서로 관련이 없는 항목들의 모임',
#             }

# print('다음은 어떤 단어에 대한 설명일까요?')
# # l=problems.values()     # dict_values(['최근에 가장 떠오르는 프로그래밍 언어', '데이터를 저장하는 메모리 공간', '작업을 수행하는 문장들의 집합에 이름을 붙인것', '서로 관련이 없는 항목들의 모임'])
# # print(l)
# # print(list(l))
# n1 = random.choice(list(problems.values()))
# print(n1)
# answer = input()
# if answer in problems:
#     if problems[answer] == n1:
#         print('정답입니다.!')
#     else:
#         print('정답이 아닙니다.')
# else:
#     print('정답이 아닙니다.')




# Question 17 
# string = '''I love three with the passion put to use
# In my old griefs, and with my childhood's faith.
# I love thee with a love I seemed to lose
# With my lost sain t - l love thee with the breath.
# Smiles, tears, of all my life! - and if God choose,
# I shall but love thee better after death.'''


# import re, collections 
# s2 = re.sub("[,.!\-\']", '', string)
# s2 = s2.split()
# final = ''.join(s2)
# # print(final)
# for character, frequency in sorted(list(collections.Counter(final).items()), reverse= True, key = lambda x:x[-1] ):
#     print('{:<5}{:<5}'.format(character,frequency))



# Question 18   
# 딕셔너리 안쓰고 
# l1 = ['345-4958', '334-0948', '394-9050', '473-3853']
# l2 = ['서울', '경기', '부산', '제주']
# area_no = {'서울':'02', '경기':'031', '부산':'051', '제주':'064'}


# combined_list = list(zip(area_no.values(), l1))
# final = []
# for i in combined_list:
#     tmp = ')'.join(i)
#     final.append(tmp)
# print(final)


# or    

# 딕셔너리 써서 
# l1 = ['345-4958', '334-0948', '394-9050', '473-3853']
# l2 = ['서울', '경기', '부산', '제주']
# area_no = {'서울':'02', '경기':'031', '부산':'051', '제주':'064'}


# combined = {city:num for city,num in zip(l2,l1)}    # {'서울': '345-4958', '경기': '334-0948', '부산': '394-9050', '제주': '473-3853'}
# final = []
# for city in combined:
#     final.append(')'.join( [(area_no[city]), (combined[city])] ))
# print(final)



