import random
import string
art = { 0:('      ',
           '       ',
           '        '), 
      1:('    O  ',
           '       ',
           '        '),
        2:('    O  ',
           '    |   ',
           '        '),
        3:('    O  ',
           '   /|   ',
           '        '),
        4:('    O  ',
           '   /|\   ',
           '        '),
        5:('    O  ',
           '   /|\   ',
           '   /     '),
        6:('    O  ',
           '   /|\   ',
           '   / \    ')      
}
words = ['apple', 'banana', 'coconut', 'orange', 'mango']

def display_man(wrong):
   for line in art[wrong]:
      print(line)

def display_hint(hint):
    print(' '.join(hint))

def display_answer(answer):
   print(' '.join(answer))

def main():
   wrong = 0
   answer = random.choice(words)
   running = True
   guessedL = set()
   hint = ['_'] * len(answer)
   while running:
      display_man(wrong)
      display_hint(hint)
      guess = input('Guess a word: ').lower()

      if guess in answer:
         for i in range(len(answer)):
            if answer[i] == guess:
               hint[i] = guess

      else:
         wrong += 1
         display_man(wrong)

      if not '_' in hint:
         running = False
         print('YOU WON!')
         display_answer(answer)

      elif wrong >= len(art) -1:
         running = False
         print('you lose :(')
         display_answer(answer)

      if len(guess) != 1 or not guess.isalpha:
         print('Invalid input')
         continue 

      if guess in guessedL:
         print(f'{guess} is already guessed')
         continue
        
      guessedL.add(guess)

if __name__ == "__main__":
   main()