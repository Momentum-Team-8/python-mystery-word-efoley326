import random

with open("words.txt") as words_txt:
    word_options = words_txt.read()

def gamePrompt():
    # split_words = list(map(str, word_options.split()))
    # split_letters = list(random_word)
    # print(split_letters)
    # tries = 0
    # while tries > 10:
    # word_selection = "_" * word_length
    # split_words = random_words.split(' ')
     # number_of_guesses = 8

    random_words = ["Carrot", "goal"]
    random_words = [each_string.lower() for each_string in random_words]
    random_word = random.choice(random_words)
    word_length = (len(random_word))
    guesses = []
    numberoftries = 0
    level_choice = input("Choose your difficulty: (E)easy   (M)medium   (D)difficult").upper()
    for letter in random_word:
        guesses.append('_')

# EASY
    if level_choice == "E":
        while numberoftries < 9:
            print(guesses)
            input_letter = str(input("Make a guess: ").lower())
            if "input_letter" in "random_word":
                print("Correct")
            for letter in range(word_length):
                if input_letter == random_word[letter]:
                    guesses[letter] = random_word[letter]
                print(guesses)
        else:
         print("Sorry, no more guesses. You lose.")

# MEDIUM
    if level_choice == "M":
        print(guesses)
        guesses = +1
        if guesses <= 6:
            input_letter = str(input("Make a guess: ").lower())
            if input_letter in random_word:
                print("Correct")
                for letter in range(word_length):
                    if input_letter == random_word[letter]:
                        guesses[letter] = random_word[letter]
                print(guesses)
        else :
            print("Sorry, no more guesses. You lose.")

# DIFFICULT
    if level_choice == "D":
        print(guesses)
        guesses = +1
        if guesses <= 4:
            for letter in random_word:
                guesses.append('_')
            print(guesses)
            input_letter = str(input("Make a guess: ").lower())
            if input_letter in random_word:
                print("Correct")
                for letter in range(word_length):
                    if input_letter == random_word[letter]:
                        guesses[letter]= random_word[letter]
                print(guesses)
        else :
            print("Sorry, no more guesses. You lose.")


    
    # guesses += input_letter 
    # print(guesses)
    # print(type(input_letter))

    # if the input letter number corresponds to the space number, then replace space with input letter. 
        
    # letter_list[0].replace("_", input_letter)
    # # word_selection[0] += input_letter
    # print(letter_list)


    # for letter of words:
        # print(randomword)
        #input("Your Guess " )
        # word_selection = "_" * len(words)

gamePrompt()