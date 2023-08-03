from spellchecker import SpellChecker
import os

def check_words(file_to_check):
    spell = SpellChecker()
    wrong = []

    with open(file_to_check, 'r') as i:
        for line in i:
            words = line.strip().split()
            for word in words:
                if word and word.lower() not in spell:
                    wrong.append(word)
    return wrong

def fix_words(misspelled_words):
    spell = SpellChecker()

    fixed_words = []
    for word in misspelled_words:
        suggestions = spell.candidates(word)
        if suggestions:
            fixed_words.append(suggestions.pop())  # Choose a suggested word
        else:
            fixed_words.append(word)  # Use the original word if no suggestions are available
    return fixed_words

def create_fixed_file(original_file_path, misspelled_words, fixed_words):
    new_file_path = original_file_path.replace('.txt', '_fixed.txt')

    with open(original_file_path, 'r') as f:
        content = f.read()

    for original_word, fixed_word in zip(misspelled_words, fixed_words):
        content = content.replace(original_word, fixed_word)

    with open(new_file_path, 'w') as f:
        f.write(content)

    return new_file_path

def mainfunction():
    fpath = input("Please enter the path to the file to spell check: ")
    f = os.path.isfile(fpath)

    if f:
        misspelled_words = check_words(fpath)
        fixed_words = fix_words(misspelled_words)
        new_file_path = create_fixed_file(fpath, misspelled_words, fixed_words)
        print(f"\nThe fixed text has been saved to: {new_file_path}")
    else:
        print("Invalid file path. Exiting.")

if __name__ == '__main__':
    mainfunction()
