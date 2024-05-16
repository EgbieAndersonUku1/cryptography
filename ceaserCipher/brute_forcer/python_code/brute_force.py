import sys

from string import ascii_lowercase
from os.path import join
from os import getcwd
from pathlib import Path
from time import sleep

# Get the directory of the current script
current_directory = Path(__file__).resolve().parent

# Add the parent directory of ceaser_cipher to the Python path
parent_folder = current_directory.parent.parent.parent
sys.path.append(str(parent_folder))

from ceaserCipher.python_code.python_class.ceaser_cipher import CaesarCipher
from detect_english.python_code.detector import EnglishDetector


class CeaserCipherBruteForcer:
    """A class for performing brute-force decryption of Caesar cipher text.

    Attributes:
        cipher_text (str or None): The cipher text to be decrypted.
        _ALPHABET (str): A string containing the lowercase English alphabet.
        _english_detector (EnglishDetector or None): An instance of EnglishDetector class
            for detecting valid English text.
        _ceaser_cipher (CaesarCipher): An instance of CaesarCipher class for performing
            Caesar cipher decryption.
    
    Methods:
        init(): Initialize the EnglishDetector instance.
        set_cipher_text(cipher: str): Set the cipher text to be decrypted.
        run_brute_force(silent: bool = True) -> tuple: Perform brute-force decryption
            of the cipher text and return the decrypted text and the decryption key.
        _display_text(show: bool, key: str, text: str, decrypted: bool): Display
            decryption progress and result.

    """
    def __init__(self) -> None:
      
        self.cipher_text = None
        self._ALPHABET = ascii_lowercase
        self._english_detector = None
        self._ceaser_cipher = CaesarCipher()

    def init(self):
        """Initialize the EnglishDetector instance."""
        english_detector = EnglishDetector()
        dictionary_file_path = join(getcwd(), "detect_english", "dictionary.txt")

        english_detector.set_dictionary_file_path(dictionary_file_path)
        english_detector.load_dictionary()
        self._english_detector = english_detector

    def set_cipher_text(self, cipher):
        """Set the cipher text to be decrypted.

        Args:
            cipher (str): The cipher text to be decrypted.
        """
        self.cipher_text = cipher

    def run_brute_force(self, silent=True) -> tuple:
        """Perform brute-force decryption of the cipher text.

        Args:
            silent (bool, optional): If True, only return the decrypted text and key without
                displaying decryption progress. If False, display decryption progress.
                Defaults to True.

        Returns:
            tuple: A tuple containing the decryption key and the decrypted text, or (-1, False)
                if decryption fails.
        """
        assert self.cipher_text, "The cipher text has not be set"

        self._english_detector.set_text(self.cipher_text)

        for letter in self._ALPHABET:
            self._ceaser_cipher.set_shift(letter)
            self._ceaser_cipher.set_text(self.cipher_text)
            decrypted_text = self._ceaser_cipher.translate("decrypt")
           
            self._english_detector.set_text(decrypted_text)

            found = self._english_detector.is_valid_english()

            if not silent:
                self._display_text(show=silent, key=letter, text=decrypted_text, decrypted=found)
            if found and silent:
                return (letter.upper(), decrypted_text)
            elif found and not silent:
                return (letter.upper(), decrypted_text)

        return (-1, False)

    def _display_text(self, show, key, text, decrypted):
        """Display decryption progress and result."""
        if not show:
            print("[-] Attempting to decrypt cipher text with key ({})...".format(key.upper()))
            print(text)
            print("\n")
        if decrypted and not show:
            print(f"[+] Successfully decrypted cipher text with the key {key.upper()}")
            print(text)
        print("\n")
        sleep(1)




text = """In fair Verona, where we lay our scene, From ancient grudge break to new mutiny, Where civil blood makes civil hands unclean, A pair of star-cross'd lovers take their life."""

# set up the cipher
shift_key = "w"
ceaser_cipher = CaesarCipher()
ceaser_cipher.set_shift(shift_key)
ceaser_cipher.set_text(text)
cipher_text = ceaser_cipher.translate()

print("Encrypted Cipher text encrypted with key ({})".format(shift_key))
print("-" * 80)
print(cipher_text)


print("Decrypted text")
print("-" * 80)


# set up the brute force
brute_forcer = CeaserCipherBruteForcer()
brute_forcer.init()
brute_forcer.set_cipher_text(cipher_text)

shift_key, decrypted_text = brute_forcer.run_brute_force(silent=False)


if (decrypted_text):
    print(f"Cipher text decoded with key: {shift_key}")
    print("\nDecrypted text", sep="\n")
    print(decrypted_text)
