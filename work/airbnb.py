"""
Driver/Navigator: Michael Kwakye
Emails: mkwakye99@gmail.com
Assignment: Exercise 9
Date: 4_14_21

"""
import seaborn
import pandas
#import numpy
import matplotlib.pyplot as plt
fig, ax = plt.subplots()


#Requirement 1
dataframe = pandas.read_csv("AB_NYC_2019.csv")
dataframe1 = dataframe[(dataframe['price'] < 400)]
bplot = seaborn.boxplot(x = 'neighbourhood_group', y = 'price', hue = 'room_type', data = dataframe1)
plt.savefig('boxplot1.png')

#Requirement 2
groupframe = dataframe.groupby('host_id').count()
groupframe2 = groupframe.nlargest(2, 'host_id') #terminal had an issue with this
bplot2 = seaborn.boxplot(x = 'minimum_nights', y = 'price', hue = 'room_type', data = groupframe2)
plt.savefig('boxplot2.png')