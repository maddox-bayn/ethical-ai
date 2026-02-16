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

# Test Cases
print(palindrome_check("")) 
print(palindrome_check("A man a plan a canal Panama"))  
print(palindrome_check("hello"))  
