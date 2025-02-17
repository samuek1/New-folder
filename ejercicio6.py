def anagrama(palabra,prefijo=""):
    if len(palabra) == 0:
        print (prefijo)


    for i in range(len (palabra)):
        anagrama(palabra[:i] + palabra[i+1:], prefijo + palabra[i])

print(anagrama("abc"))


