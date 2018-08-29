from bs4 import BeautifulSoup
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#css선택자를 이용하여 정확한 타겟을 지정
#https://www.w3schools.com/cssref/trysel.asp

html = """
<html><body>
<div id="main">
  <h1>강의목록</h1>
  <ul class="lecs">
    <li>Java 초고수 되기</li>
    <li>파이썬 기초 프로그래밍</li>
    <li>파이썬 머신러닝 프로그래밍</li>
    <li>안드로이드 블루투스 프로그래밍</li>
  </ul>
</div>
</body></html>
"""
soup = BeautifulSoup(html, 'html.parser')
print('prettify',soup.prettify())

h1 = soup.select("div#main > h1") #div 태그의 아이디가 main 이고 하위에 h1 태그
print("h1",h1)
print("h1",type(h1)) #리스트 형태로 가져온다
#print("h1", h1.string) #에러

#가져올 노드가 하나라면 select_one 이용
h1 = soup.select_one("div#main > h1")
print("h1",h1.string)

#여러개라면 for문 이용
list_li = soup.select("div#main > ul.lecs > li")
for li in list_li:
    print("li = ", li.string)
