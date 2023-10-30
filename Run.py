# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 13:36:45 2023

@author: ila
"""
# ## 42577 Introduction to Business Analytics 

##test breyting


import pandas as pd
import numpy as np
from DataLoader import DataLoader

'''import more stuff here'''

import matplotlib.pyplot as plt

#matplotlib style options
plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (15, 8)

plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (15, 8)


# read the existing subset of the data
df = DataLoader.read_data('Trips_subset.csv')
# Display few variables
df.head(8).T 


""" data description """ 

print(f"the number of the rows = {len(df)} \n")
print("dataframe information")
df.info()

df.isnull().any()

print("data summary statistics = \n")
df.describe()


print("data correlation = \n")
df.corr()


""" Gender """
print(f"available values (classes) for the gender column = {df['gender'].unique()}")
print(f" the length data where gender=0: {len(df[df['gender']==0])}")
print(f" the length data where gender=1: {len(df[df['gender']==1])}")
print(f" the length data where gender=2: {len(df[df['gender']==2])}")


""" usertype """
print(f"available values (classes) for the gender column = {df['usertype'].unique()}")
print(f" the length data where usertype=Subscriber: {len(df[df['usertype']=='Subscriber'])}")
print(f" the length data where usertype=Customer: {len(df[df['usertype']=='Customer'])}")



# ## Data prep

# Convert a datetime column to datetime data type
df['starttime'] = pd.to_datetime(df['starttime'])
df['stoptime'] = pd.to_datetime(df['stoptime'])

# convert gender and usertype into category
df['gender'] = df['gender'].astype('category')
df['usertype'] = df['usertype'].astype('category')

# Getting the weekdays
df['weekday'] = [d.weekday() for d in df['starttime']] 

df=df.set_index('starttime')
df.head()

# # Data visualization

# ### Gender
# Let's visualize the gender distribution. We have three categories; 1, 2, and 0. 1 represents men, 2 represents women and 0 are users that did not declare their gender.

# Create a bar plot for the "gender" column

df['gender'].value_counts().plot(kind='bar')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.title('Gender Distribution')
plt.show()


# Create a pie chart for the "gender" column

gender_counts = df['gender'].value_counts()
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%')
plt.title('Gender Distribution')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()


# From this we can see that most users are men.

# Create a bar plot for the "usertype" column

df['usertype'].value_counts().plot(kind='bar')
plt.xlabel('user_type')
plt.ylabel('Count')
plt.title('user_type Distribution')
plt.show()


# ### bike id

# Create a histogram for the "bikeid" column

plt.figure(figsize=(6, 3))
plt.hist(df['bikeid'], bins=50)  # Adjust the number of bins as needed
plt.xlabel('Bike ID')
plt.ylabel('Frequency')
plt.title('Bike ID Distribution (Histogram)')
plt.show()


# ### birth_year

# Create a histogram for the "birth_year" column

plt.figure(figsize=(6, 3))
plt.hist(df['birth_year'], bins=50)  # Adjust the number of bins as needed
plt.xlabel('birth Year')
plt.ylabel('Frequency')
plt.title('birth Year Distribution (Histogram)')
plt.show()



# Let's visualize the distribution of the start stations by doing a scatter plot of the latitude and longitude coordinates of the stations.


plt.scatter(df.start_station_latitude, df.start_station_longitude, label = "Starting stations")
plt.legend(prop = {'size': 20})
plt.ylabel('Latitude')
plt.xlabel('Longitude')


# Now let's do the same for the end stations as well.

plt.scatter(df.end_station_latitude, df.end_station_longitude, label = "End stations")
plt.legend(prop = {'size': 20})
plt.ylabel('Latitude')
plt.xlabel('Longitude')


# From this we can tell that there are more end stations than starting stations. This would make sense since all the bikes start at certain stations where Citi bikes places the bikes at the start of the day, but then the bikes will spread out around the city as the day goes by and they are used.

# # Data analysis 

# 

# ## group by starttime

# group by >> get the number of trips 





# # Prediction Challenge




# # Exploratory Component



# # Conclusions




