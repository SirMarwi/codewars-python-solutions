import re

def increment_string(string):
    match = re.search(r"\d+$", string)

    if match:
        number_str = match.group()
        sufix = str(int(number_str) + 1)

        sufix = sufix.zfill(len(number_str))

        return string[:match.start()] + sufix

    return string + '1'

print(increment_string('fo1o'))