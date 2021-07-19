##################################################
###   Author      : Ahmed Gamal               ####
###   Description : Bikeshare system          ####
###   Date        : 17 july 2021              ####
###   Version     : v1                        ####
##################################################

###      Import Libraries                      ###
import tkinter                     ###  To Welcome GUI Banner
from tkinter import *              ###  To Welcome GUI Banner
from PIL import Image, ImageTk     ###  To insert image to welcome banner

import time
import pandas as pd
import numpy as np
###############################################################
###              Global Variabls                            ###
###############################################################

CITY_DATA = {'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv'}
### my Lists                                    ####
myCities = ['chicago','new york city','washington']
myMonths = ['all','january', 'february', 'march', 'april', 'may', 'june']
myDays   = ['all','sunday','monday','tuesday','wednesday','thursday','friday','saturday']

flag = 1                        ###    check flag
###############################################################
###          Creat tkinter GUI Welcome Banner            ######
###############################################################

root = tkinter.Tk()
root.title("Welcome to Bike Share Data Analysis System") 
root.geometry("600x400+100+100")

i=0
while i< 4:
    root.columnconfigure(i,minsize='10')
    i+=1
i=0
while i<4:
    root.rowconfigure(i,minsize='10')
    i+=1

label = tkinter.Label(root, text ="please click Enter to run on console")
label.grid(row = 4, column = 4)
btn1 = Button(root, text = 'Enter', bd = '5', command = root.destroy) 
btn1.grid(row = 5, column = 4)       

load= Image.open("BikeShare.jpg")
render = ImageTk.PhotoImage(load)
img = Label(root, image=render)
img.place(x=100, y=100)

#####################################################################
###      Functions Implementation                                 ###
#####################################################################

##### Get input frome user ,filter and validation ###################
def validate_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    ### Local variables      #####
    city_str    = "Would you like to see the data for chicago, new york city or washington?"
    month_str   = "Which Month (all, january, ...may, june)?"
    day_str     = "Which day you want? (all, monday, tuesday, ... sunday)?"
    city_error  = "the input city is wrong, try again"
    month_error = "the input month is wrong, try again"
    day_error   = "the input day is wrong try again"
    ####   Welcome Message  Printing banner    ####
    print("|**********************************************************|")
    print("| Welcome to Bikeshare system                              |")
    print("| You can choose city (chicago, new york city, washington) |")
    print("| You can choose day and month                             |")
    print("|**********************************************************|")
    print("\n\n")
    print('Hello! Let\'s explore some US bikeshare data!')
    ######    collection input and validation       ##############
    while flag == 1 :  ###   for infinit loop or using while True
    # get input from user
        city = input(city_str).lower()     ### lower() method for lower case
        if city in myCities:     ### input validation
            break
        else :
            print(city_error)
            
     # get input from user
            
    while flag == 1 :  ###   for infinit loop or using while True
        month = input(month_str).lower()   ### lower() method for lower case
        if month in myMonths :             ### input validation
            break
        else :
            print(month_error)
            
    # get input from user
            
    while flag == 1 :  ###   for infinit loop or using while True
        day = input(day_str).lower()   ### lower() method for lower case
        if day in myDays :             ### input validation
            break
        else :
            print(day_error)
            
    print('-'*70)   ####   print line  --------------------------------    ##### 
    return city , month, day
#########################  load Data function     ##############################################
def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month, day of week, hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month_name()    # to save the month by letter name
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        
        # filter by month to create the new dataframe
        df = df[df['month'] == month.title()]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df
####################    Time stats Function      ######################################
def statsofTime(df):
    ###   Displays statistics on the most frequent times of travel.  #####

    print('\nDisplays statistics on the most frequent times of travel.\n')
    print('-'*20)    ####   print line  --------------------------------    ##### 
    timeStart = time.time()                 ### time()  method
    ### print most common start hour
    most_common_start_hour = df['hour'].mode()[0]           ### mode method to find the most popular item
    print('The Common Most Start Hour:', most_common_start_hour)
    ### print most common day of week
    most_common_day_of_week = df['day_of_week'].mode()[0]   ### mode method to find the most popular item
    print('The Common Most Day Of Week:', most_common_day_of_week)
    ### print most common month
    most_common_month = df['month'].mode()[0]               ### mode method to find the most popular item
    print('The Common Most Popular Month:', most_common_month)
    #### render The Time Elapsed in seconds unit
    print("\n The Time Elapsed =  %s seconds." % (time.time() - timeStart))
    print('-'*70)                              ####   print line  --------------------------------    #####
##########################     Station Function            ##################################

def statsOfStation(df):
    print('\nDisplays statistics on the most popular stations and trip.\n')
    print('-'*20)    ####   print line  --------------------------------    ##### 
    start_time = time.time()

    #### render most most commonly used start station  ###
    Most_start_station = df['Start Station'].mode()[0]

    print('The Common Most Start Station:', Most_start_station)

    ### render most most commonly used end station   ####
    Most_end_station = df['End Station'].mode()[0]
    print('Most End Station:',  Most_end_station)

    # render most frequent combination of start station and end station trip    ###
    CellCombined=df.groupby(['Start Station','End Station'])   ###    for grouped combined   ###
    Most_grouped_station = CellCombined.size().sort_values(ascending=False).head(1)
    print('Most frequent combination of Start Station and End Station trip:\n', Most_grouped_station.to_frame())
        #### render The Time Elapsed in seconds unit   ####
    print("\nThe Elapsed Time =  %s seconds." % (time.time() - start_time))
    print('-'*70)

############################  Trip Function       ###############################################
def statsofTrip_duration(df):
    """Displays statistics on the total and average trip duration."""

    print('\nDisplays statistics on Trip Duration...\n')
    print('-'*20)    ####   print line  --------------------------------    ##### 
    start_time = time.time()

    ### render total travel time  ######
    overallTimeTravel = df['Trip Duration'].sum()

    print('Total Travel Time = ', overallTimeTravel)

    ### render mean travel time   ####
    avaredge_travel_time = df['Trip Duration'].mean()

    print('Mean Travel Time = ', avaredge_travel_time)
    ###   Time render in seconds unit  #####
    print("\nThe Time Elapsed =  %s seconds." % (time.time() - start_time))
    print('-'*70)    ####   print line  --------------------------------    ##### 

##########################   Stats user function      #################################################
def statsOfUser(df,city):    ### city for solve problem in washington
    """Displays statistics on bikeshare users."""

    print('\nDesplay User Stats...\n')
    print('-'*20)    ####   print line  --------------------------------    ##### 
    start_time = time.time()

    # Display counts of user types
    print('User Type Stats:')
    print('-'*20)    ####   print line  --------------------------------    ##### 
    print(df['User Type'].value_counts())
    if city != 'washington':         ###   washington  city     #####
        #### render counts of Gender   ######
        print('Stats of Gender :')
        print('-'*20)    ####   print line  -------------------------------  ##### 
        print(df['Gender'].value_counts())   ####  counts() method for counting 
        # Display earliest, most recent, and most common year of birth
        print('Stats of Birth Year:')
        print('-'*20)    ####   print line  --------------------------------    ##### 
        ####     most_common_year      #####
        most_common_year = df['Birth Year'].mode()[0]
        print('Most Common Year:',most_common_year)
        ####     most_recent _year      #####
        most_recent_year = df['Birth Year'].max()
        print('Most Recent Year:',most_recent_year)
        ####     most_Earliest_year      #####
        yearOf_earliest = df['Birth Year'].min()
        print('Earliest Year:',yearOf_earliest)
    ###   Time render in seconds unit  #####
    print("\nThe Time Elapsed =  %s seconds." % (time.time() - start_time))
    print('-'*70)    ####   print line  --------------------------------    ##### 
########################### new Raw input render according user   ##################################
def render_raw_data(city):
    print('\nRaw data is available to render... \n')
    print('-'*20)    ####   print line  --------------------------------    ##### 
    con_check = input('To View the availbale raw data in chuncks of 5 rows type: Yes or No if you don\'t want \n').lower()
    while con_check not in ('yes', 'no'):
        print('That\'s invalid input, please enter your selection again')
        print('-'*20)    ####   print line  --------------------------------    ##### 
        con_check = input('To View the availbale raw data in chuncks of 5 rows type: Yes or No if you don\'t want \n').lower()
    while con_check == 'yes':
        try:
            for i in pd.read_csv(CITY_DATA[city], index_col = 0 ,chunksize=5):
                print(i)
                con_check = input('To View the availbale raw in chuncks of 5 rows type: Yes\n').lower()
                if con_check == 'no':
                    print("Good Luck")
                    print('-'*20)    ####   print line  --------------------------------    #####
                    break
            break

        except KeyboardInterrupt:   ###   an Exception ERROR     #####
            print('Thank you.')
            print('-'*20)    ####   print line  --------------------------------    #####

############################################################
####        the main function                           ####
############################################################
def main():
    while True:
        city, month, day = validate_filters()
        ###  Validate Check 3 inputs from user    ###
        input_txt = "Your City input is {}, Month is {} and day is {} ."
        print('-'*70)   ####   print line  --------------------------------    ##### 
        print(input_txt.format(city,month, day))     ### Show what user inputs #####
        print('-'*70)   ####   print line  --------------------------------    ##### 
        print('-'*70)   ####   print line  --------------------------------    ##### 
        df = load_data(city, month, day)
        statsofTime(df)
        statsOfStation(df)
        statsofTrip_duration(df)
        statsOfUser(df,city)
        print('-'*70)   ####   print line  --------------------------------    ##### 
        print('-'*70)   ####   print line  --------------------------------    ##### 
        render_raw_data(city)
        ### for asking user  continue or Exit the system
        system_restart = input('\nWould you like to restart? Enter yes or no.\n').lower()  ### lower() method for lower case
        if system_restart == 'no':
            print('-'*70)   ####   print line  --------------------------------    ##### 
            print("We are sorry to leave our system, see you later, Best Regards")
            print("                      Good Luck                             ")
            print('-'*70)   ####   print line  --------------------------------    ##### 
            break
###############################################################
#####           To run the code                           #####
###############################################################
root.mainloop()       ####    to run GUI Welcome Bikeshare using Tkinter  
main()                ####    to run the Main Function
