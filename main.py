
def main():
    path_to_file = "books/frankenstein.txt"
    report = write_report(path_to_file)
    print(report)

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def count_words(text):
    return len(text.split())

def get_character_count(text):
    character_count = {}
    text = text.lower()
    
    text = ''.join(char for char in text if char.isalpha())
    
    for character in text:
        if character in character_count:
            character_count[character] += 1
        else:
            character_count[character] = 1
            
    return character_count

def write_report(path_to_file):
    text = get_book_text(path_to_file)
    word_count = count_words(text)
    character_count = get_character_count(text)
    
    sorted_characters = sorted(character_count.items(), key=lambda x: x[1], reverse=True)
    
    characters = ""
    
    for character, count in sorted_characters:
        characters += f"The '{character}' was found {count} times\n"
    
    report_text = f"--- Begin report of book {path_to_file} ---\n{word_count} words in the document\n\n{characters}"
    
    return report_text

if __name__ == "__main__":
    main()
    