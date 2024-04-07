#!/usr/bin/env python3
import os
import io
import sys
from pathlib import Path

# 표준 출력 인코딩을 UTF-8로 설정
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')


class ParseNew:
    # 클래스 변수로 경로와 로그 파일명을 정의합니다.
    workspace_path = "D:\\etc\\plainjava\\unix"
    destspace_path = "D:\\etc\\plainjava\\unix\\dest"
    log_file_name = "vsttrest2_2023-04-21"

    def exec_run(self):
        # os.path.join을 사용하여 파일 경로를 구성합니다. 이 방식은 운영체제에 독립적입니다.
        dest_file_path = os.path.join(self.destspace_path, f"report.{self.log_file_name}.txt")

        # dest 폴더가 없으면 생성
        if not os.path.exists(self.destspace_path):
            os.makedirs(self.destspace_path)

        # os.path.exists로 파일 존재 여부를 확인합니다.
        if os.path.exists(dest_file_path):
            print(f"Error: File <report.{self.log_file_name}.txt> already exists. Execution stopped.")
            return

        # 로그 파일의 기본 데이터를 가져옵니다.
        lines = self.get_base_data_key_list(f"{self.log_file_name}.log")
        # 가져온 데이터를 처리하여 문자열로 변환합니다.
        print_str = self.create_text_log(lines)
        # 최종적으로 처리된 문자열을 파일로 출력합니다.
        self.line_print(f"report.{self.log_file_name}", print_str)

    def line_print(self, category, output_str):
        file_path = os.path.join(self.destspace_path, f"{category}.txt")
        if os.path.exists(file_path):
            return

        # 파일을 쓰기 모드로 열고, 내용을 작성합니다. 인코딩은 UTF-8로 설정합니다.
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(output_str)

    def get_base_data_key_list(self, fname):
        file_path = os.path.join(self.workspace_path, fname)
        try:
            # 파일을 열고, 모든 라인을 리스트로 반환합니다.
            with open(file_path, 'r', encoding='utf-8') as file:
                return file.readlines()
        except Exception as e:
            print(e)
            return []

    def check_ch(self, ch, text):
        # 문자열 내에 특정 채널 번호가 있는지 확인합니다.
        return f"[{ch}]" in text

    def get_text_ch(self, text):
        # 주어진 텍스트에서 채널 번호를 추출합니다.
        start = text.find('[') + 1
        end = text.find(']')
        return int(text[start:end])

    def check_welcome(self, text):
        # 'WELCOME' 문자열이 있는지 확인합니다.
        return "WELCOME" in text

    def check_ending(self, text):
        # 'ENDING' 문자열이 있는지 확인합니다.
        return "ENDING" in text

    def set_ch_scope_list(self, line_no, ch_num, lines):
        ch_scope_list = []
        for i in range(line_no, len(lines)):
            if self.check_ch(ch_num, lines[i]):
                ch_scope_list.append(lines[i])
                if self.check_ending(lines[i]):
                    break
        return ch_scope_list

    def get_log_info(self, ch_scope_list):
        if len(ch_scope_list) == 2:
            return ""

        ch = self.get_text_ch(ch_scope_list[0])
        stt_code = "STTCD_NONE"  # vsqa 코드
        stt_txt = None  # STT 결과
        rec_key = None
        rec_time_start = None
        rec_time_end = None
        rec_tel = None
        rec_info = None  # 파일명
        rec_code = None  # 콜 분기 위치정보

        for line in ch_scope_list:
            if "send_dlg_update: 1 0.00 0" in line or "send_chat" in line or "stage detected" in line:
                continue

            if "WELCOME" in line:
                parts = line.split()
                rec_time_start = parts[1].strip()  # 시작 시간 추출 및 양 끝 공백 제거
                info_parts = line.split(" i=")[1].split(",")
                rec_info = info_parts[0].strip()  # REC_INFO 추출 및 양 끝 공백 제거
                parts = rec_info.split("_")
                rec_key = parts[0].strip()  # REC_KEY 추출 및 양 끝 공백 제거
                rec_tel = parts[2].strip()  # REC_TEL 추출 및 양 끝 공백 제거
                rec_code = parts[3].strip()  # REC_CODE 추출 및 양 끝 공백 제거

            if " c=" in line and "WELCOME" not in line and "ENDING" not in line:
                stt_txt = line.split(" c=")[1].strip()  # STT_TXT 추출 및 양 끝 공백 제거

            if "send_dlg_update" in line:
                stt_code = line.split("send_dlg_update")[1].split(",")[1].strip()  # STT_CODE 추출 및 양 끝 공백 제거

            if "ENDING" in line:
                parts = line.split()
                rec_time_end = parts[1].strip()  # 종료 시간 정보 및 양 끝 공백 제거

        ch = f"[{ch:02}]"  # CH 자리수 2자리로 통일하기

        if rec_time_start and rec_time_end:
            return_str = f"{ch}\t'{rec_time_start}\t'{rec_time_end}\t'{rec_tel}\t{stt_code}\t{rec_code}\t{stt_txt}\t\t'{rec_key}\t{rec_info}"
            print(return_str)
            return return_str
        else:
            return ""

    def create_text_log(self, lines):
        # 열 제목 추가
        column_titles = "채널\t시작시간\t종료시간\t전화번호\tSTT_CD\tREC_CD\tSTT_결과\t\tREC_KEY\t파일명"
        return_str = column_titles + "\n"  # 첫 줄에 열 제목을 추가하고, 다음 줄로 넘어갑니다.
        for i, line in enumerate(lines):
            if self.check_welcome(line):
                ch_num = self.get_text_ch(line)
                scope_list = self.set_ch_scope_list(i, ch_num, lines)
                str_tmp = self.get_log_info(scope_list)
                if str_tmp:
                    return_str += str_tmp + "\n"
        return return_str


if __name__ == "__main__":
    ps = ParseNew()
    ps.exec_run()
