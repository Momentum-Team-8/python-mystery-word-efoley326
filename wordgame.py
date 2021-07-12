import random

# open words.txt

# log guesses

# number guesses

# display right or wrong

# adjust difficulty 
with open ("words.txt", 'r') as w:
    allText = w.read()
    

def gamePrompt ():
    words = list(map(str, allText.split()))
    word = "carrot"
    # (random.choice(words))
    # for letter of words:
    wordLetters = list(word)
    wordLength = (len(wordLetters))
    word_selection = "_" * len(wordLetters)
    print (word_selection)
    a = input("Make a guess: ")
    while a == (wordLetters) :
        replaced = word_selection.replace(word_selection, a)
        print (replaced)
        print("You guessed" + replaced)
    


    # if letters == 


    # input("Your guess: ")


gamePrompt()
    