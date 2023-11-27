import math
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
        week = math.ceil(day/7)
        Lever = False
        category = input("Please enter the category of expenses: ")
        for i in range(len(expenses)):
            if day in expenses[i]:
                if category in expenses[i][day][week][month]:
                    expenses[i][day][week][month][category] += amount
                    Lever = True
                    print(f"The category {category} is already in the record, the amount was added to the total.")
                    break
                else:
                    expenses[i][day][week][month][category] = amount
                    Lever = True
                    print(f"1Added to the record.")
                    break
            elif day not in expenses[i]:
            else:
                break
        if Lever != True:
            expenses.append({day: {week: {month: {category: amount}}}})
            print(f"2Added to the record.")
    def viewExpenses():
        output = ""
        pick = input("select the period of expenses: Day, Week, Month\nWrite 'Exit' to select other operations: ")
        if pick == "Day":
            Day = (input("please enter the day. DD.MM: "))
            day_list = Day.split('.')
            day = int(day_list[0])
            month = int(day_list[1])
            week = math.ceil(day / 7)
            for i in range(len(expenses)):
                if day in expenses[i]:
                    if month in expenses[i][day][week]:
                        total_amount = math.fsum(expenses[i][day][week][month].values())
                        output += f"Total expenses: {total_amount}"
                        for j in expenses[i][day][week][month]:
                            percentage = (expenses[i][day][week][month][j]/total_amount)*100
                            output += f"\n{j}: {percentage}% "
                    else:
                        print(f"No such day of month found in records. (you typed {Day}) ")
                        break
                else:
                    break
            print(f"Data exported in file.")
        elif pick == "Week":
            Week = (input("please enter the week. WW.MM: "))
            week_list = Week.split('.')
            week = int(week_list[0])
            month = int(week_list[1])
            amount_dict = {}
            total_amount = 0
            for i in range(len(expenses)):
                for day in expenses[i]:
                    if week in expenses[i][day]:
                        if month in expenses[i][day][week]:
                            for h in expenses[i][day][week][month].keys():
                                if h in amount_dict.keys():
                                    amount_dict[h] += expenses[i][day][week][month][h]
                                else:
                                    amount_dict[h] = expenses[i][day][week][month][h]
                        else:
                            print(f"No such month was found in records. (you typed {month}) ")
                            break
                    else:
                        print(f"No such week was found in records. (you typed {week}) ")
                        break
            for g in amount_dict.values():
                total_amount += g
            output += f"Total expenses: {total_amount}"
            for l in amount_dict.keys():
                percentage = (amount_dict[l]/total_amount)*100
                output += f"{l}: {percentage}%"
            print(f"data added")
            return output
        elif pick == "Month":
            amount_dict = {}
            total_amount = 0
            month = int(input("please enter the month. MM: "))
            for i in range(len(expenses)):
                for day in expenses[i]:
                    for week in expenses[i][day]:
                        if month in expenses[i][day][week].keys():
                            for category in expenses[i][day][week][month]:
                                if category in amount_dict.keys():
                                    amount_dict[category] += expenses[i][day][week][month][category]
                                else:
                                    amount_dict[category] = expenses[i][day][week][month][category]
                        else:
                            break
            for g in amount_dict.values():
                total_amount += g
            output += f"Total expenses: {total_amount}"
            for l in amount_dict.keys():
                percentage = (amount_dict[l] / total_amount) * 100
                output += f"{l}: {percentage}%"
            print(f"Data exported in file.")
        else:
            print("Error, please try again. ")
            return "Error"
        return output
    def statsExpenses():
        output = ""
        amount_dict = {}
        total_amount = 0
        for i in range(len(expenses)):
            for day in expenses[i]:
                for week in expenses[i][day]:
                    for month in expenses[i][day][week]:
                        for category in expenses[i][day][week][month]:
                            if category in amount_dict:
                                amount_dict[category] += expenses[i][day][week][month][category]
                                print(f"{category}: {amount_dict[category]}")
                            else:
                                amount_dict[category] = expenses[i][day][week][month][category]
                                print(f"{category}: {amount_dict[category]}")
        for g in amount_dict.values():
            total_amount += g
        compare_list = list(amount_dict.items())
        compare_list.sort()
        top = total_amount
        i = 0
        output += f"Place #1: {compare_list[0][0]} - {compare_list[0][1]}"
        compare_list.remove(compare_list[0])
        while i < 4:
            for k in range(len(compare_list)):
                i += 1
                if compare_list[k][1] < top:
                    output += f"Place #{i+1} - {compare_list[k][0]} = {compare_list[k][1]}"
                    top = compare_list[k][1]
                else:
                    output += f"Place #{i+1} - "
        #print(f"Balls<3.") # horny programmer!!!!!!!!
        return output
    def exportExpenses(e): #optional!!!
        file = open("C:\Expenses\expenses.txt", 'w')
        file.write(e)
    if command == "Add":
        addExpenses()
    elif command == "Period":
        exportExpenses(viewExpenses())
    elif command == "Statistics":
        exportExpenses(statsExpenses())
    else:
        print("Error, please try typing the command again.")
