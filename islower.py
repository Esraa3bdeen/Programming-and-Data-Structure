def islower(c):
    # Check if c is a single character
    if len(c) != 1:
        raise ValueError("Input must be a single character")
    
    # Get the Unicode code point of the character
    char_code = ord(c)
    
    # Check if the character is lowercase
    # Lowercase letters in Unicode range from 97 ('a') to 122 ('z')
    if 97 <= char_code <= 122:
        return True
    else:
        return False