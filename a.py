

# Guessing game


secret_num = 79
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess:  '))
    guess_count += 1

    if guess == secret_num:
            print('You won')
            break

else:
    print('Sorry you failed')





# Modni Rother © 2020
# Created 𝗐𝗂𝗍𝗁 ❤