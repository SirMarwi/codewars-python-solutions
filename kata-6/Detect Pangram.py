def is_pangram(st):
    txt = ''.join( letter.lower() for letter in st if letter.isalpha() )
    uniq_txt_len = len(set(txt))

    return True if uniq_txt_len == 26 else False
    
