import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import zscore
import dtale

from ipyvizzu import chart, Data, Config, Style

## This statement allows the visuals to render within your Jupyter Notebook.
%matplotlib inline

Jadarat_Data = pd.read_csv('Jadarat_data.csv')

dtale.show(Jadarat_Data)





