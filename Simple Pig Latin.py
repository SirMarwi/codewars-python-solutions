def pig_it(text):
    pigged_text = []
    for word in text.split():
        if word.isalpha():
            pigged_text.append(f'{word[1:]}{word[0]}ay')
        else:
            pigged_text.append(word)
    return ' '.join(pigged_text)
