# Sum of numbers
def my_sum(*param, j=0):
    n = 0
    for el in param:
        el += n
        n = el
    return n + j


# j is an optional parameter
# the splat operator allows the function to be called in the usual way
# our list becomes three separate arguments
print(my_sum(*[10, 12, 10], 2))


# Mean of numbers
def my_mean(*param):
    n = 0
    num_of_param = 0
    for el in param:
        num_of_param += 1
        el += n
        n = el
    return n / num_of_param


print(my_mean(*[10, 12, 10]))
