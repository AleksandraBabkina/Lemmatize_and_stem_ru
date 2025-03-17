# Lemmatize_and_stem_ru
## Description
This script performs text preprocessing on Russian-language text files. It reads input text files from a specified folder, processes the text by converting it to lowercase, removing punctuation, removing stopwords, lemmatizing and stemming the words, and then saves the cleaned text files into an output folder. The script uses the NLTK library for tokenization, stopword removal, lemmatization, and stemming, making it useful for preparing Russian texts for further natural language processing (NLP) tasks or machine learning models.

## Functional Description
The script performs the following steps:
1. Reads input `.txt` files from a specified folder.
2. Converts all text to lowercase.
3. Removes punctuation symbols.
4. Tokenizes the text into words.
5. Removes stopwords (with some customizable exceptions).
6. Lemmatizes each word using WordNet lemmatizer.
7. Applies stemming to each word using Porter stemmer.
8. Saves the processed text to an output folder with modified filenames.

## How It Works
1. The script uses the **NLTK** library to download necessary datasets (stopwords, wordnet, etc.).
2. It defines a set of Russian stopwords and allows specific words to be excluded from removal.
3. It defines a regular expression pattern to remove punctuation from the text.
4. For each `.txt` file in the input folder:
    - Reads the file.
    - Applies text processing (lowercasing, punctuation removal, tokenization, stopword removal, lemmatization, stemming).
    - Saves the cleaned text to the output folder with "_вывод" added to the filename.
5. The processed text files are saved in UTF-8 encoding.

## Input Structure
- **Input folder path**: Folder containing original Russian `.txt` files.
- **Output folder path**: Folder where the processed text files will be saved.

You need to specify:
- Path to the input folder containing `.txt` files.
- Path to the output folder for saving results.

## Technical Requirements
To run the script, the following are required:
1. Python 3.x
2. Installed libraries:
   - `nltk`
   - `re`
   - `os`
3. Downloaded NLTK resources:
   - `punkt`
   - `stopwords`
   - `wordnet`
   - `omw-1.4`

## Usage
1. Specify the absolute paths to your input and output folders in the script:
   ```python
   input_folder = '/path/to/input/folder'
   output_folder = '/path/to/output/folder'
