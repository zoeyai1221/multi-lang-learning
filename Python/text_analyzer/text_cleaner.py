import re


class TextCleaner:
    """
    Implements methods for text pre-processing
    """
    def clean(self, text):
        # Convert text to lowercase
        text = text.lower()

        # Replace commas with COMMA token
        text = text.replace(',', ' COMMA')

        # Define exceptions for common abbreviations
        exceptions = ["Mr.", "Mrs.", "Dr.", "etc."]

        # Replace periods in exceptions with a unique placeholder
        for exception in exceptions:
            text = text.replace(exception, exception.replace(".", "###"))

        # Remove all other punctuations except for apostrophes
        text = re.sub(r'[^a-zA-Z0-9\s\']', '', text)

        # Restore periods in exceptions
        for exception in exceptions:
            text = text.replace(exception.replace(".", "###"), exception)

        return text

    def split_into_sentences(self, text):
        # Split text into sentences based on periods
        sentences = re.split(r'(?<=[.!?])\s+', text)
        return sentences
