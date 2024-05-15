

function encrypt(plainText) {
   return translate(plainText);

}

function decrypt(cipher) {
    return translate(cipher);
}

function translate(text) {
    let textLength = text.length;
    let translated = [];

    while (textLength >= 0) {
        let lastChar = text[textLength];
        translated.push(lastChar);
        textLength -= 1;
    }

    return translated.join("");
}

const plainText  = "The way of the dragon";
const cipher     = encrypt(plainText);
const normalText = decrypt(cipher);

console.log(cipher);
console.log(normalText);