import path from "path";
import fs from "fs";

/**
 * A class to detect the presence of English words in a given text.
 */
class EnglishDetector {
   
    constructor() {
       
        this._englishWords = null;
        this._filePath     = null;
        this.text          = null;
    }

    /**
     * Sets the file path of the dictionary.
     * @param {string} filePath - The path to the dictionary file.
     * @returns {Promise<void>}
     */
    async setDictionaryFilePath(filePath) {
        await this._doesFileExist(filePath);
        this._filePath = filePath;
    }

    /**
     * Sets the text to be analyzed.
     * @param {string} text - The text to be analyzed.
     */
    setText(text) {
        this.text = text;
    }

    /**
     * Checks if the provided text contains a valid percentage of English words.
     * @param {number} [percentageWordMatch=75] - The required percentage of English words for validity.
     * @returns {boolean} - True if the text contains a valid percentage of English words, otherwise false.
     */
    isValidEnglish(percentageWordMatch = 75) {
        return this._getNumOfEnglishWordPercentage() >= percentageWordMatch;
    }

    /**
     * Calculates the percentage of English words in the provided text.
     * @private
     * @returns {number} - The percentage of English words.
     */
    _getNumOfEnglishWordPercentage() {
        let match = 0;
        const words = this.text.split(" ");
        const percentage = 100;

        for (let word of words) {
            if (this._englishWords[word]) {
                match++;
            }
        }
        return (match / words.length) * percentage;
    }

    /**
     * Loads the dictionary from the specified file path.
     * @returns {Promise<void>}
     */
    async loadDictionary() {
        try {
            const fileContent = await fs.promises.readFile(this._filePath, 'utf8');
            this.populateEnglishWordsFromContent(fileContent);
        } catch (error) {
            console.error(`Error expected file but received an error of ${error}`);
        }
    }

    /**
     * Populates the English words dictionary from the provided file content.
     * This method parses the content of the dictionary file and adds each word to the English words dictionary.
     * Each word is converted to lowercase and trimmed before being added to the dictionary.
     * @param {string} fileContent - The content of the dictionary file, where each line represents a word.
     *                             
     * @private
     */
    populateEnglishWordsFromContent(fileContent) {
        if (fileContent) {
            for (let word of fileContent.split("\n")) {
                word = word.toLowerCase().trim();
                if (word) {
                    this._englishWords[word] = word;
                }
            }
        }
    }

    /**
     * Checks if the specified file exists.
     * @param {string} filePath - The path to the file.
     * @returns {Promise<void>}
     * @private
     */
    async _doesFileExist(filePath) {
        try {
            await fs.promises.access(filePath, fs.constants.F_OK);
        } catch (error) {
            console.error("The file could not be found!!");
            throw error;
        }
    }
}

export default EnglishDetector;

// async function main() {
//     const DICTIONARY_FILE_PATH = path.join(process.cwd(), "detect_english", "dictionary.txt");
//     const text  = "the way of the dragon? word word";

//     const englishDetector = new EnglishDetector();
//     englishDetector.setText(text);

//     await englishDetector.setDictionaryFilePath(DICTIONARY_FILE_PATH);
//     await englishDetector.loadDictionary();

//     const percentage = englishDetector.isValidEnglish();
//     console.log(percentage)
    
// }

// main().catch(error => {
//     console.error('An error occurred:', error);
// });
