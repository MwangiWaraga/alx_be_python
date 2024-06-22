income = int(input("Enter your monthly income: "))
expenses = int(input("Enter your total monthly expenses: "))
savings = income - expenses
print("Your montly savings are " + "$" + str(savings) + ".")
print("Projected savings after one year, with interest, is: " + "$" + str(int(savings * 12 + (savings * 12 * 0.05))) + ".")