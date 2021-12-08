# /c/ProgramData/Anaconda3/python
# -*- coding: utf-8 -*-

# Context Manager               # 일일 파티 식당 종업원
# - Sets up a context             - 테이블 세팅
# - Runs your code                - 초대 손님 와서 식사 주문
# - Removes the context           - 테이블 닦고 테이블 정리

def main():
    with open("data/my_file.txt") as my_file:
        text = my_file.read()
        text_length = len(text)

    print("파일 글자 총 길이는 {} 과 같다.".format(text_length))

if __name__ == "__main__":
    main()


# Context Manager
# with <context_manager>(<args>) as <variable_name>:
    # 코드 실행
    # 마지막 코드까지 실행

# with 코드는 제거됨
