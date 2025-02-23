from text_cleaner import TextCleaner
from frequencies import NgramFrequencies


def main():
    """
    The main function to get the language information
    of file corpse_bride.txt
    """
    # Read the text from the 'corpse_bride.txt' file
    with open('corpse_bride.txt', 'r') as file:
        text = file.read()

    # Initialize TextCleaner to preprocess the text
    cleaner = TextCleaner()

    # Preprocess the text
    cleaned_text = cleaner.clean(text)

    # Split the text into sentences
    sentences = cleaner.split_into_sentences(cleaned_text)

    unigrams = NgramFrequencies()
    bigrams = NgramFrequencies()
    trigrams = NgramFrequencies()

    # Iterate through tokens to collect n-grams
    for sentence in sentences:
        words = sentence.split()
        for i in range(len(words)):
            # Add unigrams
            unigrams.add_item(words[i])

            if i < len(words) - 1:
                # Add bigrams
                bigram = f'{words[i]}_{words[i+1]}'
                bigrams.add_item(bigram)

                if i < len(words) - 2:
                    # Add trigrams
                    trigram = f'{words[i]}_{words[i+1]}_{words[i+2]}'
                    trigrams.add_item(trigram)

    # Get and print top N unigrams, bigrams, and trigrams
    # by counts and frequencies
    top_unigrams_freqs = unigrams.top_n_freqs(10)
    top_bigrams_freqs = bigrams.top_n_freqs(10)
    top_trigrams_freqs = trigrams.top_n_freqs(10)

    print("Top 10 unigrams:")
    for i in top_unigrams_freqs:
        print(' '*4, i)
    print("Top 10 bigrams:")
    for i in top_bigrams_freqs:
        print(' '*4, i)
    print("Top 10 trigrams:")
    for i in top_trigrams_freqs:
        print(' '*4, i)


main()
