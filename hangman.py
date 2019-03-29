import string
from words import choose_word
from images import IMAGES

# End of helper code
# -----------------------------------

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: ek string word jo ki user ko guess karna hai
    letters_guessed: ek list hai, jisme wo letters hai jo ki user nai abhi tak guess kare hai
    returns: return True kare agar saare letters jo ki user ne guess kiye hai wo secret_word mai hai, warna no
      False otherwise
    '''
    if secret_word==get_guessed_word(secret_word,letters_guessed):
        return True
    return False

#Iss function me hum check karenge ki user ka input valid hai ya nahi.
#matlab agar user input only single alphabet me nahi deta hai to wo Invalid show karega.
def ifValid(letter):
    if len(letter) != 1:
        return False
        # Agar user input 1 se jyada character hua to False return karega
    if not letter.isalpha():
        return False
        # Agar user input alphabet nahi hua to False return karega.
    return True
    # Yeha only wo lwtter True honge jo only single alphabet hoga.

# Iss function ko test karne ke liye aap get_guessed_word("kindness", [k, n, d]) call kar sakte hai
def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: ek string word jo ki user ko guess kar raha hai
    letters_guessed: ek list hai, jisme wo letters hai jo ki user nai abhi tak guess kare hai
    returns: ek string return karni hai jisme wo letters ho jo sahi guess huye ho and baki jagah underscore ho.
    eg agar secret_word = "kindness", letters_guessed = [k,n, s]
    to hum return karenge "k_n_n_ss"
    '''

    index = 0
    guessed_word = ""
    while (index < len(secret_word)):
        if secret_word[index] in letters_guessed:
            guessed_word += secret_word[index]
        else:
            guessed_word += "_"
        index += 1
    
    return guessed_word


def get_available_letters(letters_guessed):
    '''
    letters_guessed: ek list hai, jisme wo letters hai jo ki user nai abhi tak guess kare hai
    returns: string, hame ye return karna hai ki kaun kaun se letters aapne nahi guess kare abhi tak
    eg agar letters_guessed = ['e', 'a'] hai to humme baki charecters return karne hai
    jo ki `bcdfghijklmnopqrstuvwxyz' ye hoga
    '''
    all_letters=string.ascii_lowercase
    letters_left=""

    for letter in all_letters:
        if letter not in letters_guessed:
            letters_left+=letter
    return letters_left

def get_hint(secret_word,letters_guessed):
    import random
    letters_not_guessed =[]
    for i in secret_word:
        if i not in letters_guessed:
            if i not in letters_not_guessed:
                letters_not_guessed.append(i)
    return random.choice(letters_not_guessed)


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Hangman game yeh start karta hai:

    * Game ki shuruaat mei hi, user ko bata dete hai ki
      secret_word mei kitne letters hai

    * Har round mei user se ek letter guess karne ko bolte hai

    * Har guess ke baad user ko feedback do ki woh guess uss
      word mei hai ya nahi

    * Har round ke baar, user ko uska guess kiya hua partial word
      display karo, aur underscore use kar kar woh letters bhi dikhao
      jo user ne abhi tak guess nahi kiye hai

    '''
    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is " + str(len(secret_word)) + " letters long."
    print "You can use hint once "
    print ""

    try_hint=True
    flag=False
    letters_guessed = []

    while(True):
        user_difficulty_choice=raw_input("Aap abhi kitni difficulty par yeh game khelna chahte ho?\na)\tEasy\nb)\tMedium\nc)\tHard\n\nApni choice a, b, ya c ki terms mei batayein\n")
        total_lives=Remaining_lives=7

        image_selection_list_indicate = [0,1,2,3,4,5,6,7]
        if user_difficulty_choice not in ['a','b','c']:
            print "Aapki choice invalid hai.\nGame easy mode mei start kar rahe hai"
            continue

        else:
            if user_difficulty_choice=="b":
                total_lives=Remaining_lives=5
                image_selection_list_indicate=[0,2,3,5,6,7]

            elif user_difficulty_choice=="c":
                total_lives=Remaining_lives=3
                image_selection_list_indicate=[1,3,5,7]
        
        while (Remaining_lives>=0):    
            available_letters = get_available_letters(letters_guessed)
            print "Available letters: " + available_letters

            guess = raw_input("Please guess a letter: ")
            
            if guess=="hint" and try_hint==True:
                letter=get_hint(secret_word,letters_guessed)
                try_hint=False
            else:
                letter = guess.lower()

                if(not ifValid(letter)):
                    print "Please enter the valid input from Available letters\n"
                    continue

            if letter in secret_word:
                letters_guessed.append(letter)
                print "Good guess: " + get_guessed_word(secret_word, letters_guessed)
                print ""

                if is_word_guessed(secret_word, letters_guessed) == True:
                    print " * * Congratulations, you won! * * "
                    print ""
                    flag=True
                    break

            else:
                print "Oops! That letter is not in my word: " + get_guessed_word(secret_word, letters_guessed)
                print ''   
                
                print IMAGES[image_selection_list_indicate[total_lives-Remaining_lives]]
                print "Remaining_lives : ",Remaining_lives
                print ''
                letters_guessed.append(letter) 
                Remaining_lives-=1
                print ""
        if flag==True:
            break
        else:
            print "Sorry you are ran out of guesses. You lost the game. ! The correct word was : %s ."%secret_word
            break


# Load the list of words into the variable wordlist
# So that it can be accessed from anywhere in the program
secret_word = choose_word()
hangman(secret_word)