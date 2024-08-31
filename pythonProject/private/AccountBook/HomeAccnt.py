import xlwings as xw
import os
import glob
from datetime import datetime

# 오늘 날짜를 YYYYMMDD 형식으로 가져오기
today_date = datetime.now().strftime("%Y%m%d")

# 현재 스크립트가 있는 디렉토리 경로 가져오기
base_directory = os.path.dirname(os.path.abspath(__file__))

# 소스 파일이 위치한 디렉토리 설정 (현재 디렉토리 기준 상대경로)
source_directory = os.path.join(base_directory, "거래내역", "2024")

# 오늘 날짜가 포함된 .xls 파일 찾기
file_pattern = os.path.join(source_directory, f"*{today_date}*.xls")
files = glob.glob(file_pattern)

# 대상 파일이 위치한 디렉토리 설정 (현재 디렉토리 기준 상대경로)
target_directory = base_directory

# 파일이 존재하는지 확인하고 열기
if files:
    file_to_open = files[0]  # 파일이 여러 개일 경우 첫 번째 파일을 염
    app = xw.App(add_book=False)
    wb_source = app.books.open(file_to_open)
    ws_source = wb_source.sheets[0]

    # A8부터 G열까지 마지막 행 찾기
    last_row = ws_source.range('A8').end('down').row

    # 1단계: 거래시간(B열)을 기준으로 A8:G 마지막 행 범위 정렬
    ws_source.range(f'A8:G{last_row}').api.Sort(
        Key1=ws_source.range('B8').api,  # 거래시간 열을 기준으로 정렬
        Order1=1,  # 오름차순 정렬
        Orientation=1  # 상향식(위에서 아래로) 정렬
    )

    # 2단계: 거래일자(A열)을 기준으로 다시 정렬
    ws_source.range(f'A8:G{last_row}').api.Sort(
        Key1=ws_source.range('A8').api,  # 거래일자 열을 기준으로 정렬
        Order1=1,  # 오름차순 정렬
        Orientation=1  # 상향식(위에서 아래로) 정렬
    )

    # 정렬 후 A8:G 마지막 행 범위의 데이터만 복사
    data_to_copy = ws_source.range(f'A8:G{last_row}').value

    # 가계부_2024.xlsx 파일 열기
    target_wb_path = os.path.join(target_directory, "가계부_2024.xlsx")
    wb_target = app.books.open(target_wb_path)
    ws_target = wb_target.sheets[2]  # 3번째 시트는 인덱스 2에 해당

    # 표의 마지막 행 찾기 (머릿말을 제외한 마지막 행)
    tbl = ws_target.api.ListObjects(1)  # 첫 번째 표 객체 (기본적으로 첫 번째 테이블을 가리킵니다)
    last_row_target = tbl.ListRows.Count + tbl.HeaderRowRange.Row  # 표의 마지막 행 번호 찾기

    # 마지막 행 아래쪽에 데이터 붙여넣기
    ws_target.range(f'A{last_row_target + 1}').value = data_to_copy

    # 피벗 테이블 새로 고침 (피벗 테이블들이 존재하는 시트로 이동)
    pivot_sheet = wb_target.sheets[1]  # 2번째 시트가 피벗 테이블들이 있는 시트라고 가정
    for pivot in pivot_sheet.api.PivotTables():
        pivot.PivotCache().Refresh()

    # 저장 및 종료
    wb_target.save()
    wb_source.close()
    wb_target.close()
    app.quit()

else:
    print("오늘 날짜가 포함된 .xls 파일을 찾을 수 없습니다.")
