def word_count(book):
    word_counter = 0
    for word in book.split():
        word_counter +=1
    return word_counter

def character_count(book):
    character_dict = {}
    for word in book.lower():
        if word not in character_dict:
            character_dict[word] = 1
        elif word in character_dict:
            character_dict[word] += 1
    return character_dict
