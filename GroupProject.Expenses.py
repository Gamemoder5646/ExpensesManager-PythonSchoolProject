
amount = 0
day = {}
wek = {}
#expenses = {"month": ["week", "day", {"category": "amount"}]}
expenses = {11: [2, 9, {"b": 100}]}
while True:
    command = input("Welcome to the expenses. Please type what would you like to do.\n Type 'Add' to add an expense.\n Type 'Period' to start viewing the expenses in a period.\n Type 'Statistics' to recieve the top 5 categories.\n : ")
    def addExpenses():
        amount = int(input("Please input the amount: "))
        date = input("Please enter the date. DD.MM format: ")
        date_list = date.split('.')
        if int(date_list[0]) <= 7:
            week = 1
        elif int(date_list[0]) <= 14 and int(date_list[0]) >= 7:
            week = 2
        elif int(date_list[0]) <= 21 and int(date_list[0]) >= 14:
            week = 3
        elif int(date_list[0]) >= 21:
            week = 4
        category = input("Please enter the category of expenses: ")
        cat = {category: amount}
        day[int(date_list[0])] = cat
        wek[week] = day
        #month = {date_list[1], week}
        expenses[int(date_list[1])] = wek
        # if expenses[date_list[1]] in expenses:
        #     print(1)
            # expenses.pop(expenses.index(date_list[1]))
            # expenses.append({date_list[1]: [week, date_list[0], {category: amount}]})
        # else:
        #     print(0)
            # expenses.append({date_list[1]: [week, date_list[0], {category: amount}]})
    def viewExpenses():
        Day = input("please enter the day: ")
        Week = input("please enter the week: ")
        Month = input("please enter the month: ")


    def statsExpenses():
        print("empty, fuck you :P")
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