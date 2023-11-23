import math
import time
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
        category = input("Please enter the category of expenses: ")
        for i in range(len(expenses)):
            if day in expenses[i]:
                #print(i)
                if category in expenses[i][day][week][month]:
                    #print(1)
                    expenses[i][day][week][month][category] += amount
                    print(f"Day {day} ")
                else:
                    expenses[i][day][week][month][category] = amount
                    break
            elif day not in expenses[i]:
                expenses.append({day: {week: {month: {category: amount}}}})
                break
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
                        print(f"No such day of month found in records. (you typed {Day}) ")
                        break
                break
            elif pick == "Week":
                Week = (input("please enter the week. WW.MM: "))
                week_list = Week.split('.')
                week = int(week_list[0])
                month = int(week_list[1])
                amount_dict = {}
                total_amount = 0
                for i in range(len(expenses)):
                    #print(f"list index: {i}")
                    for day in expenses[i]:
                        #print(f"Day: {j}")
                        if week in expenses[i][day]:
                            #print(f"Week: {True}")
                            if month in expenses[i][day][week]:
                                #print(f"Month: {True}")
                                for h in expenses[i][day][week][month].keys():
                                    #print(h)
                                    if h in amount_dict.keys():
                                        amount_dict[h] += expenses[i][day][week][month][h]
                                    else:
                                        amount_dict[h] = expenses[i][day][week][month][h]
                            else:
                                #print(False)
                                print(f"No such month was found in records. (you typed {month}) ")
                                break
                        else:
                            #print(False)
                            print(f"No such week was found in records. (you typed {week}) ")
                            break
                #print(amount_dict)
                for g in amount_dict.values():
                    total_amount += g
                print(f"Total expenses: {total_amount}")
                for l in amount_dict.keys():
                    percentage = (amount_dict[l]/total_amount)*100
                    print(f"{l}: {percentage}%")
                break
                #total_amount = math.fsum(amount_list)
                #percentage =
            elif pick == "Month":
                amount_dict = {}
                total_amount = 0
                month = int(input("please enter the month. MM: "))
                for i in range(len(expenses)):
                    #print(f"list index: {i}")
                    for day in expenses[i]:
                        #print(f"day: {j}")
                        for week in expenses[i][day]:
                            #print(f"week: {k}")
                            if month in expenses[i][day][week].keys():
                                #print(f"Month: {True}")
                                for category in expenses[i][day][week][month]:
                                    #print(k)
                                    if category in amount_dict.keys():
                                        amount_dict[category] += expenses[i][day][week][month][category]
                                    else:
                                        amount_dict[category] = expenses[i][day][week][month][category]
                            else:
                                #print(False)
                                break
               # print(amount_dict)
                for g in amount_dict.values():
                    total_amount += g
                print(f"Total expenses: {total_amount}")
                for l in amount_dict.keys():
                    percentage = (amount_dict[l] / total_amount) * 100
                    print(f"{l}: {percentage}%")
                break
            else:
                print("Error, please try typing again")
    def statsExpenses():
        amount_dict = {}
        total_amount = 0
        for i in range(len(expenses)):
            #print(f"list index: {i}")
            for day in expenses[i]:
                #print(f"day: {day}")
                for week in expenses[i][day]:
                    #print(f"week: {week}")
                    for month in expenses[i][day][week]:
                        #print(f"month: {month}")
                        for category in expenses[i][day][week][month]:
                            #print(f"amount: {expenses[i][day][week][month][category]}")
                            if category in amount_dict:
                                amount_dict[category] += expenses[i][day][week][month][category]
                            else:
                                amount_dict[category] = expenses[i][day][week][month][category]
       # print(amount_dict)
        for g in amount_dict.values():
            total_amount += g
        #print(f"Total expenses: {total_amount}")
        for l in amount_dict.keys():
            percentage = round((amount_dict[l] / total_amount)) * 100
            amount_dict[l] = percentage
            #print(f"{l}: {percentage}%")
        compare_list = list(amount_dict.items())
        compare_list.sort()
        #print(compare_list)
        top = compare_list[0][1]
        print(f"Place №1: {compare_list[0][0]} - {compare_list[0][1]}")
        for i in range(5):
            for k in range(len(compare_list)):
                if compare_list[k][1] < top:
                    print(f"Place №{i+1}: {compare_list[k][0]} - {compare_list[k][1]}")
                    top = compare_list[k][1]
                else:
                    print(f"Place №{i+1}: ")
                    break

        # print("empty :P")
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
