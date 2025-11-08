'''Make the following changes to the sitka_highs.py program:
    Open the program with instructions on how to use the menu; Highs, Lows, or Exit.
    When the program starts, allow the user to select whether they want to see the high temperatures or the low temperatures, or to exit.
    When the user selects 'lows', they should see a graph, in blue, that reflects the lows for those dates.
        Allow the program to loop until the user selects exit.
    When the user exits, provide an exit message.
    Use what elements you can from previous programs, perhaps including sys to help the exit process.
    Document all your changes, and save as sitka_high_low_"<your initials>".py. Ex. sitka_high_low_mss.py to your module-4 directory.
    Open up your initial flowchart and revise it to reflect the changes made to the program. Take a screenshot and add it to your Word document, and save to your module-4 directory.'''


import csv
import sys #ADDED: for exit
from datetime import datetime

from matplotlib import pyplot as plt

filename = 'sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates and high temperatures from this file. (ADDED Lows)
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)
        high = int(row[5])
        highs.append(high)
        low = int(row[6])           # ADDED: lows
        lows.append(low)

#ADDED: Loop to keep program running until user exits.
while True:

    #ADDED: Menu for user to select whether they want to see highs, lows, or exit.
    while True:
        print("\nSelect 'highs', 'lows', or 'exit'.")
        selection = input("> ").strip().lower()

        if selection == 'highs':
            plot_highs = True
            break
        elif selection == 'lows':
            plot_highs = False
            break
        elif selection == 'exit':
            print("Exiting program. Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice. Please type 'highs', 'lows', or 'exit'.")

    #Plot the temperatures.
    #plt.style.use('seaborn')
    fig, ax = plt.subplots()

    #ADDED: if/else statement to plot highs or lows.
    if plot_highs:
        ax.plot(dates, highs, c='red')
    else:
        ax.plot(dates, lows, c='blue')

    # Format plot.

    #ADDED: if/else statement to change title for highs or lows.
    if plot_highs:
        plt.title("Daily high temperatures - 2018", fontsize=24)
    else:
        plt.title("Daily low temperatures - 2018", fontsize=24)

    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()