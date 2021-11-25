# First - Last

def first_last(sequence):
    '''
    for every sequence passed, return the first and last
    elements with the same type of the original sequence
    passed
    '''

    return sequence[:1] + sequence[-1:]


print(first_last([1,2,3]))
print(first_last((1,2,3)))
print(first_last('abc'))
