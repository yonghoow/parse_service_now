import pandas as pd

#read data into dataframe
df = pd.read_csv('sn_customerservice_case.csv', encoding='ISO-8859-1')

#print dataframe
print(df)

#print line that matches string 'Jun Jie' in description
print(df[df.description.str.contains(r'\bJun Jie\b', regex=True)])