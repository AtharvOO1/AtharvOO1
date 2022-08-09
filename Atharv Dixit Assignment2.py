#1. What are the two values of the Boolean data type? How do you write them?

#Ans1: The two boolean data type values are: True and False and are written in capital letters.

#2. What are the three different types of Boolean operators?

#Ans2: The three types are: AND, OR, NOT.

#3. Make a list of each Boolean operator's truth tables (i.e. every possible combination of Boolean values for the operator and what it evaluate ).

#Ans3: For AND:

#     A= True B= True, then A AND B= True
#     A= False B= False, then A AND B= False
#     A= False B= True, then A AND B= False
#     A= True B= False, then A AND B= False

#     For OR:

#     A= True B= True, then A OR B= True
#     A= False B= False, then A OR B= False
#     A= False B= True, then A OR B= True
#     A= True B= False, then A OR B= True

#     For NOT:
#     A= True, NOT A= False
#     A= False, NOT A= True

#4. What are the values of the following expressions?
# (5 > 4) and (3 == 5)
# not (5 > 4)
# (5 > 4) or (3 == 5)
# not ((5 > 4) or (3 == 5))
# (True and True) and (True == False)
# (not False) or (not True)

#Ans4: (5 > 4) is True and (3 == 5) is False. True AND False= False.
#      not (5 > 4) is False as 5 > 4 is True & NOT True is False.
#      (5 > 4) is True or (3 == 5) is False. True OR False= True.
#      not ((5 > 4) or (3 == 5)) is False as the answer to (5 > 4) or (3 == 5) is True & NOT True is False.
#      (True and True) and (True == False) is False.
#      (not False) or (not True) is True.

#5. What are the six comparison operators?

#Ans5: Python has six comparison operators:

#      less than ( < ),
#      less than or equal to ( <= ),
#      greater than ( > ),
#      greater than or equal to ( >= ),
#      not equal to ( != ),
#      equal to ( == ).

#6. How do you tell the difference between the equal to and assignment operators?Describe a condition and when you would use one.

#Ans6: The “=” is an assignment operator is used to assign the value and store it. For Eg, x= 5
#      The '==' operator checks whether the two given operands are equal or not. For Eg, x=5 y=5. So, x==y.

#7. Identify the three blocks in this code:
# spam = 0
# if spam == 10:
# print('eggs')
# if spam > 5:
# print('bacon')
# else:
# print('ham')
# print('spam')
# print('spam')

#Ans7: The three blocks are everything inside the if statement and the lines print('bacon') and print('ham').

#8. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.

#Ans8: if spam==1:
#           print("Hello")
#      if spam== 2:
#           print("Howdy")
#      else:
#           print("Greetings!")

#9. If your programme is stuck in an endless loop, what keys you’ll press?

#Ans9: Ctrl-C can be used to stop an endless loop.

#10. How can you tell the difference between break and continue?

#Ans10: The purpose the break statement is to break out of a loop and
#       The continue skips the rest of the loop statement and starts the next iteration of the loop to take place.

#11. In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?

#Ans11: They all have same meaning. range(10) is range(0-9), range(0, 10) is range(0-9) and range(0,10,1) is range(0-9) with a diff. of 1.

#12. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.

#Ans12: for i in range(11):
#           print(i)

#       a= 1
#       b= 10
#       while a<=b:
#           print(a)
#           a=a+1

#13. If you had a function named bacon() inside a module named spam, how would you call it after importing spam?

#Ans13: We can call it with spam.bacon(). 