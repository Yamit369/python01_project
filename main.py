from mailbox import linesep
import random 

MAX_LINES = 3 #CONSTANTVALUE AND GLOBAL #
MAX_BET = 100
MIN_BET = 1


#FOR THE CREATION OF THE MACHINE WHEN CREATING THIS EXERCISE
ROWS = 3
COLS =  3

symbol_count = {
    "A":  2,
    "B":  4,
    "C":  6,
    "D":   8
}


def get_slotmachine_spin(rows, cols, symbols):
    all_symbols =  []
    for symbol, symbol_count in symbol.items(): #WHEN USING SYMBOL.ITEMS WE ARE SAYING TOGET THE KEY  AND THE VALUE OF THAT KEY#
        for _ in range(symbol_count): # IN PYTHON THE _ IS A ANONYMUS VARIABLE THATIS USE WHENWE DONOT CARE THE ITERATIONS 
            all_symbols.append(symbol) #whit this we areensuring to count twice the count of the symbol 
    
    columns = []  #here westructurint the columns not the rows
    for _ in range(cols):
        column = [] #BELOW THIS CODE WE NEED TOMAKE A LIST THAT REMOVES THEVALUES THAT WERE ALREADY USE SO WE NEED TOMAKE A COPY
        current_symbols = all_symbols [:] #SLICE OPERATOR COPY
        for  _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def deposit():
    while True:
        amount = input(" What would you like to  deposit $")
        if amount.isdigit():
            amount = int(amount)
            if  amount > 0: 
                break 
            else:
                print("Amount must be greater than 0.")
        else:
            print("Pleaseenter a number ")

    return amount

def get_num_of_lines():

     while True:
        lines = input("Enter thenumber of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if  1 <= lines <=  MAX_LINES:  #OTHER WAY ON WRITTING VALUES #
                break 
            else:
                print("Please enter the valid numberof lines  ")
        else:
            print("Pleaseenter a number ")

     return lines 


def get_bet():
    while True:
        amount = input(" What would you like to  bet on each line $")
        if amount.isdigit():
            amount = int(amount)
            if  MIN_BET <= amount <= MAX_BET : 
                break 
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Pleaseenter a number ")

    return amount




def main():

    balance = deposit()
    lines = get_num_of_lines()
    while True:
        bet =  get_bet()
        total_bet = bet * lines

        if total_bet  > balance:
            print(f"You do not have enought to  bet that amount, your current balance is: ${balance}")
        else:
            break

    
    print(f"you are betting ${bet} on {lines} lines. Total bet is equal to:${total_bet} ")
    

main()