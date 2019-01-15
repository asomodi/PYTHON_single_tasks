#!/usr/bin/env python
# coding: utf-8

# In[ ]:


numberOfPasswords = int(input("How many passwords do you need?"))
length = int(input("Password length?"))

chars = "qayíesxdrctfvzgbnhuijmkolpéőáűúóüöQWERTZUIOPŐÚŰÁÉLKJHGFDSAÍYXCVBNM1234567890!@#$%^&*()?"

for b in range(numberOfPasswords):
    password = ' '
    for c in range(length):
        password += random.choice(chars)
    print(password)
    print('\n')

