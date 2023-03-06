#ex02_file.py

f = open("test.txt", "w", encoding="utf-8")
# f.write("하하하하하하하하하하하")
students = ["이나영", "김아랑", "강하늘", "김우리"]
scores = [98, 80, 77, 65]

for i in range(4):
    data = "%s님은 %s점입니다. \n" %(students[i], scores[i])
    f.write(data)
f.close()

# readline() 파일의 첫번째 줄 출력
# readlines() 모든 줄을 읽어서 각각의 줄을 요소로 갖는 리스트를 반환
# read() 파일의 내용 전체를 문자열로 반환

d = open("test.txt", "r", encoding="utf-8")
readData = d.readlines()
print(readData)     #한줄로 반환
# for i in readData:
#     print(i)

d.close()