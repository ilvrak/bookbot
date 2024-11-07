def get_book_text(book):
    book_path = f"books/{book}.txt"
    with open(book_path) as f:
        text = f.read()
        return text


def get_words_count(text):
    words_count = len(text.split())
    return words_count


def get_characters_count(text):
    text = text.lower()
    chars = {}
    for c in text:
        if c.isalpha():
            chars[c] = chars.get(c, 0) + 1
    return chars


def report(book):
    text = get_book_text(book)
    words_count = get_words_count(text)
    characters_count = get_characters_count(text)
    sorted_chars_count = sorted(characters_count.items(), key=lambda item: item[1], reverse=True)
    print('--- Begin report of books/frankenstein.txt ---')
    print(f'{words_count} words found in the document')
    print()
    for char, count in sorted_chars_count:
        print(f"The '{char}' character was found {count} times")
    print('--- End report ---')


def main():
    report('frankenstein')


if __name__ == '__main__':
    main()

