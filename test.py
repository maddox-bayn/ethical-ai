def palindrome_check(input):
    left_pointer = 0
    right_pointer = len(input)-1

    while left_pointer < right_pointer:
        if not input[left_pointer].isalnum():
            left_pointer += 1
        elif not input[right_pointer].isalnum():
            right_pointer -= 1
        else:
            if input[left_pointer].lower() != input[right_pointer].lower():
                return False
        return True
print(palindrome_check("MAdam")) 
print(palindrome_check("A man a plan a canal Panama"))  
print(palindrome_check("hello"))  
