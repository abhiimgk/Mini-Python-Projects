print("Welcome to XYZ Bank\nTo proceed further please insert your card.")
total_amount=500000
pin=4545
chances=3
while chances>0:
    user_pin=int(input("Enter your 4 digit pin: "))
    if user_pin==pin:
        a=input("Please choose the services:\n1.Cash Withdrawl 2.Balance Enquiry 3.Deposit: ")
        if a=="1":
            debit_amount=int(input("Please enter your amount: "))
            if debit_amount<total_amount:
                print(f'Amount of Rs{debit_amount} debited from your account')
                total_amount=total_amount-debit_amount
                print(f'Amount left now Rs{total_amount}')
                print("Thank you for using our Bank!\nFor further Servcies please Re-insert your card")
            else:
                print("Insufficient Funds\nFor further Servcies please Re-insert your card")
            break
        elif a=="2":
            print(f'Balance in your account is Rs{total_amount}')
            print("Thank you for using our Bank!\nFor further Servcies please Re-insert your card")
            break
        elif a=="3":
            amount_cred=int(input('enter the amount for deposit: '))
            total_amount=total_amount+amount_cred
            print(f'Amount present now is Rs{total_amount}')
            print("Thank you for using our Bank!\nFor further Servcies please Re-insert your card")
            break
    else:
        if chances>1:
            print(f"Invalid pin,{chances-1} chances left")
        else:
            print("You lost your all chances, please try after 24 hours, Thank You!")
        chances=chances-1
    

        