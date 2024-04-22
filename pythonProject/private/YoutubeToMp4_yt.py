import yt_dlp
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
# 설정 가능한 변수들
video_url = 'https://www.youtube.com/watch?v=11cta61wi0g'
download_folder = r'D:\Movie\Youtube'
filename = 'Hype Boy.mp4'  # 파일 이름에 확장자 포함
resolution = '720p'  # 해상도 설정


def download_video(url, folder, file_name, res):
    ydl_opts = {
        'outtmpl': f'{folder}/{file_name}',
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
