/**
 * CeaserCipher class provides methods for encrypting and decrypting text using the Caesar cipher technique.
 * @class
 */
class CeaserCipher {
   
    constructor() {
      
        this.text        = null;
        this.shiftLetter = null;
        this._ALPHABET   = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    }

    /**
     * Sets the text to be encrypted or decrypted.
     * @param {string} text - The text to be set.
     */
    setText(text) {
        this.text = text;
    }

    /**
     * Sets the letter used for shifting in the cipher.
     * @param {string} char - The character to set as the shift letter.
     * @throws {Error} Throws an error if the shift character is not a valid letter.
     */
    setShiftLetter(char) {
        this._isCharValid(char);
        this.shiftLetter = char;
    }

    /**
     * Encrypts the text using the Caesar cipher technique.
     * @returns {string} The encrypted text.
     */
    encryptText() {
        return this._transformText(this._encrypt.bind(this));
    }
    
    /**
     * Decrypts the text using the Caesar cipher technique.
     * @returns {string} The decrypted text.
     */
    decryptText() {
        return this._transformText(this._decrypt.bind(this));
    }

    /**
     * Transforms the text using the specified transformation function.
     * @param {function} transformFunction - The transformation function.
     * @returns {string} The transformed text.
     * @private
     */
    _transformText(transformFunction) {
        const NOT_FOUND = -1;
        this.text = this.text.split("").map(char => {
            const charIndex = this._toNumber(char)
            if (charIndex === NOT_FOUND) {
                return char
            } else  {
                const translateChar = transformFunction(char);
                return char === char.toUpperCase() ? translateChar.toUpperCase() : translateChar.toLowerCase();
            }
        }).join("");
        return this.text;
    }

    /**
     * Encrypts the specified character using the Caesar cipher mathematical formula Ex(n) = x + n mod 26.
     * @param {string} char - The character to encrypt.
     * @returns {string} The encrypted character.
     * @private
     */
    _encrypt(char) {
        const cipherCharIndex = (this._toNumber(char) + this._toNumber(this.shiftLetter)) % this._ALPHABET.length;
        return this._toLetter(cipherCharIndex);
    }

    /**
     * Decrypts the specified character using the Caesar cipher formula Dx(n) = x - n mod 26.
     * @param {string} char - The character to decrypt.
     * @returns {string} The decrypted character.
     * @private
     */
    _decrypt(char) {
        const cipherCharIndex = (this._toNumber(char) - this._toNumber(this.shiftLetter)) % this._ALPHABET.length;
        return this._toLetter(cipherCharIndex);
    }

    /**
     * Converts the specified character to its corresponding index in the alphabet.
     * @param {string} char - The character to convert.
     * @returns {number} The index of the character in the alphabet.
     * @private
     */
    _toNumber(char) {
        return this._ALPHABET.indexOf(char.toUpperCase())
    }

    /**
     * Converts the specified index to its corresponding character in the alphabet.
     * @param {number} index - The index to convert.
     * @returns {string} The character at the specified index in the alphabet.
     * @private
     */
    _toLetter(index) {
        const START_INDEX = 0;
        const END_INDEX   = 25;
        
        if (!Number.isInteger(index)) {
            console.error("Index must be an integer.");
            return null;
        }

        return index >= START_INDEX && index <= END_INDEX ? this._ALPHABET[index] : null;
    }

    /**
     * Validates whether the specified character is a valid letter in the alphabet.
     * @param {string} char - The character to validate.
     * @throws {Error} Throws an error if the character is not a valid letter.
     * @private
     */
    _isCharValid(char) {
        const isValid = this._ALPHABET.indexOf(char.toUpperCase())
        const NOT_FOUND = -1
        if (isValid === NOT_FOUND) {
            throw new Error("The shift character must be between A-Z including A and Z")
        }
    }
}

// Example usage uncomment to use and comment out export default CeaserCipher:
// const ceaerCipher = new CeaserCipher()
// ceaerCipher.setShiftLetter("b");
// ceaerCipher.setText("The way of the dragon.");

// const cipher = ceaerCipher.encryptText();
// console.log(cipher);

// ceaerCipher.setText(cipher);
// const text = ceaerCipher.decryptText();

// console.log(text);

export default CeaserCipher;