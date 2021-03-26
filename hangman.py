import random
import json

class Hangman:
    def __init__(self):
        with open("words.json", "r+") as list_of_words:
            self.words = json.load(list_of_words)
        self.chosen_word = ""
        self.lives = 10
        self.hangman = []
        self.wrong_letters = []

    def get_random_word(self, words: list) -> str:
        # gets a random word off of the word list.
        return words[random.randint(0, len(words)-1)]

    def update_hangman(self, letter: str) -> list:
        # replaces the "_" with the found letter.
        for idx, value in enumerate(self.chosen_word):
            if letter == value:
                self.hangman[idx] = value

    def start(self):
        print("Welcome to Hangman!")

        # apply stuff i think i dont know never coded
        self.chosen_word = self.get_random_word(self.words)

        # make the hangman message
        for _ in self.chosen_word:
            self.hangman.append("_")
        
        # make a loop for the game
        while True:
            print(" ".join(self.hangman))
            print("Lives: ", self.lives)

            letter = input("Take a wild guess: ").lower()
            if len(letter) > 1 or letter.isnumeric(): # if its not a single letter, make the user try again
                print("Only letters.\n")
                continue

            if letter in self.wrong_letters or letter in self.hangman:
                print("You've already chosen this word!\n")
                continue

            # check if the letter is in the word and also if the letter is not already in the hangman
            if letter in self.chosen_word and not letter in self.hangman:
                print("You got it right!\n") # tell the user they got it right

                # update the hangman and amount of letters left to be found.
                self.update_hangman(letter)
            else:
                # remove a life!
                self.lives -= 1

                # notify them it was wrong
                print("You got it wrong! Try again!\n")
                self.wrong_letters.append(letter) # add the letter in the list so they don't make the same mistake
            
            # if there's no letters left to be found, the user wins.
            if "".join(this.hangman) == self.chosen_word:
                print(" ".join(self.hangman))
                print("You've won!")
                break

            if self.lives == 0: # if no lives left, the user has lost!
                print("You lost!")
                print("The word was:", self.chosen_word)
                break

            # print out the wrong letters when there are any
            if this.wrong_letters:
                    print("All wrong letters: ", ", ".join(self.wrong_letters))

            continue # lesss goooooooo


if __name__ == '__main__':
    Hangman().start()
