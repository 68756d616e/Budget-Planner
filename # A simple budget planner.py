# A simple budget planner

while True:
    
    # Initial question
    budget = float(input("How much would you like your budget to be?"))

    # Define income and expenses
    expenses = float(input("What are your expenses?"))

    # Check if budget is over, under or equal
    if expenses > budget:
        print("Your budget is over by", expenses - budget)
    elif expenses == budget:
        print("Both your expenses and budget are equal")
    else:
        print("Your budget is in line, with a remaining", budget - expenses)
