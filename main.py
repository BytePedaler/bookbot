import sys
from stats import get_num_words, get_num_char, sort_on


def get_book_text(filepath):
    with open(filepath) as input_file:
        file_contents = input_file.read()

    return file_contents


def main():
    if len(sys.argv) <= 1: 
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else: 
        file_contents = get_book_text(sys.argv[1])
        get_num_words(file_contents)
        chars = get_num_char(file_contents)
        sort_on(chars)

if __name__ == "__main__":
    main()