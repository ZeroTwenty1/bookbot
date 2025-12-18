import sys
from stats import word_count, character_count, dict_sort

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents



def main():
    if len(sys.argv)==2:
        book = get_book_text(sys.argv[1])
        words = word_count(book)
        characters = character_count(book)
        sorted_list = dict_sort(characters)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")
        print(f"Found {words} total words")
        print("--------- Character Count -------")
        for item in sorted_list:
            char = item["char"]
            num = item["num"]
            if char.isalpha():
                print(f"{char}: {num}")
        print("============= END ===============")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
if __name__=="__main__":
    main()