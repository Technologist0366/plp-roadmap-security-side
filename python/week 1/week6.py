
Task 1: Load and Explore the Dataset
Choose a dataset in CSV format (for example, you can use datasets like the Iris dataset, a sales dataset, or any dataset of your choice).
Load the dataset using pandas.
Display the first few rows of the dataset using .head() to inspect the data.
Explore the structure of the dataset by checking the data types and any missing values.
Clean the dataset by either filling or dropping any missing values

import kagglehub
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('default')

from adjustText import adjust_text
from google.colab import files
uploaded = files.upload()

from sklearn.preprocessing import LabelEncoder as le







df = pd.read_csv("Global_Cybersecurity_Threats_2015-2024.csv")

# Check structure
df.head()
df.info()
df.isnull().sum()




<class 'pandas.core.frame.DataFrame'>
RangeIndex: 3000 entries, 0 to 2999
Data columns (total 10 columns):
 #   Column                               Non-Null Count  Dtype  
---  ------                               --------------  -----  
 0   Country                              3000 non-null   object 
 1   Year                                 3000 non-null   int64  
 2   Attack Type                          3000 non-null   object 
 3   Target Industry                      3000 non-null   object 
 4   Financial Loss (in Million $)        3000 non-null   float64
 5   Number of Affected Users             3000 non-null   int64  
 6   Attack Source                        3000 non-null   object 
 7   Security Vulnerability Type          3000 non-null   object 
 8   Defense Mechanism Used               3000 non-null   object 
 9   Incident Resolution Time (in Hours)  3000 non-null   int64  
dtypes: float64(1), int64(3), object(6)
memory usage: 234.5+ KB

	0
Country 	0
Year 	0
Attack Type 	0
Target Industry 	0
Financial Loss (in Million $) 	0
Number of Affected Users 	0
Attack Source 	0
Security Vulnerability Type 	0
Defense Mechanism Used 	0
Incident Resolution Time (in Hours) 	0

dtype: int64




count_attacked = df['Country'].value_counts().reset_index()
# print(count_attacked)

plt.figure(figsize=(16, 12))
sns.barplot(data=count_attacked, x='Country', y='count', alpha=.8, gap=.1)
plt.grid(alpha=.5, axis='y')
plt.title('Total Number of Cybersecurity Attacks (2015-2024)', pad=1)
plt.xlabel('Countries', labelpad=10)
plt.ylabel('Number of Attacks', labelpad=10)
plt.show()


import matplotlib.pyplot as plt

loss_per_year = df.groupby("Year")["Financial Loss (in Million $)"].sum()
loss_per_year.plot(kind="line", marker='o', title="Total Financial Loss Over Time")
plt.xlabel("Year")
plt.ylabel("Financial Loss (in Million $)")
plt.grid(True)
plt.show()

df.plot(kind="scatter", x="Number of Affected Users", y="Financial Loss (in Million $)", alpha=0.5)
plt.title("Users Affected vs. Financial Loss")
plt.xlabel("Number of Affected Users")
plt.ylabel("Financial Loss (in Million $)")
plt.grid(True)
plt.show()
