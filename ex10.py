# Summing anything

def mysum(*items):  # the splat * operator build always a tuple
    if not items:  # in Python everything is considered True in an "if", excepte None, False, 0 and empty collections
        return items
    output = items[0]

    for item in items[1:]:
        output += item
    
    return output


print(mysum())
print(mysum(10, 20, 30, 40))
print(mysum('a', 'b', 'c', 'd'))
print(mysum([10, 20, 30], [40, 50, 60], [70, 80]))
