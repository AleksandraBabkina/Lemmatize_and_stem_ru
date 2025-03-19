# Lemmatize_and_stem_ru

## Description

This script processes a set of Russian text files by:
- Removing punctuation.
- Tokenizing the text.
- Removing stopwords.
- Lemmatizing the words using the `spaCy` library.
- Stemming the lemmatized words using `NLTK's SnowballStemmer`.

The processed texts are then saved in a specified output folder.

## Functional Description

### Steps Involved:
1. **Text Preprocessing**: 
   - Converts the text to lowercase.
   - Removes punctuation characters.
   - Tokenizes the text.
   - Removes stopwords (optional: can remove specific words like negations).
   - Lemmatizes and stems the words to reduce them to their base form.

2. **File Handling**: 
   - The script reads each `.txt` file in a specified input folder.
   - Processes the text in the file and saves the results in an output folder.
   
3. **Saving Processed Text**: 
   - The processed text is saved in the output folder with a `_processed` suffix in the filename.

### Key Functions

1. **`process_text(text, stopwords)`**:
   - Processes the input text by:
     - Converting it to lowercase.
     - Removing punctuation.
     - Tokenizing, lemmatizing, and stemming the words.
     - Removing stopwords from the text.

2. **`os.makedirs(output_folder, exist_ok=True)`**:
   - Ensures that the output folder exists. If it doesn't, it creates it.

3. **Text File Handling**:
   - Reads `.txt` files from the specified input folder.
   - Processes the text and saves it to the output folder.

### Input Structure

- **Input Folder**: Contains `.txt` files that need to be processed.
- **Output Folder**: Stores the processed `.txt` files, each with `_processed` appended to its filename.

### Example Workflow

1. The script reads all `.txt` files from the input folder.
2. For each file:
   - The text is processed by:
     - Converting to lowercase.
     - Removing punctuation.
     - Tokenizing and lemmatizing the words.
     - Removing stopwords.
     - Stemming the lemmatized words.
3. The processed text is saved in the output folder with `_processed` in the filename.

### Example Output

1. **Processed Text**:
*страховани договор страхование филиал*
(Text after processing: punctuation removed, stopwords removed, words lemmatized and stemmed)

3. **Processed File Name**:
- If the original file is `sample.txt`, the output file will be `sample_processed.txt`.

### Error Handling

If any error occurs while reading or processing a file, the script will print an error message and move on to the next file.

### Conclusion

This script automates the process of cleaning, tokenizing, lemmatizing, and stemming Russian text data. It is useful for text preprocessing tasks, such as preparing data for natural language processing or analysis. The processed texts are saved in an output folder for further use.
