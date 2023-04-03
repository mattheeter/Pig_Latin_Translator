# Function to determine if the inputted character is a consonant
def Cons_Checker(character):
    vowels = ['A','E','I','O','U','Y','a','e','i','o','u','y']
    # If the argument character is not in the list of vowels (ie. is a consonant or special character), return true, else return false
    if character not in vowels:
        return True
    return False

# Function to determine if the inputted character is a special character by comparing its ASCII code to that of all types of letters.
def Special_Checker(character):
    # Converting character to its ASCII value with ord() function
    character = ord(character)
    if (character <= 64) or (character >= 91 and character <= 96) or (character >= 123):
        return True
    return False

# This function will translate an English word into Pig Latin
def Pig_Latinfy(word):
    i = 0
    for character in word:
        if not Cons_Checker(character): # Once character is a vowel, extract letters before it and put them at the end
            word = word[i:] + word[:i] + "ay"
            return(word)
        i += 1

# Function to find the location of special characters (non alphanumerics) 
def Non_Alnum_Loc(word):
    i = 0
    for character in word:
        if Special_Checker(character):
            return i
        i += 1

# Function to check if a word contains a special character (non alphanumeric)
def Special_Check(word):
    for character in word:
        if Special_Checker(character):
            return True
    return False
