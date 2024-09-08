def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    char_counts = get_char_counts(text)
    print(f"{word_count} words in text")
    print("the counts of each character are as follows :", char_counts)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_word_count(text):
    words = text.split()
    return len(words)

def get_char_counts(text):
    count_dict = {}
    lower_text = text.lower()
    for char in lower_text:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1
    return count_dict        


main()