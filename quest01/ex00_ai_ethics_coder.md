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
# AI REVIEW AND FEEDBACK

***The time complexity:*** is o(n), where n is the length of the string.
    Why: Each character is visited at most once by either the left_pointer or the right_pointer. Even though you have nested logic (the if/else), the pointers only ever move toward the center.
***Space Complexity:***This is the biggest advantage of your approach. You aren't creating a new reversed string or a list of filtered characters; you are only storing two integer pointers
***Edge Cases to Consider:*** The Empty String, Single Character / Single Alphanumeric: "a" or "a!" will return True., No Alphanumeric Characters: A string like "!!! --- ???" will finish the loop and return True, 
***Trade-offs:*** use case will returning a comperison  of the input and direct reverse of it which create extra variable in memory causing an O(n) space complexity 
***Performance on Very Long StringsMemory Efficiency:*** Because it'sspace, you can process a string that takes up 90% of your RAM without triggering a "Memory Error."
**Early Exit:** Your code returns False the instant it finds a mismatch. If the first and last letters are "A" and "Z", your code stops immediately. The "One-Liner" approach above would still filter the entire string and reverse it before realizing it's not a palindrome.
**Cache Friendliness:** Modern CPUs are very good at predicting linear memory access (moving pointers inward), making this very fast at the hardware level.

# Reflection
***What did you learn by struggling first?***
struggling first gave a stronger mindset instead of just saying "AI give me the answer", struggling first strengthens cognitive retention and builds problem-solving endurance. as the saying goes muscle build memory, this approach to task helped to gained full understanding of the task and concept involved.

***How is your understanding different than if you'd just asked for the solution?***
Using This appproach was not easy but it made me understoodthe complex task, breaking it down into small task and then solve, create psuedocode for your task and i try codin it it appear hard i try and try again untill i have done all edge cases, deburg and check for any trade offs or better approach.

***Can you now implement similar functions (reverse a string, find duplicates) without AI?***
Due to the implementation of this approuch, i can write other similar function: write a psuedocode of task, understand how the algorithm work how each concept flow together then i try implementing my code if it fails, try again and try again, check all error, if any misssing edege case, until it works.

***What mental model did you build?***
systematic thinking and Architecture, thinking in terms of systems and The use of AI as "code Review" rather "Q&A" and also a person who can fix the code when AI is offline

# modify my code to return position of failed index 
# Alternative function to check if input is palindrom

def palindrome_check(input):
    # create two pointer to compare charaacter from both end moving inward 
    left_pointer = 0
    right_pointer = len(input)-1

    # while left_pointer < right_pointer
    while left_pointer < right_pointer:
        # skip if character in unput is not alphalnumeric
        if not input[left_pointer].isalnum():
            left_pointer += 1
            continue  

        elif not input[right_pointer].isalnum():
            right_pointer -= 1
            continue

        # else compare character from both end in lower case
        else:
            if input[left_pointer].lower() != input[right_pointer].lower():
                return {
                    "is_palindrome":False,
                    "left_index_mIsmatch":left_pointer,
                    "char_left_index_mismatch":input[left_pointer],
                    "char_right_index_mismatch":input[right_pointer]
                }
            left_pointer += 1
            right_pointer -= 1
    return {
        "is_palindrome":True,
        "Index_mismatch":None
    }
# reflection
this code handles the expected constraints of this problem and work well, the program has a  linear time complexity of O(n) and space complexity O(1) 

# The Fairness Contract

# I will use AI when:

    After I've attempted a problem for at least 20 minutes

    To understand why my solution works/doesn't

    To explore alternatives after I have a working solution

    i will use the 15 minutes rules by trying to fix the code cursing the frustrtion 

    always  have solved similar task of any task given for deeper knowledge.



# I will NOT use AI when:

    I haven't tried the problem myself

    I'm taking an assessment or test

    I need to build fundamentals

    immidiately i ecounter an error

    when thinking in system

#   I know I'm using AI fairly when:

    I can explain my code without looking at AI's response

    I could solve similar problems without AI

    I feel more confident in my abilities

    I can explain and rewrite it in my own word before using it 

    i will always try to explain my code to other as prove to my knowledge

    in terms of logic i will reprodruce any AI-generatednlogic without looking   

***Sign***
Oduh Emmanuel Aba
***Date***
16 febuary 2026

# Real-World Scenario Analysis
***Interview***: if i always rely on AI, and i was ask to implement a caching system i would not be able to implement a caching system during an interview or task

***production bug at 2 AM***
if i rely only on AI and don't fully understand my code i wuill not be able to the bug

***New tech with little documentation:***
when a new tech comes and i have not learned to read docs and experiment, i will be frustratinig for me to learn about the tech or i will not be able to know more abou it.

# How does using AI fairly now prepare you for these scenarios?
for new concept or tech i will nuture a habbit of reading and refrencing documentation, get full fundamental understanding about concept,usage, and also explain it to someone to confirm my understanding, so at any time i can re-define my code, can isolate variable,an work on any new tech, and can write my exam without the need of AI.

# Building Irreplaceable Skills
|skills                      |Rate          |improvement plan                                                                                               |
|----------------------------|--------------|---------------------------------------------------------------------------------------------------------------|
|Problem Decomposition 	     |3/5           |breaking larg, complex challenge into smaller, more manageable part, branch out realated ideas to process steps|
|system thinkng              |3/5           |learn about workflow and how code or program work right, understand how system and large model works together  |
|Debugging Mindset           |4/5           |hands on practice with systematic toubleshooooting techniqes, not just giving AI the error for but doing it    |
|Conceptual Understanding    |4/5           |Reading more Programming Book(e.g structure and interpretation of computer programs), emphasizing fundamental understading|

# 3 specific actions this week to improve it without outsourcing thinking to AI.
This week on System Thinking learn more on how and why web request works: *Client, *DNS, *Server, *Database, *Response Build a tiny system: * input ----> Process ----> Store ----> Output (a Cli that save file that will make me think about the flow) Ask more system queston on any given task e.g (where would palindrome function live in real application, what call it, what handles errors)
This week on problem decomposition, learn more on how to breake large complex model into small step and solve them gain full undertstanding of ehat actually matter.git 