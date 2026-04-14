def duplicate_count(text):
    duplicates= {}
    text = text.upper()
    
    for sign in text:
        if sign in duplicates:
            duplicates[sign] += 1
        else:
            duplicates[sign] = 1
    
    sign_duplicates= 0 
    for sign in duplicates.values():
        if sign > 1:
            sign_duplicates += 1
        
    return sign_duplicates