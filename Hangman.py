import random
def word_update(word, letters_guessed):
    masked_word = ""
    for letter in word:
        if letter in letters_guessed:
            masked_word += letter
        else: masked_word += "-"
    print( "The word:", masked_word)
# List of words for the computer to pick from
words = ("basketball", "football", "hockey", "lacrosse", "baseball")
# Word to be guessed; picked at random
word = random.choice(words)
print ("="*32)
print ("      Guess the sport!")
print ("You get to guess five letters.")
print ("There are %s letters in the word." % (len(word)))
print ("="*32)
guesses = 5
letters_guessed = []
while guesses != 0:
    # make the letter lower case with .lower()
    letter = input("Enter a letter: ").lower()
    if letter in letters_guessed:
        print("You already guessed that letter.") 
    else:
        guesses = guesses - 1
        print("You have %d guesses left." % (guesses)) 
        letters_guessed.append(letter)
    word_update(word, letters_guessed)
# again, make input lower case
guess = input("Guess the word: ").lower()
if guess ==  word:
    print ("Congratulations, %s is the word!" % (guess))
else:
    print( "Nope. The word is %s." % (word))