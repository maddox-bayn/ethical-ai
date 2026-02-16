# Exercise 00: Learning to Use AI Ethically as a Coder
# 1 The Critical Distinction

# How have you used AI for coding so far?
integrating and use os AI in my task: i have used AI as an assistance not a a tool for code generation, and now instead of "Give me the code and explain it " i switch to "Here is my attempt. Where is my reasosning flawed", instead of "AI write for me" to AI sharpens me", in cases when i hit a waal or can't through, i research concept to get full fundamrntal udersstanding or for conceptial understanding  theni can try and try again if failed to generate the code.
# Do you ask AI for solutions before trying yourself?
when i am giving a task to perform instead of "AI generate the code for me", firstly i gete a step by step breakedown (algorithms) of the task, i get full understanding of concept how i work it's edge cases or tradw offs that i may mis then after implimentation in code that it work then i give the AI for more better approache, time complexity, space complexity, and it efficency in real world scale.

# Can you explain code you've submitted without AI's help?
Due to style i use to implement in solving my task, i can explain the code in steps and it's underlying concept, what is happening behind the scene: that is after breaking complex task into smaller part to solve each part, if needed i do further research on the concept, after implementing my code, i test all edge cases, trace execution?, read logs and treat all bugs, at the and of the task i can implement my code by myself

# What would happen if AI was suddenly unavailable during an exam or interview?
when practice meet oppurtunity there will be success, when i used AI rightly i find it hard to fail my exams but when used wrongly to learn surely  there is failure ahead, so success or failure in an exam or interview depend on the level of how right or wrong AI is used during preparation

# 2  Identify your current pattern: 
Learner B: "AI is my learning amplifier"
Track B — The Right Way 
# Write pseudocode for a palindrome check
FUNCTION palindrome_check(input)
    SET left_pointer TO first index
    SET right_pointer TO last index
    while left_pointer is less than right_pointer DO 
        IF character of left_pointer not alphanumeric string
            INCREMENT left_pointer
        IF character of right_pointer not alphanumeric string
            DECREMENT right_pointer
        ELSE character of left_pointer in lower case not equal character of right_pionter in lower case DO 
            RETURN false
        INCREMENT left_pointer 
        DECREMENT right_pointer
    RETURN true  
END FUNCTION  
# function to check if input is palindrom

def palindrome_check(input):
    # create two pointer to compare charaacter from both end moving inward 
    left_pointer = 0
    right_pointer = len(input)-1

    # while left_pointer < right_pointer
    while left_pointer < right_pointer:
        # skip if character in unput is not alphalnumeric
        if not input[left_pointer].isalnum():
            left_pointer += 1
        elif not input[right_pointer].isalnum():
            right_pointer -= 1
        # else compare character from both end in lower case
        else:
            if input[left_pointer].lower() != input[right_pointer].lower():
                return False
            left_pointer += 1
            right_pointer -= 1
    return True

# Test Cases
print(palindrome_check("")) 
print(palindrome_check("A man a plan a canal Panama"))  
print(palindrome_check("hello"))  

# Reflection
***What did you learn by struggling first?***
struggling first gave a stronger mindset instead of just saying "AI give me the answer"as the saying goes muscle build memory, this approach to task helped to gained full understanding of the task and concept involved.

***How is your understanding different than if you'd just asked for the solution?***
Using This appproach was not easy but it made me understoodthe complex task, breaking it down into small task and then solve, create psuedocode for your task and i try codin it it appear hard i try and try again untill i have done all edge cases, deburg and check for any trade offs or better approach.

***Can you now implement similar functions (reverse a string, find duplicates) without AI?***
Due to the implementation of this approuch, i can write other similar function: write a psuedocode of task, understand how the algorithm work how each concept flow together then i try implementing my code if it fails, try again and try again, check all error, if any misssing edege case, until it works.

***What mental model did you build?***
systematic thinking and Architecture, thinking in terms of systems and security and The use of AI as "code Review" rather "Q&A" and also a person who can fix the code when AI is offline