import random
import sys

secret_number = random.randint(1, 100)
#secret_number = 50

print "Guess my \"Magic\" number in 3 guesses and win a quick fondle!"
print "If you fail, no fondle."


def process_user_guess(asked_count):
    print "Make your {} guess now!".format(asked_count)

    value = sys.stdin.readline()
    value = value.strip()
    number = int(value)

    if number == secret_number:
        print "Awww nuts, you got it!"
        return  True
    elif number > secret_number:
        print "You're too high bro!"
    else:
        print "You're not high enough, bra!"
    return False

guessed = process_user_guess("one")
if not guessed:
    guessed = process_user_guess("two")
if not guessed:
    guessed = process_user_guess("three")

print "AAAActually, the number was {}".format(secret_number)