# Pig Latin

def pig_latin(word):
    if word[-1] in ".!?,;:":
        punctuation = word[-1]
        word = word[:-1]

    elif word[0] in "aAeEiIoOuU":
        return f"{word}way{punctuation}"
    
    elif word[0].isupper():
        return f"{word[1:].capitalize()}{word[0].lower()}ay{punctuation}"
    
    return f"{word[1:]}{word[0]}ay{punctuation}"


print(pig_latin("Python."))
