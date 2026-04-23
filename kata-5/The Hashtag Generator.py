def generate_hashtag(s):
    new_s = '#' + s.lower().strip().title().replace(' ', '')
    if not s or len(new_s) > 140:
        return False
    else:  
        return new_s
    
print(generate_hashtag('Hello there thanks for trying my Kata'))
