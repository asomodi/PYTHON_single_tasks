word = "madam"

def Palindrome(word):
    if (word[0::] == word[::-1]):
        return(True)    
    else:
        return(False)
print(Palindrome(word))