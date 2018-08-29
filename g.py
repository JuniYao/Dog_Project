
import time
import pandas as pd
import numpy as np 

#filename='chicago.csv'
filename='/Users/juni/Downloads/UdaCity_Study/Programm2/bikeshare-2/chicago.csv'
df=pd.read_csv(filename)

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        cities=['all','chicago','new york','washington']
        city=input('Would you like to see data for Chicago,New York or Washington?\n')
        city=city.lower()
        if city in cities:
            print(city)
            break
        

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        months=['all','january', 'february', 'march', 'april', 'may', 'june']
        month=input('Would you like to filter the data by which month? January, Feburary, March, April,May , June or all of them?\n')
        month=month.lower()
        if month in months:
            print(month)
            break
        

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        days=['all','mondy','tuesday','wednesday','thursday','friday','saturday','sunday']
        day=input('would you like to filter the data by which day or all? e.g, Sunday,Monday\n)')
        day=day.lower()
        if day in days:
            print(day)
            break
        

    print('-'*40)
    return city, month, day

get_filters()

