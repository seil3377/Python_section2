import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#클래스 선언
class UserInfo:
    def __init__(self, name, phone): #클래스 생성자 __init__ : 객체 초기화
        self.name = name
        self.phone = phone

    def print_info(self):
        print("--------------")
        print("Name:" + self.name)
        print("Phone: " + self.phone)
        print("--------------")

    def __del__(self):
        print("delete!")

#인스턴스화
user1 = UserInfo("kim","010-1111-2222")
user2 = UserInfo("park","010-3333-4444")

#인스턴스 주소
print(id(user1))
print(id(user2))

#메소드 활용
#user1.set_info("kim","010-1111-2222")
#user2.set_info("park","010-3333-4444")

user1.print_info()
user2.print_info()

print(user1.__dict__)
print(user2.__dict__)

print(user1.phone, user1.name)
print(user2.phone, user2.name)
