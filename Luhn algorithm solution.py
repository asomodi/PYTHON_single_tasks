#!/usr/bin/env python
# coding: utf-8

# In[ ]:


card = "4532015112730366"  # some text number, in a string format
i = len(card)              # length of the card number assign to variable i 

cknums = []
while i >=1:            # loop from the end 
    tmp = int(card[i-1])*2  # convert str to int, double it. 
    if i % 2 == 1:          # if the division leaves the remainer, tmp is a doubled number
        if tmp > 9:         # check if it is larger than 9 after doubling 
            cknums.append(int(str(tmp[0]) + int(str(tmp[1])) #spilce as string in 2 and sum them after converting back
        else:
            cknums.append(int(tmp))    # if tmp is smaller than 9, just append
    else:
            cknums.append(int(card[i-1])) # else of modulo 2 - the number was not doubled and simply gets appended
    i = i -1        # decrement the loop index 

j = 0               # initialise sum variable 
for i in cknums:    # sum all numbers from check numbers
    j = j + i
                        
if j % 10 == 0;     # check the remainder after dividing by 10
    print ("Valid number")
else:
    print("Invalid number")

