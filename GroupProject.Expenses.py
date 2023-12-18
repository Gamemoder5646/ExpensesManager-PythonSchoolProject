import math
from func import addExpenses, exportExpenses, viewExpenses, statsExpenses
#expenses = {day: {week: {month: {category: amount}}}}

while True:
    command = input("Welcome to the expenses. Please type what would you like to do.\n Type 'Add' to add an expense.\n Type 'Period' to start viewing the expenses in a period.\n Type 'Statistics' to recieve the top 5 categories.\n : ")
    if command.lower() == "add":
        addExpenses()
    elif command.lower() == "period":
        exportExpenses(viewExpenses())
    elif command.lower() == "statistics":
        exportExpenses(statsExpenses())
    else:
        print("Error, please try typing the command again.")
