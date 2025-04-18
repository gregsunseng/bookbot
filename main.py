def get_book_text (file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

from stats import num_words

from stats import get_characters


def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"{num_words(get_book_text ("books/frankenstein.txt"))} words found in the document")
    print("--------- Character Count -------")
    print(get_characters(get_book_text("books/frankenstein.txt")))

main()

