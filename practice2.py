# print(abs(-5)) #5    abs=absoulte 절대값
# print(pow(4,2))   #4^2   
# print(max(5,12))   # 12 
# print(min(5,12))  #5
# print(round(3.14))  #3  반올림


from random import *
# print(floor(4.99))  #4   내림
# print(ceil(3.14))  #4  올림

# print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의 값 생성
# print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의 값 생성
# print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의 값 생성
# print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의 값 생성
# print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의 값 생성
# print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의 값 생성

# print(randrange(1, 46)) # 1~ 45 미만의 임의의 값 생성
# print(randrange(1, 46)) # 1~ 45 미만의 임의의 값 생성
# print(randrange(1, 46)) # 1~ 45 미만의 임의의 값 생성
# print(randrange(1, 46)) # 1~ 45 미만의 임의의 값 생성
# print(randrange(1, 46)) # 1~ 45 미만의 임의의 값 생성
# print(randrange(1, 46)) # 1~ 45 미만의 임의의 값 생성

# sentence = '나는 소년입니다'
# print(sentence)
# sentence2 = "파이썬은 쉬워요"
# print(sentence2)
# sentence3 = """
# 나는 소년이고, 
# 파이썬은 쉬워요
# """
# print(sentence3)

# jumin = "990120-1234567"
# print("성별 : " + jumin[7])
# print("연 : " + jumin[0:2])  # 0:2 -> 0부터 2 직전까지 (0,1)
# print("월 : " + jumin[2:4])
# print("일 : " + jumin[4:6])

# #print("생년월일 : " + jumin[:6])   # :6 -> 처음부터 6직전까지
# print("생년월일 : " + jumin[0:6]) 

# print("뒤 7자리 : " + jumin[7:14]) 
# #print("뒤 7자리 : " + jumin[7:]) 7: -> 7부터 끝까지
# print("뒤 7자리 (뒤에서부터) : " + jumin[-7:] )

python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python", "Java"))

index = python.index("n")
print(index)
index = python.index("n", index + 1)
print(index)

print(python)