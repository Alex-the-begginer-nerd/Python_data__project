import random
def spin_row():
    symbols = ['❤', '🍒', '🍉', '💎']

    return [random.choice(symbols) for symbol in range(3)]

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '💸':
            return bet * 2 
        if row[0] == '🍒':
            return bet * 3
        if row[0] == '🍉':
            return bet * 5
        if row[0] == '💎':
            return bet * 10
        if row[0] == '❤':
            return bet * 50
    return 0

def print_row(row):
    print(' | '.join(row))

def main():
    balance = 100
    print('***************************')
    print('Welcome to pyslots!')
    print('symbols:  💸 🍒 🍉 💎, ❤')
    print('***************************')

    while balance > 0:
        print(f'Current balance ${balance}')
        bet = (input('Select your bet: '))
    
        if not bet.isdigit():
            print('invalid input')
            continue
        bet = float(bet)
 
        if bet > balance:
            print('Insuffisient balance')
            continue

        if bet <= 0:
            print('Bet should be greater than zero')
        
        balance -= bet

        row = spin_row()
        print('Spinning...\n')
        print_row(row)

        payout = get_payout(row, bet)
        balance += payout
        if payout > 0:
            print(f'You won ${payout}!')
        else:
            print('Sorry you lost.')

        play_again = input('Do you want to spin again? (Y/N)').upper()
        if not play_again == 'Y':
            break

    print(f'GAME OVER! YOUR FINAL BALANCE IS ${balance}')


        



if __name__ in '__main__':
    main()
