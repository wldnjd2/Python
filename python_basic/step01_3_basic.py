# /c/ProgramData/Anaconda3/python
# -*- coding: utf-8 -*-

def cnt_letter(content, letter):
    """content 안에 있는 문자를 세는 함수입니다.
    # Google Style
    Args:
        content(str): 탐색 문자열
        letter(str): 찾을 문자열

    Returns:
        int

    Raises:
        ValueError: 만약 Return 값이 문자가 아니라면 에러를 발생시킨다.
    """
    if (not isinstance(letter, str)) or len(letter) != 1:
        raise ValueError('`letter` 글자의 갯수가 한개 입니다.')
    return len([char for char in content if char == letter])

if __name__ == "__main__":
    help(cnt_letter)