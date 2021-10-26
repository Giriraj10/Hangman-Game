from words import wordlist
import random

def get_word():
    word = random.choice(wordlist)
    return word.upper()


def play(word):
    word_complete = "_"*len(word)
    guessed = False
    guessed_letters = []
    guessed_words =[]
    tries = 6
    print("Welcome To Hangman")
    print(hangman_animation(tries))
    print(word_complete)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Guess a word or letter: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You Already Guessed this letter" , guess)
            elif guess not in word:
                print("Oops ! ",guess," is not a part of the word")        
                tries -= 1 
                guessed_letters.append(guess)
            else:
                print("Great ",guess," is in the word !" )
                guessed_letters.append(guess)
                word_as_list = list(word_complete)
                indices = [i for i , letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_complete = "".join(word_as_list)
                if "_" not in word_complete:
                    guessed = True
        
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You Already Guessed ",guess)
            elif guess != word:
                print(guess," is not the Word, Try Again ")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_complete = word
        else:
            print("Not a Valid Guess")
        print(hangman_animation(tries))
        print(word_complete)
        print("\n")
    if guessed:
        print("Good Job you guessed it Right")
    else :
        print("Sorry you've ran out of tries , the word was "+word+" Better Luck Next Time")

def hangman_animation(tries):
    stages = [
        """
        ---------
        |       |
        |       o
        |      \|/
        |       |
        |      / \\
        |________
        """,
        """
        ---------
        |       |
        |       o
        |      \|/
        |       |
        |      / 
        |________
        """,
        """
        ---------
        |       |
        |       o
        |      \|/
        |       |
        |      
        |________
        """,
        """
        ---------
        |       |
        |       o
        |      \|/
        |       
        |      
        |________
        """,
        """
        ---------
        |       |
        |       o
        |      \|
        |       
        |      
        |________
        """,
        
        """
        ---------
        |       |
        |       o
        |      
        |       
        |  
        |________
        """,
        """
        ---------
        |       |
        |       
        |      
        |       
        |  
        |________
        """
        
    ]
    return stages[tries]


def main():
    word = get_word()
    play(word)
    while input("Play Again ? Y/N").upper() == "Y":
        word = get_word()
        play(word)


if __name__ == "__main__":
    main()