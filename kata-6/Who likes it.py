def likes(names):
    n = len(names)
    if n == 0:
        return 'no one likes this'
    if n == 1:
        return f'{names[0]} likes this'
    if n == 2:
        return f'{names[0]} and {names[1]} like this'
    if n == 3:
        return f'{names[0]}, {names[1]} and {names[2]} like this'
    else:
        rest = n - 2
        return f'{names[0]}, {names[1]} and {rest} others like this'