from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as rep
import sys
import io
import os

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#403error : 헤더(Header)정보를 심어서 User-agent 정보를 같이 보내는 코드를 통해 해결
opener = req.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
req.install_opener(opener)

base = "https://www.inflearn.com/"
quote = rep.quote_plus("추천-강좌")
url = base + quote

res = req.urlopen(url)
savePath = "D:/Atom_Workspace/section2/img/"

#폴더 생성 & 예외처리
try:
    if not(os.path.isdir(savePath)):
        os.makedirs(os.path.join(savePath))
except OSError as e:
    if e.errno != errno.EEXIST:
        print("폴더 만들기 실패!")
        raise

soup = BeautifulSoup(res, "html.parser")
img_list = soup.select("ul.slides")[0]
#print("test", img_list)

for i, e in enumerate(img_list,1):
    with open(savePath+"text_"+str(i)+".txt","wt") as f:
        f.write(e.select_one("h4.block_title > a").string)
    fullfilename = os.path.join(savePath, savePath+str(i)+'.png')
    req.urlretrieve(e.select_one("div.block_media > a > img")['src'],fullfilename)
    print(i)
print("다운로드 완료")
