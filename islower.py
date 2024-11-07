def islower(c):
    
    if len(c) != 1:
        raise ValueError("Input must be a single character")
    
    
    char_code = ord(c)
    
    
    if 97 <= char_code <= 122:
        return True
    else:
        return False
