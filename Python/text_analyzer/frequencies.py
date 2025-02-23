
# Magic number replacement
ROUND_PLACES = 3
INDEX_ONE = 1
NUM_ONE = 1
INCREMENTAL_VALUE = 1
INITIAL_VALUE = 0


class NgramFrequencies:
    """
    Hold a dictionary of the corresponding n-grams with counts
    and
    hold a total value containing the total counts for ngrams
    """
    def __init__(self):
        self.ngrams = {}
        self.total = INITIAL_VALUE

    def add_item(self, ngram):
        """
        Take an n-gram and increments its count in the dictionary
        """
        if ngram in self.ngrams:
            self.ngrams[ngram] += INCREMENTAL_VALUE
        else:
            self.ngrams[ngram] = NUM_ONE
        self.total += INCREMENTAL_VALUE

    def top_n_counts(self, n):
        """
        Return a list of items sorted on the count
        with the most frequent first
        """
        sorted_ngrams = sorted(self.ngrams.items(), key=lambda x: x[INDEX_ONE],
                               reverse=True)
        return sorted_ngrams[:n]

    def top_n_freqs(self, n):
        """
        Return a list with frequencies instead of counts
        """
        sorted_freqs = [(item, round((count / self.total), ROUND_PLACES))
                        for item, count in self.ngrams.items()]
        sorted_freqs = sorted(sorted_freqs, key=lambda x: x[INDEX_ONE],
                              reverse=True)
        return sorted_freqs[:n]

    def frequency(self, ngram):
        """
        Take an item and return its frequency
        """
        if ngram in self.ngrams:
            return self.ngrams[ngram] / self.total
        return INITIAL_VALUE
