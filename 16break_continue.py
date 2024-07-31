# 1 
# a = 2 
# while a < 10:
#     print(a)

# 2 
# a = 0 
# while a < 10:
#     print(a)
#     a = a + 1 
#     if a == 5:
#         break
# print('end.....')

# 3 
# while True:
#     light = input('신호등 색상을 입력하세요 :')
#     if light == 'blue':
#         break
# print('전진 !!')

# 4 
# while True:
#     y = int(input('나이를 입력하시오:'))
#     if 1 <= y <= 100:
#         break
#     else:
#         print('1~100사이 값 입력요망.')
# print('당신의 나이는 %d 살이군요~' % y)


# 5      
# n = int(input('양의 정수--> '))
# for i in range(2,n):
#     if not n % i:
#         bPrime = False 
#         break
#     else:        
#         bPrime = True 
# if bPrime:
#     print('{}은 소수이다.'.format(n))
# else:
#     print('{}은 소수가 아니다.'.format(n))


# 6        
# strInput = input('숫자를 포함한 문자열 --> ')     # 두개 이상의 단어가 모였을때 첫번째는 소문자, 두번째는 대문자 --> 변수 만들때 관례상 규칙 
# nSum = 0 
# for s in strInput:
#     if not s.isnumeric():       # 숫자로 만들어진 스트링인지 확인 
#         continue
#     nSum += int(s)
# print("nSum = ", nSum)


# 7 
# import sys, random

# while True:
#     name = input('이름: (종료하려면 엔터키) ')

#     if name == "":
#         sys.exit()

#     question = input("무엇에 대하여 알고 싶은가요? ")
#     print(name + "님", "\"", question, "\"에 대하여 질문 주셨군요.")
#     print("운명의 주사위를 굴려볼께요...")

#     answers = random.randint(1,8)

#     if answers == 1:
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
#         print('그럼요, 명백히 올바른 선택을 했습니다.')

#     elif answers == 7:
#         print('제 답변은 No입니다.')
    
#     else : 
#         print('나중에 댜시 물어 보세요.')