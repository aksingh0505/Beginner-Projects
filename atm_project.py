balance=10000.00
def atm_menu():
    print('\n===ATM===')
    print('1. Check Balance')
    print('2. Deposit Money')
    print('3. Withdraw Money')
    print('4. Exit')
while True:
    atm_menu()
    choice=input('Choose an option(1-4): ')

    if choice=='1':
        print(f'Your Balance is ${balance:.2f}')
    

    elif choice=='2':
        try:
            amt=float(input('Enter the amount $. '))
            if amt <=0:
                print('Enter positive value')
            else:
                balance += amt
                print(f'${amt:.2f} deposited successfully.')
        except ValueError:
            print('Invalid input. Please enter a number.')

    elif choice == '3':
        try:
            amt = float(input('Enter the withdrawal amount $: '))
            if amt <= 0:
                print('Insufficient Balance')
            else:
                balance -= amt
                print(f'${amt:.2f} withdrawn amount')
        except ValueError:
            print('Invalid input. Please enter a number.')
        
    elif choice == '4':
        print('Thank You For Using the ATM')
        break

    else:
        print('enter a valid option')
