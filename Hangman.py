# a=1
# b=2
# c=3
# d=4
# cookies = True
# kale = False
# word="hello"
# name = "Q"
# print(word + " " + name + str(b))
# if cookies == kale:
#     print("True")
# else:
#     print("False")
# for i in range (1,10):
#     print("hi")
# while True:
#     print("hi")
# nextLetter=raw_input("Guess a letter: ")
# print(nextLetter)
import random
myList = ["cookies", "hi", "realization", "Q", "eagles", "fly", "squeak" ]
hangman_word = random.choice(myList)
lettersGuessed = []
while True:
    print("\nLetters already guessed:" + str(lettersGuessed))
    wordinprogress = ""
    for i in range (len(hangman_word)):
        print(i)
        print("The current letter in question is :" + str(hangman_word[i]))
        if hangman_word[i] in lettersGuessed:
            wordinprogress+=str(hangman_word[i])
        else:
            wordinprogress+=str("_")
        print(wordinprogress)
    nextLetter=raw_input("Guess a letter: ")
    if nextLetter not in lettersGuessed:
        if nextLetter in hangman_word:
            print("Good guess! This letter is in the word.")
            lettersGuessed.append(nextLetter)
        else:
            print("Letter not in word. Try again!")
            lettersGuessed.append(nextLetter)
    else:
        print("You already guessed that letter. Try again.")
