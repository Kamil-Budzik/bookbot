from stats import get_book_text, count_book_words, count_characters, sort_characters
import sys


def main():
    argv = sys.argv
    if len(argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = argv[1]
    book = get_book_text(path)
    word_count = count_book_words(book)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")

    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")

    print("--------- Character Count -------")
    character_count = count_characters(book)
    
    character_count = count_characters(book)
    sorted_characters = sort_characters(character_count)

    for item in sorted_characters:
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

main()
