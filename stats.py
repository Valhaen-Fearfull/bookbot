def get_num_words(file_contents):
    words = file_contents.split()
    num_words = len(words)
    return num_words

def get_char_count(file_contents):
    lower_char = str.lower(file_contents)
    chars = {}
    for char in lower_char:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars  

def sort_on(chars):
    return chars["num"]

def sorted_dict(chars):
    char_list = []
    for character in chars:
        char_dict = {"char": character, "num": chars[character]}
        char_list.append(char_dict)
        
    char_list.sort(reverse=True, key=sort_on)
    return char_list
    
