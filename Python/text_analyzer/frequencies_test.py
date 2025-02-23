from frequencies import NgramFrequencies

# Magic number replacement
FREQ_NUM_ONE = 1
TOP_NUM_TWO = 2
FREQ_NUM_HALF = 0.5
FREQ_NUM_ZERO = 0
"""
Test methods implemented in NgramFrequencies
"""


def test_add_item():
    freq = NgramFrequencies()
    freq.add_item("test")
    assert freq.total == FREQ_NUM_ONE
    assert freq.ngrams == {"test": 1}


def test_top_n_counts():
    freq = NgramFrequencies()
    freq.add_item("test")
    freq.add_item("test")
    freq.add_item("this")
    freq.add_item("this")
    freq.add_item("and")
    top_counts = freq.top_n_counts(TOP_NUM_TWO)
    assert top_counts == [("test", 2), ("this", 2)]


def test_top_n_freqs():
    freq = NgramFrequencies()
    freq.add_item("test")
    freq.add_item("test")
    freq.add_item("this")
    top_freqs = freq.top_n_freqs(TOP_NUM_TWO)
    assert top_freqs == [("test", 0.667), ("this", 0.333)]


def test_frequency():
    freq = NgramFrequencies()
    freq.add_item("test")
    freq.add_item("this")
    assert freq.frequency("test") == FREQ_NUM_HALF
    assert freq.frequency("this") == FREQ_NUM_HALF
    assert freq.frequency("and") == FREQ_NUM_ZERO


if __name__ == '__main__':
    test_add_item()
    test_top_n_counts()
    test_top_n_freqs()
    test_frequency()
