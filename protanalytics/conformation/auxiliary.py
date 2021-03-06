import os
import numpy as np 
import scipy as sp 
import pandas as pd


def check_directories(directories):
  for directory in directories:
    if not os.path.exists(directory):
      os.makedirs(directory)


def radian_distance_metric(a, b):
  d = abs(a - b) % 360
  return 360 - d if d > 180 else d
  

def radian_matrix_to_sin_cos_matrix(radian_matrix):
  sin_matrix = radian_matrix.apply(np.sin)
  sin_matrix.columns = map(lambda x : x + "--SIN", radian_matrix.columns)
  cos_matrix = radian_matrix.apply(np.cos)
  cos_matrix.columns = map(lambda x : x + "--COS", radian_matrix.columns)
  return pd.concat([sin_matrix, cos_matrix], axis=1, join='outer', join_axes=None, ignore_index=False, keys=None, levels=None, names=None, verify_integrity=True)

def sin_cos_matrix_to_radian_matrix(sin_cos_matrix):
  radian_matrix = pd.DataFrame(index = sin_cos_matrix.index)
  for name in [col[:-5] for col in sin_cos_matrix.columns]:
    radian_matrix[name] = np.arctan2(sin_cos_matrix[name + "--SIN"].values, sin_cos_matrix[name + "--COS"].values)
  return radian_matrix
