from string import ascii_letters


def encrypt(char, shift_letter):
    """Encrypts a character using a Caesar cipher.

    :param char: The character to encrypt.
    :param shift_letter: The letter between A-Za-z that will be used for the encryption.
    :return: The encrypted character.

    The Caesar cipher encryption formula is: En(x) = (x + n) mod 26,
    where x is the character to encrypt, and n is the index of the shift_letter
    in the alphabet (0-indexed).
    """
    cipher_index = (
        get_shift_letter_index(char) + get_shift_letter_index(shift_letter)
    ) % len(ascii_letters)
    return to_letter(cipher_index)


def decrypt(char, shift_letter):
    """Decrypts a character encrypted using a Caesar cipher.

    :param char: The character to decrypt.
    :param shift_letter: The letter between A-Za-z that was used for the encryption.
    :return: The decrypted character.

    The Caesar cipher decryption formula is: Dn(x) = (x - n) mod 26,
    where x is the encrypted character, and n is the index of the shift_letter
    in the alphabet (0-indexed).
    """
    cipher_index = (
        get_shift_letter_index(char) - get_shift_letter_index(shift_letter)
    ) % len(ascii_letters)
    return to_letter(cipher_index)


def translate(func, shift_letter, text):
    """Translates text using a specified encryption or decryption function and a shift letter.

    :param func: The encryption or decryption function to apply to each alphabetic character.
    :param shift_letter: The letter between A-Za-z used for encryption or decryption.
    :param text: The text to translate.
    :return: The translated text.

    This function iterates through each character in the input text. If the character is alphabetic,
    it applies the provided encryption or decryption function (`func`) to translate it. The translation
    preserves the case of the original character. Non-alphabetic characters remain unchanged.
    The translated text is then returned as a single string.

    Example:
    >>> translate(encrypt, 'b', 'Hello, World!')
    'Jgnnq, Yqtnf!'
    >>> translate(decrypt, 'b', 'Jgnnq, Yqtnf!')
    'Hello, World!'

    """
    translated_list = []
    translated_char = ""

    for char in text:
        if char.isalpha():
            translated_char = func(char, shift_letter)
        else:
            translated_char = char

        # preserve the state of the original character
        if char.islower():
            translated_list.append(translated_char.lower())
        else:
            translated_list.append(translated_char.upper())
    return "".join(translated_list)


def get_shift_letter_index(shift_letter):
    """Returns the index of the specified letter in the ASCII alphabet.

    :param shift_letter: The letter whose index is to be retrieved.
    :return: The index of the letter in the ASCII alphabet (0-indexed), or None if the letter is not found.

    This function attempts to find the index of the specified letter in the ASCII alphabet,
    regardless of its case. If the letter is found, its index is returned.
    If the letter is not found in the alphabet, None is returned.

    Example:
    >>> get_shift_letter_index('A')
    0
    >>> get_shift_letter_index('z')
    25
    >>> get_shift_letter_index('@')
    None
    """
    try:
        return ascii_letters.index(shift_letter.lower())
    except ValueError:
        return None


def to_letter(shift_index):
    """Returns the letter corresponding to the specified index in the ASCII alphabet.

    :param shift_index: The index of the letter to retrieve.
    :return: The letter corresponding to the index in the ASCII alphabet, or None if the index is out of range.

    This function attempts to retrieve the letter corresponding to the specified index in the ASCII alphabet.
    If the index is within the valid range, the corresponding letter is returned.
    If the index is out of range, None is returned.

    Example:
    >>> to_letter(0)
    'A'
    >>> to_letter(25)
    'Z'
    >>> to_letter(30)
    None
    """
    try:
        return ascii_letters[shift_index]
    except IndexError:
        return None


text = "The way of the dragon"
shift_letter = "b"

cipher = translate(encrypt, shift_letter=shift_letter, text=text)
text = translate(decrypt, shift_letter=shift_letter, text=cipher)


print(cipher)
print(text)
