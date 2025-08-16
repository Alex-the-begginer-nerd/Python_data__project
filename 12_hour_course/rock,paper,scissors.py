import random
options = ('rock', 'paper', 'scissors')
running = True
while running:
    computer = random.choice(options)
    player = input('Enter a choice (rock, paper, scissors): ').lower()

    while player not in options:
        print('ERROR: invalid input')
        player = input('Enter a choice (rock, paper, scissors): ').lower()

    print(f'Player: {player}')
    print(f'Computer: {computer}')


    if player == 'rock' and computer == 'scissors':
        print('You win!')
    elif player == 'paper' and computer == 'rock':
        print('You win!')
    elif player == 'scissors' and computer == 'paper':
        print('You win!')
    elif player == computer:
        print('DRAW :|')

    else:
        print('You lose :(')

    if not input('Play again? (y/n): ').lower() == 'y':
        running = False
        print('Thanks for playing')



