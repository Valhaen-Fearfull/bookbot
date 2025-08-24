import sys
from stats import (
    get_num_words,
    chars_dict_to_sorted_list,
    get_chars_dict,
)

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book1> [path_to_book2] ...")
        sys.exit(1)
    
    # Get all book paths (everything after the script name)
    book_paths = sys.argv[1:]
    
    for book_path in book_paths:
        analyze_book(book_path)
        print()  # Add a blank line between books

def analyze_book(book_path):
    try:
        text = get_book_text(book_path)
        num_words = get_num_words(text)
        chars_dict = get_chars_dict(text)
        chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
        print_report(book_path, num_words, chars_sorted_list)
    except FileNotFoundError:
        print(f"Error: Could not find book at {book_path}")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()