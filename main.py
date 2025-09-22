from stats import get_book_text, count_book_words, count_characters, sort_characters

def main():
    path = "./books/frankenstein.txt"
    book = get_book_text(path)
    word_count = count_book_words(book)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")

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
