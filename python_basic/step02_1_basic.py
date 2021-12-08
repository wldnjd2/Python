# /c/ProgramData/Anaconda3/python
# -*- coding: utf-8 -*-

# 정규화 공식
# normalization
# 데이터의 범위를 0과 1로 변환하여 데이터의 분포를 조정하는 방법
# x_new = (x - x_min) / ((x_max) - (x_min)
import seaborn as sns

def min_max_normalize(column):
    """데이터의 정규화를 만드는 과정이다.
    Args:
        column (pandas Series): 정규화를 하기 위한 것

    Returns: series
        pandas series: min_max 정규화 공식의 답을 가져온다.
    """

    min_max_score = (column - column.min()) / (column.max() - column.min())
    return min_max_score

if __name__ == "__main__":
    iris = sns.load_dataset("iris")
    print(iris.head())

    iris['sepal_length'] = min_max_normalize(iris['sepal_length'])
    iris['sepal_width'] = min_max_normalize(iris['sepal_width'])
    iris['petal_length'] = min_max_normalize(iris['petal_length'])
    iris['petal_width'] = min_max_normalize(iris['petal_width'])

    print(iris.head())