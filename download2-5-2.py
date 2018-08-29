from bs4 import BeautifulSoup
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#줄바꿈이 포함된 문자열 작성
html = """
<html>
<body>
  <h1>파이썬 BeautifulSoup</h1>
  <p>태그선택자</p>
  <p>CSS 선택자</p>
</body>
</html>
"""

#print('html', html)

soup = BeautifulSoup(html, 'html.parser')
#print('soup', type(soup))
#print('prettify',soup.prettify())

#직접 접근(순차적)
h1 = soup.html.body.h1
print('h1', type(h1))
print('h1',h1)

p1 = soup.html.body.p
print('p1',p1)

#p2 = p1.next_sibling # \n을 가져옴
p2 = p1.next_sibling.next_sibling # 두번 해주거나, 공백을 없애주어야 함
print('p2',p2)

p3 = p1.previous_sibling.previous_sibling
print('p2',p3)

print("\nh1 = " + h1.string)
print("p  = " + p1.string)
print("p  = " + p2.string)
