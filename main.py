def main():
    book_path = "books/frankenstein.txt"
    text = open_book_text(book_path)
    print (text)

def open_book_text(path):
    with open(path) as f:
        return f.read()

main()
