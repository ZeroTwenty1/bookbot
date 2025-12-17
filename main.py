from stats import word_count, character_count

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents



def main():
    book = get_book_text("books/frankenstein.txt")
    words = word_count(book)
    characters = character_count(book)
    print(characters)

    print(f"Found {words} total words")

if __name__=="__main__":
    main()