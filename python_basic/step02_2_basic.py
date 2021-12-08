# /c/ProgramData/Anaconda3/python
# -*- coding: utf-8 -*-

# z_score 공식
# seaborn에서 다이아몬드 데이터셋
# column, x, y, z 표준화한다.

import seaborn as sns

def standardize(column):
    """데이터의 정규화를 만드는 과정이다.
    Args:
        column (pandas Series): 정규화를 하기 위한 것

    Returns: series
        pandas series: 표준화 공식을 적용한다.
    """
    # Finish the function so that it returns the z-scores
    z_score = (column - column.mean()) / column.std()
    return z_score

if __name__ == "__main__":
    # Use the standardize() function to calculate the z-scores
    diamonds = sns.load_dataset("diamonds")
    print(diamonds.head())
    diamonds['x'] = standardize(diamonds['x'])
    diamonds['y'] = standardize(diamonds['y'])
    diamonds['z'] = standardize(diamonds['z'])

    print(diamonds.head())