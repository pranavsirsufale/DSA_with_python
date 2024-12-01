def naive_pattern_match(text,pattern):
    n = len(text)
    m = len(pattern)
    till_run = (n-m) + 1
    found = False       # initically match found is flase 

    #? we cannot use return and yeild together in a function /method, these create inconsistency 


    for i in range(till_run):
        if text[i:i+m] == pattern :
            yield f'pattern found at index {i} to {i+m}'        # yeild keyworkd simultnenously return's the vlaue but without closing the function until loop is closed
            found = True                                        # change the flag found = True
    if not found :
        yield f'for the pattern {pattern},No Match found'        
    
   
        
text = 'abarakadabaraabadabaaavaaba'
pattern = 'aba'

for found in naive_pattern_match(text,pattern):
    print(found)


'''
output ::::
pattern found at index 0 to 3
pattern found at index 8 to 11
pattern found at index 13 to 16
pattern found at index 17 to 20
pattern found at index 24 to 27
'''


