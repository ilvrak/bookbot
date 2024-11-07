def get_book_text(book):
    book_path = f"books/{book}.txt"
    with open(book_path) as f:
        text = f.read()
        return text


def get_words_count(text):
    words = text.lower().split()
    words_count = len(words)
    word_dict = {}
    for word in words:
        word = word.strip(",.!?\"';:-()[]{}")
        word_dict[word] = word_dict.get(word, 0) + 1
    return words_count, word_dict


def get_char_dict(text):
    text = text.lower()
    chars = {}
    for c in text:
        if c.isalpha():
            chars[c] = chars.get(c, 0) + 1
    return chars


def report(book):
    text = get_book_text(book)
    words_count, word_dict = get_words_count(text)
    char_dict = get_char_dict(text)
    sorted_char_dict = sorted(char_dict.items(), key=lambda item: item[1], reverse=True)
    sorted_word_dict = sorted(word_dict.items(), key=lambda item: item[1], reverse=True)
    print(f'--- Begin report of books/{book}.txt ---')
    print(f'{words_count} words found in the document')
    print()
    for char, count in sorted_char_dict:
        print(f"The '{char}' character was found {count} times")
    print()
    for word, count in sorted_word_dict:
        print(f"The '{word}' word was found {count} times")
    print()
    print('--- End report ---')


def main():
    report('frankenstein')


if __name__ == '__main__':
    main()

