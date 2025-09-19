from stats import get_book_text, count_book_words, count_characters 

def main():
    path = "./books/frankenstein.txt"
    book = get_book_text(path)
    word_count = count_book_words(book)
    print("Word count:", word_count)
    character_count = count_characters(book)
    print("Character count:", character_count)



main()
