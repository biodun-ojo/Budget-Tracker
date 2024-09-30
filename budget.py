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
category = input('\n Enter the expense category (e.g.  grocries, rent): ')
expense = float(input('enter the expense amount: '))

thedict = {
    'bobo':'hello',
    'me':'yins'
}

thedict.update({category: expense})

print(thedict)


def addIncome():
    income = float(input('enter the amount of income: '))
    print(f'income of {income} added successfully!')
    
    test()
    
def addExpense():
    category = input('Enter the expense category (e.g.  grocries, rent): ')
    expense = float(input('enter the expense amount: '))
    print(f'expense of {expense} added to {category}')
    
    test()
    
def summary():
    print('\n\n ---- budget summary -----')
    print('Total income: ?')
    print(f'total expenses: {expense}')
    print('\nExpense by category')
    for x, y in thedict.items():
        print(f'{x}: {y}')
    
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