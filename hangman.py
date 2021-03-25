import random
import json

class Hangman:
    def __init__(this):
        with open("words.json", "r+") as list_of_words:
            this.words = json.load(list_of_words)
        this.chosen_word = ""
        this.lives = 10
        this.hangman = []
        this.wrong_letters = []

    def get_random_word(this, words: list) -> str:
        # gets a random word off of the word list.
        return words[random.randint(0, len(words)-1)]

    def update_hangman(this, letter: str) -> list:
        # replaces the "_" with the found letter.
        for idx, value in enumerate(this.chosen_word):
            if letter == value:
                this.hangman[idx] = value

    def start(this):
        print("Welcome to Hangman!")

        # apply stuff i think i dont know never coded
        this.chosen_word = this.get_random_word(this.words)

        # make the hangman message
        for _ in this.chosen_word:
            this.hangman.append("_")
        
        # make a loop for the game
        while True:
            print(" ".join(this.hangman))
            print("Lives: ", this.lives)

            letter = input("Take a wild guess: ").lower()
            if len(letter) > 1 or letter.isnumeric(): # if its not a single letter, make the user try again
                print("Only letters.\n")
                continue

            if letter in this.wrong_letters or letter in this.hangman:
                print("You've already chosen this word!\n")
                continue

            # check if the letter is in the word and also if the letter is not already in the hangman
            if letter in this.chosen_word and not letter in this.hangman:
                print("You got it right!\n") # tell the user they got it right

                # update the hangman and amount of letters left to be found.
                this.update_hangman(letter)
            else:
                # remove a life!
                this.lives -= 1

                # notify them it was wrong
                print("You got it wrong! Try again!\n")
                this.wrong_letters.append(letter) # add the letter in the list so they don't make the same mistake
            
            # if there's no letters left to be found, the user wins.
            if "".join(this.hangman) == this.chosen_word:
                print(" ".join(this.hangman))
                print("You've won!")
                break

            if this.lives == 0: # if no lives left, the user has lost!
                print("You lost!")
                print("The word was:", this.chosen_word)
                break

            # print out the wrong letters when there are any
            if this.wrong_letters:
                    print("All wrong letters: ", ", ".join(this.wrong_letters))

            continue # lesss goooooooo


if __name__ == '__main__':
    Hangman().start()