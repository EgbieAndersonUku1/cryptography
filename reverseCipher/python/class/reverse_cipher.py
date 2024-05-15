
class ReverseCipher(object):

    def __init__(self, plain_text):
        self.plain_text  = plain_text
        self._translated = ""

    def encrypt(self):
        self._translate(self.plain_text)

    def decrypt(self):
       self._translate(self._translated)

    def _translate(self, text_to_translate):
        message_length = len(text_to_translate) - 1
        translated     = []

        while message_length >= 0:
            char = text_to_translate[message_length]
            translated.append(char)
            message_length -= 1
        self._translated = "".join(translated)

    def show(self):
        return self._translated


message = "This is the way of the dragon"

reverse_ciper = ReverseCipher(message)
reverse_ciper.encrypt()
cipher = reverse_ciper.show()
reverse_ciper.decrypt()
translated = reverse_ciper.show()

print(cipher)
print(translated)





