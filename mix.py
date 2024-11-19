import numpy as np
import pandas as pd

empsalary = pd.DataFrame(data=np.arange(0, 100).reshape(10, 10))
print(empsalary.head())
print(empsalary.loc[2, 3])