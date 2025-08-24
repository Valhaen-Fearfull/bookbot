import sys
if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

from stats import get_num_words, get_char_count, sorted_dict

def get_book_text(filepath=sys.argv[1]):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    file_contents = get_book_text(filepath)
    num_words = get_num_words(file_contents)
    char_count = get_char_count(file_contents)
    sorted_chars = sorted_dict(char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("---------- Word Count -----------")
    print(f"Found {num_words} total words")
    print("------- Character Count ---------")
    for item in sorted_chars:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']} ")
    
main()
        
