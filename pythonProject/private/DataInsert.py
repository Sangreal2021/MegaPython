'''
pip install openpyxl
pip install pandas
'''

import pandas as pd

# 엑셀 파일 경로
file_path = r'D:\private\study\SQLD\자료\etc\project\AP_IF_MAST.xlsx'

# 엑셀 파일 읽기
excel_data = pd.read_excel(file_path)

# 테이블 이름
table_name = '"AP_IF_MAST$"'

# 컬럼 이름 가져오기
columns = excel_data.columns

# INSERT INTO 쿼리 생성
insert_queries = []

for index, row in excel_data.iterrows():
    values = [f"'{str(value).replace("'", "''")}'" if pd.notna(value) else "NULL" for value in row.values]
    insert_query = f'INSERT INTO {table_name} ({", ".join(columns)}) VALUES ({", ".join(values)});'
    insert_queries.append(insert_query)

# 첫 번째 쿼리 예시 출력
print(insert_queries[0])

# 전체 쿼리를 파일로 저장 (선택 사항)
with open(r'D:\private\study\SQLD\자료\etc\project\AP_IF_MAST.txt', 'w') as f:
    for query in insert_queries:
        f.write(query + '\n')
