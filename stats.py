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

def dict_sort(character_dict):
    dict_list = []
    for char, count in character_dict.items():
        dict_list.append({"char":char,"num":count})
    dict_list.sort(key=sort_on, reverse=True)
    return dict_list

def sort_on(item):
    return item["num"]