# /c/ProgramData/Anaconda3/python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

def load_and_plot(datasetname):
    """데이터를 불러오고 그래프를 작성합니다.
    Args:
        datasetname (str): 데이터셋 이름을 부릅니다.

    Returns:
        tuple of ndarray: (features, labels)
    """
    data = sns.load_dataset(datasetname)
    y = data.iloc[:, 1].values
    X = data.columns
    num_list = data.select_dtypes(include=[np.number]).columns
    print(num_list)
    sns.scatterplot(x = num_list[0], y = num_list[1], data = data)
    plt.show()

    return X, y

# 위 코드는 좋지 않습니다.
# 데이터를 불러오는 코드와 시각화 코드를 동시에 작성하는 것은 옳지 않습니다.

if __name__ == "__main__":
    X, y = load_and_plot("tips")
    print("X is:", X)
    print("y is:", y)
