def num_words(get_book_text):
    return (len(get_book_text.split()))

def get_characters(get_book_text):
    character_dict = {}
    for character in get_book_text:
       if character.lower() in character_dict:
           character_dict[character.lower()] += 1
       else:
           character_dict[character.lower()] = 1
    return character_dict
          
           
        
    

