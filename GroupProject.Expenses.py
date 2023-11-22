import math
#expenses = {day: {week: {month: {category: amount}}}}
expenses = [{8: {2: {11: {"b": 100}}}}, {9: {2: {11: {"b": 100}}}}]
while True:
    command = input("Welcome to the expenses. Please type what would you like to do.\n Type 'Add' to add an expense.\n Type 'Period' to start viewing the expenses in a period.\n Type 'Statistics' to recieve the top 5 categories.\n : ")
    def addExpenses():
        lever = False
        amount = int(input("Please input the amount: "))
        date = input("Please enter the date. DD.MM format: ")
        date_list = date.split('.')
        day = int(date_list[0])
        month = int(date_list[1])
        week = math.ceil(day/7)
        category = input("Please enter the category of expenses: ")
        for i in range(len(expenses)):
            if day in expenses[i]:
                lever = True
                #print(i)
                if category in expenses[i][day][week][month]:
                    #print(1)
                    expenses[i][day][week][month][category] += amount
                else:
                    expenses[i][day][week][month][category] = amount
            elif lever == False:
                expenses.append({day: {week: {month: {category: amount}}}})
            else:
                #print(0)
                break

    def viewExpenses():
        while True:
            pick = input("select the period of expenses: Day, Week, Month: ")
            if pick == "Day":
                Day = (input("please enter the day. DD.MM: "))
                day_list = Day.split('.')
                day = int(day_list[0])
                month = int(day_list[1])
                week = math.ceil(day / 7)
                for i in range(len(expenses)):
                    if day in expenses[i]:
                        #print(i)
                        if month in expenses[i][day][week]:
                            total_amount = math.fsum(expenses[i][day][week][month].values())
                            print(f"Total expenses: {total_amount}.")
                            for j in expenses[i][day][week][month]:
                                percentage = (expenses[i][day][week][month][j]/total_amount)*100
                                print(f"{j}: {percentage}%")
                            #print(f""expenses[i][day][week][month])
                    else:
                        break
                break

            elif pick == "Week":
                Week = (input("please enter the week. WW.MM: "))
                week_list = Week.split('.')
                week = int(week_list[0])
                month = int(week_list[1])
                for i in range(len(expenses)):
                    print(f"list index: {i}")
                    for j in expenses[i]:
                        print(f"Day: {j}")
                        if week in expenses[i][j]:
                            print(f"Week: {True}")
                            if month in expenses[i][j][week]:
                                print(f"Month: {True}")
                                for h in expenses[i][j][week][month].values():
                                    print(f"amount: {h}")
                            else:
                                print(False)
                                break
                        else:
                            print(False)
                            break

            elif pick == "Month":
                Month = int(input("please enter the month. MM: "))
            else:
                print("Error, please try typing again")


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
