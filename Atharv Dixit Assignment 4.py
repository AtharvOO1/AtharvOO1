#1. What exactly is []?
#2. In a list of values stored in a variable called spam, how would you assign the value 'hello' as the
#   third value? (Assume [2, 4, 6, 8, 10] are in spam.)


#   Let's pretend the spam includes the list ['a', 'b', 'c', 'd'] for the next three queries.
#3. What is the value of spam[int(int('3' * 2) / 11)]?
#4. What is the value of spam[-1]?
#5. What is the value of spam[:2]?


#   Let's pretend bacon has the list [3.14, 'cat', 11, 'cat', True] for the next three questions.
#6. What is the value of bacon.index('cat')?
#7. How does bacon.append(99) change the look of the list value in bacon?
#8. How does bacon.remove('cat') change the look of the list in bacon?

#9. What are the list concatenation and list replication operators?
#10. What is difference between the list methods append() and insert()?
#11. What are the two methods for removing items from a list?
#12. Describe how list values and string values are identical.
#13. What's the difference between tuples and lists?
#14. How do you type a tuple value that only contains the integer 42?
#15. How do you get a list value's tuple form? How do you get a tuple value's list form?
#16. Variables that "contain" list values are not necessarily lists themselves. Instead, what do they contain?
#17. How do you distinguish between copy.copy() and copy.deepcopy()?


#Ans1: [] is an empty list.

#Ans2: spam[2]= "hello"

#Ans3: spam[3] is 'd'

#Ans4: spam[-1] is 'd'

#Ans5: spam[:2] is ['a', 'b']

#Ans6: bacon.index('cat') is 1

#Ans7: [3.14, 'cat', 11, 'cat', True, 99]

#Ans8: [3.14, 11, 'cat', True]

#Ans9: The list concatenation operator is +, while the replication operator is *

#Ans10: append() adds the element at the end and insert() allows to add element at any specific index.

#Ans11: The two methods for removing items from a list are: remove(), pop().

#Ans12: They both are identical in one thing and that is they both are in ordered collection.

#Ans13: Tuples are immutable while the Lists are mutable.

#Ans14: (42,)

#Ans15: List value's tuple form: Use tuple() and Tuple value's list form: Use list()

#Ans16: They contain reference to list values.

#Ans17: The copy.copy() function will do a shallow copy of a list i.e. If you change copied object, you also change the original object.
#       while the copy.deepcopy() function will do a deep copy of a list i.e. If you change new deepcopied object it doesn't affect original object.