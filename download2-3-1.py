import sys
import io
import urllib.request as req
from urllib.parse import urlparse

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "http://www.encar.com"

mem = req.urlopen(url)

# print(mem) #<http.client.HTTPResponse object at 0x0000015567A0F860>
# print(type(mem)) #<class 'http.client.HTTPResponse'>

    #자료형
    #{} : dict
    #[] : list
    #() : tuple

# print("geturl :",mem.geturl()) #http://www.encar.com
# print("status :",mem.status) #200
# print("headers :",mem.getheaders())
# print("info :",mem.info(),"\n")
# print("getcode :",mem.getcode())
# print("read :",mem.read(10).decode('utf-8')) #해당 숫자만큼의 데이터만 읽어옴 & 디코딩해서 가져옴
print(urlparse('http://www.encar.com'))
#print(urlparse('http://www.encar.co.kr?test=test').query)
