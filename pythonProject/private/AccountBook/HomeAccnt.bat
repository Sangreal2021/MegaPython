@echo off

echo 현재 경로: %cd%
move /y "C:\Users\hiw15\Downloads\신한은행_거래내역조회_*.xls" "D:\private\study\AccountBook\거래내역\2024\"
echo %errorlevel% 이동 명령어 종료 코드
if %errorlevel% neq 0 (
    echo 파일을 이동하는데 문제가 발생했습니다. 파일 경로와 이름을 확인하세요.
) else (
    echo 파일이 성공적으로 이동되었습니다.
)

cd /d "D:\private\study\AccountBook"  
echo 현재 작업 경로: %cd%

python HomeAccnt.py

pause
