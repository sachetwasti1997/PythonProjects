import random

def play():
    user = input("'r' for rock, 's' for scissor, 'p' for paper! ")
    computer = random.choice(['r', 'p', 's'])

    print(f'Computer\'s choice: {computer}')
    if is_win(user, computer):
        print('You won')
        return
    elif user == computer:
        print('It\'s a Tie')
        return
    print('You Lost')

def is_win(player, computer):
    if (player == 'r' and computer == 's') or (player == 'p' and computer == 'r') \
    or (player == 's' and computer == 'p'):
        return True
    return False

play()