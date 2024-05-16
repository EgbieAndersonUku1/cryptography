
const ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";


/**
 * Encrypts the given text using the Caesar cipher technique.
 * @param {string} text - The text to be encrypted.
 * @param {string} shiftLetter - The letter used for shifting the characters in the text.
 * @returns {string} The encrypted text.
 */
function encryptText(text, shiftLetter) {
    return transformText(text, shiftLetter, "encrypt");
}

/**
 * Decrypts the given text encrypted with the Caesar cipher technique.
 * @param {string} text - The text to be decrypted.
 * @param {string} shiftLetter - The letter used for shifting the characters in the text.
 * @returns {string} The decrypted text.
 */
function decryptText(text, shiftLetter) {
    return transformText(text, shiftLetter, "decrypt");
}


/**
 * Transforms the given text based on the specified mode (encrypt or decrypt).
 * @param {string} text - The text to be transformed.
 * @param {string} shiftLetter - The letter used for shifting the characters in the text.
 * @param {string} mode - The mode of transformation, either "encrypt" or "decrypt".
 * @throws {Error} Throws an error if the shift letter index could not be found.
 * @returns {string} The transformed text based on the specified mode.
 */
function transformText(text, shiftLetter, mode) {
    const translatedText = [];
    const NOT_FOUND = -1;

    if (toNumber(shiftLetter) === NOT_FOUND) {
        throw new Error("The shift letter index could not be found !!!")
    }
    for (char of text) {

        const charIndex = toNumber(char);
        let translatedChar = "";

        if (charIndex === NOT_FOUND)
            translatedText.push(char);

        switch (true) {
            case mode.toLowerCase() === "encrypt":
                translatedChar = encryptChar(char, shiftLetter);
                break;
            case mode.toLowerCase() === "decrypt":
                translatedChar = decryptChar(char, shiftLetter);
                break;
        }

        // manage the state of the original characters
        if (char === char.toLowerCase()) {
            translatedText.push(translatedChar.toLowerCase())
        } else {
            translatedText.push(translatedChar.toUpperCase())
        }
    }
    return translatedText.join("");
}


/**
 * Encrypts a single character using the Caesar cipher technique.
 * @param {string} char - The character to be encrypted.
 * @param {string} shiftLetter - The letter used for shifting the characters in the text.
 * @returns {string} The encrypted character.
 */
function encryptChar(char, shiftLetter) {
    // Ex(n) = x + n mod 26
    return toLetter((toNumber(char) + toNumber(shiftLetter)) % ALPHABET.length);
}


/**
 * Decrypts a single character encrypted with the Caesar cipher technique.
 * @param {string} char - The character to be decrypted.
 * @param {string} shiftLetter - The letter used for shifting the characters in the text.
 * @returns {string} The decrypted character.
 */
function decryptChar(char, shiftLetter) {
    // Dx(n) = x - n mod 26
    return toLetter((toNumber(char) - toNumber(shiftLetter)) % ALPHABET.length);
}


/**
 * Converts a character to its corresponding index in the alphabet.
 * @param {string} char - The character to be converted.
 * @returns {number} The index of the character in the alphabet.
 */
function toNumber(char) {
    return ALPHABET.indexOf(char.toUpperCase())
}


/**
 * Converts an index to its corresponding character in the alphabet.
 * @param {number} index - The index to be converted.
 * @returns {string} The character corresponding to the index in the alphabet.
 */
function toLetter(index) {
    return ALPHABET.charAt(index);
}


const text = "The way of the dragon";
const shiftLetter = "B";
const cipher = transformText(text, shiftLetter, "encrypt");

const decryptedCipherText = transformText(cipher, shiftLetter, "decrypt");
console.log(cipher);
console.log(decryptedCipherText)


