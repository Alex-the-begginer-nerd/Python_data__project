it = [0]
for i in range(6):
    i += 1
    print(i)

    display = ['_' for letter in rand_fr]
print(' '.join(int(len(display)) * '_'))


running = True

guess = input('Try to guess a letter or a word: ').lower()

while running:
   wrong = 0
   for letter in guess:
      if letter in rand_fr:
         for i, char in enumerate(rand_fr):
               if char == letter:
                  display[i] = letter
               else:
                  wrong += 1
   print(' '.join(display))


   if ' '.join(display) == ' '.join(rand_fr):
      print('You won!')
      running = False

   

   else:
      guess = input('your next guess: ')
 
  
   

   for line in art.get(art_list[index]):
      print(line)