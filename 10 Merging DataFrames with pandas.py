import os
os.chdir('/Users/randou/Esther/Coding/Python/Data Scientist with Python/Python-for-Data-Scientist')

# =============================================================================
# PREPARING DATA
# =============================================================================

import pandas as pd
filenames = ['/Users/randou/Esther/Coding/Python/Data Scientist with Python/Python-for-Data-Scientist/Sales/sales-jan-2015.csv',
             '/Users/randou/Esther/Coding/Python/Data Scientist with Python/Python-for-Data-Scientist/Sales/sales-feb-2015.csv']
dataframes = []
for f in filenames:
    dataframes.append(pd.read_csv(f))
dataframes = [pd.read_csv(f) for f in filenames]

from glob import glob
filnames = glob('sales*.csv')   # use wildcard pattern to match target names




























