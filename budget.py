#WELCOME TO BUDGET TRACKER

Category = None
Expense = 0
Income = 0

thedict = {
    'Kareem':10,
    'Soi':14
}

def addIncome():
    global Income
    
    while True:
        try:  
            forNowIncome = input('enter the amount of income: ')
            Income += float(forNowIncome)
            print(f'income of {Income} added successfully!')
            break
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            addIncome()

    test()

def addExpense():
    global Category
    global Expense
    
    while True:
        try:
            Category = input('Enter the expense category (e.g.  grocries, rent): ')
            
            if Category.isalpha():  # Check if the string contains only alphabetic characters
                break
            else:
                print("to value error")               
        except ValueError:
            print("Invalid input! Please enter a string with only letters.")
            #Category = input('Enter the expense category (e.g.  grocries, rent): ')  
    
    
    while True:
        try:
            forNowExpence = input('Enter the expense amount: ')
            Expense = float(forNowExpence)
            break
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    
    print(f'expense of {Expense} added to {Category}')
    
    thedict.update({Category: Expense})
    print(thedict)
    
    test()
    
def summary():
    print('\n\n ---- budget summary -----')
    print(f'Total income: {Income}')
    print(f'total expenses: {Expense}')
    print('\n--Expense by category--')
    for x, y in thedict.items():
        print(f'{x}: {y}')
        
    spent = sum(thedict.values())
    
    dif = spent - Income
    
    if spent >  Income:   
        print(f'you are spending {dif} over the budget')
    else:
        print()
            
    test()
    
def test():
    print('\n\n ---- Personal Budget Tracker ----')
    print('1.Add Income')
    print('2.Add Expense')
    print('3.View Summary')
    print('4.Exit')
    
    while True:
        try:  
            forNowOptions = input('Enter your choice (1-4): ')
            options = int(forNowOptions)
            break
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    if options == 1 :
        addIncome()
    elif options == 2 :
        addExpense()
    elif options == 3 :
        summary()
    elif options == 4 :
        print('Exiting program, Goodbye')
    else:
        print('\ninvalid option')
        test()              
    
test()