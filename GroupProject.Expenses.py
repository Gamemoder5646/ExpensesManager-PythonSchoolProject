
#expenses = {day: {week: {month: {category: amount}}}}
expenses = [{8: {2: {11: {"b": 100}}}}, {9: {2: {11: {"b": 100}}}}]
while True:
    command = input("Welcome to the expenses. Please type what would you like to do.\n Type 'Add' to add an expense.\n Type 'Period' to start viewing the expenses in a period.\n Type 'Statistics' to recieve the top 5 categories.\n : ")
    def addExpenses():
        amount = int(input("Please input the amount: "))
        date = input("Please enter the date. DD.MM format: ")
        date_list = date.split('.')
        day = int(date_list[0])
        month = int(date_list[1])
        if int(date_list[0]) <= 7:
            week = 1
        elif int(date_list[0]) <= 14 and int(date_list[0]) >= 7:
            week = 2
        elif int(date_list[0]) <= 21 and int(date_list[0]) >= 14:
            week = 3
        elif int(date_list[0]) >= 21:
            week = 4
        category = input("Please enter the category of expenses: ")
        for i in range(len(expenses)):
            if day in expenses[i]:
                print(i)
                if category in expenses[i][day][week][month]:
                    expenses[i][day][week][month][category] += amount
                else:
                    expenses[i][day][week][month][category] = amount
            else:
                expenses.append([{day: {week: {month: {category: amount}}}}])
                break
    def viewExpenses():
        Day = input("please enter the day: ")
        Week = input("please enter the week: ")
        Month = input("please enter the month: ")


    def statsExpenses():
        print("empty :P")
    def exportExpenses(): #optional!!!
        file = open("C:\Expenses\expenses.txt", 'w')
        file.write(str(expenses))
    if command == "Add":
        addExpenses()
    elif command == "Period":
        viewExpenses()
    elif command == "Statistics":
        statsExpenses()
    else:
        print("Error! Please try again")


    exportExpenses()
