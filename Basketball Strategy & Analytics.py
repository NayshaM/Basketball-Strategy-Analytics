import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import statistics as stat
from scipy import stats as sp
from random import random, seed, randint, sample

#read in data
data=pd.read_csv("C:/Users/Naysha/Desktop/Internship/nbaplayersdraft.csv")

#make sure data was inserted properly
data.head()

#find the total number of Duke draft pics in our before the 2000 draft
sum((data.college=="Duke") & (data.year <= 2000))

#univariate analysis for draft year
data['year'].describe ()

#turn made two new categories from the variable year; before and after 2000 Draft
def year_range(series):
    if series <= 2000:
        return "Before or in 2000 draft"
    elif series >2000 :
        return "After 2000 draft"

#apply the previous change to the data set
data['year_range'] =data['year'].apply(year_range)

#make sure I correctly coded the data
data['year_range'].value_counts()

#created a trivariate frequency table that showed the team, draft picks from Duke, and if they were drafted before
# or after the 2000 draft
table3 = pd.crosstab([data['team'], data['college']=='Duke'],
                        data['year_range'],
                            margins = True)

#printed the table to make sure I created it right
print(table3)

#converted the table to an excel file and exported it to my computer
table3.to_csv(r"C:/Users/Naysha/Desktop/Internship/table3.csv")

#using the table in excel, I found the answer
# Dallas, Minnesota, and Phoenix have all drafted 2 players who attended Duke in or before the 2000 Draft

#univariate analysis for draft year
data['year'].describe ()

#made two new categories from the variable year ; even and odd year
def year_even(series):
    if series % 2:
        return "Even year"
    else :
        return "Odd year"

#applied the previous change to the data set
data['year_even'] =data['year'].apply(year_even)

#made sure I correctly coded the data
data['year_even'].value_counts()

#created a trivariate frequency table that showed the team, player, and if they were drafted in an even year or not
table4 = pd.crosstab([data['team'], data['player']],
                        data['year_even'],
                            margins = True)

#printed the table to make sure I created it right
print(table4)

#converted the table to an excel file and exported it to my computer
table4.to_csv(r"C:/Users/Naysha/Desktop/Internship/table4.csv")

#using the table in excel I found the answer
# Atlanta, Cleveland, and Toronto all have 6 players whose first name starts with the letter D and were drafted in an
# even year draft

#valuing draft picks
def draft_value(series):
    if series <= 30:
        return "High"
    elif series > 30:
        return "Low"

#apply previous change to the data set
data[ 'draft_value'] =data[ 'overall_pick'].apply(draft_value)

#made sure I correctly coded the data
data['draft_value'].value_counts()

#mean for win_shares
data['win_shares'].mean()

#valuing win shares
def performance(series):
    if series >= 18:
        return "Above Average"
    elif series < 18:
        return "Below Average"

#apply previous change to the data set
data[ 'performance'] =data[ 'win_shares'].apply(performance)

#made sure I correctly coded the data
data['performance'].value_counts()

#created a trivariate frequency table that showed the nba team, draft value, and performance based on win shares
table5 = pd.crosstab([data['team'], data['draft_value']],
                        data['performance'],
                            margins = True)

#converted the table to an excel file and exported it to my computer
table5.to_csv(r"C:/Users/Naysha/Desktop/Internship/table5.csv")

#underperformed: CHO, NOP, NOK
#overperformed: MIL, CHI, SEA

#created a trivariate frequency table that showed the college team, draft value, and performance based on win shares
table6 = pd.crosstab([data['college'], data['draft_value']],
                        data['performance'],
                            margins = True)

#converted the table to an excel file and exported it to my computer
table6.to_csv(r"C:/Users/Naysha/Desktop/Internship/table6.csv")

#underperformed: Vanderbilt, Baylor, VCU
#overperformed: Texas A&M, Bowling Green, Butler County Community College

#Resources
#https://www.kaggle.com/datasets/mattop/nba-draft-basketball-player-data-19892021


