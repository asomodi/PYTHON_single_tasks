#!/usr/bin/env python
# coding: utf-8

# In[2]:


word="GUESS"
guessed=0
current_guess=["_"]*len(word)
count=0


print("HANGMAN Experience :-)\nThe word has " + str(len(word)) + "letters.\nGOOD LUCK\n\n")
print(("_"+" ")*len(word))

while count <6:
    
    guess=input("\nGuess your letter: ").upper()
    
    
    for letter in range(0,len(word)):
        if word[letter]==guess:
            current_guess[letter]=guess
    
    if "_" not in current_guess:
        guessed=1
        break
    else:
        for i in range(0,len(word)):
            print ( current_guess[i] + " ", end="")
        print("\n")    
        
    count+=1
if guessed==1:
    print("Yeah, you managed to find the word: ", word)
else:
    print("Sorry, you'r dad, man!\nThe right word would have been: ", word)
    
        


# In[ ]:




