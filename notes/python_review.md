# Python Review
## Date:  June 22, 2026
## Return Statements and Loops

1. What does return do inside a function?
   - My Answer: The return statement exits a function immediately, sending a specific value back and returns control to the code that called it.
     
   - ChatGPT: Correct - Tighter Version:  return immediately ends the function and sends a value back to the caller.

2. What happens when return is inside a for loop?
    - My Answer: It will stop the for loop once the return statement is reached and any iteration of the for loop that should have executed, will not occur.
  
    - ChatGPT: Correct - Also: A return inside a loop does not just stop the loop.  It stops the entire function.

3. What happens when return is after a for loop?
    - My Answer: It will execute the return statements code(see #1) after the for loop has executed the number of iteration it was intended to execute.
  
    - ChatGPT: Correct - Refinement: If return is after the loop, Python lets the loop finish first.  Then the function returns a value after all iterations are complete.

4. What is the difference between printing a value and returning a value?
    - My Answer: Printing a value, is for humans, it displays a text representation of data to the screen.  Returning a value, is intended for the computer, it returns data to the calling function that the computer or programs logic uses.
  
    - ChatGPT: Excellent - Also: print shows information.  Return gives information back to the program.

5. Why does returning too early cause bugs?
    - My Answer: Because not all of the code that the program requires for proper operation has been performed and therefore this early return will cause the program not to operate as desired.
  
    - ChatGPT: Correct - Returning too early causes bugs because the function exits before it has completed the full decision-making process.

ChatGPT Grades:
   - Conceptual understanding: Approved
   - Wording clarity: Good
   - Ready for practice exercises: Yes

## Return Placement Practice
- You have a list of email addresses.
- You want to check whether "bob@example.com" exists.
- Where should return True go?
  The 'return True' statement should go within the for loop and be executed when the if statement has returned true for a match of an email in the list with "bob@example.com".
  
  Why?
  Because once a match has been found by the if statement, there is no need to iterate through the rest of the list, this would just add to the program's runtime.

- Where should return False go?
    The 'return False' statement should go after the for loop structure, where it has iterated through all the item in the list since the nested if statement has never returned true for a match of an email in the list with "bob@example.com".

    Why?
        Because the for statement/structure needs to iterate through the entire list of items, if no match is being found by the if statement. Otherwise the search process is not complete and it can not be determined if the email already exists in the list of emails.


### Exercise 1: Search a list
Goal: Find whether a value exists in a list.

### Exercise 2: Count matches
Goal: Count how many values match a condition.

### Exercise 3: Validate all items
Goal: Check whether every item passes a rule.


### My current understanding
See Answers to question above.

### Examples that confuse me
None at this moment.

### Rules I need to remember

When searching a list:
- Return success inside the loop when the item is found.
- Return failure after the loop, once every item has been checked.
Do not return failure inside the loop unless one failed item is enough to end the whole function. 


### Practice results



# Python Review
# Date

