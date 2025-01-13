def main():
    book_path = "books/frankenstein.txt"
    text = open_book_text(book_path)
    words = count_words(text)
    print(f"{words} words found in the document.")

def open_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    count = len(text.split())
    return count

main()
