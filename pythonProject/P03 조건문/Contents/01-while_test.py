import re # Regular Expressions

class InputValidator:
    # self : this 와 유사 (해당 클래스 내 다른 속성값 및 메서드 호출시 사용)
    def get_valid_input(self):
        input_str = ""  # 사용자 입력을 저장할 변수
        result = ""  # 유효한 입력을 저장할 변수
        is_valid_input = False

        while not is_valid_input:
            input_str = input("숫자 입력 (3자리 숫자): ")
            if self.is_valid_input(input_str):
                is_valid_input = True
                result = input_str  # 유효한 입력값을 result 변수에 저장
            else:
                print("오류: 입력은 한글, 영문, 특수문자를 포함하지 않는 정확히 3자리의 숫자여야 합니다.")
        return result

    def is_valid_input(self, input_str):
        return bool(re.match(r"[0-9]{3}$", input_str))

# main 부분은 스크립트가 직접 실행될 때 호출되는 코드 영역
# 프로그램의 실행 시작점(entry point)으로 작용
# 이 스크립트가 다른 파일에서 모듈로 임포트되어 사용된다면, 이 조건문 아래의 코드는 실행되지 않음.
if __name__ == "__main__":
    validator = InputValidator()
    valid_input = validator.get_valid_input()
    print("정상 처리된 입력: " + valid_input)
