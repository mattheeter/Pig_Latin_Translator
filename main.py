# This program will convert a user inputted string from English to Pig Latin

from My_Functions import Cons_Checker, Pig_Latinfy, Non_Alnum_Loc, Special_Check

fhand = open("test_file.txt", 'r')
eng = fhand.read()

# eng = input("Enter string to be translated: ")
#eng = "Translate this sentence into Pig Latin. Would you look at all that!" # Test case
eng = eng.strip() # Removing anyleading and trailing whitespace from input       

engSplit = eng.split()
pigLatin = ""

for word in engSplit: # Iterating through each word in the input
    if Cons_Checker(word[0]): 
        word = Pig_Latinfy(word) # If the first letter of the word is a consonant, translating it to Pig Latin
        if Special_Check(word): 
            loc = Non_Alnum_Loc(word)
            word = word[:loc] + word[loc+1:] + word[loc] + ' ' # If the word contains a special character, putting it at the end    
        else:
            word += ' '
        pigLatin += word

    else:
        pigLatin += word + "yay" + ' ' # If the word starts with a vowel, doing its version of Pig Latinifying
     
print(pigLatin)