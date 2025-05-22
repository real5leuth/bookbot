import sys

from stats import count_words, count_letters, sort_letter_counts

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    book_path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    
    text = get_book_text(book_path)
    word_count = count_words(text)
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    
    print("--------- Character Count -------")
    letter_counts = sort_letter_counts(count_letters(text))
    for letter_dict in letter_counts:
        print(f"{letter_dict['char']}: {letter_dict['num']}")
    
    print("============= END ===============")

def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()

main()