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

symbol_value = {
    "A":  5,
    "B":  4,
    "C":  3,
    "D":  2
}


def check_winnings(columns, lines, bet, values):
    winnings  =  0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns: 
            symbol_to_check  =  column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(lines  + 1)

    return  winnings, winning_lines



def get_slotmachine_spin(rows, cols, symbol):
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


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i,  column in enumerate(columns):
            if i  != len(columns) -1:
                print(column[row], end=" | ") #separation of the item
            else:
                print(column[row], end="") 

        print()


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


def  sping(balance):
    lines = get_num_of_lines()
    while True:
        bet =  get_bet()
        total_bet = bet * lines

        if total_bet  > balance:
            print(f"You do not have enought to  bet that amount, your current balance is: ${balance}")
        else:
            break

    
    print(f"you are betting ${bet} on {lines} lines. Total bet is equal to:${total_bet} ")



    slots =  get_slotmachine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winnings_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}")
    print(f"You won on lines: ",  *winnings_lines)

    return  winnings - total_bet
    



def main():

    balance = deposit()
    while True:
        print(f"Current balanceis ${balance}")
        answer = input("Press enter to Play (q to quit).")
        if answer == "q":
            break
        balance += sping(balance)


    print(f"You left with ${balance}")
    
main()