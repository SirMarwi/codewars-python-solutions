def solution(s):
    match = 0
    n = 0
    new_string = s
    for letter in s:
        if letter.isupper():
            new_string = new_string[:n + match] + ' ' + new_string[n + match:]
            match += 1
        n += 1
    return new_string



x = solution('breakCamelCaseCamelCase')
print(x)


