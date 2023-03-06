#ex01_print.py

print("python" "javascript" "java")     #띄어쓰기 는 공백이 출력 X
print("python"+"javascript"+"java")     #+ 는 공백이 출력 X
print("python","javascript","java")     #,  는 공백이 출력 O
#print 함수 호출 시 end 매개변수에 끝문자를 지정할 수 있다.
#지정하지 않으면 \n이 지정되어있다.

print(1, end=" ")
print(2)
for i in range(5):
    print(i, end=" ")