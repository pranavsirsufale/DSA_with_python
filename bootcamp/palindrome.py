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
# print(check_if_palindrome(pal))



# Lenght > 8
## altelst one letter should be capital
# it shold containe atlest 1 special character ( )
# shold not 



## ---> Length >= 8
## ---> Atleast one letter should be Capital
## ----> It should Contain atleast 1 special character (@,#,$,%,&)
##-----> should not contain "-"


password = 'aasdfdfdfAdrf@'
special_chars = ['@','#','$','%','&']

def check_pass(password):
    isSpecialChar = False
    isNotDash = True
    valid = True
    isCapital = False
    if len(password) < 8:
        valid = False
        return "Invalid Password , It has less than 8 Char"
    for i in password:
        if i.isupper():
            isCapital = True
    if not isCapital:
        return "There must atleast be a capital character"
    for i in special_chars:
        if i in password:
            isSpecialChar = True
    if not isSpecialChar:
        return "In the Password there must be a special character"
    if '-' in password:
        return 'The password must not contain the charater "-" '
    if isSpecialChar and isNotDash and valid and isCapital:
        return "Password Is Valid you can take it"
    else :
        return "Password is invalid"
print(check_pass(password))

    
    









