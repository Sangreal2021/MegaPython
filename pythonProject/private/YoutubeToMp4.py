'''
※ pytube 설치
    pip install pytube
해상도 종류
144p
240p
360p
480p
720p (HD)
1080p (Full HD)
1440p (2K)
2160p (4K)
4320p (8K)
'''

from pytube import YouTube
import os

# 설정 가능한 변수들
video_url = 'https://www.youtube.com/watch?v=js1CtxSY38I'
download_folder = r'D:\Movie\Youtube'
filename = 'Attention_Official MV - NewJeans.mp4'  # '.mp4' 확장자를 파일 이름에 포함
resolution = '1080p'


def download_video(url, folder, file_name, res):
    # 다운로드 폴더가 존재하는지 확인하고, 없으면 생성
    if not os.path.exists(folder):
        os.makedirs(folder)

    yt = YouTube(url)
    # 지정된 해상도로 MP4 파일 형식의 첫 번째 스트림 선택
    stream = yt.streams.filter(res=res, file_extension='mp4').first()
    # 지정된 경로와 파일 이름으로 비디오 다운로드
    stream.download(output_path=folder, filename=file_name)


if __name__ == '__main__':
    download_video(video_url, download_folder, filename, resolution)

print('다운로드 완료했습니다.')
