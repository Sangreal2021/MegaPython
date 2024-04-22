import yt_dlp
import os

# 사용자 설정 부분
download_url = 'https://www.youtube.com/watch?v=gdZLi9oWNZg'
file_title = 'Dynamite - BTS'
download_path = r'D:\Music\Youtube'
file_ext = 'mp4'


def download_media(url, folder, file_name, ext):
    # 확장자가 이미 파일 이름에 포함되어 있는지 확인하고 조정
    if not file_name.endswith(f'.{ext}.{ext}'):
        file_name_with_ext = f'{file_name}'
    else:
        file_name_with_ext = file_name

    output_template = os.path.join(folder, file_name_with_ext)

    if not os.path.exists(folder):
        os.makedirs(folder)

    if ext == 'mp3':
        quality = '192'
        ydl_opts = {
            'outtmpl': output_template,
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': ext,
                'preferredquality': quality,
            }]
        }
    elif ext == 'mp4':
        quality = '720p'
        ydl_opts = {
            'outtmpl': output_template,
            'format': f'bestvideo[height<={quality}][ext=mp4]+bestaudio[ext=m4a]/best[height<={quality}]',
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4',  # 비디오 포맷을 mp4로 변환
            }]
        }
    else:
        print("지원하지 않는 형식입니다. mp3 또는 mp4 중 하나를 선택해주세요.")
        return

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print(f'{ext.upper()} 다운로드 완료했습니다.')


if __name__ == '__main__':
    download_media(download_url, download_path, file_title, file_ext)
