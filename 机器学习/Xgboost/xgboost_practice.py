# coding=utf-8
import xgboost as xgb
import pandas as pd
import numpy as np
import pickle
import sys
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error, make_scorer
from sklearn.preprocessing import StandardScaler
# from sklearn.grid_search import GridSearchCV
from sklearn.model_selection import GridSearchCV
from scipy.sparse import csr_matrix, hstack
# from sklearn.cross_validation import KFold, train_test_split
from sklearn.model_selection import KFold,train_test_split
from xgboost import XGBRegressor
