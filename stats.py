def get_book_text(path_to_file: str) -> str:
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents


def count_book_words(book_content: str) -> int:
    splitted = book_content.split()
    return len(splitted)

def count_characters(text: str) -> dict[str, int]:
    text = text.lower() 
    characters: dict[str, int] = {}
    for c in text:
        characters[c] = characters.get(c, 0) + 1
    return characters
