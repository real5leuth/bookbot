def count_words(text):
    return len(text.split()) 

def count_letters(text):
    letters = {}
    for letter in text.lower():
        if letter.isalpha():
            letters[letter] = letters.get(letter, 0) + 1
    return letters

def get_count(letters):
    return letters["num"]

def sort_letter_counts(letters):
    # Convert dictionary to list of dictionaries with char and num keys
    letter_list = [{"char": char, "num": count} for char, count in letters.items()]
    # Sort the list by num in descending order using the get_count function
    letter_list.sort(reverse=True, key=get_count)
    return letter_list

