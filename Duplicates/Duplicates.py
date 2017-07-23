def duplicate_count(text):
 
    text = text.lower()
    copytext = text
    count = 0
    
    for char in text:
        copytext = copytext[1:] 
        if (char in copytext):
                copytext = copytext.replace(char, "")
                count+=1
    return count