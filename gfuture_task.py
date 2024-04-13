# -*- coding: utf-8 -*-
"""Gfuture Task.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/15BR6jX6S9CZc48K6RjKXckmK4QpoJJQt
"""

from google.colab import files
uploded = files.upload()

import pandas as pd
import numpy as np

df = pd.read_csv('transaction_data.csv')

df

"""# **Check if any null is available or not in date set**"""

df.isnull().sum()

"""# **This define that how many unique customer are there in the data set**"""

df['CustomerID'].unique()

"""# **Check all data types**"""

df.dtypes

"""# **Conver Data type to datetime for better analisis**"""

df['TransactionDate'] = pd.to_datetime(df['TransactionDate'])

df['TransactionDate'].dtype

df.shape

df.info()

"""# This specify that how many quantity that Customer purchase on different Category of product"""

pivot_table = pd.pivot_table(df,values='Quantity',
                              index=['CustomerID'],
                              columns='ProductCategory',
                              aggfunc=np.sum)
pivot_table

"""# **This specify that how much amount Customer spend on different Category of product **"""

pivot_table = pd.pivot_table(df,values='TotalPrice',
                              index=['CustomerID'],
                              columns='ProductCategory',
                              aggfunc=np.sum)
pivot_table

import datetime
df['Date_month'] = df['TransactionDate'].dt.month

df['Date_month']

import matplotlib.pyplot as plt

"""# **This define that which category have how much sales in different months**"""

grouped_data = df.groupby(['Date_month', 'ProductCategory'])['Quantity'].sum().unstack()

fig, ax = plt.subplots(figsize=(12, 8))
grouped_data.plot.bar(ax=ax)

ax.set_xlabel('Month')
ax.set_ylabel('Quantity')
ax.set_title('Quantity of Products Sold by Month and Category')

plt.xticks(rotation=45)

plt.show()

"""# **this define that how a customer spend total amount on different category**"""

pivot_table_Customer = pd.pivot_table(df,values='TotalPrice',
                              index=['ProductCategory'],
                              columns='CustomerID',
                              aggfunc=np.sum)
pivot_table_Customer

"""# **Explain About Which month they spent high with data of product categorty**"""

pivot_table_Customer_Month = pd.pivot_table(df,values='TotalPrice',
                              index=['ProductCategory'],
                              columns='Date_month',
                              aggfunc=np.sum)
pivot_table_Customer

"""# **this define that how a customer spend total amount on different category in easy visual format**"""

labels = pivot_table_Customer.index.to_list()
colors = ['lightgreen', 'gold', 'lightcoral', 'yellowgreen', 'lightskyblue']

plt.pie(pivot_table_Customer.sum(axis=1), explode=[0.1] * len(labels), labels=labels, autopct='%1.1f%%', shadow=True, colors=colors)
plt.title("Total Amount Spent by Customers on Different Categories")
plt.show()

"""# **this define that how a customer spend total amount on different Months in Visual format**"""

labels = grouped_data.index.to_list()
colors = ['lightgreen', 'gold', 'lightcoral', 'yellowgreen', 'lightskyblue']

plt.pie(grouped_data.sum(axis=1), explode=[0.1] * len(labels), labels=labels, autopct='%1.1f%%', shadow=True, colors=colors)
plt.title("Total Amount Spent by Customers on Different Months")
plt.show()

"""# **Customer By Details That How Many Quantity Of product that they Purchase**"""

grouped_data_quantity = df.groupby(['CustomerID', 'ProductCategory'])['Quantity'].sum()
grouped_data_quantity

"""# brief summary of findings and recommendations :


*  **Here we can see the data of customer that have a higher purchase on Home Decore products**

*   **We find that a Customer spend a more amount In March and December**

*   **By the Visual Data of Bar char we find that our Home Decore Product Are less sales in Summer Seasion**

*   **Our home Decore Product are sells good in 11Th and 12Th month than summer time**

*   **Our marketing team need to focus more on Electronic and clothing market for better result**




"""