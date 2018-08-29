import pytube
import os
import subprocess

#yt = pytube.YouTube("https://www.youtube.com/watch?v=xj6fHiF8Osg") #다운받을 동영상 url 지정
yt = pytube.YouTube(input("다운받을 youtube 동영상 주소는?")) #다운받을 동영상 url 지정
videos = yt.streams.all()

print('videos', videos)

for i in range(len(videos)) : #range(1,6) 1이상 6미만
    print(i,',', videos[i])

cNum =  int(input("다운 받을 화질은?(0~13입력)"))

down_dir = "D:/Atom_Workspace/section2/youtube"

videos[0].download(down_dir)
#anaconda prompt 상에서 ffmpeg -i filename mp3

oriFileName = videos[cNum].default_filename
newFileName = input("변환 할 파일 mp3 명은?")


subprocess.call(["ffmpeg",'-i',
    os.path.join(down_dir,oriFileName), #하나의 경로로 합쳐줌
                                        # D:/Atom_Workspace/section2/youtube/oriFileName.mp4
    os.path.join(down_dir,newFileName)

])

print("동영상 다운로드 및 mp3 변환 완료!")
