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

f = dw.urlopen(imgUrl).read()   #urlopen : 변수 할당 -> 파싱 -> 저장
f2 = dw.urlopen(htmlUrl).read()

saveFile1 = open(savePath1, "wb")  # w : write , r : read , a : add
                                   # b : binary
saveFile1.write(f)
saveFile1.close()

with open(savePath2,'wb') as saveFile2:
    saveFile2.write(f2)



print("다운로드 완료!")
