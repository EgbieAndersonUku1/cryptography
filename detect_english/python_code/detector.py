from os import getcwd
from os.path import exists, join


class EnglishDetector(object):
    """
    A class for detecting English-like text.

    Attributes:
        text (str): The text to be analyzed.
        _english_words (dictionary): A set containing English words for quick lookup.

    Methods:
        __init__(): Initializes the class attributes.
        load_dictionary(dictionary_path="dictionary.txt"): Loads a dictionary of English words from a file.
        set_text(text): Sets the text to be analyzed.
        is_valid_english(word_percentage_match=20, letters_percentage_match=80):
            Determines if the text resembles English based on the percentage of English words and letters.
        _get_num_of_english_word_percentage(): Calculates the percentage of English words in the text.
    """

    def __init__(self) -> None:
        self.text           = ""
        self._english_words = {}
        self.file_path      = ""

    def load_dictionary(self):
        """
        Loads a dictionary of English words from a file.

        Args:
            dictionary_path (str, optional): The path to the dictionary file. Default is "dictionary.txt".
        """
        running = True

        try:
            with open(self.file_path) as f:
                while running:
                    word = f.readline().strip()
                    if not word:
                        running = False
                    else:
                        self._english_words[word.lower()] = True
        except Exception as e:
            raise Exception(f"Expected dictionary but got {e} error")

    def set_text(self, text):
        """
        Sets the text to be analyzed.

        Args:
            text (str): The text to be analyzed.
        """
        self.text = text

    def set_dictionary_file_path(self, file_path):
        """
        Sets the file path
        Args:
            text (str): The file path
        """
        if not exists(file_path):
            raise Exception("The file was not found!!")
        self.file_path = file_path

    def is_valid_english(self, word_percentage_match=75):
        """
        Determines if the text resembles English based on the percentage of English words and letters.

        Args:
            word_percentage_match (int, optional): The minimum percentage of English words required for a match.
                Default is 75.

        Returns:
            bool: True if the text resembles English, False otherwise.
        """
        return self._get_num_of_english_word_percentage() >= word_percentage_match

    def _get_num_of_english_word_percentage(self):
        """
        Calculates the percentage of English words in the text.

        Returns:
            float: The percentage of English words in the text.
        """
        words = self.text.split()
        percentage = 100

        if not words:
            return 0
        word_match = sum(
            (
                1
                for word in words
                if self._english_words.get(word.lower().strip(), False)
            )
        )

        return (word_match / len(words)) * percentage


if __name__ == "__main__":

    text = "This is the way of the dragon egbie"
    dictionary_file_path = join(getcwd(), "detect_english", "dictionary.txt")

    detector = EnglishDetector()
    detector.set_text(text)
    detector.set_dictionary_file_path(dictionary_file_path)
    detector.load_dictionary()

    is_valid_english = detector.is_valid_english()
    print(f"is the passage a valid English text: {is_valid_english}")

    text = "???????????????????????????????dd??? word word"
    detector.set_text(text)
    is_valid_english = detector.is_valid_english()
    print(f"is the passage a valid English text: {is_valid_english}")
