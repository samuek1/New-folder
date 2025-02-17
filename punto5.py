def palindromo(text): 
    if len (text) <= 1: 
        return True
    if text[0] != text[-1]:
        return False
    return palindromo(text[1:-1])
print (palindromo("python"))
