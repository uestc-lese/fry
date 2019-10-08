def break_words(stuff):
    """this function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """sorts the words."""
    return sorted(words)

def print_first_word(words):
    """prints the first words after popping it off."""
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """prints the last word after popping it off."""
    words = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """takes in a full sentence and returns the sorted words."""
    words = brake_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """print the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """sorts the words then prints the fist and last one."""
    words = sort_words(words)
    print_first_word(words)
    print_last_word(words)
