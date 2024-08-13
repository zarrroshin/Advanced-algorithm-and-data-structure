import numpy as np
import pandas as pd

# array = np.array(range(15))
# array2 = np.arange(15)

# dataframe=pd.DataFrame({1: array, 2: array2}, index=np.arange(15))
# dataframe[3] = np.arange(15,30)
# dataframe.rename(columns={1:"first",2:"second",3:"third"},inplace=True)
# print(dataframe)


# nums = {'Car Model Number': [223, np.nan, 237, 195, np.nan,
# 							575, 110, 313, np.nan, 190, 143,
# 							np.nan],
# 	'Engine Number': [4511, np.nan, 7570, 1565, 1450, 3786,
# 						2995, 5345, 7777, 2323, 2785, 1120]}

# # Create the dataframe
# df = pd.DataFrame(nums, columns =['Car Model Number'])

# # Apply the function
# #df['Car Model Number'] = df['Car Model Number'].replace(np.nan, 0)

# print(df.isna())


frame = pd.DataFrame(np.arange(8))