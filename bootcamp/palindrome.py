def check_if_palindrome(text):
    end = len(text)-1
    palindrome = True
    for i in text:
        if i == text[end]:
            end -= 1
        else : 
            palindrome = False
    return palindrome

pal = 'abcba'
print(check_if_palindrome(pal))









