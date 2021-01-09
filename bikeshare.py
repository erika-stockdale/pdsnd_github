import time
import pandas as pd
import numpy as np

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
# Prompt user to enter a valid city of interest (chicago, new york city, washington) and display error if unexpected value entered.

    while True:
        city = input("Would you like to view data from Chicago, New York City or Washington? Type the name of your desired city:\n").lower() # converts input to lower case
        if city.lower() not in ("chicago", "new york city", "washington"):

        # Validation error displayed if user enters an unexpected city or integer
            print("That's not a valid city. Enter Chicago, New York City or Washington.\n").lower() # converts input to lower case
            continue #enables user a second chance to enter valid data
        else:
    # Provide user with success message verifying the selection
            print("That's great, we'll prepare data for ", city)
            break # exit the loop once user submits a valid city

    # Prompt user to confirm if he/she wants to view data for a specific single month or all available data and display error message for invalid input

    while True:
        month = input("Would you like to view data for a specific month between January and June? If so, type the month's name; otherwise, type All to view data for all months:\n").lower() # converts input to lower case

    # converts input to lower case and validates against available months
        if month.lower() not in ("january", "february", "march", "april", "may", "june", "all"):

        # error message reminding user of required formatting and available data and enabling opportunity for correction and progression
            print("This data isn't available or you have entered a number. Please type the name of a month between January and June, or type All to view all data\n").lower()
            continue
        else:
        # provide user with message of success and validation of entered data
                print("No problem, we'll retrieve data for: ", month)
                break # exit the loop once user submits valid month filter

# Prompt user to confirm if he/she wants to view data for a specific day of the week or all available days and display error message for invalid input
    while True:
         day = input("Do you want to view data for a specific day of the week? If so, type the day; if not, type All:\n").lower() # converts input to lower case
         if day.lower() not in ("monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "all"):

        # error message displayed if invalid data entered that also reminds user of required format and allows an opportunity for correction and progression
             print("Oops, there's a problem. Please type the day you want in full e.g. Monday, or type All:\n").lower() # converts input to lower case
             continue
         else:
            print("Perfect, we'll retrieve data for: ", day)
            break # exit the loop once user submits valid day filter

    return city, month, day # stores user filter selections for later use

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

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month, if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding integer
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

        #filter by day of week, if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df # stores dataframe output for later use

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # identify the most common month in which journeys started using pandas
    #convert Start Time to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month from Start Time
    df['month'] = df['Start Time'].dt.month

    # compute most common month
    popular_month = df['month'].mode()[0]

    # display the most common month
    print('Most Popular Month:', popular_month)

    # identify the most common day of week for starting journeys using pandas
    # extract day of week from Start Time
    df['day'] = df['Start Time'].dt.dayofweek

    # compute the most common day of week
    popular_day = df['day'].mode()[0]

    # display the most common day of week
    print('Most Popular Day: ', popular_day)

    # identify the most common start hour using pandas
    # extract hour from the Start Time column
    df['hour'] = df['Start Time'].dt.hour

    # find the most popular hour
    popular_hour = df['hour'].mode()[0]

    print('Most Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # identify the most commonly used start station using pandas
    popular_start_station = df['Start Station'].mode()[0]

    # identify the most commonly used end station
    popular_end_station = df['End Station'].mode()[0]

    # TO DO: display most frequent combination of start station and end station trip
    print("\nMost popular Start Station: '{}'. \nMost populart End Station: '{}'.'.".format(popular_start_station, popular_end_station))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # calculate total travel time using pandas
    total_travel_time = df['Trip Duration'].sum

    # calculate mean travel time
    average_travel_time = df['Trip Duration'].mean

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Calculate counts of user types
    user_types = df['User Type'].value_counts()


    # Calculate counts of gender
    try:
        df['Gender'] is not None # to avoid key errors caused by missing data
        gender_totals = df['Gender'].value_counts()
    except:
        print("\nSorry, gender statistics were not collected for Washington.\n")

    # Calculate earliest, most recent, and most common year of birth
    try:
        df['Birth Year'] is not None # to avoid key errors caused by missing data
        earliest = df['Birth Year'].min()
        most_recent = df['Birth Year'].max()
        most_common = df['Birth Year'].mode()[0]
        print("\nEarliest birth year: '{}'. \nMost recent birth year: '{}'. \nMost common birth year: '{}'.".format(earliest, most_recent, most_common))
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
    except:
        print("\nSorry, birth date statistics were not colleced for Washington.\n")


def main():
        while True:
            city, month, day = get_filters()
            df = load_data(city, month, day)

            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)

            i = 0
            view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower() # converts user input into lower case
            while True:
                if view_data == 'no':
                    break
                print (df.iloc[i:i+5])
                view_data= input('\nWould you like to see the next 5 rows of data?\n').lower()
                i += 5

            restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
            if restart.lower() != 'yes':
                break

if __name__ == "__main__":
	    main()
