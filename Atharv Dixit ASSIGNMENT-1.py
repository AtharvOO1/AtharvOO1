#!/usr/bin/env python
# coding: utf-8
1. In the below elements which of them are values or an expression? eg:- values can be
integer or string and expressions will be mathematical operators.

Ans: 

* is an Expression
'hello' is a Value
-87.81 is a Value
- is an Expression
/ is an Expression
+ is an Expression
6 is a value2. What is the difference between string and variable?

Ans:

String is a sequence of alphabets or numbers or special charaters enclosed in ' ' or " " or ''' ''' (For Multiline)
Eg: s= "Atharv" , s1= "Atharv1" , s2= "I am learning Python"

Variable is a location in the memory used to store any value i.e. A= 10 (which is an integer), B= 9.5 (which is a float), C= "AI" (which is a string)3. Describe three different data types.

Ans: 

The three different data types are:

1. List: The list is represented by [] and the elements are separated by commas. The list is ordered in sequence of index. It can contain different types of elements like Int, String, Float. List can be modified.
eg: List=[2,7.7, "AI"] where 2 is at 0 index, 7.7 is at 1 index, "AI" is at 2 index.

2. Tuple: Tuple is represented by () and separated by commas. Tuple is also ordered in sequence of index. A tuple can't be modified.  
eg: T= (2,7.7, "AI")

3. Dictionaries: It is represented by {} and are unordered pair of Key and Values.
eg: d= {1: "Atharv", 2: "Dixit"} where 1&2 are Keys and Atharv & Dixit are values.4. What is an expression made up of? What do all expressions do?

Ans:

An expression is made up of operators and operands that gives a single outcome when the operation is performed.
eg: [2+4] is an expression, where 2&4 are operands and + is an operator.
    
    
    5. This assignment statements, like spam = 10. What is the difference between an
expression and a statement?

Ans:

An expression is made up of operators and operands that gives a single outcome when the operation is performed while a statement is a set of instructions that an interpreter can execute.6. After running the following code, what does the variable bacon contain?

bacon = 22
bacon + 1

Ans:

After performing, bacon+1 it will give 23 but the value of bacon will remain 22.
7. What should the values of the following two terms be?
'spam'+ 'spamspam'
'spam'*3

Ans:

'spam'+ 'spamspam' will give 'spamspamspam' (Additon of strings)
'spam'*3 will also give 'spamspamspam'8. Why is eggs a valid variable name while 100 is invalid?

Ans:

Eggs is a valid variable name while 100 isn't because Variable name can't be an Integer.9. What three functions can be used to get the integer, floating-point number, or string
version of a value?

Ans:

Integer: int()
Float: float()
String: str()10. Why does this expression cause an error? How can you fix it?
'I have eaten' + 99 + 'burritos.'

Ans:

This expression causes an error as here we are trying to add integer with strings. This can be fixed by converting the integer to a string.

'I have eaten'+ str(99) + 'burritos'