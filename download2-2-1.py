#references
#https://docs.python.org

import sys
import io #한글 관련 package
import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


print("hi")
print("한글") #

imgUrl = "https://search.pstatic.net/common/?src=http%3A%2F%2Fcafefiles.naver.net%2F20121020_201%2Frnldudnsdbsk_1350727997756Qh1sM_JPEG%2F%25B5%25BF%25B9%25B020.jpg&type=b400"
htmlUrl = "http://google.com"

savePath1 = "test1.jpg"
savePath2 = "index.html"

#urllib.request.urlretrieve(imgUrl, savePath) # 저장 -> open('r') -> 파싱 -> 저장
dw.urlretrieve(imgUrl, savePath1)
dw.urlretrieve(htmlUrl, savePath2)

print("다운로드 완료!")
