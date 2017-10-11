secret = 7
correct = False
while not correct:
    guess = input('Guess a number (1 - 10): ')    
    if guess == secret:
        print 'You guessed right'
        correct = True
    elif guess < secret:
        print 'Your guess is too small'
    else:
        print 'Your guess is too big'
