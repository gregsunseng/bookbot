def get_book_text (file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def num_words(get_book_text):
    return (len(get_book_text.split()))



def main():
    print(f"{num_words(get_book_text ("books/frankenstein.txt"))} words found in the document")

main()

