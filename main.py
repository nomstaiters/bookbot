def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    char_counts = get_char_counts(text)
    list_char_counts = list_of_dicts(char_counts)
    list_char_counts.sort(reverse=True, key=sort_on)
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print()
    for char in list_char_counts:
        if char['char'].isalpha():
            print(f"The '{char['char']}' character was found {char['num']} times")
    print("End of report")


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

#turn char counts into list of dictionaries
def list_of_dicts(dict):
    char_counts = []
    for name in dict:
        char_dict = {}
        char_dict["char"] = name
        char_dict["num"] = dict[name]
        char_counts.append(char_dict)
    return char_counts

def sort_on(dict):
    return dict["num"]

# test = "abracadabra boo"
# count_dict = get_char_counts(test)
# test_list = list_of_dicts(count_dict)
# test_list.sort(reverse=True, key=sort_on)
# print(test_list)

main()