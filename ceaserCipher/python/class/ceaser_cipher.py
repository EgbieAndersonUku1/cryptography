from string import ascii_letters


class CaesarCipher:
    """Class for performing encryption and decryption using Caesar cipher."""

    def __init__(self):
        """Initialize CaesarCipher object."""
        self.text                = ""
        self.shift_letter        = ""
        self._shift_letter_index = ""

    def set_text(self, text):
        """Set the text to be encrypted or decrypted.

        Args:
            text (str): The text to be encrypted or decrypted.
        """
        self.text = text

    def set_shift(self, shift_letter):
        """Set the shift letter for encryption or decryption.

        Args:
            shift_letter (str): The letter used for shifting the cipher.
        """
        assert len(shift_letter) == 1, "Must be a single letter ranging from A-Z or a-z"
        assert shift_letter.isalpha(), "The must a letter"
        self.shift_letter = shift_letter.lower()

        try:
            self._shift_letter_index = ascii_letters.index(self.shift_letter.lower())
        except ValueError:
            raise Exception("The shift letter must be a letter between A-Z")

    def translate(self, mode="encrypt"):
        """Translate the text using Caesar cipher.

        Args:
            mode (str, optional): The mode of translation, either 'encrypt' or 'decrypt'. 
            Defaults to 'encrypt'.

        Returns:
            str: The translated text.
        """
        translated_text = []

        for char in self.text:
            translated_char = self._translate_char(char, mode)

            # maintain the original capital or lowercase for the word
         
            if char.islower():
                translated_text.append(translated_char.lower())
            else:
                translated_text.append(translated_char.upper())

        return "".join(translated_text)

    def _translate_char(self, char, mode="encrypt"):
        """Translate a single character using Caesar cipher.

        Args:
            char (str): The character to be translated.
            mode (str, optional): The mode of translation, either 'encrypt' or 'decrypt'. 
            Defaults to 'encrypt'.

        Returns:
            str: The translated character.
        """
        char_index = ascii_letters.find(char.lower())
        NOT_FOUND = -1

        if mode.lower() not in ["encrypt", "decrypt"]:
            raise Exception("The encryption must be either decrypt or encrypt!!!")
        elif char_index == NOT_FOUND:
            return char
        elif mode.lower() == "encrypt":
            translated_char_index = (char_index + self._shift_letter_index) % len(ascii_letters)
        elif mode.lower() == "decrypt":
            translated_char_index = (char_index - self._shift_letter_index) % len(ascii_letters)
        return ascii_letters[translated_char_index]


# Example usage
plain_text = "The way of the dragon."
caesar_cipher = CaesarCipher()

# Encrypt
caesar_cipher.set_text(plain_text)
caesar_cipher.set_shift("b")
cipher_text = caesar_cipher.translate()

# Decrypt
caesar_cipher.set_text(cipher_text)
text = caesar_cipher.translate("decrypt")



print(cipher_text)
print(text)

