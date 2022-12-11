import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')
print(df)
new_df = df.dropna(subset=['Date'], inplace=True)
print ('-----------')
#df.plot()
print(new_df)
plt.show()