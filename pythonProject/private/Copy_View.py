'''
1. pip install openpyxl
2. pip install pandas
3. Microsoft Visual C++ Build Tools 다운로드
    (1) 다운로드한 설치 파일을 실행하고, "Workloads" 탭에서
        "Desktop development with C++"를 선택한 후 설치를 진행
    (2) cl.exe가 포함된 경로가 시스템의 PATH 환경 변수에 추가되었는지 확인. 기본적으로 다음 경로에 설치
        C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Tools\MSVC\<version>\bin\Hostx64\x64
4. pip install cx_Oracle
0. python -m pip install --upgrade pip
'''

import cx_Oracle

# 192.168.1.72:1521:XE id : dev_kfms / pw : devkfms
# Oracle 데이터베이스 연결 정보
source_host = '192.168.1.72'
source_port = '1521'  # 일반적으로 1521
source_service_name = 'XE'
source_user = 'dev_kfms'
source_password = 'devkfms'

# 127.0.0.1:1523:XE id : hiw15 / pw : 1234
target_host = '127.0.0.1'
target_port = '1523'  # 일반적으로 1521
target_service_name = 'XE'
target_user = 'hiw15'
target_password = '1234'

# DSN 생성
source_dsn = cx_Oracle.makedsn(source_host, source_port, service_name=source_service_name)
target_dsn = cx_Oracle.makedsn(target_host, target_port, service_name=target_service_name)

# 데이터베이스 연결
source_connection = cx_Oracle.connect(user=source_user, password=source_password, dsn=source_dsn)
target_connection = cx_Oracle.connect(user=target_user, password=target_password, dsn=target_dsn)

source_cursor = source_connection.cursor()
target_cursor = target_connection.cursor()

# 복사할 뷰 이름 리스트
view_name = 'AP_IF_MAST'

# 소스 스키마에서 뷰 정의 가져오기
source_cursor.execute(f"SELECT text FROM user_views WHERE view_name = '{view_name.upper()}'")
view_definition = source_cursor.fetchone()[0]

# 타겟 스키마에 테이블 생성 (필요한 경우)
source_cursor.execute(f"SELECT column_name, data_type, data_length, data_precision, data_scale FROM user_tab_columns WHERE table_name = '{view_name.upper()}'")
columns_info = source_cursor.fetchall()

columns = [col[0] for col in columns_info]
columns_str = ', '.join(columns)

# 테이블 구조 출력
print(f"Table structure for {view_name}:")
for col in columns_info:
    print(col)

# 타겟 스키마에 테이블 생성
create_table_sql = f"CREATE TABLE {view_name} ("
for col in columns_info:
    col_name = col[0]
    col_type = col[1]
    if col_type == 'NUMBER':
        if col[3] is not None and col[4] is not None:
            col_type += f"({col[3]},{col[4]})"
        elif col[3] is not None:
            col_type += f"({col[3]})"
    elif col_type in ['VARCHAR2', 'CHAR']:
        col_type += f"({col[2]})"
    create_table_sql += f"{col_name} {col_type},"
create_table_sql = create_table_sql.rstrip(',') + ')'

try:
    target_cursor.execute(create_table_sql)
    print(f"Table {view_name} created successfully in the target database.")
except cx_Oracle.DatabaseError as e:
    print(f"Table creation failed for {view_name}: {e}")

# 인덱스 복사
source_cursor.execute(f"""
    SELECT index_name, column_name
    FROM user_ind_columns
    WHERE table_name = '{view_name.upper()}'
    ORDER BY index_name, column_position
""")
indexes = {}
for index_name, column_name in source_cursor:
    if index_name not in indexes:
        indexes[index_name] = []
    indexes[index_name].append(column_name)

for index_name, columns in indexes.items():
    create_index_sql = f"CREATE INDEX {index_name} ON {view_name} ({', '.join(columns)})"
    try:
        target_cursor.execute(create_index_sql)
        print(f"Index {index_name} created successfully.")
    except cx_Oracle.DatabaseError as e:
        print(f"Index creation failed for {index_name}: {e}")

# 소스 DB에서 뷰 데이터 가져오기
source_cursor.execute(f"SELECT {columns_str} FROM {view_name}")
rows = source_cursor.fetchall()

# 데이터 삽입
insert_query = f'INSERT INTO {view_name} ({columns_str}) VALUES ({", ".join([":" + str(i+1) for i in range(len(columns))])})'
for row in rows:
    target_cursor.execute(insert_query, row)
print(f"Data copied successfully for {view_name}.")

# 커밋 및 연결 닫기
target_connection.commit()
source_cursor.close()
source_connection.close()
target_cursor.close()
target_connection.close()
