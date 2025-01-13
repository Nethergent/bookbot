def main():
    book_path = "books/frankenstein.txt"
    text = open_book_text(book_path)
    word_count = count_words(text)
    character_count = count_characters(text)

    print(f"{word_count} words found in the document.")
    print(f"{character_count}")

def open_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    count = len(text.split())
    return count

def count_characters(text):
    characters = {}
    
    # convert all characters to lowercase, avoiding duplicates
    text = text.lower()   
    
    for c in text:
        if c not in characters:
            characters[c] = 1

        else:
            characters[c] += 1
    return characters

main()
