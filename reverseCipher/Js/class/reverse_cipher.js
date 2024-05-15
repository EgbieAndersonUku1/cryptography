
class ReverseCipher{
    
    constructor (plainText) {
        this.plainText   = plainText;
        this._translated = null;
    }

    encrypt() {
        let translated = []

        for (let i = this.plainText.length - 1; i >= 0; i--) {
            translated.push(this.plainText[i]);
        }
        this._translated = translated.join("");
    }

    decrypt() {

        if (!(this._translated)) {
            return;
        }

        let translated = []

        for (let i = this._translated.length - 1; i >= 0; i--) {
            translated.push(this._translated[i]);
        }
        this._translated = translated.join("");
    }

    show() {
        return this._translated;
    }
}

const plainText = "This is the way of the dragon";
const reverseCipher = new ReverseCipher(plainText);

reverseCipher.encrypt();
const cipher = reverseCipher.show();
console.log(cipher);


reverseCipher.decrypt();
const translated = reverseCipher.show();


console.log(translated)

