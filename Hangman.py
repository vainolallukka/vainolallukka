def main():
    print("Welcome to Hangman!")
    print("Game organiser, please enter the word which other players will try to guess:")
    word = str(input())

    print("The word is {:s}. Do you wish to continue?".format(word))
    choice = str(input())

    while choice != "yes" and choice != "no":
        print("yes/no")
        choice = str(input())

    if choice == "no":
        main()
    else:
        print("Let the game begin.")

    right_letters = list(word)
    wrong_letters = []
    incomplete_word = []
    for i in range(len(right_letters)):
        incomplete_word.append("_")
    lives = 10

    while True:
        if lives == 0:
            print("You ran out of lives. The correct word was {:s}.".format(word))
            break
        elif incomplete_word == right_letters:
            print("You got all the letters correct! The word was {:s}!".format(word))
            break

        print("You have {:d} lives left".format(lives))
        print("Wrong guesses:", *wrong_letters, sep=" ")
        print("Correct guesses:", *incomplete_word, sep=" ")
        print("Guess a letter or the word!")
        guess = str(input())

        if len(guess) > 1:
            if guess == word:
                print("Your guess was correct! Victory!")
                break
            else:
                print("That was not the correct word.")
                print("You lose one life.")
                lives -= 1

        elif len(guess) == 1:
            if guess in right_letters:
                print("The letter {:s} was correct!".format(guess))
                for i in range(len(right_letters)):
                    if right_letters[i] == guess:
                        incomplete_word[i] = guess

            else:
                print("Your guess was incorrect. You lose one life.")
                lives -= 1
                wrong_letters.append(guess)

main()