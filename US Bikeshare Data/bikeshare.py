import time
import pandas as pd

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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Choose one of these cities (Chicago, New York City, Washington): ").lower()
        if city in ["chicago", "new york city", "washington"]:
            break
        else:
            print("Please make sure to choose one of these cities (Chicago, New York City, Washington)\n(Don't use any non-alphabetical characters except whitespace.).")

    # get user input for month (january, february, ... , june)
    while True:
        filter_month = input("Do you want to filter the results to a specific month? (Enter 'yes'(or 'y') or 'no'(or 'n')): ")
        if filter_month.lower() == "yes" or filter_month.lower() == "y":
            while True:
                # keep prompting the user until a valid answer is given.
                month = input("Choose a month: ").lower()
                if month in ["january", "february", "march", "april", "may", "june"]:
                    break
                else:
                    print("Please make sure to enter a month name, and that it's without typos.")
            break
        elif filter_month.lower() == "no" or filter_month.lower() == "n":
            month = None
            break
        else:
            print("Please enter either 'yes'(or 'y') or 'no'(or 'n')")


    # get user input for day of week (monday, tuesday, ... sunday)
    while True:
        filter_day = input("Do you want to filter the results to a specific day? (Enter 'yes' or 'no'): ")
        if filter_day.lower() == "yes" or filter_day.lower() == "y":
            while True:
                # keep prompting the user until a valid answer is given.
                day = input("Choose a day: ").lower()
                if day in ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]:
                    break
                else:
                    print("Please make sure to enter a day name, and that it's without typos.")
            break
        elif filter_day.lower() == "no" or filter_day.lower() == "n":
            day = None
            break
        else:
            print("Please enter either 'yes'(or 'y') or 'no'(or 'n')")


    print('-'*40)
    return city, month, day


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
    df = pd.read_csv(CITY_DATA[city], parse_dates=["Start Time", "End Time"])
    df.drop(columns=["Unnamed: 0"], inplace=True)  # removes an unnecessary column.
    
    if month:
        month_filter = df["Start Time"].dt.month_name().str.lower() == month
        df = df[month_filter]
    
    if day:
        day_filter = df["Start Time"].dt.day_name().str.lower() == day
        df = df[day_filter]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_common_month = df["Start Time"].dt.month_name().mode()[0]
    print("Most common month:", most_common_month)

    # display the most common day of week
    most_common_day = df["Start Time"].dt.day_name().mode()[0]
    print("Most common day:", most_common_day)

    # display the most common start hour
    most_common_hour = df["Start Time"].dt.hour.mode()[0]
    print("Most common hour:", most_common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_used_start_station = df["Start Station"].mode()[0]
    print("Most commonly used start station:", most_used_start_station)


    # display most commonly used end station
    most_used_end_station = df["End Station"].mode()[0]
    print("Most commonly used end station:", most_used_end_station)


    # display most frequent combination of start station and end station trip
    most_used_start_end_station = (df["Start Station"] + " --> " + df["End Station"]).mode()[0]
    print("Most frequent combination of start station and end station:", most_used_start_end_station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df["Trip Duration"].sum()
    print("Total travel time:", total_travel_time)


    # display mean travel time
    mean_travel_time = df["Trip Duration"].mean()
    print("Mean travel time:", mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("User types and their counts:")
    zipped_user_counts = zip(df["User Type"].value_counts().index, df["User Type"].value_counts())
    user_counts = [user_type + " : " + str(_count) for user_type, _count in zipped_user_counts]
    for user_count in user_counts:
        print("\t" + user_count)


    # Display counts of gender
    print("\nUser's genders and their counts:")
    zipped_gender_counts = zip(df["Gender"].value_counts().index, df["Gender"].value_counts())
    gender_counts = [gender + " : " + str(_count) for gender, _count in zipped_gender_counts]
    for gender_count in gender_counts:
        print("\t" + gender_count)


    # Display earliest, most recent, and most common year of birth
    print("\nEarliest, most recent, and most common year of birth:")
    earliest_birthyear = df["Birth Year"].min()
    print("\tEarliest year of birth:", earliest_birthyear)
    
    most_recent_birthyear = df["Birth Year"].max()
    print("\tMost recent year of birth:", most_recent_birthyear)
    
    most_common_birthyear = df["Birth Year"].value_counts().index[0]
    print("\tMost common year of birth:", most_common_birthyear)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def show_raw_data(df):
    """Display 5 lines of raw data at a time depending on user's input."""
    
    shown_once = False
    last = 5  # a variable to keep track of which line the program stopped at the last time the lines were displayed.
    show_5_lines = input("Do you want to see 5 lines of raw data? Enter 'yes'(or 'y') or 'no'(or 'n').\n")
    
    while True:
        if show_5_lines == "no" or show_5_lines == "n":
            break    
        elif show_5_lines == "yes" or show_5_lines == "y":
            # check if lines were shown before, if they were,  show the next 5 lines, if not,  show the first 5 lines.
            if not shown_once:
                print(df.head())
                shown_once = True
                show_5_lines = input("Do you want to see 5 more lines of raw data? Enter 'yes'(or 'y') or 'no'(or 'n').\n")
            else:
                print(df.drop(index=df.index[:last]).head())
                last += 5
                show_5_lines = input("Do you want to see 5 more lines of raw data? Enter 'yes'(or 'y') or 'no'(or 'n').\n")
        else:
            print("Please enter either 'yes'(or 'y') or 'no'(or 'n').\n")
            show_5_lines = input("Do you want to see 5 more lines of raw data? Enter 'yes'(or 'y') or 'no'(or 'n').\n")


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        show_raw_data(df)

        while True:
            # keep prompting the user until a valid answer is given.
            restart = input("\nWould you like to restart? Enter 'yes'(or 'y') or 'no'(or 'n').\n")
            if restart.lower() == "yes" or restart.lower() == "y":
                break
            elif restart.lower() == "no" or restart.lower() == "n":
                return
            else:
                print("Please enter either 'yes'(or 'y') or 'no'(or 'n')")
                
                


if __name__ == "__main__":
	main()
