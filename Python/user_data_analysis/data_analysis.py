import re

# Use a regular expression to find all 2-letter strings
pattern = r'\b\w{2}\b'  # Matches 2-letter words

# Magic number replacement
INITIAL_VALUE = 0
INDEX_ONE = 1
INCREMENTAL_NUM = 1
LANGUAGE_INDEX_IN_FILE = -1
EMAIL_INDEX_IN_FILE = 3


class DataAnalysis:

    def __init__(self, file_name):
        # set up the necessary instance variables
        self.file_name = file_name
        self.lang_counts = {}
        self.lang_total_count = INITIAL_VALUE
        self.langs = []  # Initialize the list to store languages
        self.emails_country_code_counts = {}
        self.emails_domain = []
        self.emails_last_period = []
        self.emails_count = INITIAL_VALUE
        self.emails_country_code = []
        # Initialize the list to store 2-letter codes

    def read_data(self):
        # read the data and get the counts
        try:
            with open(self.file_name, 'r') as file:
                for line in file:
                    # language is in the last position in file
                    self.langs.append(
                        str(line.split(",")[LANGUAGE_INDEX_IN_FILE]).rstrip()
                        )
                    # email is in the fourth position, i.e.index three, in file
                    self.emails_domain.append(
                        str(line.split(",")[EMAIL_INDEX_IN_FILE]).rstrip()
                        )
        except FileNotFoundError:
            print("Can't find", self.file_name)
            return

    # Implement top_n_lang_freqs()
    # Should take a number N as an argument and return
    # an N-length list of tuples representing languages
    # and their frequencies in the data, ordered from
    # highest frequency to lowest.
    # get a list of dictionary items of languages and their counts
    def top_n_lang_freqs(self, N):
        # get rid of the first element 'language' in the first row in the file
        for lang in self.langs[INDEX_ONE:]:
            self.lang_total_count += INCREMENTAL_NUM
            if lang in self.lang_counts:
                self.lang_counts[lang] += INCREMENTAL_NUM
            else:
                self.lang_counts[lang] = INDEX_ONE

        # return a list of dictionary items sorted by count values
        sorted_lang_counts = sorted(self.lang_counts.items(),
                                    key=lambda x: x[INDEX_ONE],
                                    reverse=True)

        # return a list of dictionary items sorted by frequency
        sorted_lang_freqs = [(item, (count/self.lang_total_count))
                             for (item, count) in sorted_lang_counts]

        # return the top N higest frequency list of languages
        return sorted_lang_freqs[:N]

    # Implement top_n_country_tlds_freqs()
    # Should take a number N as an argument and return
    # an N-length list of tuples representing country (2-letter)
    # top-level domain identifiers (e.g. 'jp', 'uk', 'cn', 'ca')
    # and their frequencies as email domains the data, ordered
    # from highest frequency to lowest.
    def top_n_country_tlds_freqs(self, N):
        for email in self.emails_domain[INDEX_ONE:]:
            self.emails_last_period.append(email.split(".")[-INDEX_ONE])
            self.emails_count += INCREMENTAL_NUM

        # Top-level domains are always the last letters after
        # the last period in an email domain name, and country
        # codes are always exactly 2 letters long.
        # So if the letters after '.' in the email domain is two
        # letters, it should be a country code
        for i in self.emails_last_period:
            matches = re.findall(pattern, i)
            self.emails_country_code.extend(matches)

        # return a list of dictionary items of country code and their counts
        for country_code in self.emails_country_code:
            if country_code in self.emails_country_code_counts:
                self.emails_country_code_counts[country_code] += \
                    INCREMENTAL_NUM
            else:
                self.emails_country_code_counts[country_code] = INDEX_ONE

        # return a list of dictionary items sorted by count values
        sorted_country_code_counts = sorted(
            self.emails_country_code_counts.items(),
            key=lambda x: x[INDEX_ONE],
            reverse=True
            )

        # return a list of dictionary items sorted by frequency values
        sorted_country_code_freqs = [
            (item, (count/self.emails_count))
            for (item, count) in sorted_country_code_counts
            ]

        # return the top N higest frequency list of country code
        return sorted_country_code_freqs[:N]
