def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    letter_count = get_letter_count(text)
    sorted_list = sort_letter_list(letter_count)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")

    for letter in sorted_list:
        print(f"The '{letter["name"]}' character was found {letter["num"]} times")
    
    print("--- End report ---")
    
def sort_letter_list(letters):
    def sort_on(dict):
        return dict["num"]

    # change it into a list of dictioaryes
    letter_list = []
    for letter in letters:
        letter_dict = {"name": letter, "num" : letters[letter]}
        if letter_dict["name"].isalpha():
            letter_list.append(letter_dict)
    
    letter_list.sort(reverse=True, key=sort_on)

    return letter_list


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_letter_count(text):
    letter_count = {}
    for letter in text.lower():
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1    
    
    return letter_count

main()
