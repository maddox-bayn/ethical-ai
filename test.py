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
