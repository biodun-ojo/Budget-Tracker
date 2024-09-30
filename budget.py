#WELCOME TO BUDGET TRACKER

"""
Features


Track Income & Expenses:

Allow users to input income and categorize expenses (e.g., rent, groceries, utilities, etc.).
Store these as variables and update them regularly.


Use Data Types & Variables:

Use appropriate data types for different inputs (e.g., floats for income/expenses, strings for categories).


Conditionals:

Ensure budget limits are not exceeded and warn users if they are spending too much in certain categories.
Offer a comparison if monthly spending exceeds income.


Functions:

Create modular functions for adding income, recording expenses, and viewing a summary of finances.
Use built-in functions like sum() for total spending.


Lists, Dictionaries, Tuples:

Store transactions using a dictionary (category as key, amount as value).
Keep track of past expenses with a list, where each is a tuple (category, amount, date).


Exceptions:

Handle errors gracefully, such as invalid input types (e.g., entering a string when a number is expected).
"""

Category = None
Expense = 0
Income = 0


thedict = {
    'bobo':10,
    'me':100
}


def addIncome():
    global Income
    
    Income += float(input('enter the amount of income: '))
    print(f'income of {Income} added successfully!')

    test()

    
def addExpense():
    global Category
    global Expense
    
    Category = input('Enter the expense category (e.g.  grocries, rent): ')
    Expense = float(input('enter the expense amount: '))
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
    options = int(input('Enter your choice (1-4): '))
    
    if options == 1 :
        addIncome()
    elif options == 2 :
        addExpense()
    elif options == 3 :
        summary()
    elif options == 4 :
        print('Exiting program, Goodbye')
    else:
        test()        
    
test()