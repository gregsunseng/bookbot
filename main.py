def get_book_text (file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

from stats import num_words

from stats import get_characters


def main():
    frankensteins_characters = get_characters(get_book_text("books/frankenstein.txt"))
    print(f"{num_words(get_book_text ("books/frankenstein.txt"))} words found in the document")
    print()
    print(frankensteins_characters)

main()

