import yt_dlp
import os

'''
audio_quality 설정 - 오디오 품질 (비트레이트 kbps)
    32 kbps: 매우 낮은 품질, 음성 파일용
    64 kbps: 낮은 품질, 음성 파일에 적합
    96 kbps: 인터넷 라디오 품질
    128 kbps: 보통 품질, 음악 스트리밍의 표준
    160 kbps: 더 나은 품질의 음악 파일용
    192 kbps: 높은 품질의 음악 파일용
    256 kbps: 매우 높은 품질, 프로페셔널 오디오
    320 kbps: 최고 품질의 오디오 파일
'''

# 사용자 설정 부분
file_title = "Overworld_Theme-SuperMarioWorld"
download_url = 'https://www.youtube.com/watch?v=tAaGKo4XVvM'
file_ext = "mp3"
download_path = r'E:\Music\Youtube'
audio_quality = '192'

# 완성된 파일 경로 및 이름 설정
# output_template = os.path.join(download_path, f'{file_title}.{file_ext}')
output_template = os.path.join(download_path, f'{file_title}')

# 다운로드 옵션 설정
ydl_opts = {
    'outtmpl': output_template,
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',  # 비디오에서 오디오 추출
        'preferredcodec': file_ext,  # 오디오 파일 형식 (mp3)
        'preferredquality': audio_quality,  # 오디오 품질 설정
    }]
}

# 다운로드 실행
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([download_url])

print('다운로드 완료했습니다.')