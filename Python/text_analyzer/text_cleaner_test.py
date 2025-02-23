from text_cleaner import TextCleaner


def test_clean():
    """
    Test methods implemented in TextCleaner
    """
    cleaner = TextCleaner()

    # Test converting text to lowercase
    text = "THIS IS A TEST"
    cleaned_text = cleaner.clean(text)
    assert cleaned_text == "this is a test"

    # Test replacing commas with COMMA token
    text = "This, is, a, test"
    cleaned_text = cleaner.clean(text)
    assert cleaned_text == "this COMMA is COMMA a COMMA test"

    # Test Handling abbreviations with periods
    text = "Mr. Smith and Dr. Johnson"
    cleaned_text = cleaner.clean(text)
    assert cleaned_text == "mr smith and dr johnson"

    # Test removing other punctuations and keeping apostrophes
    text = "This's a test!"
    cleaned_text = cleaner.clean(text)
    assert cleaned_text == "this's a test"


def test_split_into_sentences():
    cleaner = TextCleaner()

    # Test using periods to split into sentences
    text = "Hello. This is a test. Hello."
    sentences = cleaner.split_into_sentences(text)
    assert sentences == ['Hello.', 'This is a test.', 'Hello.']


if __name__ == '__main__':
    test_clean()
    test_split_into_sentences()
