def find_missing_letter(chars):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    lower_type = chars.islower()
    chars = chars.lower()
    char_start = alphabet.find(chars[0])
    
    for i in range(len(chars) -1):
        if chars[i + 1] != alphabet[i + char_loc + 1]:
            if lower_type == True:
                return alphabet[char_start + i + 1].upper()
            else:
                return alphabet[char_start + i + 1]


print(find_missing_letter(['a','b','c','e']))