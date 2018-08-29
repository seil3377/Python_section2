import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#Classes Documentation : https://docs.python.org/3/tutorial/classes.html
class NameTest:
    total = 0

print(dir())
print("before: ", NameTest.__dict__)

NameTest.total = 1
print("after: ", NameTest.__dict__)

n1 = NameTest()
n2 = NameTest()

print(id(n1), "vs", id(n2))
print(dir())

print(n1.__dict__)
print(n2.__dict__)

n1.total = 77
print(n1.__dict__)

print(n1.total) #인스턴스의 네임스페이스 확인 -> 출력 : 77
print(n2.total) #인스턴스의 네임스페이스 확인 -> 클래스 네임스페이스 확인 -> 출력 : 1
                #클래스 변수(공유)

print(n1.next)
