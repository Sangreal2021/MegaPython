import subprocess
import requests

def download_video(url, save_path):
    try:
        with requests.get(url, stream=True) as response:
            response.raise_for_status()
            with open(save_path, 'wb') as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)
        print(f"Video downloaded: {save_path}")
        return True
    except requests.exceptions.RequestException as e:
        print(f"Error downloading the video: {e}")
        return False

def convert_video(input_path, output_path):
    """ 입력된 비디오 파일을 호환 가능한 MP4 (H.264/AAC)로 변환합니다. """
    cmd = [
        'ffmpeg',
        '-i', input_path,
        '-vcodec', 'libx264',   # 비디오 코덱 설정: H.264
        '-acodec', 'aac',       # 오디오 코덱 설정: AAC
        '-strict', 'experimental', # AAC 오디오 사용을 위한 설정
        '-b:v', '2000k',        # 비디오 비트레이트 설정
        '-b:a', '192k',         # 오디오 비트레이트 설정
        '-preset', 'fast',      # 변환 속도 및 압축률 설정
        output_path,
        '-y'                    # 출력 파일이 이미 존재하는 경우 덮어쓰기 옵션
    ]
    try:
        subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"Video conversion completed: {output_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error during video conversion: {e.output.decode()}")

# 사용 예시
video_url = ''
download_path = 'D:\\Music\\Youtube\\test.mp4'
converted_path = 'D:\\Music\\Youtube\\test_converted.avi'

if download_video(video_url, download_path):
    convert_video(download_path, converted_path)
else:
    print("Download failed, check your URL or network connection.")
