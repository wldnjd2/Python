# /c/ProgramData/Anaconda3/python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np


# 총 3개의 평균과 중간값을 구하는 함수를 작성하세요. 10분 드립니다.
# 양식에 맞춰서 작성하세요.

def mean_and_median(values):
  """Get the mean and median of a sorted list of `values`

  Args:
    values (iterable of float): A list of numbers

  Returns:
    tuple (float, float): The mean and median
  """
  mean = sum(values) / len(values)
  midpoint = int(len(values) / 2)
  if len(values) % 2 == 0:
    median = (values[midpoint - 1] + values[midpoint]) / 2
  else:
    median = values[midpoint]

  return mean, median

if __name__ == "__main__":
    value_list = [1,1,2,3,4,5]
    avg, median = mean_and_median(value_list)
    print("avg:", avg) # 2.66666
    print("median:", median) # 2.5