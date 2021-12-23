# /c/ProgramData/Anaconda3/python
# -*- coding: utf-8 -*-

# immutable or mutable
# immutable: int, float, bool, string, bytes, tuple, etc
# mutable: list, dict, set, bytearray, objects, functions, almost everything else
import pandas as pd

def add_new_column(values, data = pd.DataFrame()):
    """새로운 컬럼을 df 에 추가하며, 컬럼명은 "col_<n>"형태로 저장합니다. 이 때, column의 numerical index 형태여야 합니다.

    Args:
        values (iterable): 새로운 컬럼의 값을 의미합니다.
        data (DataFrame, optional): 함수가 실행되면 업데이트가 됩니다.
            만약에 데이터프레임을 입력받지 못하면, 임의의 데이터프레임이 디폴트로 생성됩니다.

    Returns:
        DataFrame
    """
    data["col_{}".format(len(data.columns))] = values
    return data

if __name__ == "__main__":
    print(add_new_column(values=range(10)))
    print(add_new_column(values=None))
    print(add_new_column(values=range(10)))
    print(add_new_column(values=None))

