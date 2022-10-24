MAX_LINES = 3 #CONSTANTVALUE AND GLOBAL #

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
                print("Amount must be greater than 0.")
        else:
            print("Pleaseenter a number ")

    return amount



def main():

    balance = deposit()

main()