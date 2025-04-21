def get_book_text (file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

from stats import num_words

from stats import get_characters

from stats import characters_sorted


def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")

    # Read the book text from the file
    text = get_book_text("books/frankenstein.txt")

    # Print the word count
    print("----------- Word Count ----------")
    print(f"Found {num_words(text)} total words")

    # Get and sort the character counts
    character_counts = get_characters(text)
    sorted_characters = characters_sorted(character_counts)

    # Print the sorted character counts
    print("--------- Character Count -------")
    for item in sorted_characters:
        if item["character"].isalpha():  # Only print alphabetical characters
            print(f"{item['character']}: {item['count']}")

    print("============= END ===============")

main()

