import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

class SelfTest:
    def function1():
        print("function1 called!")

    def function2(self):
        print(id(self))
        print("function2 called!")

f = SelfTest() #인스턴스를 생성해 자기자신을 매개변수로 넘겨서 호출하는 방법

#print(dir(f)) #1607898276752
print(id(f)) #1607898276752, 메모리 주소값이 일치한다(=자동으로 인스턴스 주소값이 self에 담겨서 넘어감)

#f.function1() # function1() takes 0 positional arguments but 1 was given
print(SelfTest.function1()) # 클래스이름.메서드 : 직접 접근하여 호출, self인자를 받지 않음

f.function2()
