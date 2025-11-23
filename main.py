from stats import get_num_words, get_num_char


def get_book_text(filepath):
    with open(filepath) as input_file:
        file_contents = input_file.read()

    return file_contents


def main():
    file_contents = get_book_text("books/frankenstein.txt")
    get_num_words(file_contents)
    get_num_char(file_contents)

if __name__ == "__main__":
    main()