'''
1. pytube 설치
    pip install pytube
2. 해상도 종류
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

import yt_dlp
import os

# 설정 가능한 변수들
video_url = 'https://www.youtube.com/watch?v=gdZLi9oWNZg'
download_folder = r'D:\Movie\Youtube'
filename = 'Dynamite - BTS'  # 확장자를 제외한 파일 이름
resolution = '720p'  # 해상도 설정


def download_video(url, folder, file_name, res):
    # 파일 이름에 확장자 추가
    file_name_with_ext = f'{file_name}.mp4'

    # 다운로드 폴더가 존재하는지 확인하고, 없으면 생성
    if not os.path.exists(folder):
        os.makedirs(folder)

    ydl_opts = {
        'outtmpl': f'{folder}/{file_name_with_ext}',
        'format': f'bestvideo[height<={res}][ext=mp4]+bestaudio[ext=m4a]/best[height<={res}]',
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',  # 비디오 포맷을 mp4로 변환
        }]
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


if __name__ == '__main__':
    download_video(video_url, download_folder, filename, resolution)
    print('다운로드 완료했습니다.')
