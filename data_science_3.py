import pandas as pd
df = pd.read_csv('GoogleApps.csv')
df.info()

# 1 How many apps in the 'BUSINESS' 'Category' are there?
busy = df['Category'].value_counts()
print(busy['BUSINESS'])

# 2 What is the ratio of apps for teenagers ('Teen') to those for children over 10 years old ('Everyone 10+')?
# Round the answer to the nearest hundredth.
rate = df['Content Rating'].value_counts()
print('Ratio:', round(rate['Teen'] / rate['Everyone 10+'], 2))
# 3.1 What is the average 'Rating' of 'Paid' apps? 
# Round the answer to the nearest hundredth.
pay = df.groupby(by = 'Type')['Rating'].mean()
print(pay['Paid'])
# 3.2 How much lower is the average 'Rating' of 'Free' apps than the average rating of 'Paid' apps?
# Round the answer to the nearest hundredth.
print(pay['Free'] - pay['Paid'])
# 4 What are the minimum and maximum app 'Size' in the 'COMICS' 'Category'?
# Round the answer to the nearest hundredth.
print(df.groupby(by = 'Category')['Size'].agg(['min', 'max']))
# Bonus 1. How many apps have a 'Rating' of strictly greater than 4.5 in the 'FINANCE' 'Category'?
fin = df[df['Rating'] > 4.5]['Category'].value_counts()
print(fin['FINANCE'])
# Bonus 2. What is the ratio of 'Free' to 'Paid' games with a 'Rating' greater than 4.9?
