## Exercise 2: Designing Ethical Prompts
# Write three poorly designed prompts that might lead to biased/unsafe answers.
**poor prompt**: Write a short story about a brilliant surgeon and a helpful nurse saving a patient. Give them name and describe thir personalities.
**problematic**: it uses loaded adjectives(brilliant for the surgeon, helpfulfor the nurse) this align wiht historical gender sterotypes
**Hidden assumptions**:without explicit instruction to the contrary, many models will default to a male surgeon and a female nurse.
**proper_prompt_coontext**: a short story about a surgicalterm consisting of a surgeon and a nurse saving a patient. To aviod unconscious bais swap tradition gender role (if you need swap) focus their persnalities on thiertechnica expertise rather than nurturing or leadershi stereotype.
**improvement:** By asking to swap traditional roles, you forse the AI out of its statistical average

**poorprompt**: write a palindrome function for me.
**Cons & problematic:** And the task says impliment a palindrom inplemented in python that check if the reads the same backward and forwad, it should handle the following edge cases, None input, ?Extremely long Unicode strings?, Emojis?, Strings with only punctuation? Very large memory constraints?,Multilingual case folding issues?
**Hidden assumptions**: the AI will assume a very simple defult palindrome function in python 
**proper_prompt_coontext**:impliment a a palindrome function in python that check if the reads the same backward and forwad, it should handle the following edge cases, None input, ?Extremely long Unicode strings?, Emojis?, Strings with only punctuation? Very large memory constraints?,Multilingual case folding issues?
**improvement:**by givng detail prompt of original task

**poor prompt** write a python script that predicts if a loan application will default based on their social media activity and residential address.
***problematic**: it ask the AI to use proxies(social medial/address) for financial creditworthiness.it dosen't ask for a firness Audit
**Hidden assumptions**:The AI will find correlations that look like "logic" but are actually just "discrimination." For example, it might find that people who post in a certain language or live in a certain street default more often, leading to systemic exclusion of those groups.
**proper_prompt_coontext**:draft a conceptual outline for a credit scoring algorithm. Use verification financial indicators like repayment history and dept-to-income ratio. Strictly execlude nonfinancial proxies like social medial activity or residential address to prevent geographic and cultural bias.
***Improvement**:i am manually removing "Proxies"(address/social medial) that lead to discriment