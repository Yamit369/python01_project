from mailbox import linesep


MAX_LINES = 3 #CONSTANTVALUE AND GLOBAL #
MAX_BET = 100
MIN_BET = 1

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