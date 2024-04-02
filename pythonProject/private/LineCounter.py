import os
from collections import defaultdict


# LineCounter 클래스를 정의합니다.
# 이 클래스는 주어진 디렉토리에서 파일을 탐색하고 각 파일 유형별 줄 수를 계산합니다.
class LineCounter:
    def __init__(self, src_directory):
        # 생성자에서는 소스 디렉토리의 경로, 제외할 폴더, 제외할 파일 확장자 목록을 초기화합니다.
        self.src_directory = src_directory
        self.exclude_folders = [".idea", ".venv", ".git", "etc"]
        self.exclude_file_extensions = [".pdf", ".jpg", ".png"]

    # 주어진 경로가 제외할 폴더나 파일 확장자에 해당되지 않는지 확인하는 메서드입니다.
    def is_valid_path(self, path):
        # 제외할 폴더가 경로에 포함되어 있는지 확인합니다. 포함되어 있다면 False를 반환합니다.
        for folder in self.exclude_folders:
            if folder in path:
                return False
        # 제외할 파일 확장자에 해당되지 않는지 확인합니다. 해당되면 False를 반환합니다.
        return not any(path.endswith(ext) for ext in self.exclude_file_extensions)

    # 파일 종류별 라인 수를 계산하는 메서드입니다.
    def count_lines_by_file_type(self):
        # 파일 유형별 라인 수를 저장할 딕셔너리를 defaultdict 으로 생성합니다. 기본값은 0입니다.
        # defaultdict는 존재하지 않는 키에 대해 접근 시 기본값을 제공하는 딕셔너리의 확장된 형태입니다.
        line_count_by_type = defaultdict(int)

        # os.walk를 사용하여 주어진 디렉토리(self.src_directory)와 그 하위 디렉토리를 순회합니다.
        # os.walk는 탐색 중인 현재 디렉토리(root), 현재 디렉토리의 하위 디렉토리 목록(dirs),
        #   현재 디렉토리의 파일 목록(files)을 반환합니다.
        for root, dirs, files in os.walk(self.src_directory):
            # dirs 리스트를 필터링하여 유효한 폴더만 남깁니다.
            # self.is_valid_path 메서드를 사용하여 제외할 폴더나 파일이 아닌 경우에만 포함시킵니다.
            dirs[:] = [d for d in dirs if self.is_valid_path(os.path.join(root, d))]
            # 모든 파일에 대해 반복합니다.
            for file in files:
                # 파일이 유효한 경로에 위치하는지 확인합니다.
                # 유효하지 않은 경로(제외할 폴더나 파일 확장자에 해당하는 경우)는 처리에서 제외합니다.
                if self.is_valid_path(file):
                    # 파일의 확장자를 추출합니다. 확장자가 없는 경우 "Unknown"으로 처리합니다.
                    # os.path.splitext(file)[1]은 파일 이름에서 확장자 부분만 추출합니다.
                    file_type = os.path.splitext(file)[1] or "Unknown"
                    # 파일의 전체 경로를 구성합니다.
                    file_path = os.path.join(root, file)
                    # 파일을 열어 줄 수를 계산합니다.
                    # 파일을 열 때는 인코딩 문제를 방지하기 위해 'utf-8'로 설정하고,
                    # 'errors='ignore''로 설정하여 인코딩 에러를 무시합니다.
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        # 파일 내 각 줄에 대해 반복하며 줄 수를 세고, 해당 파일 유형의 줄 수를 증가시킵니다.
                        line_count_by_type[file_type] += sum(1 for line in f)

        # 계산된 파일 종류별 라인 수를 담은 딕셔너리를 반환합니다.
        # dict() 함수를 사용하여 defaultdict를 일반 딕셔너리로 변환하여 반환합니다.
        return dict(line_count_by_type)


# 메인 코드 블록입니다.
if __name__ == "__main__":
    # 소스 디렉토리 경로를 설정합니다.
    src_directory = "D:\\private\\study\\SQLD"
    # LineCounter 인스턴스를 생성합니다.
    counter = LineCounter(src_directory)
    # countLinesByFileType 메서드를 호출하여 파일 종류별 라인 수를 계산합니다.
    lines_by_file_type = counter.count_lines_by_file_type()

    # 계산된 결과를 출력합니다.
    for file_type, lines in lines_by_file_type.items():
        print(f"{file_type} files total lines: {lines}")

    # 전체 라인 수를 계산하고 출력합니다.
    total_lines = sum(lines_by_file_type.values())
    print(f"Total lines in '{src_directory}' directory: {total_lines}")
