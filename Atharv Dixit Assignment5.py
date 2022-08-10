# 1. What does an empty dictionary's code look like?
# 2. What is the value of a dictionary value with the key 'foo' and the value 42?
# 3. What is the most significant distinction between a dictionary and a list?
# 4. What happens if you try to access spam['foo'] if spam is {'bar': 100}?
# 5. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.keys()?
# 6. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.values()?
# 7. What is a shortcut for the following code?
#    if 'color' not in spam:
#    spam['color'] = 'black'

# 8. How do you "pretty print" dictionary values using which module and function?


#Ans1: Empty Dictionary: {}

#Ans2: {'foo':42}

#Ans3: The elements stored in List are ordered while in dictionary they are unordered.

#Ans4: We will receive an error: keyError

#Ans5: Both of them checks if there is a key named 'cat' in dict.

#Ans6: The expressions 'cat' in spam checks if there is a key named 'cat' in dict while 'cat' in spam.values() checks if there is value named 'cat' of any key.

#Ans7: spam.setdefault('color', 'black')

#Ans8: Within the pprint module there is a function with the same name pprint().