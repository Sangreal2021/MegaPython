@echo off

echo ���� ���: %cd%
move /y "C:\Users\hiw15\Downloads\��������_�ŷ�������ȸ_*.xls" "D:\private\study\AccountBook\�ŷ�����\2024\"
echo %errorlevel% �̵� ��ɾ� ���� �ڵ�
if %errorlevel% neq 0 (
    echo ������ �̵��ϴµ� ������ �߻��߽��ϴ�. ���� ��ο� �̸��� Ȯ���ϼ���.
) else (
    echo ������ ���������� �̵��Ǿ����ϴ�.
)

cd /d "D:\private\study\AccountBook"  
echo ���� �۾� ���: %cd%

python HomeAccnt.py

pause
