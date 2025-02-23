from extra_word_ladder import WordLadder


def main():
    """Run an interactive command line to let the user
    input word pairs and generate word ladders"""
    english_words = load_words()

    while True:
        w1, w2 = input("> ").split()
        # Create a WordLadder object
        wl = WordLadder(w1, w2, english_words)
        # Generate the word ladder
        word_ladder = wl.make_ladder()
        # if word_ladder:
        print("Ladder: ", word_ladder)
        # else:
        #     print("No ladder found.")


def load_words():
    """Load words from complete wordlist file"""
    # We're creating a dictionary keyed on word
    # length, so that we can quickly get to a set of
    # words of a given length.
    valid_words = {}
    with open('words_alpha.txt') as word_file:
        for w in word_file.read().split():
            if len(w) in valid_words.keys():
                # Add to an existing set
                valid_words[len(w)].add(w)
            else:
                # Initialize a set with one element
                valid_words[len(w)] = {w}
    return valid_words


main()

# Try with:
# a aa
# a hat
