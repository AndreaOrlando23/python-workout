# Ubbi Dubbi

def ubbi_dubbi(word):
    output = []
    for letter in word:
        if letter in 'aeiou':
            output.append(f'ub{letter}')
        elif letter in 'AEIOU':
            output.append(f'Ub{letter.lower()}')
        else:
            output.append(letter)
        
    return ''.join(output)


print(ubbi_dubbi('Abba'))
