# <파일모드>
# 'r'  읽기모드       파일의 처음부터 읽는다.
# 'w'  쓰기모드       파일의 처음부터 쓴다. 파일이 없으면 생성 
# 'a'  추가모드       파일의 끝에 추가, 파일이 없으면 생성 
# 'r+' 읽기와 쓰기모드  파일을 읽고 쓸 수 있는 모드

# 폴더는 경로 


# 1 
# f1 = open('/Users/parkchanhyuk/Desktop/data/data1.txt', 'w')  # 경로는 데이터가 들어있는 위치, get info,  뒤에 적혀져있는 data1.txt는 파일명 
# f1.write('lee  80  90  95\n')
# f1.write('kim  85  70  75\n')
# f1.write('park  70  80  90')
# f1.close()

# f2 = open('/Users/parkchanhyuk/Desktop/data/data1.txt', 'r')
# print(f2.read())


# 2 
# f2 = open('/Users/parkchanhyuk/Desktop/data/data1.txt', 'r')
# f2.seek(0)  # seek() --> 위치로 이동하라 
# print(f2.read(3))
# print(f2.read(4))
# print(f2.read(4))
# print(f2.read(4))

# f2.seek(15)
# print(f2.read())


# 3 - 줄 단위로 파일 쓰기를 하여 봅시다. 
# lines = ['first line \n', 'second line\n', 'third line\n']
# f = open('/Users/parkchanhyuk/Desktop/data/data3.txt', 'w')
# f.writelines(lines)
# f.close()


# 4   
# lines = ['first line\n', 'second line\n', 'third line\n']
# f = open('/Users/parkchanhyuk/Desktop/data/data4.txt', 'w')
# f.write(''.join(lines))
# f.close()

# join()의  example
# s = ",".join('abcd')
# print(s)


# 5 
# with open('/Users/parkchanhyuk/Desktop/data/data4.txt', 'r') as f:
#     for line in f:
#         print(line, end='')
# f.close()


# 6 - 줄 단위로 읽어 봅시다. 
# f = open('/Users/parkchanhyuk/Desktop/data/data4.txt')
# line = f.readline()
# while line:   # 읽은게 값이 있으면
#     print(line, end='')
#     line = f.readline()
# f.close()


# 7
# f = open('/Users/parkchanhyuk/Desktop/data/data4.txt' , 'r')   # open -> 파일을 열기, write -> write 용으로 열기   
# for line in f.readlines():
#     print(line, end='')
# f.close()


# 8  
# with open('/Users/parkchanhyuk/Desktop/data/data5.txt', 'w') as f1:    
#     f1.write('lee  80  90  90\n')
#     f1.write('kim  85  70  75\n')
#     f1.write('park  70  80  90\n')
# f1.close()


# with open('/Users/parkchanhyuk/Desktop/data/data5.txt', 'r') as f2:    
#     read_data = f2.read()
#     print(read_data)

#     f2.seek(0)
#     print(f2.read(3))
#     print(f2.read(4))
#     print(f2.read(4))
#     print(f2.read(4))
#     print(f2.read(1))
# f2.close()



# 9
# f2 = open('/Users/parkchanhyuk/Desktop/data/data5.txt', 'r')
# f2.seek(0)
# std_name =[]
# std_kor = []
# std_eng = []
# std_mat = []


# for line in f2.readlines():
#     name,kor,eng,mat = line.split()
#     std_name.append(name)
#     std_kor.append(kor)
#     std_eng.append(eng)
#     std_mat.append(mat)

# print(std_name)
# print(std_kor)
# print(std_eng)
# print(std_mat)



# 10
# def read_data(file_name):
#     data_list = []
#     f = open(file_name, 'r')
#     for line in f:  # f2.readlines()  ?????????? --> 이게 어떻게 똑같은지 
#         name, kor, eng, math = line.split()
#         tmp = [name, int(kor), int(eng), int(math)]
#         data_list.append(tmp)
#     f.close()
#     return data_list


# def write_data(file_name, data_list):
#     f = open(file_name, 'w')
#     f.write('   name,   kor,   eng,   math,   sum,   avg\n')
#     f.write('---------------------------------------------------------\n')
#     for data in data_list:
#         s = '{0:>8},'.format(data[0])
#         s += '{0:>8},'.format(data[1])
#         s += '{0:>8},'.format(data[2])
#         s += '{0:>8},'.format(data[3])
#         s += '{0:>8},'.format(data[4])
#         s += '{0:>8},'.format(data[5])
#         s += '\n'
#         f.write(s)
#     f.close()


# def calculateAvg(data_list):
#     i = 0 
#     for name, kor, eng, math in data_list:
#         sumScore = kor + eng + math
#         data_list[i].append(sumScore)
#         data_list[i].append(sumScore/3.0)
#         i = i + 1 

# std_list = read_data('/Users/parkchanhyuk/Desktop/data/data5.txt')
# calculateAvg(std_list)
# write_data('/Users/parkchanhyuk/Desktop/data/data5.txt', std_list)




# local, global은 변수일때 얘기 
# def make_python(data):
#     data=20
#     print(data)

# data=100
# make_python(data)
# print(data)

# list는 그대로 유지가 된다
# def make_python(data):
#     data[1]=99
#     print(data)

# data=[1,2,3]
# make_python(data)
# print(data)




# 11
# outfile = open('/Users/parkchanhyuk/Desktop/data/data5.txt', 'a')
# outfile.write('sss 010-3333-3333\n')
# outfile.write('kkk 010-4444-4444\n')
# outfile.write('jjj 010-5555-5555\n')
# outfile.close()


# 12 - 파일을 복사해보기 
# import shutil  
# shutil.copy('/Users/parkchanhyuk/Desktop/data/data5.txt', '/Users/parkchanhyuk/Desktop/data/data5_copy.txt')  # 왼쪽거를 오른쪽 이름으로 카피 


# 13 
# # 입력 파일 이름과 출력 파일 이름을 받는다.
# infilename = input('입력 파일 이름: ')
# outfilename = input('출력 파일 이름: ')


# # 입력과 출력을 위한 파일을 연다.
# infile = open(infilename, 'r')
# outfile = open(outfilename, 'w')

# # 전체 파일을 읽는다.
# s = infile.read()

# # 전체 파일을 쓴다. 
# outfile.write(s)

# # 파일을 닫는다.
# infile.close()
# outfile.close()



# Question 14
# try:
#     fp = open('/Users/parkchanhyuk/Desktop/data/python_coding.txt', 'r')
#     try:
#         lines = fp.readlines()
#         print(lines)
#     finally:
#         fp.close()
# except IOError:
#     print('피일에러')




# Question 1 
# file = open('/Users/parkchanhyuk/Desktop/data/homework1.txt', 'w')
# file.write("파일명 : myfile\n데이터 : '파일을 열었으니 데이터를 저장하자!!!'")
# file.close()


# Question 2 
# file1 = open('/Users/parkchanhyuk/Desktop/data/homework2.txt', 'w')
# file1.write('살어리 살어리랏다 청산에 살어리랏다\n\n멀위랑 달래랑 먹고 청산에 살어리랏다\n\n얄리 얄리 얄랑셩 얄라리 얄라')
# file1.write('\n\n우러라 우러라 새여 자고 니러 우러라 새여\n\n널라와 시름 한 나도 자고 니러 우리노라\n\n얄리 얄리 얄랑셩 얄라리 얄라')
# file1.close()

# file2 = open('/Users/parkchanhyuk/Desktop/data/homework2.txt', 'r')
# print(file2.read())



# Question 3 
# file1 = open('/Users/parkchanhyuk/Desktop/data/homework2.txt', 'r')
# line = file1.readline()
# l = []
# while line:
#     l.append(line)
#     line = file1.readline()

# for i in l:
#     print(i, end='')


# Question 4 
# with open('/Users/parkchanhyuk/Desktop/data/Test2.txt', 'w') as f:
#     for i in range(5):
#         f.write('{} Line\n'.format(i))
# f.close()



# Question 5 
# def organize_file():
#     with open('/Users/parkchanhyuk/Desktop/data/Text4.txt', 'r') as f:
#         lines = f.readlines()
#         student_list = []
#         for i in range(len(lines)):
#             if i == 0:
#                 continue
#             else: 
#                 splited = lines[i].split()
#                 student_list.extend(splited)
#     return student_list


# def make_dictionary():
#     final_dictionary = dict()
#     for i in student_list:
#         if i[0] not in final_dictionary:
#             final_dictionary[i[0]] = 1 
#         else:
#             final_dictionary[i[0]] += 1 
#     return final_dictionary


# student_list = organize_file()
# print(make_dictionary())


# Question 6
# def read_data():
#     data_list = []
#     file = open('/Users/parkchanhyuk/Desktop/data/text5.txt', 'r')
#     lines = file.readlines()
#     for i in range(len(lines)):
#         if i == 0:
#             continue

#         else:
#             name, math, sci, eng = lines[i].split(', ')
#             tmp = [name, int(math), int(sci), int(eng)]
#             data_list.append(tmp)
#     file.close()
#     return data_list


# def calculate_average():
#     mSum = 0
#     sSum = 0 
#     eSum = 0
#     for i in range(len(data_list)):
#         mSum += data_list[i][1]
#         sSum += data_list[i][2]
#         eSum += data_list[i][3]
    
#     math_average = mSum / len(data_list)
#     science_average = sSum / len(data_list)
#     eng_average = eSum / len(data_list)

#     return math_average, science_average, eng_average


# data_list = read_data()
# math_average, science_average, eng_average = calculate_average()


# print('수학 평균 {}'.format(math_average))
# print('과학 평균 {}'.format(science_average))
# print('영어 평균 {}'.format(eng_average))


# Question 7   
# f = open('/Users/parkchanhyuk/Desktop/data/Q7.txt', 'r')
# file_list = f.readlines()
# for i in range(len(file_list)):
#     splited = file_list[i].split()
#     if len(splited) >0 and splited[0] == '#':
#         continue
#     print('{} :  {}'.format(i+1, len(splited)))



# Question 8 
# file =  open('/Users/parkchanhyuk/Desktop/data/number.txt', 'w') 
# file.write('1 2 3 4 5 6 7 8 9 10')
# file.close()


# Question 9 
# file =  open('/Users/parkchanhyuk/Desktop/data/s.txt', 'r') 
# file_list = file.readlines()
# file_list.sort()
# final_list = []
# for i in file_list:
#     final_list.append(i.strip())
# for i in final_list:
#     print(i)

# file.close()    # file을 close하고 다시 open했을때는 시작 위치(seek(0))로 간다 




# l=[[3,5], [2,6], [5,1]]

# l.sort()
# print(l)
# l1=sorted(l)
# print(l, l1)

# l2=sorted(l, key=lambda x: x[1])  # lambda--> 함수  x[1]이 return 값 
# print(l2)
# fruits = ['apple', 'banana', ' grape', 'orange', 'kiwi']
# ordered_fruits = sorted(fruits, key = lambda x:x[-1])
# print(ordered_fruits)




# Question 10 
# def read_file():
#     with open('/Users/parkchanhyuk/Desktop/data/s.txt', 'r') as f:
#         tmp_split = []
#         file_list = f.readlines()
#         for i in file_list:
#             tmp_split.append(i.split())
#     f.close()
#     return tmp_split


# def make_dictionary():
#     dictionary = dict()
#     for i in range(len(tmp_split)):
#         dictionary[tmp_split[i][1]] = tmp_split[i][0]
#     return dictionary


# def sorting():
#     for key in sorted(dictionary):
#         print(dictionary[key], key)


# tmp_split = read_file()
# dictionary = make_dictionary()
# sorting()

# or 

# def read_file():

#     with open('/Users/parkchanhyuk/Desktop/data/s.txt', 'r') as f:
#         final_list = []
#         file_list = f.readlines()
#         for i in file_list:
#             final_list.append(i.strip())
#     return final_list


# def ordered():
#     ordered_list = sorted(final_list, key=lambda x:x[4])
#     for i in ordered_list:
#         print(i)


# final_list = read_file()
# ordered()



# Question 11
# def read_file():
#     with open('/Users/parkchanhyuk/Desktop/data/s.txt', 'r') as f:
#         tmp = []
#         file_list = f.readlines()
#         for i in file_list:
#             tmp.extend(i.split())
#     f.close()
#     return tmp 


# tmp_list = read_file()

# cnt = 1
# for i in tmp_list:
#     print(i, end=' ')
#     if cnt % 3 == 0:
#         print()
#     cnt += 1 



# Question 12
# file = open('/Users/parkchanhyuk/Desktop/data/score.txt', 'w')
# for i in range(3):
#     name = input('이름입력 : ')
#     kor, eng, math = input('국어 영어 수학 점수 : ').split()
#     file.write('{} {} {} {}\n'.format(name,kor,eng,math))
# file.close()



# file = open('/Users/parkchanhyuk/Desktop/data/score.txt', 'r')
# print('***성적표***')
# tmp = []
# sum_list = []
# for i in file.readlines():
#     name, kor, eng, math = i.split()
#     Sum = int(kor) + int(eng) + int(math)
#     average = (int(kor) + int(eng) + int(math)) / 3
#     tmp.append([name, kor, eng, math, Sum, average])
#     sum_list.append(Sum)
# sum_list.sort(reverse=True)

# for i in range(len(sum_list)):
#     for j in range(len(tmp)):
#         if sum_list[i] in tmp[j]:
#             tmp[j].append(i+1)

# for i in range(len(tmp)):
#     for j in range(len(tmp[i])):
#         if j == 5:
#             print('{:<4.0f}'.format(tmp[i][j]), end=' ')
#         else:
#             print('{:<4}'.format(tmp[i][j]), end=' ')
#     print()



# Question 13  
# import random
# file = open('/Users/parkchanhyuk/Desktop/data/word.txt', 'w')
# file.write('apple banana grape orange')
# file.close


# file = open('/Users/parkchanhyuk/Desktop/data/word.txt', 'r')
# fruits = file.read().split()
# # print(fruits)   # ['apple', 'banana', 'grape', 'orange']
# fruit = random.choice(fruits)
# fruit_list = []


# num_list = []
# while len(num_list) != len(fruit) // 2:
#     n1 = random.randint(0, len(fruit) - 1)
#     if n1 not in num_list:
#         num_list.append(n1)

# for i in fruit:
#     fruit_list.append(i)

# for i in num_list:
#     fruit_list[i] = ' '
# print(fruit_list)


# while ' ' in fruit_list:
#     for i in range(len(fruit_list)):
#         if fruit_list[i] == ' ':
#             for j in range(10000000):
#                 input1 = input('{}번째 글자는 : '.format(i+1))
#                 if input1 == fruit[i]:
#                     fruit_list[i] = fruit[i]
#                     print('맞았습니다')
#                     break
#                 else:
#                     print('틀렸습니다')


# print('정답은 ', end='')
# for i in fruit_list:
#     print(i,end='')
# print('입니다')