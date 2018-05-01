import csv # reading and writing to CSV files
import time
from datetime import datetime # operations to parse dates
import calendar
from pprint import pprint # use to print data structures like dictionaries in a nicer way than the base print function.
import pandas as pd # converts CSV files into dataframes which are more practical to use than plain text
import numpy as np

## Filenames
chicago = 'chicago.csv'
new_york_city = 'new_york_city.csv'
washington = 'washington.csv'


def get_city():
    '''Asks the user for a city and returns the filename for that city's bike share data
    Args:   none.
    Returns: (str) Filename for a city's bikeshare data.
    '''
    print('\nHello! Let\'s explore some US bikeshare data!\n'
            'Would you like to see data for chicago, new_york_city, or washington?\n')
    while True:
        city = input('Enter choice: "chicago", "new_york_city", or "washington"\n'
                'Enter -1 to exit\n')
        city = city.lower()
        if(city=='chicago' or city=='new_york_city' or city=='washington' or city=='-1'):
            break
        else:
            print("This is not valid please enter again\n")
    return city

def get_time_period():
    '''Asks the user for a time period and returns the specified filter.
    Args:none.
    Returns:Filter in terms of month, day, both or none
    '''
    while(True):
        time_period = input('\nWould you like to filter the data by month, day, both or not at all?'
                        'Type "none" for no time filter.\n'
                        'Enter -1 to exit\n')
        time_period = time_period.lower()
        if(time_period=='month' or time_period=='day' or time_period=='both' or time_period=='none' or time_period=='-1'):
            break
        else:
            print("This is not valid please enter again \n")
    return time_period


def get_month():
    '''Asks the user for a month and returns the specified month.
       Args: none.
       Returns: Month as per choice of user.
    '''
    while(True):
        month = input('\nWhich month? January(1), February(2), March(3), April(4), May(5), or June(6)?\n'
                      'Enter -1 to exit\n')
        if(month=='1' or month=='2' or month=='3' or month=='4' or month=='5' or month=='6' or month=='-1'):
            break
        else:
            print("This is not valid please enter again \n")
    return int(month)


def get_day():
    '''Asks the user for a day and returns the specified day.
    Args: none.
    Returns:  Day as per choice of user.
    '''
    while(True):
        day = int(input('\nWhich day? Please type your response as an integer.\n'
                'Eg. 0-Monday,1-Tuesday,2-Wednesday,3-Thursday,4-Friday,5-Saterday,6-Sunday.\n'
                'Enter -1 for exit \n'))
        if((day>=0 and day<=6) or day==-1):
            break
        else:
            print("This is not valid please enter again \n")
    return day


def popular_month(datetime_col, time_period):
    '''Question: What month occurs most often in the start time?
    Args: datetime_col, time_period
    Returns:  none
    Discription:idxmax() is use to return the month name with max frequency
                max() is use to return the max frequency of the month fetched
    '''
    month       = pd.Series(datetime_col.apply(lambda date:date.month))#pd.Series((date.month) for date in datetime_col)
    popular_mth = month.value_counts().idxmax()
    count       = month.value_counts().max()
    print("Most Popular month is: ",calendar.month_name[popular_mth],end="    ")
    print("Count is:",count,end="    ")
    print("Current Filter:",time_period)


def popular_day(datetime_col, time_period):
    '''Question: What day of the week (Monday, Tuesday, etc.) occurs most often in the start time?
    Args: datetime_col, time_period
    Returns:  none
    Discription:idxmax() is use to return the weekday name with max frequency
                max() is use to return the max frequency of the weekday fetched
    '''
    day          = pd.Series(datetime_col.apply(lambda date:date.weekday()))#pd.Series((x.weekday()) for x in datetime_col)
    popular_dy   = day.value_counts().idxmax()
    count        = day.value_counts().max()
    print("Most Popular weekday is: ",calendar.day_name[popular_dy],end="    ")
    print("Count :",count,end="    ")
    print("Current Filter:",time_period)


def popular_hour(datetime_col, time_period):
    '''Question: What hour of the day (1, 2, ... 23, 24) occurs most often in the start time?
    Args: datetime_col, time_period
    Returns:  none
    Discription:idxmax() is use to return the hour name with max frequency
                max() is use to return the max frequency of the hour fetched
    '''
    hour         = pd.Series(datetime_col.apply(lambda date:date.hour))
    popular_hr   = hour.value_counts().idxmax()
    count        = hour.value_counts().max()
    print("Most Popular hour : ",popular_hr,end="    ")
    print("Count :",count,end="    ")
    print("Current Filter:",time_period)


def trip_duration(Trip_dur_col, time_period):
    '''Question: What is the total trip duration and average trip duration?
    Args: Trip_dur_col, time_period
    Returns:  none
    Discription: Calculated sum of trip duration in seconds and avg of trip duration in seconds.
    '''
    print("Total trip duration : {} seconds ".format(sum(Trip_dur_col)),end="     ")
    print("Current Filter:",time_period)
    print()
    print("Average trip duration : {} seconds ".format((Trip_dur_col.mean())),end="    ")
    print("Current Filter:",time_period)


def popular_stations(city_file, time_period):
    '''Question: What is the most frequently used start station and most frequently
    used end station?
    Args: city_file, time_period
    Returns:  none
    Discription:idxmax() is use to return the  Start_Station name with max frequency
                max() is use to return the max frequency of the Start_Station fetched
                similar for the End_Station
    '''
    Start_Station        =   city_file['Start Station'].value_counts().idxmax()
    Count_Start_Station  =   city_file['Start Station'].value_counts().max()
    End_Station          =   city_file['End Station'].value_counts().idxmax()
    Count_End_Station    =   city_file['End Station'].value_counts().max()

    print("Most Frequent Start station is:",Start_Station, end="    ")
    print("Count: ",Count_Start_Station,end="    ")
    print("Current Filter:",time_period)
    print()
    print("Most Frequent End station is:",End_Station,end="    ")
    print("Count: ",Count_End_Station,end="    ")
    print("Current Filter:",time_period)


def popular_trip(city_file, time_period):
    '''
    Question: What is the most common trip (i.e., the combination of start station and
    end station that occurs the most often)?
    Args: city_file, time_period
    Return: none
    Discription: Start_Station and End_Station contains the entire column of start and end station
                 which is fetched from city file.
                 complete_trip comtains the combination of start_station and end_station columnself.
                 famous_trip contains the name of the complete_trip with the max frequency.
                 count stores the number of time complete_trip occured.
    '''
    Start_Station   =   pd.Series(city_file['Start Station'])
    End_Station     =   pd.Series(city_file['End Station'])
    complete_trip   =   Start_Station +"  to  "
    complete_trip  +=   End_Station
    famous_trip     =   complete_trip.value_counts().idxmax()
    count           =   complete_trip.value_counts().max()
    print('Most common trip is:   ', famous_trip)
    print('Count = ',count,"         Current Filter:",time_period)


def users(User_col, time_period):
    '''Question: What are the counts of each user type?
    Args: User_col, time_period
    Return: none
    Discription: It will tell the count of all the three type of user(Subscriber,Customer,Dependent).
    '''
    counts  =   pd.Series(User_col.value_counts())
    print('Various users :             Current Filter:',time_period)
    for name in counts.index:
        print(name," : ",counts.loc[name])


def gender(Gender_col, time_period):
    '''Question: What are the counts of gender?
    Args: Gender_col, time_period
    Return: none
    Discription: Gender_col.dropna(how ='any') is used if any NA values are present, drop that label
                 counts contains the count of gender present in Gender_col
    '''
    Gender_col  =   Gender_col.dropna(how = 'any')
    counts      =   pd.Series(Gender_col.value_counts())
    print("Gender count :              Filter is ",time_period)
    for name in counts.index:
        print(name," : ",counts.loc[name])


def birth_years(Birth_col, time_period):
    '''Question: What is the earliest birth year (when the oldest person was born),
    most recent birth year, and most common birth year?
    Args: Birth_col, time_period
    Return: none
    Discription: Birth_col.dropna(how = 'any') is used if any NA values are present, drop that label
                 earliest stores when the oldest person was born by calculating the min value year
                 most_recent stores when the recent person was born by calculating the max value year
                 most_common stores the most common year of birth but counting the year with max frequency
    '''
    Birth_col   =   Birth_col.dropna(how = 'any')
    earliest    =   int(Birth_col.min())
    most_recent =   int(Birth_col.max())
    most_common =   int(Birth_col.value_counts().idxmax())
    print('Earliest birth year:',earliest,"             Filter is: ",time_period)
    print('Most recent birth year:',most_recent,"           Filter is: ",time_period)
    print('Most common birth year:',most_common,"           Filter is: ",time_period)



def display_data(city_file):
    '''Displays five lines of data if the user specifies that they would like to.
    After displaying five lines, ask the user if they would like to see five more,
    continuing asking until they say stop.
    Args: city_file
    Returns: none
    Discription: While loop is used for taking repeated input and iloc function is used for fetching
                 the data from city_file.
                 if condition is used to keep the record of count.if count=5 then it will again ask the
                 user if he wants to see more.
    '''
    display = input('\nWould you like to view individual trip data?'
                    'Type \'yes\' or \'no\'.\n')
    count=1
    count2=1
    while True:
        if(display=="yes"):
            print('{')
            print(city_file.iloc[count2])
            print('}')
            count+=1
            count2+=1
        elif(display=="no"):
            break
        else:
            print("Wrong input")
            count=5

        if(count==5):
            display = input('\nWould you like to view more?'
                            'Type \'yes\' or \'no\'.\n')
            count=1


def statistics():
    '''
    Calculates and prints out the descriptive statistics about a city and time period
    specified by the user via raw input.
    Args:   none.
    Returns: none.
    '''
    city                 = get_city() # Choice of city for statistics (Chicago, New York, Washington)
    if(city=='-1'):
        return
    time_period          = get_time_period() # Filter by time period (month, day, both, none)
    if(time_period=='-1'):
        return
    print("Fetching data.....\n")
    path                 ='G:/college work/nanodegree/bikeshare/'
    city_file            = pd.read_csv(path+city+'.csv') #use to fetch the csv file from the given location

    print("Few moments.....")
    start_time_col       = city_file['Start Time']
    actual_start_time_col= pd.to_datetime(start_time_col) #use to convert given datetime into standard date time format

    print("Performing necessary calculations.....")
    city_file['month_col']      = actual_start_time_col.dt.month      #creating a month column
    city_file['day_of_week_col']= actual_start_time_col.dt.weekday    #creating a weekday column

    if(time_period == "month" or time_period == "both"):      #Filter data month wise,if filter is month or both
        month                   = get_month()
        if(month==-1):
            return
        city_file               = city_file[city_file['month_col'] == month]
        start_time_col          = city_file['Start Time']
        actual_start_time_col     = pd.to_datetime(start_time_col)

    if(time_period == "day" or time_period == "both"):         #Filter data day wise,if filter is day or both
        day                     = get_day()
        if(day==-1):
            return
        city_file               = city_file[city_file['day_of_week_col'] == day]
        start_time_col          = city_file['Start Time']
        actual_start_time_col   = pd.to_datetime(start_time_col)
        #print(city_file)

    print('Calculation of statistics in process....\n')
    s_time = time.time()

    if(time_period=='none'):                                    #print popular month only if filter is none
        popular_month(actual_start_time_col, time_period)
        print()
    if(time_period=='none' or time_period=='month'):           #print popular month only if filter is none or month
        popular_day(actual_start_time_col,time_period)
        print()

    popular_hour(actual_start_time_col,time_period)
    print()
    trip_duration(city_file['Trip Duration'],time_period)
    print()
    popular_stations(city_file, time_period)
    print()
    popular_trip(city_file,time_period)
    print()
    users(city_file['User Type'],time_period)
    print()

    if(city!='washington'):                                   # if country is not equal to Washington then only Gender and Birth year will be displayed
        gender(city_file['Gender'],time_period)
        print()
        birth_years(city_file['Birth Year'],time_period)
        print()

    print("That took %s seconds." % (time.time() - s_time))
    display_data(city_file)

if __name__ == "__main__":
    statistics()
