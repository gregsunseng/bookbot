import sys

args= sys.argv

if len(args) < 2:
    print("Usag" \
    "e: python3 main.py <path_to_book>")
    sys.exit(1)

script = args[0]
file_path = args[1]

if len(args) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


def get_book_text (file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

from stats import num_words

from stats import get_characters

from stats import characters_sorted


def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}")

    # Read the book text from the file
    text = get_book_text(file_path)

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

