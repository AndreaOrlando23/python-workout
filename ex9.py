# First - Last

def first_last(sequence):
    '''
    for every sequence passed, return the first and last
    elements with the same type of the original sequence
    passed
    '''

    return sequence[:1] + sequence[-1:]


print(first_last([1,2,3]))  # use list
print(first_last((1,2,3)))  # use tuple
print(first_last('abc'))  # use string


'''
ex 9.2
Writ a function that takes list or tuple of numbers.
Return a two-elements list, containing (respectively)
the sum of the even-indexed numbers and the sum of the odd-indexed numbers.
So calling the function as even_odd_sums([10, 20, 30, 40, 50, 60])
you'll get back [90, 120]
'''

def even_odd_sums(sequence):
    even = []
    odd = []
    for index, value in enumerate(sequence):
        if index % 2 == 0:
            even.append(value)
        else:
            odd.append(value)
    
    return [sum(even), sum(odd)]


print(even_odd_sums([10, 20, 30, 40, 50, 60]))  # list
print(even_odd_sums((10, 20, 30, 40, 50, 60)))  # tuple
